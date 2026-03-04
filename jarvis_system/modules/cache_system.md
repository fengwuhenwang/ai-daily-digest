# Jarvis V5.0 - Cache System

结果缓存管理系统，避免重复计算。

---

## 概述

缓存目标：
- 重复计算相同输入
- 相似任务快速复用
- 降低Token消耗

---

## 缓存结构

```
memory/cache/
├── index.json          # 缓存索引
└── entries/
    └── <hash>.json     # 缓存条目
```

### index.json
```json
{
  "version": "1.0",
  "last_cleanup": "ISO8601",
  "entries": {
    "hash_key_1": {
      "created_at": "ISO8601",
      "expires_at": "ISO8601",
      "hit_count": 0,
      "size_bytes": 0
    }
  }
}
```

### <hash>.json
```json
{
  "cache_key": "hash(input)",
  "input_hash": "hash(input)",
  "input_summary": "输入摘要（用于人工识别）",
  "output": {
    "status": "success",
    "data": {}
  },
  "created_at": "ISO8601",
  "expires_at": "ISO8601",
  "hit_count": 0,
  "original_task_id": "uuid"
}
```

---

## 缓存策略

### 1. TTL (Time To Live)
- 默认: 1小时
- 可配置: 5分钟 ~ 24小时
- 过期后自动清理

### 2. 缓存键生成
```python
def generate_cache_key(input_data: dict) -> str:
    """
    生成缓存键
    
    策略:
    - 使用输入的JSON序列化 + hash
    - 忽略时间戳等不相关内容
    """
    # 标准化输入
    normalized = normalize_for_hash(input_data)
    # 生成hash
    return hashlib.sha256(json.dumps(normalized)).hexdigest()[:16]
```

### 3. 相似度匹配
```python
def find_similar(cache_key: str, threshold: float = 0.95) -> dict:
    """
    查找相似缓存
    
    参数:
        cache_key: 当前输入的hash
        threshold: 相似度阈值
    
    返回:
        匹配的缓存条目或None
    """
    # 加载索引
    index = load_cache_index()
    
    for key, meta in index["entries"].items():
        if calculate_similarity(cache_key, key) >= threshold:
            return load_cache_entry(key)
    
    return None
```

---

## 核心操作

### 1. 获取缓存

```python
def get_cache(input_data: dict) -> dict | None:
    """
    获取缓存结果
    
    参数:
        input_data: 输入数据
    
    返回:
        缓存结果或None
    """
    cache_key = generate_cache_key(input_data)
    
    # 检查是否存在
    entry_path = f"memory/cache/entries/{cache_key}.json"
    
    if not file_exists(entry_path):
        return None
    
    entry = memory_get(path=entry_path)
    
    # 检查是否过期
    if is_expired(entry):
        delete_cache_entry(cache_key)
        return None
    
    # 更新命中计数
    entry["hit_count"] += 1
    write_cache_entry(cache_key, entry)
    
    return entry["output"]
```

### 2. 设置缓存

```python
def set_cache(input_data: dict, output: dict, ttl: int = 3600) -> str:
    """
    设置缓存
    
    参数:
        input_data: 输入数据
        output: 输出结果
        ttl: 过期时间（秒）
    
    返回:
        cache_key
    """
    cache_key = generate_cache_key(input_data)
    
    entry = {
        "cache_key": cache_key,
        "input_hash": cache_key,
        "input_summary": summarize_input(input_data),
        "output": output,
        "created_at": get_current_timestamp(),
        "expires_at": get_timestamp_after(ttl),
        "hit_count": 0,
        "original_task_id": get_current_task_id()
    }
    
    # 写入缓存条目
    write(f"memory/cache/entries/{cache_key}.json", json.dumps(entry))
    
    # 更新索引
    update_cache_index(cache_key, entry)
    
    return cache_key
```

### 3. 清理缓存

```python
def cleanup_cache(max_age: int = 86400, max_entries: int = 1000):
    """
    清理过期缓存
    
    参数:
        max_age: 最大保留时间（秒）
        max_entries: 最大条目数
    """
    index = load_cache_index()
    now = get_current_timestamp()
    
    # 删除过期条目
    expired_keys = []
    for key, meta in index["entries"].items():
        if is_expired(meta):
            expired_keys.append(key)
    
    for key in expired_keys:
        delete_cache_entry(key)
        del index["entries"][key]
    
    # 如果超过最大条目数，删除最旧的
    if len(index["entries"]) > max_entries:
        sorted_entries = sorted(
            index["entries"].items(),
            key=lambda x: x[1]["created_at"]
        )
        excess = len(index["entries"]) - max_entries
        for key, _ in sorted_entries[:excess]:
            delete_cache_entry(key)
            del index["entries"][key]
    
    index["last_cleanup"] = now
    save_cache_index(index)
```

---

## 缓存场景

### 推荐缓存
1. **市场数据分析** - 数据变化频率低
2. **用户偏好查询** - 变化频率低
3. **固定计算逻辑** - 相同输入产生相同输出
4. **模板渲染** - 相同模板不同数据

### 不推荐缓存
1. **实时数据查询** - 数据时效性强
2. **随机性任务** - 每次输出不同
3. **用户特定上下文** - 依赖具体用户

---

## 性能指标

### 缓存命中率
```
命中率 = 缓存命中次数 / 总请求次数
```

### 目标
- 缓存命中率: ≥ 30%
- Token节省: ≥ 20%

---

## 使用示例

### 场景: 投资组合分析

```python
# 1. 检查缓存
input_data = {
    "portfolio": portfolio_data,
    "analysis_type": "risk",
    "date": "2026-02-21"
}

cached = get_cache(input_data)
if cached:
    return cached

# 2. 执行分析
result = analyze_portfolio(portfolio_data)

# 3. 写入缓存
set_cache(input_data, result, ttl=3600)

return result
```

---

## 注意事项

1. **缓存键稳定性** - 相同输入必须产生相同键
2. **过期策略** - 定期清理过期缓存
3. **大小限制** - 控制缓存总大小
4. **一致性** - 写入失败时回滚

---

_版本: V5.0.0_
_功能: 结果缓存管理_

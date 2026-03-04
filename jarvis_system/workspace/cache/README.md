# Cache System - 结果缓存系统

## 目录结构

```
workspace/cache/
├── index.json           # 缓存索引
├── hash/                # 哈希存储
│   ├── ab1234.json
│   └── cd5678.json
└── policy.json          # 缓存策略
```

---

## 缓存策略

```json
{
  "version": "5.1",
  "policy": {
    "default_ttl_seconds": 3600,
    "max_entries": 100,
    "enabled": true
  },
  "type_policies": {
    "weather": {"ttl_seconds": 1800, "enabled": true},
    "stock_quote": {"ttl_seconds": 60, "enabled": true},
    "news": {"ttl_seconds": 900, "enabled": true},
    "calculation": {"ttl_seconds": 86400, "enabled": true},
    "analysis": {"ttl_seconds": 3600, "enabled": true}
  }
}
```

---

## 缓存索引

```json
{
  "entries": {
    "ab1234": {
      "hash": "ab1234",
      "type": "weather",
      "input_summary": "shanghai weather",
      "output_summary": "sunny 20C",
      "created_at": "2026-02-21T13:00:00Z",
      "expires_at": "2026-02-21T13:30:00Z",
      "hits": 5
    }
  },
  "stats": {
    "total_hits": 50,
    "total_misses": 100,
    "hit_rate": 0.33,
    "tokens_saved": 25000
  }
}
```

---

## API

### 缓存查询
```python
def cache_get(input_data, cache_type="default"):
    policy = load_policy()
    if not policy["type_policies"].get(cache_type, {}).get("enabled"):
        return None
    
    hash_key = hash_input(input_data)
    entry = load_cache_entry(hash_key)
    
    if entry and is_not_expired(entry):
        entry["hits"] += 1
        save_cache_entry(hash_key, entry)
        return entry["output"]
    
    return None
```

### 缓存存储
```python
def cache_set(input_data, output_data, cache_type="default"):
    hash_key = hash_input(input_data)
    policy = load_policy()
    ttl = policy["type_policies"].get(cache_type, {}).get("ttl_seconds", 3600)
    
    entry = {
        "hash": hash_key,
        "type": cache_type,
        "input_summary": summarize(input_data),
        "output_summary": summarize(output_data),
        "output": output_data,
        "created_at": get_current_iso_timestamp(),
        "expires_at": get_future_timestamp(ttl),
        "hits": 0
    }
    
    save_cache_entry(hash_key, entry)
    update_index(entry)
```

---

## 缓存命中示例

### 天气查询
```
用户: 上海今天天气怎么样?
系统: 检查缓存 → 命中 → 直接返回 (0 token)
```

### 金融计算
```
用户: AAPL当前估值
系统: 检查缓存 → 未命中 → 计算 → 缓存结果
```

---

## Token节省预估

| 缓存类型 | 命中率 | 平均节省 |
|---------|-------|---------|
| weather | 80% | ~500 tokens/次 |
| stock_quote | 60% | ~1000 tokens/次 |
| calculation | 90% | ~2000 tokens/次 |
| analysis | 30% | ~3000 tokens/次 |

---

## 清理策略

- TTL过期自动清理
- 超过max_entries时删除最旧条目
- 每周清理一次全部过期条目

---

_版本: 5.1_
_用途: 减少重复计算，节省Token_

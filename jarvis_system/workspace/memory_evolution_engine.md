# Memory Evolution Engine - 记忆进化引擎

## 记忆分层架构

| 层级 | 名称 | 存储位置 | 保留周期 | 加载方式 |
|------|------|---------|---------|---------|
| L1 | 长期记忆 | memory/l1_long_term/ | 永久 | 按需检索 |
| L2 | 重要记忆 | memory/l2_important/ | 1年 | 会话加载 |
| L3 | 临时记忆 | memory/l3_temp/ | 7天 | 自动清理 |

---

## 记忆分类规则

### L1 - 长期记忆 (Long-term)
**进入条件** (满足任一):
- 用户明确要求记住
- 重复出现 ≥ 3 次
- 对人生目标重要
- 身份/价值观相关
- 重大决策记录

**内容**:
- 用户身份信息
- 核心价值观
- 长期目标
- 重要关系
- 关键决策
- 经验教训

### L2 - 重要记忆 (Important)
**进入条件**:
- 阶段目标相关
- 项目里程碑
- 重要学习成果
- 人际关系变化
- 财务重要事件

**内容**:
- 阶段性目标
- 项目进展
- 学习笔记
- 重要关系
- 财务记录

### L3 - 临时记忆 (Temporary)
**进入内容**:
- 普通对话
- 临时任务
- 日常信息
- 待办提醒

**清理规则**:
- 7天后自动删除
- 可手动提前清理

---

## 目录结构

```
workspace/memory/
├── l1_long_term/           # 长期记忆
│   ├── identity.json       # 身份信息
│   ├── values.json        # 价值观
│   ├── goals.json         # 长期目标
│   ├── decisions.json     # 重大决策
│   ├── lessons.json       # 经验教训
│   └── relationships.json # 重要关系
│
├── l2_important/          # 重要记忆
│   ├── stage_*.json       # 阶段相关
│   ├── project_*.json    # 项目相关
│   ├── learnings/         # 学习成果
│   └── finances/          # 财务记录
│
├── l3_temp/                # 临时记忆
│   ├── sessions/          # 会话记录
│   ├── tasks/             # 临时任务
│   └── todos/             # 待办事项
│
├── index.json              # 全局索引
└── evolution_log.json     # 进化日志
```

---

## 记忆读写API

### 写入记忆
```python
def save_memory(content, level, tags=None, source=None):
    """保存记忆"""
    
    memory_entry = {
        "id": generate_uuid(),
        "content": content,
        "level": level,
        "tags": tags or [],
        "source": source,
        "created_at": get_current_iso_timestamp(),
        "last_accessed": get_current_iso_timestamp(),
        "access_count": 0
    }
    
    # 写入对应层级
    file_path = get_level_path(level, memory_entry["id"])
    write_json(file_path, memory_entry)
    
    # 更新索引
    update_index(memory_entry)
    
    return memory_entry["id"]
```

### 读取记忆
```python
def retrieve_memories(query, level=None, tags=None, top_k=5):
    """检索记忆"""
    
    # 1. 搜索索引
    index = read_json("workspace/memory/index.json")
    candidates = search_index(index, query, level, tags)
    
    # 2. 获取Top-K
    results = []
    for item in candidates[:top_k]:
        content = read_json(item["file_path"])
        results.append(content)
        
        # 更新访问统计
        update_access_stats(item["id"])
    
    return results
```

### 记忆升级
```python
def evolve_memory(memory_id):
    """记忆进化 - 压缩/降级/删除"""
    
    memory = read_json(get_memory_path(memory_id))
    age = get_days_since(memory["created_at"])
    
    # L3 -> L2: 30天后如果重要
    if memory["level"] == "l3" and age > 30:
        if is_important(memory):
            upgrade_level(memory_id, "l2")
            log_evolution(memory_id, "l3", "l2")
    
    # L2 -> L1: 1年后如果持续重要
    if memory["level"] == "l2" and age > 365:
        if is_significant(memory):
            upgrade_level(memory_id, "l1")
            log_evolution(memory_id, "l2", "l1")
    
    # L3清理: 7天后
    if memory["level"] == "l3" and age > 7:
        delete_memory(memory_id)
        log_evolution(memory_id, "l3", "deleted")
```

---

## 定期进化任务

### 每日任务
- 清理过期L3记忆
- 更新访问统计

### 每周任务
- 评估L3 -> L2升级
- 整理会话摘要

### 每月任务
- 评估L2 -> L1升级
- 压缩频繁访问的L1内容
- 生成月度记忆报告

---

## 索引结构

```json
{
  "version": "1.0",
  "last_updated": "2026-02-21T13:30:00Z",
  "total_entries": 100,
  "by_level": {
    "l1": 20,
    "l2": 30,
    "l3": 50
  },
  "by_tags": {
    "capability": 15,
    "wealth": 10,
    "health": 8,
    "relationships": 5,
    "decisions": 12
  },
  "search_index": [
    {
      "id": "mem_001",
      "keywords": ["能力", "跃迁", "学习"],
      "level": "l1",
      "file_path": "l1_long_term/goals.json",
      "importance": 0.9
    }
  ]
}
```

---

## 压缩规则

### L1压缩
- 定期将访问频率低的条目转为摘要
- 保留核心要点，删除细节

### L2压缩
- 每月汇总为周报/月报
- 删除重复内容

### L3清理
- 7天自动删除
- 用户可手动保留

---

## 集成主控

Jarvis主控启动时：
1. 加载 user_model.json
2. 加载 strategy_state.json  
3. 检索相关L1记忆 (top_k=3)
4. 构建精简上下文

任务完成后：
1. 判断记忆层级
2. 保存到对应位置
3. 更新索引

---

## 版本
- Version: 1.0
- Updated: 2026-02-21

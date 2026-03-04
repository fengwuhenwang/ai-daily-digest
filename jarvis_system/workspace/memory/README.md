# Memory Manager - 按需加载系统

## 核心原则

**RAG思想：按需检索，而非全量加载**

---

## 目录结构

```
workspace/memory/
├── user_model.json      # 用户模型（快速加载）
├── sessions/            # 会话历史
│   └── 2026-02-21/
│       └── session_001.json
├── decisions/           # 决策记录
│   └── decisions.json
├── lessons/            # 经验教训
│   └── lessons.json
├── knowledge/          # 知识库
│   └── index.json
└── index.json          # 全局索引
```

---

## 索引结构

```json
{
  "version": "5.1",
  "index": {
    "user_model": {
      "path": "workspace/user_model/user.json",
      "last_loaded": "2026-02-21T13:00:00Z"
    },
    "recent_sessions": {
      "path": "workspace/memory/sessions/",
      "files": ["2026-02-21/session_001.json"],
      "max_recent": 3
    },
    "decisions": {
      "path": "workspace/memory/decisions/decisions.json",
      "count": 10,
      "tags": ["投资", "职业", "健康"]
    },
    "lessons": {
      "path": "workspace/memory/lessons/lessons.json",
      "count": 5,
      "last_updated": "2026-02-20T00:00:00Z"
    }
  },
  "search_index": {
    "decisions": [
      {"id": 1, "tags": ["投资", "风险"], "date": "2026-02-20", "summary": "..."},
      {"id": 2, "tags": ["职业", "选择"], "date": "2026-02-19", "summary": "..."}
    ],
    "lessons": [
      {"id": 1, "tags": ["专注", "方法"], "date": "2026-02-20", "summary": "..."}
    ]
  }
}
```

---

## 检索流程

### 1. 任务类型判断
```
用户请求 → 判断任务类型 → 确定检索范围
```

### 2. 关键词提取
- 投资类 → 检索 `decisions` + `lessons` (tags: 投资, 财富)
- 健康类 → 检索 `lessons` (tags: 健康, 习惯)
- 职业类 → 检索 `decisions` + `lessons` (tags: 职业, 能力)

### 3. Top-K 加载
- 默认加载 Top-3 相关记忆
- 复杂任务可加载 Top-5
- 禁止超过 Top-10

### 4. 上下文组装
```
[用户模型关键字段] + [Top-K 记忆] + [当前任务]
```

---

## API

### 检索记忆
```python
def retrieve_memories(query, tags=[], top_k=3):
    # 1. 读取索引
    index = read_json("workspace/memory/index.json")
    
    # 2. 搜索相关记忆
    results = search(index["search_index"], query, tags)
    
    # 3. 按相关度排序
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    
    # 4. 加载Top-K
    memories = [load_memory(r["id"]) for r in results[:top_k]]
    
    return memories
```

### 存储记忆
```json
{
  "id": "mem_001",
  "type": "decision|lesson|insight",
  "tags": ["投资", "风险"],
  "summary": "简短摘要",
  "content": "详细内容",
  "created_at": "2026-02-21T13:00:00Z",
  "importance": "high|medium|low"
}
```

---

## Token优化效果

| 场景 | 优化前 | 优化后 |
|-----|-------|-------|
| 会话启动 | 加载全部MEMORY.md (~3000 tokens) | 只加载user_model (~500 tokens) |
| 决策咨询 | 复制历史对话 (~2000 tokens) | 检索相关decisions (~300 tokens) |
| 经验总结 | 全量搜索 (~1500 tokens) | Top-3检索 (~300 tokens) |

---

## 禁止事项

❌ 禁止加载全部memory
❌ 禁止在prompt中粘贴完整历史
❌ 禁止复制会话记录
❌ 禁止跨任务传递上下文

---

_版本: 5.1_
_用途: Memory按需加载，解决上下文叠加问题_

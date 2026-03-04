# Jarvis V5.0 - Memory Management System

外部记忆管理系统，负责所有持久化信息的读写。

---

## 目录结构

```
memory/
├── user/           # 用户画像（结构化JSON）
│   └── profile.json
├── tasks/          # 任务历史
│   └── task_<uuid>.json
├── knowledge/      # 知识库（可复用）
│   ├── decisions.json
│   └── lessons.json
├── state/          # 运行时状态
│   └── runtime.json
├── cache/          # 结果缓存
│   └── hash_<key>.json
└── outputs/       # 产出物
    └── <date>/
```

---

## 核心模块

### 1. MemoryReader
负责按需读取记忆。

```python
class MemoryReader:
    def read_user_profile(self) -> dict:
        """读取用户画像"""
        
    def search_related_memory(self, query: str, top_k: int = 3) -> list:
        """搜索相关记忆"""
        
    def load_task_state(self, task_id: str) -> dict:
        """加载任务状态"""
        
    def get_cached_result(self, cache_key: str) -> dict:
        """获取缓存结果"""
```

### 2. MemoryWriter
负责写入和更新记忆。

```python
class MemoryWriter:
    def update_user_profile(self, updates: dict) -> None:
        """更新用户画像"""
        
    def write_task_result(self, task_id: str, result: dict) -> None:
        """写入任务结果"""
        
    def write_knowledge(self, category: str, data: dict) -> None:
        """写入知识库"""
        
    def cache_result(self, cache_key: str, result: dict, ttl: int = 3600) -> None:
        """缓存结果"""
```

### 3. MemoryIndexer
负责索引和检索。

```python
class MemoryIndexer:
    def index_task(self, task_id: str, keywords: list) -> None:
        """索引任务"""
        
    def search(self, query: str, filters: dict) -> list:
        """全文搜索"""
```

---

## 用户画像 (user/profile.json)

### 结构
```json
{
  "identity": {
    "name": "Pony",
    "timezone": "Asia/Shanghai"
  },
  "preferences": {
    "communication_style": "理性冷静",
    "output_format": "结构化",
    "risk_tolerance": "medium"
  },
  "goals": [
    "能力跃迁",
    "财富跃迁",
    "人生自主度提升"
  ],
  "constraints": {
    "max_risk_level": 3,
    "avoid_sectors": []
  },
  "updated_at": "ISO8601"
}
```

---

## 知识库 (knowledge/)

### decisions.json - 重要决策
```json
{
  "decisions": [
    {
      "id": "uuid",
      "date": "ISO8601",
      "context": "决策背景",
      "decision": "决策内容",
      "outcome": "执行结果",
      "lessons": ["经验教训"]
    }
  ]
}
```

### lessons.json - 经验教训
```json
{
  "lessons": [
    {
      "id": "uuid",
      "date": "ISO8601",
      "category": "类别",
      "description": "描述",
      "actionable": "可执行建议"
    }
  ]
}
```

---

## 任务状态 (tasks/)

### task_<uuid>.json
```json
{
  "task_id": "uuid",
  "goal": "任务目标",
  "status": "pending|processing|completed|failed",
  "steps": [
    {
      "id": 1,
      "description": "步骤描述",
      "status": "completed|processing|pending",
      "result": "步骤结果"
    }
  ],
  "artifacts": ["file_path1", "file_path2"],
  "context": {
    "input": "输入摘要",
    "output": "输出摘要"
  },
  "token_usage": {
    "input": 0,
    "output": 0
  },
  "created_at": "ISO8601",
  "updated_at": "ISO8601",
  "completed_at": "ISO8601"
}
```

---

## 缓存机制 (cache/)

### hash_<key>.json
```json
{
  "cache_key": "hash(input)",
  "input_summary": "输入摘要",
  "output": "输出结果",
  "created_at": "ISO8601",
  "expires_at": "ISO8601"
}
```

### 缓存策略
- TTL: 1小时（默认）
- 缓存键: hash(输入)
- 命中条件: 输入相似度 > 0.95

---

## 读写流程

### 读取流程
```
1. 解析用户请求
2. 确定需要哪类Memory
3. 调用 memory_search 搜索
4. 使用 memory_get 加载具体内容
5. 构建精简上下文
```

### 写入流程
```
1. 任务完成或关键节点
2. 提取需要持久化的信息
3. 调用 write 写入对应文件
4. （可选）更新索引
```

---

## 使用示例

### 场景1: 读取用户偏好
```python
# 使用 memory_get
memory_get(path="memory/user/profile.json")
```

### 场景2: 搜索相关记忆
```python
# 使用 memory_search
memory_search(query="投资决策 风险控制")
# 返回 top 3 相关片段
```

### 场景3: 写入任务结果
```python
# 使用 write
write(file_path="memory/tasks/task_<uuid>.json", content=json.dumps(task_state))
```

---

## 优化原则

### 按需加载
- 只读取任务相关的Memory
- 禁止加载全部文件
- 使用文件路径引用

### 结构化存储
- 所有数据使用JSON格式
- 禁止自然语言描述可结构化的信息
- 便于程序化处理

### 增量更新
- 更新时只写变化部分
- 保留历史版本（可选）
- 避免重复写入

---

## 清理策略

### 临时文件
- 任务状态文件: 完成后7天删除
- 缓存文件: TTL过期后删除
- 临时输出: 30天后归档

### 长期保留
- 用户画像: 长期保留
- 知识库: 长期保留
- 重要决策: 长期保留

---

_版本: V5.0.0_
_功能: 外部记忆的读写索引管理_

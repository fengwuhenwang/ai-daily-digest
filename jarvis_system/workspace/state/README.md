# Task State Manager - 任务状态管理系统

## 文件位置
```
jarvis_system/workspace/state/task_<task_id>.json
```

---

## 任务状态结构

```json
{
  "task_id": "task_20260221_001",
  "goal": "用户原始目标描述",
  "status": "pending|running|completed|failed|paused",
  "complexity": "simple|medium|complex|strategic",
  "agents_used": ["finance_agent"],
  "artifacts": {
    "outputs": [],
    "decisions": [],
    "insights": []
  },
  "context": {
    "user_id": "pony",
    "session_id": "main",
    "channel": "telegram"
  },
  "next_step": "执行下一步描述",
  "metadata": {
    "created_at": "2026-02-21T13:00:00Z",
    "updated_at": "2026-02-21T13:05:00Z",
    "completed_at": null,
    "token_usage": {
      "input": 1000,
      "output": 500
    }
  }
}
```

---

## 状态流转

```
pending → running → completed
              → failed
              → paused
```

---

## API

### 创建任务
```python
def create_task(goal, complexity):
    task_id = f"task_{get_date()}_{random_suffix()}"
    state = {
        "task_id": task_id,
        "goal": goal,
        "status": "pending",
        "complexity": complexity,
        ...
    }
    write_json(f"workspace/state/{task_id}.json", state)
    return task_id
```

### 更新状态
```python
def update_task(task_id, updates):
    state = read_json(f"workspace/state/{task_id}.json")
    state.update(updates)
    state["metadata"]["updated_at"] = get_current_iso_timestamp()
    write_json(f"workspace/state/{task_id}.json", state)
```

### 添加产物
```python
def add_artifact(task_id, artifact_type, content):
    state = read_json(f"workspace/state/{task_id}.json")
    state["artifacts"][artifact_type].append(content)
    update_task(task_id, {"artifacts": state["artifacts"]})
```

---

## 最小上下文原则

**子Agent调用时：**
- 只发送 `task_id` 和 `goal`
- Agent从文件读取完整状态
- 禁止在prompt中粘贴完整历史

**更新时：**
- 只发送delta（变化部分）
- 禁止重新发送已完成的内容

---

## Token优化效果

| 场景 | 传统方式 | 优化后 |
|-----|---------|-------|
| 多步骤任务 | 每次发送完整上下文 | 只传task_id |
| 复杂决策 | 复制历史对话 | 读取artifacts |
| 子Agent调用 | 发送全部背景 | 按需加载state |

---

## 目录结构

```
workspace/state/
├── task_20260221_001.json
├── task_20260221_002.json
└── index.json          # 任务索引
```

---

_版本: 5.1_
_用途: 任务状态外置，避免上下文叠加_

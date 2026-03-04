# Jarvis V5.0 - Task State Manager

任务状态持久化管理器。

---

## 概述

每个任务的生命周期：
1. **创建** → 生成 task_<uuid>.json
2. **执行** → 更新状态和步骤
3. **完成** → 写入最终结果 + 可选删除临时状态
4. **归档** → 移动到历史目录

---

## 状态结构

```json
{
  "task_id": "uuid-v4",
  "goal": "任务目标（简洁描述）",
  "status": "pending|processing|completed|failed",
  "mode": "direct|stepped|agent",
  "priority": "low|medium|high|critical",
  
  "steps": [
    {
      "id": 1,
      "description": "步骤描述",
      "status": "pending|processing|completed|skipped|failed",
      "tool": "使用的工具（如果是工具调用）",
      "result": "步骤结果摘要",
      "artifacts": ["产出文件路径"],
      "started_at": "ISO8601",
      "completed_at": "ISO8601"
    }
  ],
  
  "current_step": 1,
  
  "artifacts": [
    "file_path1",
    "file_path2"
  ],
  
  "context": {
    "input_summary": "输入摘要（<100字）",
    "output_summary": "输出摘要（<100字）",
    "errors": ["错误信息"]
  },
  
  "metrics": {
    "token_usage": {
      "input": 0,
      "output": 0,
      "total": 0
    },
    "duration_ms": 0,
    "tool_calls": 0
  },
  
  "created_at": "ISO8601",
  "updated_at": "ISO8601",
  "completed_at": "ISO8601"
}
```

---

## 状态转换

```
pending → processing → completed
                  └→ failed

pending → skipped (条件跳过)
```

---

## 核心操作

### 1. 创建任务状态

```python
def create_task(goal: str, mode: str = "direct", priority: str = "medium") -> dict:
    """
    创建新任务状态文件
    
    参数:
        goal: 任务目标
        mode: 执行模式 (direct/stepped/agent)
        priority: 优先级
    
    返回:
        task_state 对象
    """
    task_id = generate_uuid()
    state = {
        "task_id": task_id,
        "goal": goal,
        "status": "pending",
        "mode": mode,
        "priority": priority,
        "steps": [],
        "current_step": 0,
        "artifacts": [],
        "context": {},
        "metrics": {"token_usage": {"input "output": ": 0,0, "total": 0}, "duration_ms": 0, "tool_calls": 0},
        "created_at": get_current_timestamp(),
        "updated_at": get_current_timestamp()
    }
    
    # 写入文件
    write(f"memory/tasks/task_{task_id}.json", json.dumps(state))
    
    return state
```

### 2. 更新步骤状态

```python
def update_step(task_id: str, step_id: int, status: str, result: str = None, artifacts: list = None):
    """
    更新步骤状态
    
    参数:
        task_id: 任务ID
        step_id: 步骤ID
        status: 新状态
        result: 步骤结果（可选）
        artifacts: 产出文件列表（可选）
    """
    state = load_task_state(task_id)
    
    for step in state["steps"]:
        if step["id"] == step_id:
            step["status"] = status
            if result:
                step["result"] = result
            if artifacts:
                step["artifacts"] = artifacts
            if status == "completed":
                step["completed_at"] = get_current_timestamp()
            break
    
    state["updated_at"] = get_current_timestamp()
    write_task_state(task_id, state)
```

### 3. 完成任务

```python
def complete_task(task_id: str, output_summary: str, artifacts: list = None):
    """
    完成任务
    
    参数:
        task_id: 任务ID
        output_summary: 输出摘要
        artifacts: 最终产出文件列表
    """
    state = load_task_state(task_id)
    
    state["status"] = "completed"
    state["context"]["output_summary"] = output_summary
    state["completed_at"] = get_current_timestamp()
    
    if artifacts:
        state["artifacts"].extend(artifacts)
    
    # 更新所有步骤为completed
    for step in state["steps"]:
        if step["status"] == "processing":
            step["status"] = "completed"
    
    write_task_state(task_id, state)
    
    # 可选：写入知识库
    write_knowledge("tasks", {
        "task_id": task_id,
        "goal": state["goal"],
        "outcome": output_summary,
        "steps_completed": len([s for s in state["steps"] if s["status"] == "completed"])
    })
```

### 4. 加载任务状态

```python
def load_task_state(task_id: str) -> dict:
    """
    加载任务状态
    
    参数:
        task_id: 任务ID
    
    返回:
        task_state 对象
    """
    # 使用 memory_get
    return memory_get(path=f"memory/tasks/task_{task_id}.json")
```

---

## 执行流程示例

### 场景: 复杂任务分步骤执行

```
1. 创建任务
   → create_task(goal="分析投资组合风险", mode="stepped")
   → 返回 task_id="uuid-xxx"

2. 执行步骤1
   → update_step(task_id, 1, "processing")
   → 执行分析...
   → update_step(task_id, 1, "completed", result="风险评分65")

3. 执行步骤2
   → update_step(task_id, 2, "processing")
   → 执行建议...
   → update_step(task_id, 2, "completed", result="建议减仓5%")

4. 完成任务
   → complete_task(task_id, output_summary="风险可控，建议微调")
   → 状态标记为completed
   → 可选：写入知识库
```

---

## 优化要点

### 1. 按需加载
- 只在需要时加载完整状态
- 可使用 memory_get 读取部分内容

### 2. 增量更新
- 不要每次重写整个文件
- 只更新变化的部分

### 3. 清理策略
- 完成后可选择删除临时状态
- 重要信息写入知识库

---

## 注意事项

1. **task_id 唯一性** - 使用 UUID 确保不冲突
2. **状态一致性** - 更新操作需要原子性
3. **错误处理** - 失败时记录错误信息
4. **可追溯性** - 保留足够的上下文供复盘

---

_版本: V5.0.0_
_功能: 任务状态持久化管理_

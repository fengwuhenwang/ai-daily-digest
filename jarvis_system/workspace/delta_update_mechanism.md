# Delta Update Mechanism - Delta更新机制

## 核心原则

**只发送变化，禁止重新生成全部内容**

---

## Delta vs Full Update

| 方式 | 描述 | Token消耗 | 适用场景 |
|------|------|----------|---------|
| Full | 完整内容替换 | 高 | 首次创建 |
| Delta | 只发送变化 | 低 | 后续更新 |
| Reference | 文件引用 | 极低 | 已有内容 |

---

## Delta更新API

### 用户模型Delta
```python
def update_user_model(delta):
    """Delta更新用户模型"""
    
    # 1. 读取当前
    current = read_json("workspace/user_model/user_model.json")
    
    # 2. 应用Delta
    for key, value in delta.items():
        if "." in key:
            # 嵌套字段: "current_stage.stage"
            set_nested(current, key, value)
        else:
            current[key] = value
    
    # 3. 更新元数据
    current["metadata"]["updated_at"] = get_current_iso_timestamp()
    
    # 4. 写入
    write_json("workspace/user_model/user_model.json", current)
    
    return {"status": "success", "updated_fields": list(delta.keys())}
```

### 战略状态Delta
```python
def update_strategy_state(delta):
    """Delta更新战略状态"""
    
    current = read_json("workspace/strategy_state.json")
    
    # 只更新变化的字段
    for key, value in delta.items():
        deep_set(current, key, value)
    
    current["metadata"]["updated_at"] = get_current_iso_timestamp()
    
    write_json("workspace/strategy_state.json", current)
    
    return current
```

### 记忆Delta
```python
def append_memory(memory_id, new_content):
    """追加记忆内容"""
    
    memory = read_json(get_memory_path(memory_id))
    
    # Delta: 追加而非替换
    if isinstance(memory.get("content"), list):
        memory["content"].append(new_content)
    else:
        memory["content"] = memory.get("content", "") + "\n" + new_content
    
    memory["updated_at"] = get_current_iso_timestamp()
    
    write_json(get_memory_path(memory_id), memory)
```

---

## Delta格式

### 标准Delta
```json
{
  "delta_type": "update",
  "target": "user_model.current_stage",
  "value": {
    "stage": "accumulation",
    "confidence": 0.85
  },
  "timestamp": "2026-02-21T13:30:00Z"
}
```

### 追加Delta
```json
{
  "delta_type": "append",
  "target": "strategy_state.active_projects",
  "value": {
    "id": "proj_001",
    "name": "新项目"
  }
}
```

### 删除Delta
```json
{
  "delta_type": "delete",
  "target": "user_model.active_projects",
  "condition": {"id": "old_project"}
}
```

---

## 主控Delta策略

### 启动时
- 读取完整 user_model.json (约200 tokens)
- 读取完整 strategy_state.json (约300 tokens)
- 检索L1记忆 top_k=3 (约300 tokens)

### 任务执行中
- 只发送Delta变化
- 不重复已存在上下文的内容
- 使用Reference引用已有文件

### 任务完成后
- 写入Delta到对应State
- 更新索引（增量）
- 记录到evolution_log

---

## 版本
- Version: 1.0
- Updated: 2026-02-21

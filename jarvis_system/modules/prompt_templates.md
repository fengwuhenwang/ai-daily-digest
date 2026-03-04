# Jarvis V5.0 - Optimized Prompt Templates

优化版Prompt模板，最大限度减少Token消耗。

---

## 核心原则

### 1. 必要信息原则
- 只包含任务必须的信息
- 禁止冗余描述
- 禁止重复说明

### 2. 引用替代复制
- 使用文件路径引用
- 使用变量替代内容
- 使用索引替代完整数据

### 3. 结构化输入
- 使用JSON格式输入
- 使用表格结构
- 使用标记语言

---

## 模板库

### 1. 任务执行模板

```markdown
# 任务执行

## 输入
- 目标: {goal}
- 模式: {mode}
- 上下文文件: {context_files}

## 执行
1. 读取上下文文件
2. 执行任务
3. 写入结果到 {output_file}

## 约束
- 输出必须为JSON格式
- 结果写入指定文件
```

**Token消耗**: ~150 tokens

### 2. 分析任务模板

```markdown
# 分析任务

## 分析目标
{goal}

## 数据源
{sources_json}

## 分析框架
{frameworks}

## 输出要求
```json
{{
  "status": "success|failed",
  "findings": [],
  "recommendations": [],
  "artifacts": []
}}
```
```

**Token消耗**: ~200 tokens

### 3. 决策任务模板

```markdown
# 决策任务

## 决策目标
{goal}

## 选项
{options_json}

## 约束
{constraints_json}

## 输出
```json
{{
  "decision": "",
  "reasoning": "",
  "risk_assessment": "",
  "next_steps": []
}}
```
```

**Token消耗**: ~180 tokens

### 4. 状态更新模板

```markdown
# 状态更新

## 任务ID
{task_id}

## 当前状态
{current_state}

## 更新内容
{updates_json}

## 输出
```json
{{
  "updated": true,
  "new_state": {}
}}
```
```

**Token消耗**: ~120 tokens

---

## Prompt压缩技巧

### 1. 删除冗余词

```markdown
# 优化前
请分析以下内容并给出详细的建议...

# 优化后
分析: {content}
建议输出:
```

### 2. 使用缩写

```markdown
# 优化前
- 首先
- 其次
- 最后

# 优化后
1. →
2. →
3. →
```

### 3. 压缩指令

```markdown
# 优化前
你是一个专业的投资分析师，你需要分析市场数据...

# 优化前
你是投资分析师。分析: {data}
```

### 4. 引用文件

```markdown
# 优化前
用户偏好: 风险承受度中等，喜欢科技股...

# 优化后
用户偏好: 见 memory/user/profile.json
```

---

## 按场景模板

### 场景1: 简单查询

```markdown
查询: {question}
约束: {constraints}

输出JSON:
```

### 场景2: 数据分析

```markdown
分析: {data_path}
指标: {metrics}
输出: {output_path}
```

### 场景3: 报告生成

```markdown
报告类型: {type}
数据源: {data_files}
模板: {template_file}
输出: {output_file}
```

### 场景4: 决策支持

```markdown
决策: {decision}
选项: {options}
风险约束: {risk_limits}
输出JSON:
```

---

## 动态上下文构建

### 构建流程

```
1. 解析用户请求
      ↓
2. 确定需要的Memory类型
      ↓
3. 搜索相关Memory (memory_search)
      ↓
4. 加载必要内容 (memory_get)
      ↓
5. 构建精简上下文
      ↓
6. 执行任务
```

### 上下文模板

```markdown
## 任务
{goal}

## 相关上下文
{context_1}  # 文件路径或引用
{context_2}

## 执行要求
{requirements}

## 输出
{output_spec}
```

---

## 输出规范

### 结构化输出
```json
{
  "status": "success",
  "artifacts": ["path/to/file.json"],
  "summary": "简要总结"
}
```

### 错误输出
```json
{
  "status": "failed",
  "error": "错误描述",
  "recoverable": true
}
```

---

## 模板选择算法

```python
def select_template(task: dict) -> str:
    """
    选择最优模板
    
    参数:
        task: 任务描述
    
    返回:
        模板名称
    """
    complexity = assess_complexity(task)
    
    if complexity < 0.3:
        return "simple_query"
    elif complexity < 0.7:
        return "analysis"
    else:
        return "decision"
```

---

## Token 估算

| 场景 | 优化前 | 优化后 | 节省 |
|------|--------|--------|------|
| 简单查询 | 500 | 150 | 70% |
| 分析任务 | 2000 | 600 | 70% |
| 决策任务 | 1500 | 500 | 67% |
| 多步骤任务 | 5000 | 1500 | 70% |

---

## 最佳实践

1. **模板复用** - 相同类型任务使用相同模板
2. **变量化** - 变化内容用变量替代
3. **引用优先** - 文件内容不直接嵌入
4. **JSON输入** - 结构化数据用JSON格式
5. **简洁输出** - 输出只包含必要信息

---

_版本: V5.0.0_
_功能: 优化版Prompt模板_

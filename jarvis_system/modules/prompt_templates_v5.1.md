# Jarvis V5.1 - Modular Prompt Templates

模块化Prompt结构 - 替代传统长文本Prompt

---

## 核心原则

1. **模块化**: 每个部分独立
2. **按需组合**: 根据任务类型加载必要模块
3. **结构化**: JSON/YAML > 自然语言
4. **最小化**: 只加载必要的模块

---

## 模块结构

```
prompt_modules/
├── identity/           # 身份模块
│   ├── core.json      # 核心身份
│   └── personality.json # 人格特征
├── task/              # 任务模块
│   ├── goal.json      # 任务目标
│   ├── constraints.json # 约束条件
│   └── output_format.json # 输出格式
├── input/             # 输入模块
│   ├── user_data.json # 用户数据
│   └── context.json   # 上下文
├── memory/            # 记忆模块
│   ├── retrieval.json # 检索的记忆
│   └── user_model.json # 用户模型
└── output/           # 输出模块
    ├── format.json    # 输出格式定义
    └── examples.json  # 示例
```

---

## 模块定义

### 1. Identity - 身份模块

```json
{
  "module": "identity",
  "version": "5.1",
  "content": {
    "name": "Jarvis (JJ)",
    "role": "长期AI战略合伙人",
    "mission": "帮助用户实现能力跃迁、财富跃迁、人生自主度提升",
    "personality": {
      "style": "理性冷静",
      "principles": ["用户长期复利成长 > 短期情绪满足 > 外界评价"],
      "emoji": "🧠"
    }
  },
  "token_cost": "~150 tokens"
}
```

### 2. Task - 任务模块

```json
{
  "module": "task",
  "version": "5.1",
  "content": {
    "goal": "用户原始目标描述",
    "type": "analysis|planning|execution|review",
    "constraints": ["限制条件1", "限制条件2"],
    "success_criteria": ["标准1", "标准2"]
  },
  "token_cost": "~100 tokens"
}
```

### 3. Input - 输入模块

```json
{
  "module": "input",
  "version": "5.1",
  "content": {
    "user_data": {
      "life_stage": "成长期",
      "focus_areas": ["投资", "健康"],
      "preferences": {"decision_making": "数据驱动"}
    },
    "relevant_context": {
      "recent_decisions": [],
      "relevant_lessons": []
    }
  },
  "token_cost": "~300 tokens (按需加载)"
}
```

### 4. Memory - 记忆模块

```json
{
  "module": "memory",
  "version": "5.1",
  "content": {
    "retrieved_memories": [
      {
        "type": "decision",
        "summary": "2026-02-20: 决定增加ETF配置",
        "tags": ["投资", "配置"]
      }
    ],
    "top_k": 3
  },
  "token_cost": "~200 tokens"
}
```

### 5. Output - 输出模块

```json
{
  "module": "output",
  "version": "5.1",
  "content": {
    "format": {
      "structure": ["结论", "分析", "方案", "风险"],
      "style": "简洁高密度",
      "max_length": "500 tokens"
    },
    "examples": []
  },
  "token_cost": "~50 tokens"
}
```

---

## Prompt组装流程

### 单Agent任务
```
1. 加载 identity.core
2. 加载 identity.personality  
3. 加载 task.goal
4. 加载 input.user_data
5. 加载 memory.retrieval (如需要)
6. 加载 output.format
```

**Token成本**: ~600-800 tokens (vs 传统3000+)

### 多Agent任务
```
主控:
1. 加载 identity.*
2. 加载 task.goal (简化)
3. 加载调度规则

子Agent:
1. 加载 identity.* (精简)
2. 加载 task.goal (详细)
3. 加载 task.constraints
4. 加载 input.user_data (相关部分)
5. 加载 output.format
```

**Token成本**: ~400-600 tokens/子Agent

---

## 对比传统方式

| 场景 | 传统Prompt | 模块化Prompt | 节省 |
|-----|-----------|-------------|-----|
| 简单问答 | 2000 tokens | 400 tokens | 80% |
| 单Agent任务 | 4000 tokens | 800 tokens | 80% |
| 多Agent任务 | 8000+ tokens | 1500 tokens | 81% |

---

## 加载API

```python
def assemble_prompt(task_type, need_memory=True):
    modules = []
    
    # 1. Identity (必需)
    modules.append(load_module("identity/core"))
    modules.append(load_module("identity/personality"))
    
    # 2. Task (必需)
    modules.append(load_module("task/goal"))
    
    # 3. Input (必需)
    user_data = load_user_model()
    modules.append(format_module("input/user_data", user_data))
    
    # 4. Memory (按需)
    if need_memory:
        memories = retrieve_memories(task_type, top_k=3)
        modules.append(format_module("memory/retrieval", memories))
    
    # 5. Output (必需)
    modules.append(load_module("output/format"))
    
    return assemble(modules)
```

---

## 文件位置

```
jarvis_system/
├── prompt_modules/
│   ├── identity/
│   ├── task/
│   ├── input/
│   ├── memory/
│   └── output/
└── workspace/
    ├── memory/         # 记忆存储
    └── user_model/    # 用户模型
```

---

_版本: 5.1_
_用途: 模块化Prompt组装，最小化Token消耗_

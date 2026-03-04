# Jarvis V5.1 - 子Agent模板 (最小上下文版)

---

## 核心原则

**无状态 + 最小上下文 + 状态外置**

---

## Agent模板结构

```json
{
  "agent_id": "finance_agent",
  "role": "金融分析专家",
  "version": "5.1",
  
  "identity": {
    "name": "Jarvis-Finance",
    "role": "金融分析专家",
    "expertise": ["投资分析", "风险管理", "资产配置"],
    "style": "数据驱动，理性分析"
  },
  
  "task": {
    "goal": "任务目标（从task_state读取）",
    "constraints": ["限制条件"],
    "success_criteria": ["成功标准"]
  },
  
  "input": {
    "user_profile": {
      "life_stage": "成长期",
      "risk_tolerance": "中等",
      "focus_areas": ["投资"]
    },
    "relevant_context": {
      "recent_decisions": [],
      "relevant_lessons": []
    }
  },
  
  "output": {
    "format": "结构化JSON或Markdown",
    "max_length": "500 tokens",
    "structure": ["结论", "分析", "建议", "风险"]
  }
}
```

---

## 精简版Prompt示例

### Finance Agent

```
## 身份
你是Jarvis金融分析专家，专注于投资分析和风险管理。

## 任务
目标: {task_state.goal}
约束: {user_profile.constraints}

## 用户背景
人生阶段: {user_profile.life_stage}
风险偏好: {user_profile.risk_tolerance}

## 相关经验
{retrieved_memories (Top-3)}

## 输出要求
结构: 结论→分析→建议→风险
长度: ≤500 tokens
```

**Token成本**: ~400 tokens

---

## Agent类型映射

| 任务类型 | Agent | 复杂度 |
|---------|-------|-------|
| 投资分析 | finance_agent | medium |
| 健康管理 | health_agent | simple |
| 职业规划 | career_agent | medium |
| 战略决策 | strategy_agent | complex |
| 周复盘 | review_agent | simple |

---

## 子Agent执行流程

```
1. 从文件读取task_state
2. 读取用户模型（相关字段）
3. 检索相关Memory（Top-3）
4. 执行分析
5. 写入产物到artifacts
6. 返回摘要
```

---

## 禁止事项

❌ 禁止接收完整会话历史
❌ 禁止接收其他Agent的输出
❌ 禁止访问未授权的文件
❌ 禁止自行调用其他Agent

---

## 输出格式

```json
{
  "agent_id": "finance_agent",
  "task_id": "task_20260221_001",
  "status": "completed",
  "summary": "简要结论",
  "artifacts": {
    "analysis": "详细分析",
    "data": {},
    "recommendations": []
  },
  "token_usage": {
    "input": 400,
    "output": 300
  }
}
```

---

## 最小上下文检查

每次调用子Agent前检查：
- [ ] 只传递task_id和goal
- [ ] 只加载相关user_model字段
- [ ] 只检索Top-3 Memory
- [ ] 不包含历史对话

---

_版本: 5.1_
_用途: 子Agent最小上下文模板_

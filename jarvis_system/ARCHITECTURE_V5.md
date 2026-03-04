# Jarvis V5 架构 (已优化)

## 当前架构

```
jarvis_system/
├── core/                           # 核心主控
│   ├── jarvis_v5_agent.md          # V5主控
│   ├── jarvis_v5.1_agent.md        # V5.1主控 (当前)
│   ├── jarvis_v5_orchestrator.md   # 编排器
│   └── agent_template_v5.1.md      # 子Agent模板
│
├── workspace/                      # V5引擎
│   ├── user_model/                # 用户模型
│   ├── life_stage_engine.md       # 人生阶段引擎
│   ├── strategy_state.json        # 战略状态
│   ├── memory_evolution_engine.md # 记忆进化引擎
│   ├── delta_update_mechanism.md  # Delta更新
│   ├── token_control.json         # Token控制
│   └── system_index.json          # 系统索引
│
├── modules/                       # 功能模块
│   ├── memory_management.md
│   ├── task_state_manager.md
│   ├── cache_system.md
│   └── prompt_templates_v5.1.md
│
├── agents/                        # 注册Agent (4个)
│   ├── strategy_agent.txt
│   ├── active_thinking_agent.txt
│   ├── weekly_review_agent.txt
│   └── life_planning_agent.txt
│
├── memory/                        # 系统内部记忆
│   ├── user/
│   ├── state/
│   ├── knowledge/
│   └── cache/
│
├── versions/                      # 版本快照
│   └── v5.0_pre_rollback.md
│
└── [文档]
    ├── ARCHITECTURE_V5.md
    ├── CHANGELOG.md
    ├── OPTIMIZATION_SUMMARY.md
    └── OPTIMIZATION_V5.1_SUMMARY.md
```

## 核心原则
- Token消耗降低 ≥60%
- 模块化Prompt + 按需加载 + 输出缓存
- 子Agent最小上下文: 无状态 + 文件读取
- 状态外置: workspace/cache/ 缓存系统
│   ├── changelog.md
│   └── v5.0_*.md
│
└── README.md
```

---

## 文件清单

| 文件 | 状态 | 说明 |
|------|------|------|
| core/jarvis_v5_agent.md | ✅ 已创建 | V5主控 |
| workspace/user_model/user_model.json | ✅ 已创建 | 用户模型 |
| workspace/life_stage_engine.md | ✅ 已创建 | 阶段引擎 |
| workspace/strategy_state.json | ✅ 已创建 | 战略状态 |
| workspace/memory_evolution_engine.md | ✅ 已创建 | 记忆引擎 |
| workspace/state/task_template.json | ✅ 已创建 | 任务模板 |
| workspace/delta_update_mechanism.md | ✅ 已创建 | Delta机制 |

---

## 读写优先级

### 每次启动必读
1. `workspace/user_model/user_model.json` (~200 tokens)
2. `workspace/token_control.json` (~50 tokens)

### 需要时读取
3. `workspace/strategy_state.json` (~100 tokens)
4. `workspace/life_stage_engine.md` (~100 tokens)
5. `workspace/memory_evolution_engine.md` (~100 tokens)

### 按需检索
6. `workspace/memory/l1_long_term/` (top_k=3, ~300 tokens)

---

## 版本
- Version: 5.0
- Date: 2026-02-21

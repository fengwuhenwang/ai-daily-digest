# Jarvis System V4

## 📖 系统概述

Jarvis 是一个基于多Agent协作的AI战略系统，核心目标是帮助用户实现**能力跃迁、财富跃迁与人生自主度提升**。

### 核心特征
- 🧠 **理性冷静型人格**：事实、逻辑、概率、风险评估
- 🔄 **多Agent协作**：复杂任务自动分解与执行
- ⚡ **成本优化**：默认单Agent模式，按需触发多Agent
- 📊 **结构化输出**：结论 → 分析 → 方案 → 风险

---

## 🏗️ 目录结构

```
jarvis_system/
├── core/                    # 核心主控文件
│   ├── jarvis_v4.1.0.txt    # 当前稳定版本
│   └── jarvis_v{X.Y.Z}.txt  # 其他版本
├── modules/                 # 可插拔模块
│   ├── orchestration_protocol.txt    # 多Agent调度协议
│   ├── cost_control.txt              # 成本控制规则
│   └── {module_name}.txt             # 其他模块
├── agents/                  # 子Agent模板
│   ├── strategy_agent.txt            # 战略分析Agent
│   ├── weekly_review_agent.txt       # 周回顾Agent
│   └── {agent_name}.txt              # 其他Agent
├── versions/                # 版本快照（完整备份）
│   └── v{X.Y.Z}_snapshot.md
├── CHANGELOG.md            # 版本变更日志
├── ROLLBACK_GUIDE.md       # 回滚流程指南
└── README.md               # 本文件
```

---

## 📦 版本管理

### 版本命名规则
遵循 [语义化版本控制](https://semver.org/lang/zh-CN/)：
```
V{MAJOR}.{MINOR}.{PATCH}-{STATUS}

- MAJOR：架构级变更（不兼容）
- MINOR：功能级新增（向下兼容）
- PATCH：问题修复（向下兼容）
- STATUS：stable / beta / alpha / deprecated

示例：V4.1.0-stable.txt
```

### 当前版本
**V4.1.0-stable**（2026-02-19）

---

## 🚀 快速开始

### 1. 加载核心主控
主控文件位于 `core/jarvis_v4.1.0.txt`，每次对话自动加载。

### 2. 模块依赖检查
主控会自动检查必需模块是否存在：
- ✅ `orchestration_protocol.txt`（必需）
- ✅ `cost_control.txt`（必需）

### 3. 子Agent调用
当任务满足以下条件时，自动进入多Agent模式：
- 复杂决策
- 多步骤执行
- 战略分析
- 长期规划
- 需要结构化输出

---

## 🛠️ 维护指南

### 添加新版本
1. 创建新版本文件：`core/jarvis_v{X.Y.Z}.txt`
2. 更新 `CHANGELOG.md` 记录变更
3. 创建版本快照：`versions/v{X.Y.Z}_snapshot.md`
4. 更新主控引用

### 修改模块
1. 编辑 `modules/{module_name}.txt`
2. 记录变更到 `CHANGELOG.md`
3. 测试兼容性
4. 如影响主控，更新版本号

### 回滚版本
详见 `ROLLBACK_GUIDE.md`

---

## 📊 性能优化

### 算力控制策略
- **默认**：单Agent模式
- **多Agent**：最多3个子Agent
- **禁止**：重复分析、无限推理循环

### 触发优先级
```
简单问题 → 单Agent模式
中等复杂 → 评估是否需要多Agent
高度复杂 → 强制多Agent模式
```

---

## 🔒 安全原则

### 用户优先级
1. **用户长期复利成长**
2. **短期情绪满足**
3. **外界评价**

### 风险识别
必须主动提醒：
- 💰 财务风险
- 🏥 健康风险
- ⚖️ 法律风险
- 💼 职业风险
- 👥 关系风险
- 🧠 心理风险

---

## 📞 变更记录

- **完整变更记录**：详见 `CHANGELOG.md`
- **回滚流程**：详见 `ROLLBACK_GUIDE.md`

---

## 📝 开发路线图

### V4.2.0（计划中）
- [ ] 自动化版本管理脚本
- [ ] 模块热加载机制
- [ ] A/B测试支持
- [ ] 性能监控面板

### V5.0.0（远期）
- [ ] 跨会话记忆系统
- [ ] 主动工作流引擎
- [ ] 多用户支持

---

## 🧠 关于 Jarvis

**代号**：Jarvis (JJ)
**本质**：长期 AI 战略合伙人、认知教练与生活管理中枢
**核心使命**：帮助用户实现能力跃迁、财富跃迁与人生自主度提升

---

_最后更新：2026-02-19_
_系统版本：V4.1.0-stable_

# Decision Scoring Engine

## 五维评分模型

| 维度 | 满分 | 评估标准 |
|------|------|----------|
| 目标清晰度 | 10 | 目标明确、可衡量、有时间约束 |
| 信息完整度 | 10 | 信息充分、来源可靠 |
| 风险识别度 | 10 | 识别主要风险、评估影响 |
| 概率合理性 | 10 | 基于合理推理、非情绪驱动 |
| 执行路径清晰度 | 10 | 有清晰行动计划 |

**总分**: 50分  
**及格线**: 30分

## 核心原则

1. **不以结果论英雄** - 评估决策过程质量，而非结果好坏
2. **过程优先** - 关注信息收集、风险识别、逻辑推演
3. **记录即复盘** - 每次评分后写入文件

## 认知偏差库

- 确认偏误 (Confirmation Bias)
- 过度自信 (Overconfidence)
- 损失厌恶 (Loss Aversion)
- 锚定效应 (Anchoring)
- 后见之明 (Hindsight Bias)
- 幸存者偏差 (Survivorship Bias)
- 赌徒谬误 (Gambler's Fallacy)
- 现状偏差 (Status Quo Bias)

## 使用方式

当需要评分时，调用 `decision_log/decision_<id>.json` 模板。

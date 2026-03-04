# Adaptive Strategy Engine

## 状态机

| 状态 | 含义 | 触发条件 |
|------|------|----------|
| STABLE | 稳定 | 正常状态 |
| DRIFTING | 偏离 | 连续3次决策评分 < 30 |
| MISALIGNED | 错位 | 风险暴露↑ + 评分↓ |
| RECONSTRUCTION_REQUIRED | 需重构 | 资本结构恶化 > 15% |

## 监控指标

### 1. 决策质量趋势
- 窗口: 最近10次决策
- 趋势: rising / neutral / falling
- 阈值: 平均分 < 30 进入 DRIFTING

### 2. 资本增长趋势
- 窗口: 最近30天
- 变化率: 百分比
- 阈值: 下降 > 15% 进入 RECONSTRUCTION_REQUIRED

### 3. 风险暴露
- 维度: 财务、健康、职业、关系
- 等级: low / medium / high / critical
- 阈值: 风险↑ + 评分↓ 进入 MISALIGNED

### 4. 战略一致性评分
- 满分: 100
- 阈值: < 60 触发警告

## 状态转换规则

```
STABLE ──(连续3次低分)──→ DRIFTING
DRIFTING ──(评分恢复)──→ STABLE
DRIFTING ──(风险↑+评分↓)──→ MISALIGNED
MISALIGNED ──(风险缓解)──→ DRIFTING
MISALIGNED ──(资本恶化)──→ RECONSTRUCTION_REQUIRED
RECONSTRUCTION_REQUIRED ──(用户确认)──→ STABLE
```

## 使用方式

1. 每次决策评分后 → 更新 decision_quality_trend
2. 定期检查资本变化 → 更新 capital_growth_trend
3. 识别风险信号 → 更新 risk_exposure
4. 定期评估一致性 → 更新 strategy_consistency

## 输出

- 系统自动诊断状态
- 进入 MISALIGNED / RECONSTRUCTION_REQUIRED 时生成重构建议
- 仅提出方案，不自动执行

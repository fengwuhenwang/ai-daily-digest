# Auto Mode 手册

## 模式列表

### 1. weekly_scan (每周扫描)
- **间隔**: ≥ 7天
- **Token预算**: 3000
- **任务**: 检查项目状态、任务进度、待办事项
- **触发**: 距上次运行≥7天

### 2. risk_alert (风险警报)
- **间隔**: ≥ 1天
- **Token预算**: 2000
- **触发条件**: 检测到健康/财务/法律/职业/关系/心理风险
- **任务**: 扫描用户环境，识别风险信号

### 3. strategy_review (战略回顾)
- **间隔**: ≥ 30天
- **Token预算**: 5000
- **任务**: 复盘目标进度、调整策略、更新战略
- **触发**: 距上次运行≥30天

## 执行规则

1. 每天最多执行一次Auto任务
2. 每次只运行一种模式（优先级: risk_alert > weekly_scan > strategy_review）
3. 禁止多Agent
4. 禁止递归调用
5. 输出简版摘要，完整结果写文件

## 输出位置

- `memory/auto/weekly_scan_YYYY-MM-DD.md`
- `memory/auto/risk_alert_YYYY-MM-DD.md`
- `memory/auto/strategy_review_YYYY-MM-DD.md`

## 状态管理

状态文件: `scheduler/auto_state.json`

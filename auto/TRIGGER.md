# Auto Mode 触发器

## 使用方式

在心跳或定时任务中调用此模块。

## 触发条件检查

```json
{
  "check": true,
  "mode": "auto_check"
}
```

## 状态读取

读取 `scheduler/auto_state.json` 获取:
- 各模式上次运行时间
- 间隔是否满足
- Token预算

## 执行流程

1. 读取 auto_state.json
2. 检查今天是否已运行
3. 按优先级检查各模式是否满足触发条件
4. 执行对应模式
5. 更新状态文件
6. 输出简版摘要

## 优先级

1. risk_alert (如满足触发条件)
2. weekly_scan (距上次≥7天)
3. strategy_review (距上次≥30天)

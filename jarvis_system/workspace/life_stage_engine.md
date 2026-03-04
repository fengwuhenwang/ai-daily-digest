# Life Stage Engine - 人生阶段引擎

## 阶段定义

| 阶段 | 英文 | 特征 | 策略重点 |
|------|------|------|---------|
| 探索期 | exploration | 不确定方向，尝试多种可能 | 广度学习，多方尝试 |
| 积累期 | accumulation | 明确方向，持续投入 | 深度学习，资源积累 |
| 突破期 | breakthrough | 积累足够，寻求突破 | 聚焦关键，精准打击 |
| 转型期 | transition | 重大改变，重新定义 | 谨慎决策，稳健过渡 |
| 稳定期 | stability | 达到目标，维持状态 | 风险控制，保持优势 |

---

## 识别算法

```python
def assess_life_stage(user_model):
    """评估当前人生阶段"""
    
    indicators = {
        "direction_clarity": measure_direction_clarity(user_model),
        "resource_accumulation": measure_resource_level(user_model),
        "stability_level": measure_stability(user_model),
        "risk_appetite": measure_risk_appetite(user_model)
    }
    
    # 决策树
    if indicators["direction_clarity"] < 0.3:
        return "exploration"
    elif indicators["resource_accumulation"] < 0.5:
        return "accumulation"
    elif indicators["stability_level"] < 0.6:
        return "breakthrough"
    elif indicators["stability_level"] < 0.8:
        return "transition"
    else:
        return "stability"
```

---

## 阶段特征指标

### Exploration (探索期)
- 方向不明确
- 尝试多种领域
- 风险承受力高
- 学习投入大

### Accumulation (积累期)
- 方向已明确
- 持续学习成长
- 资源逐步积累
- 风险承受适中

### Breakthrough (突破期)
- 积累足够
- 寻求质的飞跃
- 聚焦关键机会
- 风险承受较高

### Transition (转型期)
- 重大变化
- 重新定义目标
- 谨慎决策
- 风险承受降低

### Stability (稳定期)
- 目标达成
- 维持现状
- 风险控制优先
- 稳定收益为主

---

## 阶段转换检测

```python
def detect_stage_transition(old_stage, new_stage, evidence):
    """检测阶段转换"""
    
    if old_stage != new_stage:
        return {
            "triggered": True,
            "from": old_stage,
            "to": new_stage,
            "confidence": calculate_confidence(evidence),
            "recommendation": get_stage_recommendation(new_stage),
            "alert_level": assess_change_impact(old_stage, new_stage)
        }
    
    return {"triggered": False}
```

---

## 阶段适配策略

### 探索期策略
- 广泛学习，不急于定方向
- 保持开放心态
- 控制试错成本
- 记录各种尝试结果

### 积累期策略
- 专注核心领域
- 建立知识体系
- 积累资源人脉
- 制定长期计划

### 突破期策略
- 识别关键机会
- 集中资源突破
- 保持战略定力
- 做好风险管理

### 转型期策略
- 充分评估风险
- 制定详细计划
- 保持现有稳定
- 谨慎推进转型

### 稳定期策略
- 控制风险为主
- 优化现有配置
- 保持竞争优势
- 关注新兴机会

---

## 用户当前阶段

当前识别结果：**accumulation (积累期)**

识别依据：
- 方向相对明确（能力提升、财富增长）
- 处于资源积累阶段
- 学习意愿强烈
- 风险承受适中

---

## API接口

### 获取当前阶段
```python
def get_current_stage():
    user = read_json("workspace/user_model/user_model.json")
    return user["current_stage"]
```

### 更新阶段
```python
def update_stage(new_stage, evidence):
    user = read_json("workspace/user_model/user_model.json")
    user["current_stage"] = {
        "stage": new_stage,
        "confidence": calculate_confidence(evidence),
        "indicators": extract_indicators(evidence),
        "last_assessed": get_current_iso_timestamp()
    }
    write_json("workspace/user_model/user_model.json", user)
```

---

## 版本
- Version: 1.0
- Updated: 2026-02-21

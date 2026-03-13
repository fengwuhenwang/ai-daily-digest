# AI 日报 - 技术文档

## 架构

- **GitHub Pages**: https://fengwuhenwang.github.io/ai-daily-digest/
- **数据源**: `data.json` (动态加载)
- **渲染**: `index.html` 从 data.json 读取并动态渲染

## 更新流程

### 只需要更新 data.json
```json
{
  "date": "2026-03-13",
  "headline": {
    "title": "标题",
    "summary": "摘要"
  },
  "entries": [
    {
      "id": 1,
      "title": "文章标题",
      "summary": "摘要",
      "content": "完整内容（可选）",
      "category": "action|tools|business|analysis|learning",
      "source": "来源",
      "time": "09:00"
    }
  ]
}
```

### Category 分类
- `action` → 行动计划
- `tools` → 工具维护  
- `business` → 业务分析
- `analysis` → 数据洞察
- `learning` → 学习研究

### 部署命令
```bash
cd ai-daily-digest-repo
git add data.json
git commit -m "Update $(date +%Y-%m-%d)"
git push origin main
```

## 注意事项

### ⚠️ 历史问题（已修复）
- **问题**：index.html 之前是硬编码静态内容
- **原因**：每次只更新 data.json，没同步 index.html
- **修复**：index.html 改为动态渲染，从 data.json 读取
- **结果**：现在只需更新 data.json，无需动 index.html

## GitHub Pages 缓存
- 更新后通常 1-2 分钟生效
- 如遇缓存，尝试：`Ctrl+Shift+R` 强制刷新

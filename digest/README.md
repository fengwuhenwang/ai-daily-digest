# AI Daily Digest - GitHub Pages 部署指南

## 快速部署

### 1. 创建 GitHub 仓库
- 访问 https://github.com/new
- 仓库名: `ai-daily-digest`
- 选择 Public
- 勾选 "Add a README file"

### 2. 上传文件
将以下文件上传到仓库：
- `index.html` - 主页面
- `data.json` - 日报数据
- `.github/workflows/deploy.yml` - 自动部署配置

### 3. 启用 GitHub Pages
- 进入仓库 Settings → Pages
- Source 选择 "Deploy from a branch"
- Branch 选择 "main" / "/ (root)"
- 保存后获得链接: `https://你的用户名.github.io/ai-daily-digest`

## 本地预览
```bash
# 进入 digest 目录
cd digest

# 启动本地服务器
npx serve .

# 访问 http://localhost:3000
```

## 更新日报
运行本地脚本后，数据会更新到 `data.json`，
通过 Git 推送到 GitHub 即可自动更新网页。

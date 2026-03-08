# AI 日报 - GitHub Pages 部署包

## 📦 部署步骤

### 第一步：创建 GitHub 仓库
1. 访问 https://github.com/new
2. 仓库名称填写：`ai-daily-digest`
3. 选择 **Public**（公开）
4. 勾选 ✅ **Add a README file**
5. 点击 **Create repository**

### 第二步：上传文件
将 `digest` 文件夹中的以下文件上传到仓库：
```
├── index.html          (主页面)
├── data.json           (日报数据)
├── README.md           (说明文档)
└── .github/
    └── workflows/
        └── deploy.yml  (自动部署配置)
```

上传方法（任选一种）：
- **网页上传**：直接拖放文件到 GitHub 网页
- **Git命令**：见下方

### 第三步：启用 GitHub Pages
1. 进入仓库页面
2. 点击 **Settings** → **Pages**（左侧菜单）
3. **Source** 选择：`Deploy from a branch`
4. **Branch** 选择：`main` / `/(root)`
5. 点击 **Save**
6. 等待 1-2 分钟，获得链接：`https://fengwuhenwang.github.io/ai-daily-digest`

---

## 🔄 使用 Git 命令部署（推荐）

### 1. 安装 Git
https://git-scm.com/download/win

### 2. 配置 Git
```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

### 3. 克隆仓库并上传
```bash
# 克隆仓库
git clone https://github.com/fengwuhenwang/ai-daily-digest.git
cd ai-daily-digest

# 复制文件（从 OpenClaw workspace）
copy C:\Users\Pony\.openclaw\workspace\digest\index.html .\ncopy C:\Users\Pony\.openclaw\workspace\digest\data.json .\ncopy C:\Users\Pony\.openclaw\workspace\digest\README.md .\

# 创建 GitHub Actions 目录
mkdir .github\workflows
copy C:\Users\Pony\.openclaw\workspace\digest\.github\workflows\deploy.yml .github\workflows\

# 提交并推送
git add -A
git commit -m "初始化日报系统"
git push origin main
```

---

## 📱 日常使用

### 更新日报后推送到 GitHub
```bash
# 进入仓库目录
cd ai-daily-digest

# 复制最新数据
copy C:\Users\Pony\.openclaw\workspace\digest\current.json .\data.json

# 提交更新
git add -A
git commit -m "更新日报: $(date)"
git push origin main
```

或使用提供的脚本：
```bash
# Windows
.\deploy.bat "更新日报"

# Mac/Linux
./deploy.sh "更新日报"
```

---

## 🌐 访问地址
部署完成后，访问：
```
https://fengwuhenwang.github.io/ai-daily-digest
```

---

## ✅ 完成检查清单
- [ ] 创建 GitHub 仓库 `ai-daily-digest`
- [ ] 上传 index.html 和 data.json
- [ ] 启用 GitHub Pages
- [ ] 设置每天定时更新（可选）
- [ ] 手机收藏网页快捷方式

有任何问题告诉我！

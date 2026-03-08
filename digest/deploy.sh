#!/bin/bash
# GitHub Pages 部署脚本
# 用法: ./deploy.sh "提交信息"

REPO_URL="https://github.com/fengwuhenwang/ai-daily-digest.git"
COMMIT_MSG=${1:-"更新日报 $(date '+%Y-%m-%d %H:%M')"}

echo "🚀 开始部署到 GitHub Pages..."

# 检查是否在git仓库中
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
    git remote add origin $REPO_URL
fi

# 同步数据
echo "🔄 同步数据..."
cp ../digest/current.json ./data.json 2>/dev/null || true

# 添加文件
git add -A

# 提交
echo "💾 提交更改: $COMMIT_MSG"
git commit -m "$COMMIT_MSG" || echo "没有需要提交的更改"

# 推送
echo "📤 推送到 GitHub..."
git push -u origin main || git push origin main

echo "✅ 部署完成！"
echo "🌐 访问地址: https://你的用户名.github.io/ai-daily-digest"

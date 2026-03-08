@echo off
chcp 65001 >nul
REM GitHub Pages 部署脚本 (Windows)
REM 用法: deploy.bat "提交信息"

set REPO_URL=https://github.com/fengwuhenwang/ai-daily-digest.git
if "%~1"=="" (
    set COMMIT_MSG=更新日报 %date% %time:~0,5%
) else (
    set COMMIT_MSG=%~1
)

echo 🚀 开始部署到 GitHub Pages...

REM 检查是否在git仓库中
if not exist ".git" (
    echo 📦 初始化Git仓库...
    git init
    git remote add origin %REPO_URL%
)

REM 同步数据
echo 🔄 同步数据...
copy ..\digest\current.json .\data.json >nul 2>&1

REM 添加文件
git add -A

REM 提交
echo 💾 提交更改: %COMMIT_MSG%
git commit -m "%COMMIT_MSG%"
if errorlevel 1 echo 没有需要提交的更改

REM 推送
echo 📤 推送到 GitHub...
git push -u origin main 2>nul || git push origin main

echo ✅ 部署完成！
echo 🌐 访问地址: https://你的用户名.github.io/ai-daily-digest
pause

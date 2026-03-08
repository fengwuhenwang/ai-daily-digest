# AI Daily Digest - 快速上传包

## 📦 使用方法（无需命令行）

### 1. 创建仓库
- 访问 https://github.com/new
- 仓库名：`ai-daily-digest`
- 选择 **Public**
- ✅ 勾选 "Add a README file"
- 点击 **Create repository**

### 2. 上传文件（网页拖拽）
1. 在新仓库页面，点击 **"uploading an existing file"** 链接
2. 将以下文件拖放到上传区域：
   - `index.html`
   - `data.json`
   - `README.md`
3. 点击 **Commit changes**

### 3. 创建工作流目录
1. 点击 **"Add file"** → **"Create new file"**
2. 文件名输入：`.github/workflows/deploy.yml`
3. 将 deploy.yml 内容粘贴进去
4. 点击 **Commit new file**

### 4. 启用 GitHub Pages
1. 点击 **Settings**（顶部标签）
2. 左侧菜单点击 **Pages**
3. **Source** 选择 `Deploy from a branch`
4. **Branch** 选择 `main` / `/(root)`
5. 点击 **Save**

### 5. 完成！
等待 1-2 分钟后访问：
```
https://fengwuhenwang.github.io/ai-daily-digest
```

---

## 🔄 后续更新

当日报内容更新后：
1. 进入仓库页面
2. 点击 `data.json` 文件
3. 点击右上角 **铅笔图标**（Edit）
4. 删除旧内容，粘贴新的 data.json 内容
5. 点击 **Commit changes**

网站会自动更新！

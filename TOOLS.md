# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## 本地工具

### PDF解析

```bash
node parse-pdf.js <pdf路径>
```

- 自动尝试多种解析方法
- 支持中英文PDF
- 输出文本内容

### Excel解析

```bash
node -e "const XLSX = require('./node_modules/xlsx'); ..."
```

- 已安装xlsx包
- 支持xlsx, xls, csv格式

### Cron 时间基准规则

- **所有时间锚点以系统时间(session_status显示的Time)为准**
- 设置提醒时需先调用 session_status 确认当前系统时间
- 用户说"周一"等相对时间时，基于系统时间计算正确日期

---

Add whatever helps you do your job. This is your cheat sheet.

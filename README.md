# DeepSeek Harness (DSH) 插件实操手册 · 中文版

> 把「能装的插件」变成「能照着做的教程」。一份面向中文用户的 DSH 插件上手、选型与排错指南，由社区共建维护。

[![语言：简体中文](https://img.shields.io/badge/语言-简体中文-blue.svg)](https://www.workbuddy.cn)
[![许可：CC0](https://img.shields.io/badge/license-CC0-green.svg)](./LICENSE)
[![收录插件](https://img.shields.io/badge/收录插件-70%2B-brightgreen.svg)](./README.md)

---

## 这是什么？

[DeepSeek Harness（简称 `dsh`）](https://github.com/deepseek-ai/DeepSeek-Harness) 是深度求索开源的 agent harness：它既是一个可直接运行的 Coding Agent（Web / headless 两种形态），底层又是一套「**一切皆插件**」的框架——模型、工具、沙箱、会话存储、UI、甚至 Agent Loop 本身都是插件。

**本手册的目标**：不只罗列「有哪些插件」，而是告诉你「**我想要 X 能力，该装哪个、怎么装、踩过什么坑**」。它按「需求场景」而不是「官方分类」来组织，更适合新手直接照搬。

> ⚠️ 安全警告：安装插件等于在机器上运行第三方代码，权限与你自己一样大。安装前务必看一眼源码；不熟的插件请先在**无密钥环境**试用。

---

## 目录

- [3 分钟上手](#3-分钟上手)
- [按需求场景选插件](#按需求场景选插件)
- [全分类速览](#全分类速览)
- [安全须知](#安全须知)
- [常见故障排查](#常见故障排查)
- [贡献与共建](#贡献与共建)

---

## 3 分钟上手

### 1. 先有 DSH

DSH 目前以 Web UI 为主。官方推荐用桌面壳套一个原生窗口：

- [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop)
- [hairyf/deepseek-harness-desktop](https://github.com/hairyf/deepseek-harness-desktop)
- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop)

### 2. 安装插件（两种姿势）

**方式 A · 官方市场（推荐新手）**

```sh
dsh plugin --profile web add dshmarket
```

装好 [dsh-market](https://github.com/dsh-market/dsh-market) 后，可在界面里一键安装 / 升级本手册提到的所有插件。

**方式 B · 命令行直装**

```sh
# 通用语法：dsh plugin add <owner/repo>
dsh plugin --profile web add omdsh-dev/dsh-at-file
```

**找插件神器**（可选，装上后直接问 Agent「我想要 X 插件」）：

```sh
dsh plugin --profile web add dsh-find-plugin
```

> 收录标准：只要插件声明了 `dsh.bundle` manifest、能通过 `dsh plugin add` 安装，即可被本手册收录。来源客户端无关。

---

## 按需求场景选插件

下面按「你想干什么」来挑，而不是按官方分类。每个条目都给了仓库和一句话用途，可直接 `dsh plugin add`。

### 🎨 外观 / 主题 / 字体

想要更像 Codex、改配色、调字号、统一视觉风格：

| 需求 | 插件 | 说明 |
|------|------|------|
| 主题皮肤切换 | [EternalNight996/dsh-theme](https://github.com/EternalNight996/dsh-theme) | 内置/图片/视频壁纸皮肤，侧边栏一键切换 |
| UI 样式统一协调 | [Physicolor/dsh-ui-harmonizer](https://github.com/Physicolor/dsh-ui-harmonizer) | 协调已装插件的样式冲突，统一设计语言 |
| 对话页重排（Codex 版式） | [ChuanTianML/dsh-chat-tidy](https://github.com/ChuanTianML/dsh-chat-tidy) | 14/22px 正文、紧凑标题层级 |
| UI/UX 设计智能库 | [ChenYiming-aaa/dsh-ui-ux-pro-max](https://github.com/ChenYiming-aaa/dsh-ui-ux-pro-max) | 84 种风格、192 配色、设计评审工具 |
| 浅色主题 | [jiangnanquan/dsh-ux](https://github.com/jiangnanquan/dsh-ux) | Solarized 浅色 + 折叠胶囊 |
| 字体引擎 | [warmwine/dsh-ui-font](https://github.com/warmwine/dsh-ui-font) | 全局/逐组件字号微调，老花眼友好 |
| 节点着色 | [Max-Null/dsh-node-appearance](https://github.com/Max-Null/dsh-node-appearance) | 按工具/类别给会话节点上色 |

### 💰 余额 / 用量 / 计费（涨→红、跌→绿，遵循 A 股习惯）

| 需求 | 插件 | 说明 |
|------|------|------|
| 多厂商余额一览 | [GeekRicardo/dsh-balance](https://github.com/GeekRicardo/dsh-balance) | DeepSeek/Kimi/智谱/OpenRouter 等余额，2s 轮询 |
| 高峰/闲时状态 | [future007s/dsh-peak-indicator](https://github.com/future007s/dsh-peak-indicator) | 头部徽标显示峰谷价与每轮费用 |
| 底部信息栏 | [songoao25/dsh-bottom-info-bar](https://github.com/songoao25/dsh-bottom-info-bar) | 服务商/余额/今日·本月花费 |
| 鲸鱼余额挂件 | [MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) | 右下角常驻，带音效 |
| 峰谷电表 | [uckkk/dsh-valley-meter](https://github.com/uckkk/dsh-valley-meter) | 24h 峰谷时间轴 + 10 套配色 |
| 头部余额按钮 | [lmmzss-jk/dsh-plugin-balance](https://github.com/lmmzss-jk/dsh-plugin-balance) | 缓存命中率与费用估算 |

### 📎 文件上传 / 拖拽 / `@file` 引用

| 需求 | 插件 | 说明 |
|------|------|------|
| `@file` 文件引用 | [omdsh-dev/dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) | Codex 风格，搜索并引用工作区文件 |
| 任意文件 @ 提及 | [hatsuyuki0103/dsh-at-any](https://github.com/hatsuyuki0103/dsh-at-any) | 覆盖所有格式，无索引上限 |
| 拖拽上传 | [GLFzr/dsh-drop-file-to-path](https://github.com/GLFzr/dsh-drop-file-to-path) | 拖入即存 `~/.dsh-dropbox` 并插路径 |
| DS 同款附件 | [wqx-txdsyl/dsh-ds-attach](https://github.com/wqx-txdsyl/dsh-ds-attach) | chat.deepseek.com 风格彩色附件卡片 |
| 附件卡片与历史 | [WJZ-P/dsh-attachments](https://github.com/WJZ-P/dsh-attachments) | 拖放附件 + 持久化历史 |

### 🗂️ 文件树 / 编辑器 / 工作台（类 IDE）

| 需求 | 插件 | 说明 |
|------|------|------|
| 完整工作台 | [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | 文件/终端/Git/子代理，支持三方 Tab |
| IDE 工作台 | [loadingvx/deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) | 三栏、Monaco 编辑、Git 面板 |
| VS Code 编辑器 | [yangshen830-eng/dsh-editor](https://github.com/yangshen830-eng/dsh-editor) | 文件树 + Monaco + 差异 |
| 工作区浏览器 | [Jiyr0119/dsh-workspace-explorer](https://github.com/Jiyr0119/dsh-workspace-explorer) | 动画弹窗 + 搜索 + 中英双语 |

### 🖥️ 终端

| 需求 | 插件 | 说明 |
|------|------|------|
| 终端面板 | [giiiiiithub/terminal](https://github.com/giiiiiithub/terminal) | node-pty + xterm.js，多标签 |
| 底部终端 | [siberiah2o/dsh-plugin-terminal](https://github.com/siberiah2o/dsh-plugin-terminal) | 贴底全宽，输入框始终在上 |

### 🪟 桌面壳 / 启动器 / 系统托盘

| 需求 | 插件 | 说明 |
|------|------|------|
| macOS 原生窗口 | [MDR-EX1000/dsh-desktop-kit](https://github.com/MDR-EX1000/dsh-desktop-kit) | Tauri/WKWebView 原生全屏 |
| 原生桌面壳（Tauri） | [dsh-tauri-desk/deepseek-harness-desktop](https://github.com/dsh-tauri-desk/deepseek-harness-desktop) | 仅 5MB 安装包、零环境配置、预设开箱即用 |
| Windows 托盘壳 | [RAFOLIE/dsh-desktop-windowos](https://github.com/RAFOLIE/dsh-desktop-windowos) | Releases 自动安装升级 |
| 纯净桌面壳 | [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) | 托盘启停、离线重连 |
| 系统托盘 | [wodongx123/dsh-desktop-tray](https://github.com/wodongx123/dsh-desktop-tray) | 最小化/关闭隐藏到托盘 |
| Windows 启动器 | [HUITianYi/dsh-whale-desktop-launcher](https://github.com/HUITianYi/dsh-whale-desktop-launcher) | 鲸鱼娘图标 Chromium 窗口 |

### 📱 移动端 / 响应式

| 需求 | 插件 | 说明 |
|------|------|------|
| 移动端适配 | [TecFancy/dsh-mobile](https://github.com/TecFancy/dsh-mobile) | 抽屉浮层、桌面零回归 |
| 手机 Web 修复 | [Odefined/dsh-mobile-webui](https://github.com/Odefined/dsh-mobile-webui) | 手势 + 纯图标 composer |
| PWA + 推送 | [jasondu/dsh-ui-mobile](https://github.com/jasondu/dsh-ui-mobile) | 可安装 PWA、Web Push |
| 移动端 UI 套件 | [TZHR-invest/dsh-plugins#dsh-mobile-ui](https://github.com/TZHR-invest/dsh-plugins/tree/main/packages/dsh-mobile-ui) | 44px 触摸目标、安全区适配 |
| Android 原生客户端 | [woaiys3/deepseek-harness-android-app](https://github.com/woaiys3/deepseek-harness-android-app) | 可直接安装的 Android APK，免 Root 操作手机 |

### 🧠 记忆 / AGI / 上下文

| 需求 | 插件 | 说明 |
|------|------|------|
| 白箱 AGI 探索 | [FuRongJun-1999/dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) | 元认知、世界模型、自我改进 |
| 回退上下文 | [dygin/dsh-recover-context](https://github.com/dygin/dsh-recover-context) | 回到任意提问前并还原工作区 |
| 上下文洞察与管理 | [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) | 上下文用量洞察、压缩与回收建议 |

### ✨ 提示词优化 / 润色

| 需求 | 插件 | 说明 |
|------|------|------|
| 一键优化 | [winditer/dsh-prompt-optimizer](https://github.com/winditer/dsh-prompt-optimizer) | Alt+O，复用当前模型流式改写 |
| 前后对比 | [SongMiao-tech/dsh-prompt-optimizer](https://github.com/SongMiao-tech/dsh-prompt-optimizer) | 弹窗对比、一键替换 |
| 草稿增强 | [LCQ-1024/dsh-prompt-enhancer](https://github.com/LCQ-1024/dsh-prompt-enhancer) | 改写为可执行 prompt |

### 🧭 导航 / 大纲 / 跳转（长会话必备）

| 需求 | 插件 | 说明 |
|------|------|------|
| 对话地图 | [GeekRicardo/dsh-convmap](https://github.com/GeekRicardo/dsh-convmap) | 左缘刻度 + 全量导航 |
| 画卷式导轨 | [Max-Null/dsh-chat-rail](https://github.com/Max-Null/dsh-chat-rail) | 右侧竖排导轨，scroll-spy |
| 实时大纲 | [urzeye/dsh-outline](https://github.com/urzeye/dsh-outline) | Markdown 标题树 + 搜索 |
| 提问索引 | [lijinhao315/dsh-question-index](https://github.com/lijinhao315/dsh-question-index) | 右侧你提过的问题列表 |

### ⌨️ 终端 TUI / 全屏界面

| 需求 | 插件 | 说明 |
|------|------|------|
| ~~全屏 TUI（已失效）~~ | ~~[ccq1/dsh-TUI](https://github.com/ccq1/dsh-TUI)~~ | 仓库已 404，请改用下方社区维护版本 |
| 全屏 TUI | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚 |
| 终端工作台 | [lk251066/dsh-tui-pro](https://github.com/lk251066/dsh-tui-pro) | 多会话、结构化视图 |
| Rust TUI | [openma-ai/Martty](https://github.com/openma-ai/Martty) | ratatui，持久会话 |

### 🐳 桌面宠物

| 需求 | 插件 | 说明 |
|------|------|------|
| 桌面级桌宠 | [cookiesheep/whale-on-desk](https://github.com/cookiesheep/whale-on-desk) | 29 帧状态，盖得住全屏 |
| 像素办公室 | [EternalNight996/dsh-ui-agents-pixe](https://github.com/EternalNight996/dsh-ui-agents-pixe) | 508 张角色卡 |
| Codex 桌宠迁移 | [mengyun233/dsh-codex-pet](https://github.com/mengyun233/dsh-codex-pet) | 毛玻璃对话框 + 设置面板 |

### 📈 行情 / 股票（A 股红涨绿跌）

| 需求 | 插件 | 说明 |
|------|------|------|
| A股/港股/美股 | [FeiZhuNiU-INFJA/dsh-stock-ticker](https://github.com/FeiZhuNiU-INFJA/dsh-stock-ticker) | 上证/创业板/科创50/恒生科技，红涨绿跌 |
| 雪球面板 | [kangjinghang/dsh-xueqiu](https://github.com/kangjinghang/dsh-xueqiu) | K线蜡烛图、热榜、7×24 快讯 |

### 🔀 MCP / 设置扩展

| 需求 | 插件 | 说明 |
|------|------|------|
| MCP 可视化管理 | [Js2Hou/dsh-mcp-manager](https://github.com/Js2Hou/dsh-mcp-manager) | 设置页增删启停 MCP |
| 设置扩展 | [omdsh-dev/ex-setting](https://github.com/omdsh-dev/ex-setting) | DSH 设置扩展 |
| 规则管理 | [wzz3034026545/dsh-rule-manager](https://github.com/wzz3034026545/dsh-rule-manager) | 统一管理 AGENTS.md |

### 🧩 技能 / 提示词库 / 任务看板

| 需求 | 插件 | 说明 |
|------|------|------|
| 技能管理器 | [lcthe/dsh-skills-hub](https://github.com/lcthe/dsh-skills-hub) | 导入/启用/禁用技能 |
| 任务看板 | [1070296335-create/dph-taskboard](https://github.com/1070296335-create/dph-taskboard) | 待办/进行中/评审/完成 四列 |
| 定时任务 | [magicOF2/dsh-schedule](https://github.com/magicOF2/dsh-schedule) | 每日/每周/一次性日程 |

---

## 全分类速览

DSH 生态目前大致按 22 个官方分类组织。下表是导航地图，括号内为每类的代表插件（部分来自已采集数据）：

| 分类 | 关注点 | 代表插件 |
|------|--------|----------|
| 🧭 AGI 架构探索 | 白箱/世界模型 | [FuRongJun-1999/dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) |
| 🎨 UI 增强 | 界面/布局/交互 | [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) |
| 💰 用量与计费 | 余额/成本 | [GeekRicardo/dsh-balance](https://github.com/GeekRicardo/dsh-balance) |
| 🎭 主题与外观 | 皮肤/壁纸 | [EternalNight996/dsh-theme](https://github.com/EternalNight996/dsh-theme) |
| 🔌 模型与账号接入 | 模型/Provider | （待补充，欢迎共建） |
| 🆔 身份与通信 | 账号/IM 接入 | （待补充，欢迎共建） |
| 💬 会话与消息 | 会话管理 | [urzeye/dsh-outline](https://github.com/urzeye/dsh-outline) |
| 🧠 记忆 | 长期记忆 | [dygin/dsh-recover-context](https://github.com/dygin/dsh-recover-context) |
| 🛠️ 工具与能力 | 能力扩展 | （待补充，欢迎共建） |
| 🌐 浏览器与网页 | 网页交互 | （待补充，欢迎共建） |
| 🖼️ 视觉与多模态 | 图片/视频 | [Nagi-ovo/dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) · [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) |
| 🎙️ 语音与音频 | 语音输入 | （待补充，欢迎共建） |
| 📄 文档与渲染 | 文档/Markdown | [jiuyuechuwuhao/dsh-canvas-preview](https://github.com/jiuyuechuwuhao/dsh-canvas-preview) |
| 🧩 技能包 | Skill | [lcthe/dsh-skills-hub](https://github.com/lcthe/dsh-skills-hub) |
| 🔁 工作流与自动化 | 定时/重复 | [magicOF2/dsh-schedule](https://github.com/magicOF2/dsh-schedule) |
| 🔀 Git 与代码评审 | Git | [loadingvx/deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) |
| 🔔 通知与集成 | 提醒/推送 | [Phant0Meow/dsh-meow-smooth](https://github.com/Phant0Meow/dsh-meow-smooth) |
| 🧑‍💻 开发与运行时 | 开发/运行时 | （待补充，欢迎共建） |
| 🔒 安全与权限 | 权限/审计 | （待补充，欢迎共建） |
| 📱 远程与移动端 | 移动/远程 | [TecFancy/dsh-mobile](https://github.com/TecFancy/dsh-mobile) |
| 🛒 插件市场与管理 | 市场/管理 | [dsh-market](https://github.com/dsh-market/dsh-market) · [dshfind](https://github.com/hikariming/dshfind) |
| 🎮 娱乐 | 趣味 | [cookiesheep/whale-on-desk](https://github.com/cookiesheep/whale-on-desk) |

> 上表中标注「待补充，欢迎共建」的分类，代表插件暂未收入本手册——欢迎在 Issue/PR 里补充你用过的同类插件，让它更完整。

---

## 安全须知

- 安装插件 = 运行第三方代码，权限与你的用户相同。**装前看源码**。
- 不熟悉的插件，先在**无密钥环境**（无生产凭据）试用。
- 不做优劣「排名」：本手册以「可安装、描述一致、场景有用」为收录标准，不替你评判插件好坏。
- 所有插件均为社区维护，风险自负。

---

## 常见故障排查

**Q：装了插件但界面没变化？**
- 确认安装命令用了 `--profile web`（Web 端）或对应 profile。
- 部分插件需要先在 `dsh-market` 安装依赖包（如 `dsh-status-card` 需要 `@omdsh-dev/dsh-genui`）。
- 重启会话 / 重启 DSH 进程（可用 [miisaka19800/dsh-restart-fab](https://github.com/miisaka19800/dsh-restart-fab) 一键重启）。

**Q：插件之间样式冲突？**
- 用 [Physicolor/dsh-ui-harmonizer](https://github.com/Physicolor/dsh-ui-harmonizer) 统一视觉语言，或在设置页逐个开关排查。

**Q：想回退到之前的提问？**
- 用 [dygin/dsh-recover-context](https://github.com/dygin/dsh-recover-context) 回退并还原工作区文件。

**Q：长会话卡顿 / 上下文爆炸？**
- 用压缩按钮（[shyuan-hub/dsh-compact-button](https://github.com/shyuan-hub/dsh-compact-button)）或开启自动压缩（[guoliyuan97-png/dsh-game-hud](https://github.com/guoliyuan97-png/dsh-game-hud) 上下文不足自动压缩）。

---

## 贡献与共建

这份手册靠社区变大。欢迎：

1. **推荐插件**：在**本仓库**提交 PR，按现有表格格式补充插件（仓库链接 + 一句话用途 + 安装命令）。
2. **补充场景**：在本仓库提 Issue / PR，把「我要做 X → 装 Y」的经验写进对应章节。
3. **纠错**：发现失效链接、过时命令，直接提 PR。

> 想让手册保持新鲜？可以配置一个周期性自动化，定期扫描各插件仓库的更新与失效链接。

---

## 给仓库的 SEO / 引流建议（让你更容易被搜到）

- **GitHub Topics**：`deepseek-harness`、`dsh`、`dsh-plugin`、`deepseek`、`插件`、`ai-agent`、`plugin-guide`
- **仓库名**（建议）：`dsh-plugin-handbook` 或 `deepseek-harness-plugins-zh`
- **一句话定位**：「中文优先的 DeepSeek Harness 插件实操手册：按场景选插件、照着装、避坑」
- 在 README 顶部保留 shields 徽章与清晰的「按场景选插件」导航，降低新手上手门槛。

---

## License

本手册以 **CC0 1.0** 发布，可自由转载与派生。

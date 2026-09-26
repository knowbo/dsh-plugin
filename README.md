# DeepSeek Harness (DSH) 插件实操手册 · 中文版

> 把「能装的插件」变成「能照着做的教程」。一份面向中文用户的 DSH 插件上手、选型与排错指南，由社区共建维护。

[![语言：简体中文](https://img.shields.io/badge/语言-简体中文-blue.svg)](https://www.workbuddy.cn)
[![许可：CC0](https://img.shields.io/badge/license-CC0-green.svg)](./LICENSE)
[![收录插件](https://img.shields.io/badge/收录插件-530%2B-brightgreen.svg)](./README.md)

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
- [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop)

### 2. 安装插件（两种姿势）

**方式 A · 官方市场（推荐新手）**

```sh
dsh plugin --profile web add dshmarket
```

装好 [dsh-market](https://github.com/dsh-market/dsh-market) 后，可在界面里一键安装 / 升级本手册提到的所有插件。

**方式 B · 命令行直装**

```sh
# 通用语法：dsh plugin add <owner/repo>
dsh plugin --profile web add FSMargoo/dsh-at-file
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
| 皮肤主题 | [caoyiwei850/dsh-client-ui-skins](https://github.com/caoyiwei850/dsh-client-ui-skins) | DSH Web 皮肤插件：内置多套主题 + 自定义图片皮肤 |
| 鲸鱼角色皮肤 | [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | Deep Whale 女仆 Atelier 鲸鱼角色皮肤，重做 Web 视觉 |
| Web 插件聚合包 | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | DSH Web 插件聚合生态包：任务看板、移动端远程、SSH 运维、图像理解一站式 |
| 会话时间线整理 | [BananaSoldier01/dsh-tidychat](https://github.com/BananaSoldier01/dsh-tidychat) | 已完成轮次自动折叠 + 过程/结论分隔线 + 智能加载更早历史 + 左缘定位条 |
| 输入框历史回溯 | [WongYuYe/dsh-composer-recall](https://github.com/WongYuYe/dsh-composer-recall) | 空 composer 按 ↑ 唤回本轮提示、↓ 前进、Esc 还原正在输入的内容 |
| Web 全家桶（聚合根） | [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | Web GUI 插件全家桶 + 皮肤中心（依赖 @linxin666/dsh-web-all，一键装整包皮肤） |
| 壁纸背景 | [nishuoyang/dsh-wallpaper-bg](https://github.com/nishuoyang/dsh-wallpaper-bg) | 内置 / 自定义上传 / Wallpaper Engine 库三源，图片·视频·场景渲染，叠加 / 模糊 / 亮度 / 安全缩放调节 |
| 皮肤创作工坊 | [zhangguiping-xydt/dsh-skin-studio](https://github.com/zhangguiping-xydt/dsh-skin-studio) | 可视化、本地优先的 DSH Web 皮肤编辑器，设计令牌管理与皮肤导出 |
| 外观定制 | [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) | 主题色板、背景图、透明度/模糊、毛玻璃效果 |
| 侧边助手 Dock | [WLV-ZEDD/dsh-btw](https://github.com/WLV-ZEDD/dsh-btw) | 输入 /btw 不打断主循环后台解答，composer 上方浮动横幅 + 实时动画 |
| 电子墨水/复古主题 | [exoticknight/dsh-theme-eink-retro](https://github.com/exoticknight/dsh-theme-eink-retro) | 纸感墨色客户端主题，平衡 / 沉浸双模式 |
| 字体定制 | [citisen/dsh-font](https://github.com/citisen/dsh-font) | 设置里改 Web GUI 字体：界面字体 / 代码字体 + 三个独立字号轴 |
| 输入框体验升级 | [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) | 发送/换行键切换、右键菜单、快捷指令面板、发送前跑单独模型做 prompt 优化、OpenCode 请求头注入 |
| Wallpaper Engine 动态壁纸 | [elysia395/dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine) | 把本机 Wallpaper Engine 壁纸变 DSH 网页背景：视频动态播放、Web 以 iframe 加载、Scene 壁纸提取主纹理，含液态玻璃与可调强调色 |
| 多套换肤主题包 | [RevolutionLA/dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) | 8 套 iOS/Linear 式清透冷调主题 + 弥散光壁纸 + 每用户强调色 + 主题包分享，纯原生 token 系统，支持 DSH Desktop |
| 工业风主题 | [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) | 终末地官网风 DSH Web 主题：奶油纸底、墨黑字、信号黄强调、全直角工业编辑风 |
| 动画电影主题 | [niiang/dsh-kimino-theme](https://github.com/niiang/dsh-kimino-theme) | Kimi no Na wa（你的名字）风格 DSH Web 主题，含壁纸/Logo 资源 |
| 字体微调 | [LyaxZ/dsh-fonttune](https://github.com/LyaxZ/dsh-fonttune) | 字体微调：对话独立字体/字号/行高/字重，可存预设方案 |
| Claude 主题 | [Nwflower/dsh-claude-style](https://github.com/Nwflower/dsh-claude-style) | Claude Code 桌面主题（网页 GUI） |
| mpkg 壁纸 | [XHR666/dsh-mpkg-wallpaper](https://github.com/XHR666/dsh-mpkg-wallpaper) | 把 Wallpaper Engine .mpkg / Steam 工坊当 DSH 网页背景 |
| 外观/主题 | [KylinQ01/dsh-startup-animation](https://github.com/KylinQ01/dsh-startup-animation) | 🌸 给 DeepSeek Harness 的开机动画 + 主界面壁纸：多层动效 + 鼠标视差，两张图可在设置里自由更换并实时预览 |
| 外观/主题 | [Okazaki01/dsh-air-theme](https://github.com/Okazaki01/dsh-air-theme) | 《AIR》夏日青空 — DeepSeek Harness 高定制动漫主题皮肤（浅色/深色）。推荐环境：DSH-Desktop-EAC。反馈：qq2992254… |
| 外观/主题 | [ChenneyZhuang/estimate-before-build](https://github.com/ChenneyZhuang/estimate-before-build) | Estimate-before-build skill: bounded task list, S/M/L/XL band estimates with un… |
| 外观/主题 | [harmless0819-dev/dsh-whale-live2d](https://github.com/harmless0819-dev/dsh-whale-live2d) | Replace the whale widget static image with a Live2D model, stacked at identical… |
| 主题/外观 | [weibaohui/dsh-settings-ui](https://github.com/weibaohui/dsh-settings-ui) | dsh 插件 · 设置界面自定义：调整原生设置窗口大小（全屏/预置/自定义）、背景不透明度与背景（亮暗各一色，实时跟随主题） |
| 主题/外观 | [Andersen216/dsh-whale-girl-live2d](https://github.com/Andersen216/dsh-whale-girl-live2d) | 🐋 鲸鱼娘桌宠 · Whale Girl Live2D —— DSH（DeepSeek Harness）Web 界面里的 Live2D 桌宠：跟… |
| 主题/外观 | [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) | DeepSeek Harness Tavern Plugin - character card roleplay, worldbook mana… |
| 主题/外观 | [LeoLee0097/dsh-desktop-acrylic](https://github.com/LeoLee0097/dsh-desktop-acrylic) | Tokyo Night 暗色 / 亮色主题 for DeepSeek Harness (DSH) 桌面端 —— 注册进主题运行时的真实皮肤，含亚… |
| 主题/外观 | [EphoReal/my-skin-for-DeepSeek-Harness](https://github.com/EphoReal/my-skin-for-DeepSeek-Harness) | DeepSeek Harness 皮肤扩展插件 Skin plugin |

### 💰 余额 / 用量 / 计费（涨→红、跌→绿，遵循 A 股习惯）

| 需求 | 插件 | 说明 |
|------|------|------|
| 多厂商余额一览 | [GeekRicardo/dsh-balance](https://github.com/GeekRicardo/dsh-balance) | DeepSeek/Kimi/智谱/OpenRouter 等余额，2s 轮询 |
| 高峰/闲时状态 | [future007s/dsh-peak-indicator](https://github.com/future007s/dsh-peak-indicator) | 头部徽标显示峰谷价与每轮费用 |
| 底部信息栏 | [songoao25/dsh-bottom-info-bar](https://github.com/songoao25/dsh-bottom-info-bar) | 服务商/余额/今日·本月花费 |
| 侧栏硬件温度看板 | [whiskey1993/dsh-thermal-monitor](https://github.com/whiskey1993/dsh-thermal-monitor) | 左侧栏 CPU/内存/GPU/固态实时温度，含免提权降级模式 |
| 鲸鱼余额挂件 | [MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) | 右下角常驻，带音效 |
| 峰谷电表 | [uckkk/dsh-valley-meter](https://github.com/uckkk/dsh-valley-meter) | 24h 峰谷时间轴 + 10 套配色 |
| 头部余额按钮 | [lmmzss-jk/dsh-plugin-balance](https://github.com/lmmzss-jk/dsh-plugin-balance) | 缓存命中率与费用估算 |
| 会话成本计量 | [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) | 会话/每日成本、预算、历史、官方与自定义 Provider 余额，峰谷计价 + 系统通知预警，90+ 模型价目 |
| 多厂商余额挂件 | [andregoncalves/dsh-balance](https://github.com/andregoncalves/dsh-balance) | DeepSeek/OpenRouter/Kimi/智谱/MiniMax 等余额，轻量零依赖、不补丁核心 |
| 对话底部费用明细 | [david0702/dsh-cost](https://github.com/david0702/dsh-cost) | 按每笔请求时间+模型分批计费，分时段明细、模型归属、读图金额与账户余额 |
| 用量计费仪表盘 | [kenz1117/dsh-ui-usage-billing](https://github.com/kenz1117/dsh-ui-usage-billing) | 侧栏成本指标、会话日志真实用量聚合、多厂商价目目录 |
| Token 面板 | [olimc2016/dsh-token-meter-panel](https://github.com/olimc2016/dsh-token-meter-panel) | Token 用量与花费面板：今日消费/预算/成本构成/缓存命中 |
| 余额/计费 | [PerryLink/dsh-budget](https://github.com/PerryLink/dsh-budget) | Cost governance for DeepSeek Harness: aggregated token/cost metering per model,… |
| 插件 | [Rannist/balance-dsh](https://github.com/Rannist/balance-dsh) | DSH 插件：显示 DeepSeek 账户余额 + 会话 token/费用，含高峰/空闲计费 |
| 余额/计费 | [GooDAnDReaDY/dsh-cost-meter](https://github.com/GooDAnDReaDY/dsh-cost-meter) | DeepSeek Harness plugin: a session cost chip in the conversation header - live … |
| 余额/计费 | [Daviszhou212/dsh-cost-pill](https://github.com/Daviszhou212/dsh-cost-pill) | DSH web plugin: session API cost + account balance, as a pill merged into the o… |
| 余额/计费 | [zhanghao3693/dsh-client-ui-model-clock](https://github.com/zhanghao3693/dsh-client-ui-model-clock) | Model usage clock for DeepSeek Harness — see which model is cheapest right now:… |
| 余额/用量 | [weibaohui/dsh-sync](https://github.com/weibaohui/dsh-sync) | DeepSeek Harness 插件：会话同步与冲突解决（apiproxy、token 内联） |
| 余额/用量 | [weibaohui/context-razor](https://github.com/weibaohui/context-razor) | dsh 插件 · 上下文剃刀：逐条 token 统计 + 精确裁剪会话上下文，不经 LLM 总结 |
| 余额/用量 | [1420079678-ctrl/agent-body](https://github.com/1420079678-ctrl/agent-body) | Gates 84.7% of tool-schema prompt tokens away for DeepSeek Harness: plug… |
| 余额/用量 | [weibaohui/dsh-fireworks](https://github.com/weibaohui/dsh-fireworks) | dsh 插件 · 烟花庆祝引擎：agent 编程时在对话窗口上空放烟花——六类事件 × 30 张属性卡 × 洗牌袋随机变种，token 用量决定… |
| 余额/用量 | [AGImentu/dsh-cost-stats](https://github.com/AGImentu/dsh-cost-stats) | DSH (DeepSeek Harness) Web 插件：每条助手消息旁的费用胶囊 + 设置里的「费用统计」页（逐条计费项、回复与上下文压缩分… |
| 余额/用量 | [webkubor/dsh-llm-hub](https://github.com/webkubor/dsh-llm-hub) | 给 DSH 模型页补上官方适配器缺的那半：网关可达性探测、模型目录拉取并勾选写回、余额/配额常驻、协议与接入地址可见。零运行时依赖，不改动 DS… |
| 余额/用量 | [Ychris12138/dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) | Provider balances, subscription quotas, and token-usage analytics for th… |
| 余额/用量 | [Aa728848/dsh-chatgpt-subscription](https://github.com/Aa728848/dsh-chatgpt-subscription) |  |
| 余额/用量 | [EphoReal/Tokan-dsh-token-analytics](https://github.com/EphoReal/Tokan-dsh-token-analytics) | 精准 Token 洞察，实时追踪，智能优化提示和用量归因 Sharp token insights, real‑time tracking, s… |
| 余额/用量 | [orrinzeng/dsh-cursor-subscription](https://github.com/orrinzeng/dsh-cursor-subscription) | Log directly into your Cursor account within DeepSeek Harness and use yo… |
| 余额/用量 | [wkscc310/dsh-client-ui-cpa-quota](https://github.com/wkscc310/dsh-client-ui-cpa-quota) | Easily view your CLiProxyAPI quota in DeepSeek Harness. |

### 📎 文件上传 / 拖拽 / `@file` 引用

| 需求 | 插件 | 说明 |
|------|------|------|
| `@file` 文件引用 | [FSMargoo/dsh-at-file](https://github.com/FSMargoo/dsh-at-file) | Codex 风格，搜索并引用工作区文件 |
| 任意文件 @ 提及 | [hatsuyuki0103/dsh-at-any](https://github.com/hatsuyuki0103/dsh-at-any) | 覆盖所有格式，无索引上限 |
| 拖拽上传 | [GLFzr/dsh-file-upload](https://github.com/GLFzr/dsh-file-upload) | 拖入即存 `~/.dsh-dropbox` 并插路径 |
| DS 同款附件 | [wqx-txdsyl/dsh-ds-attach](https://github.com/wqx-txdsyl/dsh-ds-attach) | chat.deepseek.com 风格彩色附件卡片 |
| 附件卡片与历史 | [WJZ-P/dsh-attachments](https://github.com/WJZ-P/dsh-attachments) | 拖放附件 + 持久化历史 |
| 粘贴 / 拖拽增强 | [omdsh-dev/dsh-paste-input](https://github.com/omdsh-dev/dsh-paste-input) | Ctrl+V 粘贴 + 拖拽 + 选择文件，发送时进会话临时目录 |
| 收件箱 | [Chance722/dsh-inbox](https://github.com/Chance722/dsh-inbox) | 把复制粘贴的链接/图片/文本/账密收进本地仓库自动分类，可在对话里检索取回 |
| 文件引用/拖拽 | [ChenneyZhuang/backlog-triage](https://github.com/ChenneyZhuang/backlog-triage) | Backlog triage skill: sweep every source into one inventory, classify items int… |
| 文件引用/拖拽 | [chiyu-star499/dsh-folder-drop](https://github.com/chiyu-star499/dsh-folder-drop) | DSH Desktop 插件：把文件夹拖进 composer，得到它的原生绝对路径（DSH 原生只收文件） |

### 🗂️ 文件树 / 编辑器 / 工作台（类 IDE）

| 需求 | 插件 | 说明 |
|------|------|------|
| 完整工作台 | [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | 文件/终端/Git/子代理，支持三方 Tab |
| IDE 工作台 | [loadingvx/deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) | 三栏、Monaco 编辑、Git 面板 |
| VS Code 编辑器 | [yangshen830-eng/dsh-editor](https://github.com/yangshen830-eng/dsh-editor) | 文件树 + Monaco + 差异 |
| 工作区浏览器 | [Jiyr0119/dsh-workspace-explorer](https://github.com/Jiyr0119/dsh-workspace-explorer) | 动画弹窗 + 搜索 + 中英双语 |
| 文件管理器 | [joejojoking-cloud/dsh-file-explorer](https://github.com/joejojoking-cloud/dsh-file-explorer) | 文件树 + 预览 + Markdown + 语法高亮 + 面板内编辑 |
| JetBrains IDE 集成 | [JayZz210l/deepseek-harness-for-ide](https://github.com/JayZz210l/deepseek-harness-for-ide) | 把 DSH 搬进 JetBrains IDE：对话 / 工具审批 / 子代理 |
| Zed ACP 桥接 | [grunmin/dsh-acp-enhanced](https://github.com/grunmin/dsh-acp-enhanced) | Zed 编辑器 ACP 服务，块级流式 + 用量统计 |
| VSCode 式编辑器 | [Lenonss/DSH_VsCodeMode](https://github.com/Lenonss/DSH_VsCodeMode) | Monaco 编辑器（tabs/QuickOpen）、agent 编辑-差异审阅（keep/reject/archive/rollback）、LSP 智能与 VSIX 安装 |
| ~~代码库智能（已失效）~~ | ~~[shinzarou-eng/dsh-codebase-chat](https://github.com/shinzarou-eng/dsh-codebase-chat)~~ | 仓库已不可达（SSH 多次核验失败），如有替代欢迎 PR |
| Markdown 阅读器 | [wjx-ai/dsh-md-reader](https://github.com/wjx-ai/dsh-md-reader) | 会话中 MD/图片链接右侧真三栏阅读，TOC + 图片内联 + 字号缩放 |
| 元文件夹 | [ManoloRemiddi/DSH-Metafolder-Plugin](https://github.com/ManoloRemiddi/DSH-Metafolder-Plugin) | 侧边栏工作区可视化元文件夹：拖拽/菜单将真实文件夹归入可折叠命名组 |
| Codex 风侧栏工作台 | [MichengAI/dsh-codex-ui](https://github.com/MichengAI/dsh-codex-ui) | Codex 风格侧栏、工作区会话树、全局搜索、轮次导航 |
| WSL 工作区 | [6Mikao9/dsh-wsl-workspace](https://github.com/6Mikao9/dsh-wsl-workspace) | 从 Web GUI 添加 WSL 工作区，整段 agent 会话跑在 WSL 内（VS Code Remote-WSL 式），WSL 内免装工具链 |
| 配置备份迁移 | [xiajiajun516/dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) | DSH 配置一键备份/恢复/导出/导入/迁移与同步（设置/插件/MCP/技能/预设/工作区），一键迁移到另一台机器 |
| IDE Git 窗口 | [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) | IDE 级 Git 工具窗口（dsh-better-sidebar 原生 tab）：分支树等 |
| 允许显示工作区的文件树 | [yishengjun8/dsh-workspace-studio](https://github.com/yishengjun8/dsh-workspace-studio) | 允许显示工作区的文件树、浏览文件内容、并且允许对话中嵌入引用的文件内容、自由切换思维分支视图，目标是和VSCode相类似的开发体验 |
| 将code-server | [jinsiyu/dsh-code-server-app](https://github.com/jinsiyu/dsh-code-server-app) | 将code-server（VSCode网页版）打包安装到dsh内的插件，快速实现专业的文件编辑。Package and install code-server… |
| 文件树/工作台 | [TheYoungChen/dsh-annotate](https://github.com/TheYoungChen/dsh-annotate) | Annotate any web element — local or online — with DOM facts and your comments, … |
| 文件树/工作台 | [xiaoyuink/dsh-workbench](https://github.com/xiaoyuink/dsh-workbench) | DSH Web 插件：把资源管理器 / 浏览器 / 真实终端 / 后台任务注册成官方右侧 Sidebar 标签页（含 Office/TIFF/HEIC/PSD… |
| 插件 | [senyayume/dsh-edit-diff](https://github.com/senyayume/dsh-edit-diff) | DSH 插件：在文件变更工具卡片上重绘行级 diff（相同行只渲染一次 + 行内字符高亮），覆盖 run_code(PTC) 与 str_replace_ed… |
| 文件树/工作台 | [EdwardXiao-bit/dsh-run-button](https://github.com/EdwardXiao-bit/dsh-run-button) | Adds a Run button to shell code blocks in DSH replies, executing the command on… |
| 文件树/工作台 | [HaowenCang/dsh-document-selection-ask](https://github.com/HaowenCang/dsh-document-selection-ask) | DSH plugin for provenance-aware selection and Ask workflows across text, PDF, D… |

### 🖥️ 终端

| 需求 | 插件 | 说明 |
|------|------|------|
| 终端面板 | [giiiiiithub/terminal](https://github.com/giiiiiithub/terminal) | node-pty + xterm.js，多标签 |
| 底部终端 | [siberiah2o/dsh-plugin-terminal](https://github.com/siberiah2o/dsh-plugin-terminal) | 贴底全宽，输入框始终在上 |
| 主对话驱动 SSH 运维 | [caoyiwei850/dsh-ssh-ops](https://github.com/caoyiwei850/dsh-ssh-ops) | 主对话驱动 SSH，带高危命令保护与右侧终端 |
| 终端 | [tomowang/dsh-tui](https://github.com/tomowang/dsh-tui) | An open-source terminal front door for DeepSeek Harness (dsh). |

### 🪟 桌面壳 / 启动器 / 系统托盘

| 需求 | 插件 | 说明 |
|------|------|------|
| macOS 原生窗口 | [MDR-EX1000/dsh-desktop-kit](https://github.com/MDR-EX1000/dsh-desktop-kit) | Tauri/WKWebView 原生全屏 |
| 原生桌面壳（Tauri） | [dsh-tauri-desk/deepseek-harness-desktop](https://github.com/dsh-tauri-desk/deepseek-harness-desktop) | 仅 5MB 安装包、零环境配置、预设开箱即用 |
| Windows 托盘壳 | [RAFOLIE/dsh-desktop-windowos](https://github.com/RAFOLIE/dsh-desktop-windowos) | Releases 自动安装升级 |
| 纯净桌面壳 | [Icather/dsh-clean-desktop-shell](https://github.com/Icather/dsh-clean-desktop-shell) | 托盘启停、离线重连 |
| 系统托盘 | [wodongx123/dsh-desktop-tray](https://github.com/wodongx123/dsh-desktop-tray) | 最小化/关闭隐藏到托盘 |
| Windows 启动器 | [HUITianYi/dsh-whale-desktop-launcher](https://github.com/HUITianYi/dsh-whale-desktop-launcher) | 鲸鱼娘图标 Chromium 窗口 |
| 桌面客户端发行版 | [zouyuxuan122/Deepseek-Harness-EAC](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) | DeepSeek Harness 桌面客户端（dsh-desktop 发行版），开箱即用桌面壳 |
| 桌面客户端 | [MoonlitDropOfBlood/DSH-Desktop](https://github.com/MoonlitDropOfBlood/DSH-Desktop) | 为 DSH 打造的桌面端，核心可独立更新 |
| 品牌桌面客户端 | [JochenYang/dsh-app](https://github.com/JochenYang/dsh-app) | 社区维护的品牌化桌面客户端，Windows / macOS / Linux |
| 跨端控制平面 | ~~[d4551/DeepTail](https://github.com/d4551/DeepTail)~~（已失效） | Tauri 2 客户端，连接 DSH 主机，统一管理桌面/iOS/Android 会话 |
| 桌面壳/启动器 | [cilis/dsh-tauri-launcher](https://github.com/cilis/dsh-tauri-launcher) | DeepSeek Harness (DSH) Launcher，this is a dsh plugin. |

### 📱 移动端 / 响应式

| 需求 | 插件 | 说明 |
|------|------|------|
| 移动端适配 | [TecFancy/dsh-mobile](https://github.com/TecFancy/dsh-mobile) | 抽屉浮层、桌面零回归 |
| 手机 Web 修复 | [Odefined/dsh-mobile-webui](https://github.com/Odefined/dsh-mobile-webui) | 手势 + 纯图标 composer |
| PWA + 推送 | [jasondu/dsh-ui-mobile](https://github.com/jasondu/dsh-ui-mobile) | 可安装 PWA、Web Push |
| 移动端 UI 套件 | [TZHR-invest/dsh-plugins#dsh-mobile-ui](https://github.com/TZHR-invest/dsh-plugins/tree/main/packages/dsh-mobile-ui) | 44px 触摸目标、安全区适配 |
| Android 原生客户端 | [woaiys3/deepseek-harness-android-app](https://github.com/woaiys3/deepseek-harness-android-app) | 可直接安装的 Android APK，免 Root 操作手机 |
| 手机远程访问 | [shaobeichen/dsh-pocket](https://github.com/shaobeichen/dsh-pocket) | 电脑跑 dsh web，手机扫码即同步（局域网/公网实时同屏） |
| 移动端适配与安全访问 | [saya-ch/dsh-mobile](https://github.com/saya-ch/dsh-mobile) | 局域网/远程/Android App/手机浏览器访问，FRP/Tailscale/自签证书一键配置 |
| 手机远程客户端 | [zexadev/dsh-tether](https://github.com/zexadev/dsh-tether) | 用开发机上的 dsh，手机客户端远程使用 |
| 多端远程访问 | [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) | 基于插件机制的多端远程访问，P2P 优先、端到端加密 |
| Web 移动端适配 | [mexiaosqwq/dsh-web-mobile](https://github.com/mexiaosqwq/dsh-web-mobile) | DSH Web UI 移动端适配：窄屏好用、宽屏适用 |

### 🧠 记忆 / AGI / 上下文

| 需求 | 插件 | 说明 |
|------|------|------|
| 白箱 AGI 探索 | [FuRongJun-1999/dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) | 元认知、世界模型、自我改进 |
| 回退上下文 | [dygin/dsh-recover-context](https://github.com/dygin/dsh-recover-context) | 回到任意提问前并还原工作区 |
| 上下文洞察与管理 | [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) | 上下文用量洞察、压缩与回收建议 |
| 对话回退 | [SiriLee/dsh-rewind](https://github.com/SiriLee/dsh-rewind) | 同窗口内对话回退不新建分支；轻量工作区备份可一并还原文件 |
| 文献知识库 RAG | [Breeze136/dsh-kb-rag](https://github.com/Breeze136/dsh-kb-rag) | 本地优先 RAG：混合检索正文与图注，定位段落/图表，DOI 直达 |
| 上下文 Token 审计 | [Zhenyu98/dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) | 审计系统提示 / 技能 / 工具 schema 的 token 成本，圆环面板 |
| 注意力监督 | [Oscar-Williams/dsh-deepcanary](https://github.com/Oscar-Williams/dsh-deepcanary) | 证据优先信号 + 安静通知 + 可处理收件箱 |
| 跨会话长期记忆 | [LittleBlackTong/dsh-plugin-memory](https://github.com/LittleBlackTong/dsh-plugin-memory) | markdown+git 记忆库，SOUL.md 人格开机注入、remember/recall/consolidate/forget 工作流、设置面板热改 |
| Agent 记忆 | [kenz1117/dsh-engram](https://github.com/kenz1117/dsh-engram) | SQLite + 向量嵌入的本地长期记忆 |
| 上下文压缩 | [shaomingbo/dsh-codex-compaction](https://github.com/shaomingbo/dsh-codex-compaction) | Codex 原生 compaction 接入，用现有账号能力压缩长上下文 |
| 主动联想记忆 | [Aik358/dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) | 零提示自动唤回、三层自动沉淀、技能固化、Astra 式上下文管理与跨窗口续命 |
| Obsidian 知识库同步 | [Dingpenghui-good/dsh-obsidian-sync](https://github.com/Dingpenghui-good/dsh-obsidian-sync) | 按需检索 Obsidian 知识库 + 按 PARA 规则归档 DSH 会话（零 token 注入） |
| 跨会话记忆 | [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) | 有界/分层/审批门控/可审计的跨会话记忆 |
| 工程记忆 | [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) | 按项目持久化的读取时工程记忆插件 |
| 陪伴记忆 | [AkinoHaruka/companion-memory](https://github.com/AkinoHaruka/companion-memory) | 原生作用域 Riko 记忆插件 |
| 观察记忆 | [EPCN-fla/dsh-observational-memory](https://github.com/EPCN-fla/dsh-observational-memory) | 观察记忆：后台观察者把会话工作蒸馏为记忆 |
| 长期记忆 | [Fishsb/dsh-shoucang-memory](https://github.com/Fishsb/dsh-shoucang-memory) | 守藏·长期记忆：会话蒸馏沉淀 + 深度睡眠反思 + 词法/向量混合召回 + 主动遗忘 |
| 知识库 RAG | [Soren-ABT/dsh-knowledge](https://github.com/Soren-ABT/dsh-knowledge) | 知识库与 RAG：分块 / 本地嵌入 / 混合检索 |
| Jev 记忆 | [Towzai/dsh-memory-jev](https://github.com/Towzai/dsh-memory-jev) | 记忆插件：每次记忆读写皆由 TypeSafe Jev 类型判定 |
| 分层记忆 | [diqierjia/StrataGate-AgentMemory](https://github.com/diqierjia/StrataGate-AgentMemory) | 分层智能体记忆：近期详细、远期精简、重要常驻 |
| 上下文健康 | [donghangxunlang-cmd/dsh-attention-health](https://github.com/donghangxunlang-cmd/dsh-attention-health) | 上下文健康监测 + 内容退化守卫 + 零模型交接文档 |
| 记忆评估 | [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) | OMK·证据驱动的记忆/提示/RAG/技能评估与可观测 |
| 记忆宫殿 | [lovezi0/dsh-memory-palace](https://github.com/lovezi0/dsh-memory-palace) | 把 WorkBuddy 文件式记忆系统移植进 DSH |
| 长期记忆 | [paulalesius/dsh-hindsight-advanced](https://github.com/paulalesius/dsh-hindsight-advanced) | 长期记忆：每轮自动召回 + 保留/回忆机制 |
| 共享记忆 | [vshulcz/deja-vu](https://github.com/vshulcz/deja-vu) | 跨 Claude Code/Codex/Cursor 等 28+ 编码器的共享记忆 |
| 记忆归档 | [vv5v5/dsh-memory-archive](https://github.com/vv5v5/dsh-memory-archive) | 会话记忆归档 + 提示词查看器 |
| 工程记忆 | [yuyuyyyyyyyyyyyy/dsh-project-memory](https://github.com/yuyuyyyyyyyyyyyy/dsh-project-memory) | 跨会话工程记忆，按项目持久化 |
| 记忆/上下文 | [a86582751/dsh-nexttavern](https://github.com/a86582751/dsh-nexttavern) | DeepSeek Harness 长篇角色扮演agent（DSH酒馆插件）：SillyTavern 角色卡导入、行动选项卡、分支对话管理、长篇记忆、关键词与语… |
| 记忆/上下文 | [PerryLink/dsh-library](https://github.com/PerryLink/dsh-library) | Local document knowledge base for DeepSeek Harness: library_add/remove/list, hy… |
| 记忆/上下文 | [Noelune/unified-agent-memory](https://github.com/Noelune/unified-agent-memory) | Unified fleet-wide agent memory system for DeepSeek Harness — shared Obsidian V… |
| 记忆/上下文 | [Icstick/dsh-work-continuity](https://github.com/Icstick/dsh-work-continuity) | DeepSeek Harness 的 Work Continuity 插件——跨会话工作状态显式持久化，与通用记忆解耦 |
| 记忆/上下文 | [dearbld/dsh-living-memory](https://github.com/dearbld/dsh-living-memory) | Living memory for DeepSeek Harness — self-tending local knowledge base: nightly… |
| 记忆/上下文 | [iii993/dsh-manual-context](https://github.com/iii993/dsh-manual-context) | DeepSeek Harness 插件：手动上下文注入 + 对话历史/思维链编辑器 |
| 记忆/上下文 | [Icstick/dsh-context-maid](https://github.com/Icstick/dsh-context-maid) | DeepSeek Harness 自动上下文策展插件：tool 输出内容感知瘦身 + 无效日志清理 + 工作流/记忆钉扎保护 + 先归档后压缩 + 摘要模型可配 |
| 记忆/上下文 | [ChenneyZhuang/ask-batch](https://github.com/ChenneyZhuang/ask-batch) | Ask-batch skill: park piecemeal questions with context, group by decision, ask … |
| 记忆/知识 | [weibaohui/dsh-kb](https://github.com/weibaohui/dsh-kb) | dsh 插件 · 团队知识库：离线知识共享（FDE 盒子），浏览/全文检索/加工入口；写路径收口 agent，基于 Karpathy LLM W… |
| 记忆/知识 | [LoveDoLove/Veyra](https://github.com/LoveDoLove/Veyra) | Veyra — Engineering Intelligence for Coding Agents. Persistent, evidence… |
| 记忆/知识 | [weibaohui/dsh-continue](https://github.com/weibaohui/dsh-continue) | 自动续跑插件 for DeepSeek Harness — 有序规则表：按失败类型路由 继续续跑 / 换模型 / 压缩后继续 / 停止 |
| 记忆/知识 | [weibaohui/dsh-fde-tools](https://github.com/weibaohui/dsh-fde-tools) | dsh 插件全家桶：装一个插件带一批插件（Git 服务器/WebDAV 挂载盘/知识库/定时任务/自动续跑/界面微调/自动复盘） |
| 记忆/知识 | [HuaimaoCy/dsh-memory-vault](https://github.com/HuaimaoCy/dsh-memory-vault) | Knowledge and memory vault for DSH: memory groups with automatic summari… |
| 记忆/知识 | [JohnXu22786/codegraph](https://github.com/JohnXu22786/codegraph) | Code knowledge graph plugin for agent harnesses (dsh): indexes symbols, … |
| 记忆/知识 | [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) | Composable, view-based memory for DeepSeek Harness. Pluggable sources an… |
| 记忆/知识 | [kangtsang/dsh-worktree-space](https://github.com/kangtsang/dsh-worktree-space) | dsh-worktree-space is a DSH plugin that creates isolated multi-repo work… |
| 记忆/知识 | [littleblakew/msds-chain-mcp](https://github.com/littleblakew/msds-chain-mcp) |  |
| 记忆/知识 | [jonah791/dsh-agent-memory](https://github.com/jonah791/dsh-agent-memory) | Agent-driven long-term memory for DeepSeek Harness: scoped memory (globa… |
| 记忆/知识 | [Amakurai/dsh-liketavern](https://github.com/Amakurai/dsh-liketavern) | A DeepSeek Harness (dsh) plugin — turns dsh web into a SillyTavern-style… |
| 记忆/知识 | [P02-1010751281/dsh-project-context](https://github.com/P02-1010751281/dsh-project-context) | dsh (DeepSeek Harness) plugins for project-level persistent context: ses… |
| 记忆/知识 | [noteflowai/dsh-skills-anywhere](https://github.com/noteflowai/dsh-skills-anywhere) | Check Agent Skills before reuse: find missing local resources in browser… |
| 记忆/知识 | [LuminariSoftwares/context-guardian](https://github.com/LuminariSoftwares/context-guardian) | Compaction for local models that actually fires and never bricks the ses… |
| 记忆/知识 | [xswt442-cmd/dsh-ballast](https://github.com/xswt442-cmd/dsh-ballast) | DSH 上下文窗口逐条归因面板——看谁占了窗口 | Per-message context window attribution for DSH… |
| 记忆/知识 | [mattcarvercom/dsh-unified-memory](https://github.com/mattcarvercom/dsh-unified-memory) | Long-term memory for DeepSeek Harness in Claude Code's format: private, … |
| 记忆/知识 | [justhalfbit/dsh-plugin-jev-effort-selector](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector) | DeepSeek Harness (DSH) 推理等级自动选择插件：由 Jev System One 模型判断每条消息值多少思考量，按模型声明的… |

### 💬 会话管理 / 导入导出

把会话历史搬进搬出、回退与归档：

| 需求 | 插件 | 说明 |
|------|------|------|
| 外部对话历史导入 | [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) | 导入 18+/25 个 AI 编码工具（Claude Code/Codex/Gemini 等）对话历史，保留工具调用/结果/推理，转可续跑 DSH 会话；可反向导出 |
| 已归档会话恢复 | [kiligzzz/dsh-session-archive](https://github.com/kiligzzz/dsh-session-archive) | 侧边栏入口列出已归档会话，支持预览/恢复（取消归档）/删除，补上 harness 缺失的入口 |
| 消息撤回/重发/版本管理 | [yamingmou/dsh-retrace](https://github.com/yamingmou/dsh-retrace) | Recall/编辑重发/重新生成 + 会话内版本管理，基于 append-only 事件日志安全回退 |
| 消息撤回重编辑 | [Renzic-Stone/DSH-EasyRewrite](https://github.com/Renzic-Stone/DSH-EasyRewrite) | 最无感消息撤回/重编辑，兼容性强、设置丰富、现代化轻量 UI |
| 会话归档检索 | [Ultronen/dsh-archived-chats](https://github.com/Ultronen/dsh-archived-chats) | 本地优先批量归档、全文检索、回收站与 ZIP 备份恢复，数据留在本机 |
| 分支追问 | [sluminositys/dsh-nested-followups](https://github.com/sluminositys/dsh-nested-followups) | 从任意回答分支，任意深度继续分支，递归隔离追问 |
| 消息删除 | [DDDMUC/dsh-delete-turn](https://github.com/DDDMUC/dsh-delete-turn) | 按消息删除：删单条用户消息 / 单步回复 / 整段 |
| 编辑思维链 | [birew83538-oss/dsh-chat-thinking-editor](https://github.com/birew83538-oss/dsh-chat-thinking-editor) | 在对话里直接编辑任意 AI 消息正文与思维链（thinking） |
| 会话标题 | [cq-guojia/dsh-session-title-pattern](https://github.com/cq-guojia/dsh-session-title-pattern) | 自动将会话标题统一为「日期｜类型｜主题」 |
| 自动续跑 | [shengyvself/dsh-autoresume](https://github.com/shengyvself/dsh-autoresume) | 自动恢复 / 续跑中断的会话 |
| 会话管理 | [PerryLink/dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind) | Claude Code /rewind for DeepSeek Harness — git-first workspace snapshots before… |
| 会话管理 | [PerryLink/dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) | Terminal-style input history for the DeepSeek Harness web composer: edge-first … |
| 会话管理 | [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) | Cross-device DeepSeek Harness session sync: a dedicated git mirror with append-… |
| 会话清理 | [mikugui/dsh-session-eater](https://github.com/mikugui/dsh-session-eater) | 会话清理（喂鱼）：把不要的会话拖到余额挂件的小胖鱼身上「吃掉」（移入回收站，可撤销）——DSH Web 插件 |
| 会话管理 | [huangfuren/dsh-conversation](https://github.com/huangfuren/dsh-conversation) | DSH web plugin: conversation outline panel - history questions (index + time) p… |
| 会话管理 | [itchenshi/dsh-gui-last-session](https://github.com/itchenshi/dsh-gui-last-session) | DeepSeek Harness plugin: reopen the conversation you were last in after a resta… |
| 会话管理 | [ChenneyZhuang/project-handoff](https://github.com/ChenneyZhuang/project-handoff) | Project handoff skill: a dated handoff.md per project — current state, decision… |
| 会话管理 | [weibaohui/dsh-tasks](https://github.com/weibaohui/dsh-tasks) | DeepSeek Harness 插件：cron 定时事项——定时/立即执行新建 agent 会话提交提示词，全屏管理界面 |
| 会话管理 | [weibaohui/dsh-smart-title](https://github.com/weibaohui/dsh-smart-title) | dsh 插件 · 会话智能标题：LLM 总结改写会话标题，每轮对话后自动更新 |
| 会话管理 | [weibaohui/hermes-loop](https://github.com/weibaohui/hermes-loop) | DeepSeek Harness 插件：Hermes 循环——review/curator 自动化与会话循环管理 |
| 会话管理 | [weibaohui/dsh-flow](https://github.com/weibaohui/dsh-flow) | dsh 插件 · 执行流程图：把当前会话的执行过程画成实时三泳道流程图（回合/用户/助手/工具/审批/重试），子代理发散-收敛扇形 + 双击下钻… |
| 会话管理 | [weibaohui/dsh-process](https://github.com/weibaohui/dsh-process) | dsh 插件 · 工艺管理：把 ntd 的「工艺」（Process，多阶段·多环节 agent 工作流模板）接进 dsh web——浏览/编辑/… |
| 会话管理 | [Lanzgale/dsh-repo-browser](https://github.com/Lanzgale/dsh-repo-browser) | Repository Browser plugin for DeepSeek Harness — right-side GitHub repo … |
| 会话管理 | [Menghuan1918/dsh-apollo](https://github.com/Menghuan1918/dsh-apollo) | 把单一会话不可能的巨任务拆成无数可验证子系统，大规模并行有纪律执行 |
| 会话管理 | [Han-Yao94/dsh-session-toolkit](https://github.com/Han-Yao94/dsh-session-toolkit) | 会话身份、会话自动上线、会话日志按钮、会话间通信 + 全局提示词/重启服务这类工作台工具 |
| 会话管理 | [yhbd-top/dsh-plugin-top](https://github.com/yhbd-top/dsh-plugin-top) | yhbd.top 插件雷达 for DeepSeek Harness：侧边栏大面板浏览 3900+ 插件目录（搜索 / 22 分类 / 站点同款… |
| 会话管理 | [Ryuu-64/dsh-session-tools](https://github.com/Ryuu-64/dsh-session-tools) | Let the agent start a new session, or send a message to another one. |
| 会话管理 | [hawkongz/dsh-chat-locator](https://github.com/hawkongz/dsh-chat-locator) | Turn-rail settings for DSH Web: tick thickness, rail side, a curved leng… |
| 会话管理 | [HuaimaoCy/dsh-codex-chatgpt](https://github.com/HuaimaoCy/dsh-codex-chatgpt) | Use the Codex desktop app's ChatGPT models inside DeepSeek Harness: a fi… |
| 会话管理 | [Ryuu-64/dsh-find-all](https://github.com/Ryuu-64/dsh-find-all) | Ctrl+F find bar for the DSH desktop app: it searches the whole conversat… |
| 会话管理 | [fsrmqi/dsh-research-kit](https://github.com/fsrmqi/dsh-research-kit) | dsh-research-kit 是一个 浏览器侧 DSH 插件：它维护科研资源目录、把工作流和用户参数组装成可编辑 Prompt，并由 DSH… |
| 会话管理 | [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) | Continual self-evolution plugin for DeepSeek Harness: versioned, auditab… |
| 会话管理 | [kahomesl/dsh-client-ui-job-stats](https://github.com/kahomesl/dsh-client-ui-job-stats) | DeepSeek Harness 的会话后台任务统计：右侧边栏的一个标签页，累计记录本会话跑过的每一个任务。 |
| 会话管理 | [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) | DSH（DeepSeek Harness）实时重复输出守卫：模型复读时立即停止生成（默认同一字符串连续重复 ≥10 次；阈值、单元长度、检测窗口… |
| 会话管理 | [g-yixuan/dsh-sidenote](https://github.com/g-yixuan/dsh-sidenote) | 侧边开一岔对话，划选留一条注释——DSH（DeepSeek Harness）插件：fork 主会话成侧边会话，支线问题不打断主线，结论一键回流。… |
| 会话管理 | [V-Reason/dsh-task-notify](https://github.com/V-Reason/dsh-task-notify) | DeepSeekHarness任务完成时进行消息推送提醒（微信+Windows通知） |
| 会话管理 | [exoticknight/dsh-just-chat](https://github.com/exoticknight/dsh-just-chat) | One-click native conversations with independent workspaces for DeepSeek … |
| 会话管理 | [jaxzhou/dsh-file-explorer](https://github.com/jaxzhou/dsh-file-explorer) | A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) pl… |

### ✨ 提示词优化 / 润色

| 需求 | 插件 | 说明 |
|------|------|------|
| 一键优化 | [winditer/dsh-prompt-optimizer](https://github.com/winditer/dsh-prompt-optimizer) | Alt+O，复用当前模型流式改写 |
| 前后对比 | [SongMiao-tech/dsh-prompt-optimizer](https://github.com/SongMiao-tech/dsh-prompt-optimizer) | 弹窗对比、一键替换 |
| 草稿增强 | [LCQ-1024/dsh-prompt-enhancer](https://github.com/LCQ-1024/dsh-prompt-enhancer) | 改写为可执行 prompt |
| 优化器移植版 | [zhang-jiazhi/dsh-prompt-optimizer](https://github.com/zhang-jiazhi/dsh-prompt-optimizer) | 移植 linshenkx prompt-optimizer 到 DSH（非官方） |
| 提示词工具箱 | [FeatherHunter/dsh-prompt](https://github.com/FeatherHunter/dsh-prompt) | 预制 + 自定义 prompt 模板，点击即插入当前输入框（常规 + 智能悬浮卡） |
| 系统提示词覆写 | [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) | 覆写默认系统提示词、按模型切换提示词，自带设置面板 |
| 一键增强+语音识别 | [Fishsb/dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) | composer 一键增强（✨）+ 语音识别（云端/本地双引擎），服务异常一键重启 |
| 预设/宏 | [bychv/dsh-preset-enhance](https://github.com/bychv/dsh-preset-enhance) | SillyTavern 预设模式 / 宏引擎 / 编辑器 |
| 提示词优化 | [BOWLUNA/dsh-custom-mode](https://github.com/BOWLUNA/dsh-custom-mode) | Custom modes and custom prompts for DeepSeek Harness (dsh): edit a mode's syste… |

### 🧭 导航 / 大纲 / 跳转（长会话必备）

| 需求 | 插件 | 说明 |
|------|------|------|
| 对话地图 | [GeekRicardo/dsh-convmap](https://github.com/GeekRicardo/dsh-convmap) | 左缘刻度 + 全量导航 |
| 画卷式导轨 | [Max-Null/dsh-chat-rail](https://github.com/Max-Null/dsh-chat-rail) | 右侧竖排导轨，scroll-spy |
| ~~实时大纲（已失效）~~ | ~~[urzeye/dsh-outline](https://github.com/urzeye/dsh-outline)~~ | 仓库已 404，可改用 [GeekRicardo/dsh-convmap](https://github.com/GeekRicardo/dsh-convmap) 等导航类插件 |
| 提问索引 | [lijinhao315/dsh-question-index](https://github.com/lijinhao315/dsh-question-index) | 右侧你提过的问题列表 |
| 命令面板（⌘K） | [0xsline/dsh-spotlight](https://github.com/0xsline/dsh-spotlight) | 键盘优先的命令面板，⌘K/Ctrl+K 搜原生命令、近期会话、UI 操作与插件设置 |
| 对话树画布 | [RyanZeeee/dsh-chattree](https://github.com/RyanZeeee/dsh-chattree) | 把线性聊天变成可看可点的对话地图：每轮一个节点、每问长一枝 |
| 章节导航 | [jolaaa999/dsh-section-nav](https://github.com/jolaaa999/dsh-section-nav) | 章节导航栏 + 本地书签 |
| 把 对话分支 画成 | [JRJRJPRO/dsh-tree](https://github.com/JRJRJPRO/dsh-tree) | 把 对话分支 画成 可点击的树 |
| 导航/大纲 | [ChenneyZhuang/context-budget](https://github.com/ChenneyZhuang/context-budget) | Context budget skill: graduated file reads (head, section, search), a working n… |
| 导航/大纲 | [ChenneyZhuang/template-instantiator](https://github.com/ChenneyZhuang/template-instantiator) | Template instantiator skill: inventory every placeholder and example block, fil… |

### ⌨️ 终端 TUI / 全屏界面

| 需求 | 插件 | 说明 |
|------|------|------|
| ~~全屏 TUI（已失效）~~ | ~~[ccq1/dsh-TUI](https://github.com/ccq1/dsh-TUI)~~ | 仓库已 404，请改用下方社区维护版本 |
| 全屏 TUI | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚 |
| 终端工作台 | [lk251066/dsh-tui-pro](https://github.com/lk251066/dsh-tui-pro) | 多会话、结构化视图 |
| Rust TUI | [openma-ai/Martty](https://github.com/openma-ai/Martty) | ratatui，持久会话 |
| Claude Code 风 TUI 套件 | [UNLINEARITY/dsh-code](https://github.com/UNLINEARITY/dsh-code) | 充分结合 DSH 核心机制与高级特性的 TUI 套件 |
| Cordis 插件树 TUI | [dsh-blue/blue](https://github.com/dsh-blue/blue) | 模块化状态栏/编辑器/覆盖层等可组合界面，插件树式 TUI |
| 极简交互式 TUI | [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | 自研 ANSI 极简交互渲染、流式 Markdown/工具卡、16+ 主题、slash 命令 |

### 🐳 桌面宠物

| 需求 | 插件 | 说明 |
|------|------|------|
| 桌面级桌宠 | [cookiesheep/whale-on-desk](https://github.com/cookiesheep/whale-on-desk) | 29 帧状态，盖得住全屏 |
| 像素办公室 | [EternalNight996/dsh-ui-agents-pixe](https://github.com/EternalNight996/dsh-ui-agents-pixe) | 508 张角色卡 |
| Codex 桌宠迁移 | [mengyun233/dsh-codex-pet](https://github.com/mengyun233/dsh-codex-pet) | 毛玻璃对话框 + 设置面板 |
| 像素鲸鱼伙伴 | [omdsh-dev/dsh-ui-whale](https://github.com/omdsh-dev/dsh-ui-whale) | 标题栏常驻像素鲸鱼，眨眼 / 摆尾 / 喷水 / 偷懒睡觉 |
| 复古广告面板 | [Nagi-ovo/dsh-ads](https://github.com/Nagi-ovo/dsh-ads) | 横幅 / 弹窗 / 小游戏，复刻早期门户页风格 |
| 小游戏面板 | [omdsh-dev/dsh-minigames](https://github.com/omdsh-dev/dsh-minigames) | 右侧 18 款离线小游戏（俄罗斯方块 / 扫雷 / 2048 等） |
| ~~修仙陪伴宠物（已失效）~~ | ~~[weibaohui/dsh-xiuxian](https://github.com/weibaohui/dsh-xiuxian)~~ | 仓库已不可达（SSH 多次核验失败），如有替代欢迎 PR |
| 鲸鱼娘·灵动挂件 | [nickkkkkk123123/dsh-whale-girl](https://github.com/nickkkkkk123123/dsh-whale-girl) | 鲸鱼娘·灵动挂件 — 会卖萌、会记账、会弹跳的 DSH 桌面挂件插件（余额/用量/上下文/峰谷/右键菜单/拖动甩抛） |
| 桌面宠物 | [ChenneyZhuang/competitor-recon](https://github.com/ChenneyZhuang/competitor-recon) | Competitor research skill: complaint-driven recon with cited evidence from revi… |

### 🎙️ 语音 / 音频通话

| 需求 | 插件 | 说明 |
|------|------|------|
| DeepSeek 语音通话 | [biliye/dsh-voice-call](https://github.com/biliye/dsh-voice-call) | deepseek 专属语音通话插件，浏览器内语音对话 |
| Edge TTS 朗读 | [1624318455/dsh-plugin-tts](https://github.com/1624318455/dsh-plugin-tts) | Edge TTS 语音插件，朗读助手回复、自动断句 |
| 语音/朗读 | [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) | Voice-first session loop for DeepSeek Harness: a composer microphone button wit… |
| 语音/朗读 | [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) | Local-first voice conversations for DSH. Run speech recognition and speech synt… |
| 开口即成文 | [bitterSmilezzz/dsh-asr-voice](https://github.com/bitterSmilezzz/dsh-asr-voice) | 开口即成文 · Speak-to-prompt for DeepSeek Harness：云端 ASR 语音识别 + 提示词优化 + 填入草稿/自动发送，跨平… |
| 语音/朗读 | [fangqian616/dsh-say](https://github.com/fangqian616/dsh-say) | Give your DSH, speak and report in a voice you like！让你的 DSH 用你喜欢的声音开口说话、汇报内容！ |
| 语音/音频 | [hawkongz/dsh-task-reminder](https://github.com/hawkongz/dsh-task-reminder) | Conversation task-completion reminders for the DeepSeek Harness Web UI: … |

### 📈 行情 / 股票（A 股红涨绿跌）

| 需求 | 插件 | 说明 |
|------|------|------|
| A股/港股/美股 | [FeiZhuNiU-INFJA/dsh-stock-ticker](https://github.com/FeiZhuNiU-INFJA/dsh-stock-ticker) | 上证/创业板/科创50/恒生科技，红涨绿跌 |
| 雪球面板 | [kangjinghang/dsh-xueqiu](https://github.com/kangjinghang/dsh-xueqiu) | K线蜡烛图、热榜、7×24 快讯 |
| 行情/持仓 | [shuiiiiimu/dsh-stock-portfolio](https://github.com/shuiiiiimu/dsh-stock-portfolio) | DeepSeek Harness 中管理股票持仓的插件 |

### 🌐 浏览器 / 网页交互

把浏览器与控制能力搬进 DSH：

| 需求 | 插件 | 说明 |
|------|------|------|
| 内置浏览器面板 | [TEGONG00/dsh-plugin-browser](https://github.com/TEGONG00/dsh-plugin-browser) | Web 端内置浏览器：实时投屏视图、元素选取器接入 composer、Playwright 驱动浏览器工具 |
| Tavily 检索 + 抓取 | [ArcaneOrion/dsh-tavily-web](https://github.com/ArcaneOrion/dsh-tavily-web) | 注册 tavily_search / web_fetch 工具，多 key 轮询池抗额度耗尽，无 key 也能 web_fetch |
| URL 阅读 | [2672243194/dsh-read-url](https://github.com/2672243194/dsh-read-url) | 抓取任意页面返回干净正文/Markdown |
| 浏览器/网页 | [chaserchan/dsh-browser-harness](https://github.com/chaserchan/dsh-browser-harness) | DSH plugin: drive a real Chrome from your dsh agent via the browser-use Browser… |
| 浏览器 | [cfanmaoli/kimi-webbridge-dsh](https://github.com/cfanmaoli/kimi-webbridge-dsh) |  |
| 浏览器 | [weibaohui/user-management](https://github.com/weibaohui/user-management) | dsh 插件 · 用户管理：dsh web 登录门禁 + 用户/角色/登录记录/访问记录管理，首个注册者即管理员 |
| 浏览器 | [taxueseek/argo](https://github.com/taxueseek/argo) | 专门为 agent 打造的开源 agent 搜索工具，具备 200+的搜索源及多语言搜索能力，覆盖中文/英文/学术/代码/购物/金融/新闻/百科… |
| 浏览器 | [jackie-cqz/dsh-jev-plugin](https://github.com/jackie-cqz/dsh-jev-plugin) | DeepSeek Harness plugin for TypeSafe Jev: typed decisions, configurable … |
| 浏览器 | [auggie246/dsh-sidebar](https://github.com/auggie246/dsh-sidebar) | A Git sidebar for DeepSeek Harness Web |
| 浏览器 | [janpauldahlke/dsh-slot-health](https://github.com/janpauldahlke/dsh-slot-health) | DeepSeek Harness (dsh) plugin: live local LLM endpoint health in the web… |
| 浏览器 | [datit309/dsh-live-inspector](https://github.com/datit309/dsh-live-inspector) | Auto-monitor and reveal active file operations and changes in DeepSeek H… |
| 浏览器 | [penguin-oo/dsh-pathlink](https://github.com/penguin-oo/dsh-pathlink) | Ctrl+click file paths and links in DeepSeek Harness chat: paths open the… |
| 浏览器 | [victor10035445/dsh-v-explorer](https://github.com/victor10035445/dsh-v-explorer) | right slider for deepseek-harness-plugin. |
| 浏览器 | [7starsseeker/dsh-fact-check](https://github.com/7starsseeker/dsh-fact-check) | Fact-checking skill for DeepSeek Harness: multi-source verification agai… |
| 浏览器 | [xswt442-cmd/dsh-instance-manager](https://github.com/xswt442-cmd/dsh-instance-manager) | DSH 常驻插件：侧边栏面板统一查看并管理本机的 dsh 实例 | Sidebar panel to list and manage local… |
| 浏览器 | [janpauldahlke/dsh-gpu-monitor-nvml](https://github.com/janpauldahlke/dsh-gpu-monitor-nvml) | DeepSeek Harness (dsh) plugin: live NVIDIA GPU monitor in the web rightb… |
| 浏览器 | [qigelunbiya/DSH-Patrol](https://github.com/qigelunbiya/DSH-Patrol) | Browser patrol & website inspection plugin for DeepSeek Harness (DSH). T… |
| 浏览器 | [kviiinh/dsh-whale-particles-bg](https://github.com/kviiinh/dsh-whale-particles-bg) | Animated whale particle background for the DeepSeek Harness (dsh) Web UI… |

### 🔀 MCP / 设置扩展

| 需求 | 插件 | 说明 |
|------|------|------|
| MCP 可视化管理 | [Js2Hou/dsh-mcp-manager](https://github.com/Js2Hou/dsh-mcp-manager) | 设置页增删启停 MCP |
| 设置扩展 | [omdsh-dev/ex-setting](https://github.com/omdsh-dev/ex-setting) | DSH 设置扩展 |
| 规则管理 | [wzz3034026545/dsh-rule-manager](https://github.com/wzz3034026545/dsh-rule-manager) | 统一管理 AGENTS.md |
| Git 自动提交推送 | [EIGHTfs/dsh-git-push](https://github.com/EIGHTfs/dsh-git-push) | 扫描仓库一键 commit/push + 代码审计门禁（硬编码路径/IP 检测），推送后回传远端最近 3 次 |
| 变更评审 | [Binaryinject/dsh-review-checkout](https://github.com/Binaryinject/dsh-review-checkout) | Codex 风逐轮卡片 + 语法高亮 diff + 按轮回滚，跟随 DSH 主题 |
| 远程授权中转 | [nicecx/dsh-relay](https://github.com/nicecx/dsh-relay) | 把 approval/ask_user_question 按编号推到 iMessage/Email/微信等通道，通道内批准/拒绝 |
| 三方协作协议 | [victormshan/dsh-web-relay](https://github.com/victormshan/dsh-web-relay) | 用户/主 agent/外部 AI 三方协作协议 + 五级审核链（Gemini→claude-code→dialog→manual）+ 无介入续跑 |
| MCP 管理台 | [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) | 官方 MCP 客户端管理控制台（/mcp 命令） |
| AGENTS 编辑 | [Bay-Zeddie/dsh-agent-instructions](https://github.com/Bay-Zeddie/dsh-agent-instructions) | 在 Web 设置页编辑原生 AGENTS.md：分层可点选编辑、三种生效范围 |
| skill/MCP 管理 | [Fishquito7/dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) | Web 界面 skill 与 MCP 管理面板 |
| 导入 Copilot 配置 | [NEVSTOP-LAB/dsh-import-copilot-files](https://github.com/NEVSTOP-LAB/dsh-import-copilot-files) | 导入 VSCode/Copilot AI 配置（copilot-instructions.md 等） |
| 插件管理面板 | [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) | 插件管理面板：一键启停 + dsh-plugin 市场 + 自定义索引，带详情与一键安装 |
| Git worktree | [wloops/dsh-git-worktree](https://github.com/wloops/dsh-git-worktree) | Git worktree 会话目标：隔离任务会话、可回退 |
| MCP/设置 | [Totoro-qaq/dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) | DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-s… |
| 一个面向 | [PKUfudawei/dsh-capability-menu](https://github.com/PKUfudawei/dsh-capability-menu) | 一个面向 DeepSeek Harness 的统一能力管理插件，为 Tools/Skills 提供常驻、按需、禁用三档暴露策略，以减少上下文占用并支持运行时动… |
| MCP/设置 | [Imzl-zl/dsh-mcp-manager-ui](https://github.com/Imzl-zl/dsh-mcp-manager-ui) | MCP server management UI for DeepSeek Harness Web — floating panel, JSON import… |
| MCP/设置 | [alexzshl/dsh-settings-size](https://github.com/alexzshl/dsh-settings-size) | config dsh settings size |
| MCP/设置 | [ChenneyZhuang/onboarding-pack](https://github.com/ChenneyZhuang/onboarding-pack) | Onboarding pack skill: the day-one doc — what & why, exact run commands, a map … |
| MCP/设置 | [ChenneyZhuang/weekly-review](https://github.com/ChenneyZhuang/weekly-review) | Weekly review skill: reconcile last week's logged commitments against outcomes … |
| MCP/设置 | [Alphauni-x/dsh-mcp-market](https://github.com/Alphauni-x/dsh-mcp-market) | Browse, search and sync an MCP marketplace right inside DeepSeek Harness… |
| MCP/设置 | [SouleyMoni1/dsh-experience-plugin](https://github.com/SouleyMoni1/dsh-experience-plugin) | DSH plugin: per-model reasoning levels for custom API models, with famil… |

### 🔒 安全与权限

装插件＝在本机运行第三方代码。下列插件用于运行时安全治理，但请仍先读源码再装：

| 需求 | 插件 | 说明 |
|------|------|------|
| 安全护栏 | [GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard) | 拦截危险命令、防数据泄露、保护密钥；20 条检测规则 + 运行时动作评估 + 信任 registry |
| API 中继审计 | [toby-bridges/api-relay-audit](https://github.com/toby-bridges/api-relay-audit) | 审计 API 中继的 prompt 注入、模型替换、工具调用改写、SSE 异常与密钥泄露 |
| 第二模型安全审批 | [PerryLink/dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) | 只读评审子代理在审批链上判 allow/deny，默认 fail-closed，per-tool 策略可配 |
| 权限规则 | [PerryLink/dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) | Claude Code 风声明式权限规则（有序放行） |
| 注入防御 | [PerryLink/dsh-defend](https://github.com/PerryLink/dsh-defend) | 提示注入/越狱/密钥泄露防御（Aho-Corasick 等） |
| 执行前守卫 | [7starsseeker/dsh-jev-guard](https://github.com/7starsseeker/dsh-jev-guard) | 执行前安全阀门：bash/pwsh 真正执行前经静态规则 + Jev 语义判定，破坏性操作可允许/修正/拦截 |
| 权限控制 | [MrWeiCodes/dsh-permgate](https://github.com/MrWeiCodes/dsh-permgate) | 为 DSH 提供的细粒度权限控制插件 |
| 确认守卫 | [bbaz123/dsh-confirmation-resolution](https://github.com/bbaz123/dsh-confirmation-resolution) | 任务后确认决策守卫：平衡输出质量与风险 |
| 契约检查 | [imtokenxinluo/dsh-contract-check](https://github.com/imtokenxinluo/dsh-contract-check) | DSH 插件零 token 契约检查：校验 render() / session-event 词汇 |
| 安全/权限 | [yoza10635/dsh-argp](https://github.com/yoza10635/dsh-argp) | Guarded context compaction for DeepSeek Harness (dsh): the LLM proposes, determ… |
| 安全/权限 | [PerryLink/dsh-mask](https://github.com/PerryLink/dsh-mask) | PII masking middleware for DeepSeek Harness: anonymize names, phones, emails, I… |
| 安全/权限 | [weibaohui/experts-management](https://github.com/weibaohui/experts-management) | dsh 插件 · 专家市场：ntd 格式专家/专家团队管理与注入（＋专家按钮 / /expert-名称 手势），稀疏检出专家市场 |
| 安全/权限 | [xiaozhuyuqing/dsh-repeat-guard](https://github.com/xiaozhuyuqing/dsh-repeat-guard) | Tell your deepseek-v4.1-flash: "shut up! Stop looping!" |

### 🤖 智能体 / 研究 / 创作

把 DSH 当研究、写作与协作引擎用的高阶玩法：

| 需求 | 插件 | 说明 |
|------|------|------|
| 对抗式深度研究 | [grloper/dsh-deep-research](https://github.com/grloper/dsh-deep-research) | 机械核验引用、独立佐证评分（识别洗稿）、控辩仲裁、复合证据图 |
| 演示文稿专家 | [TANGZHUO12/ppt-expert](https://github.com/TANGZHUO12/ppt-expert) | persona + LibreOffice Impress MCP（9 工具）+ matplotlib 图表核 + 浏览器实时预览 |
| 长驻 AI 陪伴 | [lemoncat7/dsh-partner](https://github.com/lemoncat7/dsh-partner) | 带微信通道路由的长驻 AI 伙伴，可接入 DSH 会话 |
| 校园门户聚合与 AI 摘要 | [ZBber-lab/cau-portal-open](https://github.com/ZBber-lab/cau-portal-open) | 农大门户通知公告聚合、AI 摘要与对话查询（可改造成任意门户源） |
| 数学建模论文流水线 | [Aampidy/dsh-mcmp](https://github.com/Aampidy/dsh-mcmp) | 粘贴赛题即跑：5 阶段 22 子阶段，子代理执行 + 质量分级（P0-P3）回滚，产出 Final_Paper.md |
| 可验证研究报告 | [PerryLink/dsh-research-report](https://github.com/PerryLink/dsh-research-report) | 内容寻址证据链的可验证研究报告引擎 |
| 网文体检 | [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) | 本地章节体检：16 工具句式/情感/风格分析，本地模型零 API |
| 持久 Agent 团队 | [wowyuarm/dsh-agent-team](https://github.com/wowyuarm/dsh-agent-team) | 不重置的持久成员（Members）多 agent 团队 |
| 子代理接入 | [2025Bigeye/dsh-nanobot-subagent-link](https://github.com/2025Bigeye/dsh-nanobot-subagent-link) | 把 Nanobot 实例接入 DSH，启用子代理能力 |
| 认知预设 | [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) | J-Space 认知套件 SV1：原生 DSH 智能体预设 + 独立 Cordis 插件，含深层推理路由与持久控制器 |
| 圆桌会议 | [Fishsb/dsh-plugin-roundtable](https://github.com/Fishsb/dsh-plugin-roundtable) | 圆桌会议：把一次会话变可视化、可辩论、可拍板的专家圆桌（含红队评审） |
| 社交约伴 | [liudejua27-blip/fitmeet-dsh-plugin](https://github.com/liudejua27-blip/fitmeet-dsh-plugin) | FitMeet：找同好/约球友/找人帮忙的社交插件 |
| 无人值守控制台 | [picsky/dsh-pocket-console](https://github.com/picsky/dsh-pocket-console) | 无人值守控制台：只把卡住的决策交给你 |
| 画布创作 | ~~[wild-River2016/dsh-canvas-xiaohe](https://github.com/wild-River2016/dsh-canvas-xiaohe)~~（已失效） | 小禾画布 AI 创作助手 |
| 嘉立创EDA专业版 | [zhoushoujianwork/easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) | 嘉立创EDA专业版(EasyEDA Pro)自动化：给 AI harness 装上画板的「手」—— 一套 typed 原理图/PCB 动作，CLI / Age… |
| 智能体/研究 | [PerryLink/dsh-industry-research](https://github.com/PerryLink/dsh-industry-research) | Industry and company research domain pack for DeepSeek Harness: methodology ski… |
| 智能体/研究 | [PerryLink/dsh-fund-research](https://github.com/PerryLink/dsh-fund-research) | DeepSeek Harness plugin: deterministic research reports for Chinese public mutu… |
| 智能体/研究 | [PerryLink/dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) | Double-check before you ship: grill the requirements, test the implementation, … |
| 智能体/研究 | [PerryLink/dsh-data-quality](https://github.com/PerryLink/dsh-data-quality) | DeepSeek Harness plugin: deterministic data profiling, cleaning, and verificati… |
| 智能体/研究 | [ChongCyrus/Vibe-Mathematics](https://github.com/ChongCyrus/Vibe-Mathematics) | Vibe Mathematics —— 多代理数学问题求解与形式化验证框架 |
| 插件生态透明排行与推荐 | [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) | DSH 插件生态透明排行与推荐：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行/推荐插件与静态站 |
| 智能体/研究 | [PerryLink/dsh-background-agents](https://github.com/PerryLink/dsh-background-agents) | Interactive long-session background agents for DeepSeek Harness: start a durabl… |
| 智能体/研究 | [joekytc/dsh-swarm](https://github.com/joekytc/dsh-swarm) | Run multi-agent task pipelines on DSH like a team — plan, execute, review, and … |
| 智能体/研究 | [PerryLink/dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms) | Team rooms for DeepSeek Harness: persistent shared rooms across independent ses… |
| 专家编排模式 | [mario841859784/dsh-expert-orchestrator](https://github.com/mario841859784/dsh-expert-orchestrator) | DSH 专家编排模式 agent preset — PM-first planning, Agency expert delegation, gated de… |
| 智能体/研究 | [mikasa-servent/dsh-research-check](https://github.com/mikasa-servent/dsh-research-check) | Deliverable evidence-chain & conformance checks for DSH — turn requirements int… |
| 智能体/研究 | [huxin7735-collab/dsh-maintainer-doc-guard](https://github.com/huxin7735-collab/dsh-maintainer-doc-guard) | Keeps a long agent turn answerable to the user's actual request: a standing mai… |
| 智能体/研究 | [johnny-ggao/trading-agent](https://github.com/johnny-ggao/trading-agent) | trading agent for dsh |
| 智能体/研究 | [S-AN-Shu/dsh-progress-narrator](https://github.com/S-AN-Shu/dsh-progress-narrator) | Quiet progress narration and folding compatibility for DeepSeek Harness |
| 智能体/研究 | [PerryLink/dsh-laya](https://github.com/PerryLink/dsh-laya) | Laya decision engine as a first-class Cordis service and model-visible tools fo… |
| 智能体/研究 | [GooDAnDReaDY/dsh-goal](https://github.com/GooDAnDReaDY/dsh-goal) | Autonomous Goal Execution & Multi-Turn Task Tracking Engine with Sticky Header … |
| 智能体/研究 | [ChenneyZhuang/decision-records](https://github.com/ChenneyZhuang/decision-records) |  |
| 智能体/研究 | [harmless0819-dev/dsh-agent-chat](https://github.com/harmless0819-dev/dsh-agent-chat) | Turn-injection message channel between DSH agents on two machines: messages lan… |
| 通知/推送 | [THEWOLFWALKER/dsh-notifier](https://github.com/THEWOLFWALKER/dsh-notifier) | DSH notification & remote-control plane: 28 outbound channels, 6 inbound… |
| 智能体/研究 | [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) | Zotero toolkit for DeepSeek harness; Turn your Zotero library into an ev… |
| Git/评审 | [weibaohui/dsh-git-server](https://github.com/weibaohui/dsh-git-server) |  |
| 视觉/多模态 | [qikairo7/dsh-gemini-pool](https://github.com/qikairo7/dsh-gemini-pool) | 多账号 Google Gemini 提供商（DSH 插件）：按剩余额度挑选账号，遇 429 指数退避切换，后台探活已禁用账号，附中英双语设置页 |
| 智能体/研究 | [weibaohui/dsh-file-share](https://github.com/weibaohui/dsh-file-share) | dsh 插件 · 目录共享：任意可配置目录经 HTTP 在线浏览/上传/下载 + 对话框 @ 文件给 agent 处理 |
| 智能体/研究 | [ggfgfgf-on/dsh-trajectory-anchor](https://github.com/ggfgfgf-on/dsh-trajectory-anchor) | A DeepSeek Harness plugin that stops agents from drifting off-task: it l… |
| 能力扩展 | [vINyLogY/dsh-bluebubbles](https://github.com/vINyLogY/dsh-bluebubbles) | Who needs openclaw? |
| 模型/账号 | [DLive/dsh-qqbot-community](https://github.com/DLive/dsh-qqbot-community) | 为 DeepSeek Harness 提供 QQ 官方机器人的接入能力 |
| 视觉/多模态 | [TikaFlow/dsh-model-fix](https://github.com/TikaFlow/dsh-model-fix) | DSH 插件：给非官方（自定义）提供方的模型自动填充推理级别、最大上下文、输出上限与图片模态等参数（数据来自 models.dev），并提供兼容… |
| 视觉/多模态 | [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) | DSH 插件：Web GUI 里的 IDE 风格 Git 面板——分支/提交历史总览、变更提交与 amend、文件浏览、代码与图片新旧差异对照、… |
| 智能体/研究 | [NBagent-dev/metaflywheel](https://github.com/NBagent-dev/metaflywheel) | Meta-Problem Modeling (MPM) cognitive flywheel as a resident engine for … |
| 模型/账号 | [Ztyss/dsh-llm-provider](https://github.com/Ztyss/dsh-llm-provider) | 全量接管模型服务，并提供直观的配置方式与额度显示 |
| Git/评审 | [peterwangze/software-project-governance](https://github.com/peterwangze/software-project-governance) | AI coding delivery trust layer for evidence-backed planning, review, ris… |
| 通知/推送 | [VoodooB0Ys/dsh-desktop-notify](https://github.com/VoodooB0Ys/dsh-desktop-notify) | DeepSeek Harness 的 Windows 桌面提醒：需要授权 / 提问 / 完成 / 出错 / 被中止时在屏幕角落弹出提醒，点一下回… |
| 智能体/研究 | [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) | DeepSeek Harness plugin market - browse, search & install dsh-plugin top… |
| 智能体/研究 | [chen731215-dev/dsh-muv-engine](https://github.com/chen731215-dev/dsh-muv-engine) | DSH Native MUV Engine - tavern companion: regex script execution, variab… |
| 模型/账号 | [bruceyork00-a11y/PinMe](https://github.com/bruceyork00-a11y/PinMe) | Just Pin a model to Favorites, so you dont need to choose it from menu. … |
| 智能体/研究 | [chen731215-dev/dsh-muv-table](https://github.com/chen731215-dev/dsh-muv-table) | MUV Variable Table Editor - tavern companion plugin for DeepSeek Harness… |
| 视觉/多模态 | [HaoyueQin/deepseek-harness-background](https://github.com/HaoyueQin/deepseek-harness-background) | 为 DeepSeek Harness Web GUI 添加自定义背景图片：上传本地图片或粘贴图片链接，可调不透明度、遮罩、面板透明与毛玻璃模糊，… |
| 智能体/研究 | [JularDepick/dsh-wakatime-plugin](https://github.com/JularDepick/dsh-wakatime-plugin) | A plugin for dsh: quantify every dsh Agent interaction as a visualized p… |
| 智能体/研究 | [xiaoso456/dsh-tool-plus](https://github.com/xiaoso456/dsh-tool-plus) | DeepSeek Harness 基础工具增强：持久 bash、结构化 read、多模式 edit、原子 write、双引擎 grep/glob… |
| 视觉/多模态 | [Lee-Hilex/dsh-mineru](https://github.com/Lee-Hilex/dsh-mineru) | 基于 MinerU 的 DeepSeek Harness 多模态文档解析插件：PDF/Word/PPT/Excel/HTML/图片 → 结构化 … |
| Git/评审 | [xswt442-cmd/dsh-unsandboxed-winbash](https://github.com/xswt442-cmd/dsh-unsandboxed-winbash) | 让 dsh 在 Windows 上使用用户自安装的 Git Bash，并绕过其沙箱限制 | Enable dsh to use a user-i… |
| 通知/推送 | [Archaofan/dsh-notify-relay](https://github.com/Archaofan/dsh-notify-relay) | DSH 外联通知中枢：生命周期事件经去重/免打扰/摘要合批后路由到 Bark/Server酱/Telegram/企业微信/飞书/ntfy/web… |
| 智能体/研究 | [sjh9714/dsh-win32](https://github.com/sjh9714/dsh-win32) | Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell… |
| 视觉/多模态 | [DamonBao/dsh-models-input-modalities](https://github.com/DamonBao/dsh-models-input-modalities) | DeepSeek Harness Web plugin: per-model input-modality selector (text/ima… |
| Git/评审 | [omdsh-dev/dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) | Advisor - Pair a second model that passively reviews each turn and injec… |
| 模型/账号 | [latte03/dsh-select-quote](https://github.com/latte03/dsh-select-quote) | 在对话里划词加批注——把选中的原文连同你的评论一起交给模型，并让它在回答里明确指出说的是哪一段。 |
| 视觉/多模态 | [fengyungithub/dsh-short-video-studio](https://github.com/fengyungithub/dsh-short-video-studio) | 基于deepseek harness和ComfyUI的AI视频创作工作台 |

### 📄 文档与渲染

| 需求 | 插件 | 说明 |
|------|------|------|
| 办公套件集成 | [dream-num/dsh-univer-office](https://github.com/dream-num/dsh-univer-office) | DSH × Univer：内置协作网关与查看器，表格/文档/演示内联预览、浮动 Worktree 窗口、会话末审阅 |
| 图片读字 | [jing-hy/picturereader](https://github.com/jing-hy/picturereader) | 纯文本模型用的像素转文字图片读取（image_scan/image_ocr 工具） |
| 文档/渲染 | [hanzhangzzz/dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) | Turn DeepSeek Harness articles into editable Excalidraw canvases — live diagram… |
| 文档/渲染 | [PerryLink/dsh-draw](https://github.com/PerryLink/dsh-draw) | Unified static-image generation router for DeepSeek Harness: one image_generate… |
| 文档/渲染 | [ChenneyZhuang/web-cliplibrary](https://github.com/ChenneyZhuang/web-cliplibrary) | Web clip library skill: save research as markdown clips with URL, fetch date, v… |
| 文档/渲染 | [zuoyunlai/lunheng-article-pipeline-dsh](https://github.com/zuoyunlai/lunheng-article-pipeline-dsh) | 论衡（lunheng-article-pipeline）DeepSeek Harness bundle 插件（DSH 适配版） |
| 文档/渲染 | [JularDepick/dsh-system-monitor-plugin](https://github.com/JularDepick/dsh-system-monitor-plugin) | A plugin for dsh: monitor the resource utilization of dsh system process… |
| 文档/渲染 | [naodeng/dsh-qa](https://github.com/naodeng/dsh-qa) | dsh-qa · QA Workbench — A local software testing workbench plugin for De… |

### 🧩 技能 / 提示词库 / 任务看板

| 需求 | 插件 | 说明 |
|------|------|------|
| 技能管理器 | [lcthe/dsh-skills-hub](https://github.com/lcthe/dsh-skills-hub) | 导入/启用/禁用技能 |
| 任务看板 | [1070296335-create/dph-taskboard](https://github.com/1070296335-create/dph-taskboard) | 待办/进行中/评审/完成 四列 |
| 定时任务 | [magicOF2/dsh-schedule](https://github.com/magicOF2/dsh-schedule) | 每日/每周/一次性日程 |
| 侧栏定时任务 | [534119219/chicheng-cron](https://github.com/534119219/chicheng-cron) | cron 调度 Shell/Python/Node/Skill/Agent 任务，推送通知与执行历史归档 |
| 技能卡组 | [FeatherHunter/dsh-mattpocock-skills-deck](https://github.com/FeatherHunter/dsh-mattpocock-skills-deck) | 把 mattpocock/skills 引入 DSH，看得见、派得动的技能卡组 |
| 多智能体团队 | [nanmicoder/dsh-agent-teams](https://github.com/nanmicoder/dsh-agent-teams) | 自然语言拉多智能体团队，右上角实时活动面板 |
| 技能中心 | [xusuyang030218/dsh-skill-ui](https://github.com/xusuyang030218/dsh-skill-ui) | 按来源浏览已加载技能、skillhub 市场安装、向导创建与 AI 起草（Web 面板） |
| 技能自我进化 | [WODE25500/dsh-skillopt](https://github.com/WODE25500/dsh-skillopt) | 夜间睡眠循环：harvest 历史会话、回放重复任务、把关后沉淀技能（SkillOpt-Sleep 引擎） |
| 技能中枢 | [cheshireez/dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) | 浏览/搜索本地技能目录、启用禁用、诊断、新建（基于官方 ctx.skills） |
| 插件市场 / DSH | [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) | DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub… |
| 模块化 AI | [Azzygoatcoder/agent-useful-skills](https://github.com/Azzygoatcoder/agent-useful-skills) | 模块化 AI 科研/工程技能 monorepo（DeepSeek Harness / Claude Code 通用）— plugins/ + skills/ … |
| 全网最强 | [hoyyang/dsh-mall](https://github.com/hoyyang/dsh-mall) | 全网最强 DeepSeek Harness 插件商场：全量收录 GitHub #dsh-plugin 生态插件，五维实用评分雷达图，智能搜索（AI 理解需求）… |
| 插件市场 | [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) | DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令） |
| 技能/任务看板 | [squirrel20/dsh-cron](https://github.com/squirrel20/dsh-cron) | Unattended scheduled jobs for the DeepSeek Harness (dsh): agent/command tasks o… |
| 技能/任务看板 | [ddtcorex/maestro-skills](https://github.com/ddtcorex/maestro-skills) | Universal AI Agent Development Skills Hub & Cordis Plugin for Govard, Magento 2… |
| 在 dsh 里浏览 | [zhanghao3693/dsh-dpharness](https://github.com/zhanghao3693/dsh-dpharness) | 在 dsh 里浏览 dpharness.com 的插件目录并一键安装 —— 严选插件（汉化优先 + 可信度筛选）。Curated dsh plugin cat… |
| 技能/任务看板 | [EiffelBS/dsh-plugin-ideas-manager](https://github.com/EiffelBS/dsh-plugin-ideas-manager) | Capture ideas, anywhere: the Ideas manager brings an idea backlog straight into… |
| 技能/任务看板 | [ChenneyZhuang/changelog-capture](https://github.com/ChenneyZhuang/changelog-capture) | Changelog capture skill: user-facing entries at change time in who/what/upgrade… |
| 技能/任务看板 | [ChenneyZhuang/expense-capture](https://github.com/ChenneyZhuang/expense-capture) | Expense capture skill: receipts to ledger-ready rows without invention — transc… |
| 技能/任务看板 | [ChenneyZhuang/deliverable-versioning](https://github.com/ChenneyZhuang/deliverable-versioning) |  |
| 技能/任务看板 | [ChenneyZhuang/plain-business-english](https://github.com/ChenneyZhuang/plain-business-english) |  |
| 技能/任务看板 | [ChenneyZhuang/resume-localize-cn2en](https://github.com/ChenneyZhuang/resume-localize-cn2en) | Resume localization skill (CN to EN): demographic fields stripped, duties becom… |
| 技能/任务看板 | [aa2246740/dsh-skillhub](https://github.com/aa2246740/dsh-skillhub) | DSH manager for user Skills already on disk in Agent home and DSH home |
| 技能/任务看板 | [ChenneyZhuang/delivery-checklist](https://github.com/ChenneyZhuang/delivery-checklist) | Delivery checklist skill: verify deliverables by opening the real file — row/de… |

---


---
| 技能/看板 | [weibaohui/skills-management](https://github.com/weibaohui/skills-management) | DeepSeek Harness 插件：技能市场——安装/删除/详情 API + 管理界面 |
| 技能/看板 | [xsoc1/math-research-dsh](https://github.com/xsoc1/math-research-dsh) | DSH adaptation of the math-research Codex plugin marketplace: rigorous-o… |
| 技能/看板 | [cloader/dsh-taskboard](https://github.com/cloader/dsh-taskboard) | deepseekharness 任务看板插件 |

### 🔁 工作流 / 自动化

把重复劳动交给机器：

| 需求 | 插件 | 说明 |
|------|------|------|
| 无人值守任务队列 | [alin-ever/dsh-plugin-autoqueue](https://github.com/alin-ever/dsh-plugin-autoqueue) | 丢 .md 进收件箱 → AI 自动执行 → 产出报告 |
| 工作流 JIT 编译 | [fly3366/DeepJIT](https://github.com/fly3366/DeepJIT) | 把重复的 agent 工作流编译成 hot skills 与 flow 模板 |
| 自主多模型协同调度 | [beijingwahw/dsh-proactive](https://github.com/beijingwahw/dsh-proactive) | 主动感知、自主决策、多模型并行、质量反思自愈、经验沉淀进化 |
| 自进化升级 | [Across2005/harness-self-evolution-plugin](https://github.com/Across2005/harness-self-evolution-plugin) | 全盘自进化升级：扫描全部插件、监控性能、生成进化提案并协同升级（MCP Server） |
| 任务进度 | [Rice00/dsh-job-progress](https://github.com/Rice00/dsh-job-progress) | 长时后台任务实时进度：可拖拽浮动面板 |
| 会话报告 | [ciceroyang/dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio) | 把会话转交付物报告（日报/周报/交接/成文） |
| 双向同步 | [dpskk2/dsh-sync-plugin](https://github.com/dpskk2/dsh-sync-plugin) | 通过私有 GitHub 仓库在电脑间双向同步会话/附件/工作区/设置 |
| 工作流/自动化 | [Kreatur-ECHO/dsh-task-complete-notifier](https://github.com/Kreatur-ECHO/dsh-task-complete-notifier) | DeepSeek Harness 任务完成通知插件：任务真正结束时右下角弹出置顶深色卡片，可输入下一条指令，内置可开关叮声与自定义音效 |
| 工作流 | [xswt442-cmd/dsh-treekeeper](https://github.com/xswt442-cmd/dsh-treekeeper) | 对账 DSH 任务账本与 OS 进程树，定位归属、检测泄漏并安全治理｜Reconcile DSH task ledgers with OS pr… |

### 🔌 身份与通信 / 桥接

把 DSH 接进你已经在用的协作工具：

| 需求 | 插件 | 说明 |
|------|------|------|
| 飞书 / Lark 桥接 | [moyu-good/dsh-lark-bridge](https://github.com/moyu-good/dsh-lark-bridge) | 在飞书/Lark 内运行完整 DSH coding agent：原生思维链、交互式审批卡片、slash 命令、WS 长连接，无需公网回调 |
| QQ Bot 接入 | [tencent-connect/dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) | QQ 私聊/群聊接入 DSH agent loop（WebSocket 事件驱动） |
| 飞书 / Lark 一体化 | [tkwkeven/dsh-lark-all](https://github.com/tkwkeven/dsh-lark-all) | 官方 WS 长连接（免公网/回调），单/群聊、文件/图片/语音/视频入站、云文档读取 |
| QQ Bot 增强版 | [gcry13067381632-jpg/dsh-qqbot](https://github.com/gcry13067381632-jpg/dsh-qqbot) | 基于 tencent-connect/dsh-qqbot 的 fork：表情包图库、富媒体收发、定时任务、多实例人格、好感度系统 |
| 多 IM 接入 | [xmanrui/dsh-im](https://github.com/xmanrui/dsh-im) | 扫码/机器人凭据把飞书/微信/钉钉/企业微信/QQ/Slack/Telegram/Discord/WhatsApp 接入 DSH |
| 订阅代用模型 | [V1ki/dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) | 用 ChatGPT(Codex)/Claude/Grok 订阅作为 DSH 模型源（OAuth） |
| Codex 订阅接入 | [WSL043/dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) | 通过 OAuth 用 ChatGPT/Codex 订阅接入 DSH，含模型路由 |
| OpenCode 免费模型 | [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) | 免费 OpenCode Zen 模型接入 DSH（Free LLM API） |
| ClineBot 接入 | [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) | 原生 ClineBot / ClinePass provider 伴侣插件 |
| 模型同步 | [GooDAnDReaDY/dsh-model-sync](https://github.com/GooDAnDReaDY/dsh-model-sync) | 动态模型目录同步 + 自动余额监控（DeepSeek） |
| 局域网暴露模型 | [Saretheya/dsh-lantern](https://github.com/Saretheya/dsh-lantern) | 把本机 DSH 模型以 OpenAI/Anthropic 兼容方式暴露到局域网 |
| 模型扩展 | [lovezi0/dsh-model-extension](https://github.com/lovezi0/dsh-model-extension) | 解决 DSH 自定义模型提供商无法设置推理模式与多模态的问题 |
| 身份/通信 | [chaos-03x/dsh-agy](https://github.com/chaos-03x/dsh-agy) | Google Antigravity (agy) OAuth auth + model access plugin for DeepSeek Harness:… |
| 身份/通信 | [dingminhua/dsh-connect-workbuddy](https://github.com/dingminhua/dsh-connect-workbuddy) | Connect locally signed-in WorkBuddy models to DeepSeek Harness with a read-only… |
| 将 WorkBuddy | [XDTrees/dsh-workbuddy-xdpool](https://github.com/XDTrees/dsh-workbuddy-xdpool) | 将 WorkBuddy 桌面 App 里登录过的所有账号自动并入一个 DeepSeek Harness 模型池：无需任何手动配置，你在 WorkBuddy 桌… |
| 基于 DeepSeek | [HiQ-AI/dingtalk-dsh-assistant](https://github.com/HiQ-AI/dingtalk-dsh-assistant) | 基于 DeepSeek Harness 的钉钉群聊常驻个人助理插件 |
| 将 | [masknull/dsh-qoder-connect](https://github.com/masknull/dsh-qoder-connect) | 将 Qoder（国内版 / 国际版）的模型以个人访问令牌（PAT）接入 DeepSeek Harness —— 双变体独立配置、侧栏额度展示、上下文窗口一键切… |
| 身份/通信 | [lcestou/dsh-oh-my-claude](https://github.com/lcestou/dsh-oh-my-claude) | Claude Code CLI as an LLM provider for dsh (DeepSeek Harness): live model list,… |
| 身份/通信 | [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) | OAuth subscription LLM providers for DeepSeek Harness: ChatGPT Codex, Claude, G… |
| 身份/通信 | [songoao25/dsh-chatgpt-subscription](https://github.com/songoao25/dsh-chatgpt-subscription) | ChatGPT Subscription - a DeepSeek Harness plugin: bind your ChatGPT account via… |
| 身份/通信 | [PerryLink/dsh-reach](https://github.com/PerryLink/dsh-reach) | Multi-channel decision & remote-control bridge for DeepSeek Harness: pushes any… |
| 身份/通信 | [Gdenich/dsh-opencode-go-key-broker](https://github.com/Gdenich/dsh-opencode-go-key-broker) | DSH plugin: OpenCode Go API-key pool with quota-driven automatic switching, a S… |
| 身份/通信 | [libre-webui/dsh-native-provider](https://github.com/libre-webui/dsh-native-provider) | Use DeepSeek Harness providers in Libre WebUI over a private local connection. |
| 身份/通信 | [itchenshi/dsh-opencode-go-path](https://github.com/itchenshi/dsh-opencode-go-path) | DeepSeek Harness plugin: declares the OpenCode Go route wire protocol, auto-add… |
| 身份/通信 | [ChenneyZhuang/verify-claims](https://github.com/ChenneyZhuang/verify-claims) |  |
| 身份/通信 | [cloga/dsh-github-copilot](https://github.com/cloga/dsh-github-copilot) | DSH companion for GitHub Copilot sign-in, account-aware model profiles, tool co… |
| 身份/通信 | [MochiNek0/dsh-vendor-login](https://github.com/MochiNek0/dsh-vendor-login) | Sign in to AI coding plans that have no API key — Claude Pro/Max/Team, ChatGPT … |

### 🧑‍💻 开发 / 运行时 / Profile

面向插件作者与「一键装齐」的用户：

| 需求 | 插件 | 说明 |
|------|------|------|
| 预置插件全家桶 Profile | [Yiklek/dsh-web-profile](https://github.com/Yiklek/dsh-web-profile) | 一个 profile 预装 19 个常用 dsh 插件（better-sidebar/context/mermaid/univer-office 等），开箱即用 |
| Git 凭据加密 | [revive/dsh-git-credentials](https://github.com/revive/dsh-git-credentials) | GitLab/GitHub API Token 加密存储（AES-256-GCM）、按需工具调用、Web 设置面板 |
| 架构感知护栏 | [GanyuanRan/Aegis](https://github.com/GanyuanRan/Aegis) | 基线优先、证据校验、漂移检测，长任务安全护栏（兼 skills 包） |
| Codex 形态编码 | [bainianlaoyao/dsh-codex-harness](https://github.com/bainianlaoyao/dsh-codex-harness) | Codex 风格编码工具（exec/apply_patch/view_image）+ OpenAI 模型路由 + 创造模式预设 |
| 子代理模型路由 | [NinjaSln-labs/dsh-subagent-router](https://github.com/NinjaSln-labs/dsh-subagent-router) | 委派子代理时按 provider/model/max_tokens 路由，支持 model:"auto" 可审计策略 |
| 推理强度编辑 | [HaoyueQin/dsh-better-reasoning-effort](https://github.com/HaoyueQin/dsh-better-reasoning-effort) | 第三方模型推理强度编辑（按模型可调） |
| 推理默认与网关 | [hytime/dsh-thinking-effort](https://github.com/hytime/dsh-thinking-effort) | 推理强度默认值与协议感知网关 |
| 适配 opencode | [Duskriver/dsh-opencode-go](https://github.com/Duskriver/dsh-opencode-go) | 让 DSH 适配 opencode-go 套餐 |
| 真实 bash | [Fishquito7/dsh-gitbash](https://github.com/Fishquito7/dsh-gitbash) | 给 DSH 真实 bash 工具（Windows）：直接调 bash，免 pwsh 转义 |
| 发布镜像 | [KasenRi/dsh-orbit](https://github.com/KasenRi/dsh-orbit) | 可安装发布镜像（原项目 KasenRi/dsh-orbit） |
| 日志查询 | [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) | 用中文自然语言时间查询本地日志文件 |
| Jev 决策 | [kaijia323/dsh-plugin-jev](https://github.com/kaijia323/dsh-plugin-jev) | TypeSafe Jev（系统一决策模型）原生 jev_decide 工具插件 |
| 上下文压缩 | [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) | 通用上下文压缩代理（面向所有 AI 编码代理） |
| Codex 编码 | [shuind/dsh-codex-harness](https://github.com/shuind/dsh-codex-harness) | Codex 形态编码工具（exec/apply_patch/view_image） |
| 开发/运行时 | [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) | Installable DSH bundle: the dsh-plugin-guide plugin-development knowledge base … |
| 开发/运行时 | [hyzyn/dsh-plugin-kit](https://github.com/hyzyn/dsh-plugin-kit) | Plugin family for the DeepSeek Harness (DSH) Web GUI: a pnpm monorepo with a pl… |
| 开发/运行时 | [PerryLink/dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions) | LSP action surface for DeepSeek Harness: diagnostics, formatting, completion, c… |
| 开发/运行时 | [PerryLink/dsh-github](https://github.com/PerryLink/dsh-github) | Official-grade GitHub CI for DeepSeek Harness: composite action.yml, PR review … |
| 开发/运行时 | [PerryLink/dsh-local-ai](https://github.com/PerryLink/dsh-local-ai) | Local-model (Ollama) integration for DeepSeek Harness: discover, pull, remove, … |
| 开发/运行时 | [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) | Always-on compatibility testing for DeepSeek Harness plugins: exact releases, i… |
| 开发/运行时 | [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) | Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a… |
| 开发/运行时 | [PerryLink/dsh-translate](https://github.com/PerryLink/dsh-translate) | Vendor parameter translation and deterministic JSON repair for DeepSeek Harness… |
| 开发/运行时 | [PerryLink/dsh-observe](https://github.com/PerryLink/dsh-observe) | OpenTelemetry and Langfuse observability exporter for DeepSeek Harness: turn/st… |
| 开发/运行时 | [PerryLink/dsh-score](https://github.com/PerryLink/dsh-score) | Multi-dimensional quality scoring for DeepSeek Harness plugins: scores a repo o… |
| 开发/运行时 | [PerryLink/dsh-output-styles](https://github.com/PerryLink/dsh-output-styles) | Claude Code outputStyles for DeepSeek Harness - session-scoped, durable, runtim… |
| 开发/运行时 | [PerryLink/dsh-fast](https://github.com/PerryLink/dsh-fast) | Read-only performance diagnostics for DeepSeek Harness: session load/restore ti… |
| 开发/运行时 | [gehennawu/dsh-service](https://github.com/gehennawu/dsh-service) | DSH Web 一站式运维面板：安全重启、健康诊断、模型用量与额度查询、会话管理、备份与权限维护、任务通知、技能与子代理模型路由。｜All-in-one op… |
| 开发/运行时 | [astra3294/dsh-doctor](https://github.com/astra3294/dsh-doctor) | Deterministic diagnostics and recovery for DeepSeek Harness |
| 开发/运行时 | [zsxh1990/pr-genius](https://github.com/zsxh1990/pr-genius) | PR Genius — 提交前改进顾问 + 大型开源项目 PR 知识库 |
| 开发/运行时 | [bitterSmilezzz/dsh-model-selector](https://github.com/bitterSmilezzz/dsh-model-selector) | DeepSeek Harness (DSH) 的增强模型选择器：单层菜单（搜索 + 分组）+ 底部内联推理强度（Effort）滑杆。 |
| 开发/运行时 | [PerryLink/dsh-autotier](https://github.com/PerryLink/dsh-autotier) | Automatic strong/cheap model-tier routing for DeepSeek Harness: intent-gated ti… |
| 开发/运行时 | [Circleyan/whiteboat-dsh](https://github.com/Circleyan/whiteboat-dsh) | Whiteboat for DeepSeek Harness; the quiet water surface is the first feature sl… |
| 开发/运行时 | [VoidPrim/dsh-wsl-windows-folder-picker](https://github.com/VoidPrim/dsh-wsl-windows-folder-picker) | Windows folder picker for dsh on WSL |
| 开发/运行时 | [GreenLv/dsh-completion-guard](https://github.com/GreenLv/dsh-completion-guard) | Task-contract and completion-certification layer for DeepSeek Harness |
| 小助手 | [vianvio/dsh-assistant](https://github.com/vianvio/dsh-assistant) | DSH小助手：原生 Swift 悬浮窗 + DSH 会话状态驱动，含素材管线与日报 |
| 开发/运行时 | [PerryLink/dsh-plugin-upgrade](https://github.com/PerryLink/dsh-plugin-upgrade) | Plugin-author upgrade skill for DeepSeek Harness: one package, one corridor ind… |
| 开发/运行时 | [WoodSettler/dsh-local-proxy](https://github.com/WoodSettler/dsh-local-proxy) | DSH plugin: discover this machine's HTTP proxy (explicit .env value, else the W… |
| 开发/运行时 | [lengmoXXL/dsh-remote-workspace](https://github.com/lengmoXXL/dsh-remote-workspace) | A DeepSeek Harness (DSH) plugin that runs the harness's file, shell, and termin… |
| 开发/运行时 | [tomowang/dsh-data-agent](https://github.com/tomowang/dsh-data-agent) | DeepSeek Harness (dsh) plugin for managing database connections, browsing/annot… |
| 开发/运行时 | [andyfan1094/dsh-devforge](https://github.com/andyfan1094/dsh-devforge) | Spec-driven service forge and integrated operations plugin for DSH |
| 开发/运行时 | [harmless0819-dev/dsh-power-controls](https://github.com/harmless0819-dev/dsh-power-controls) | Close / restart DSH buttons in Settings > General, plus an opt-out auto-close t… |
| 开发/运行时 | [harmless0819-dev/dsh-codex-micro](https://github.com/harmless0819-dev/dsh-codex-micro) | Turn a Vaydeer 9-key keypad into a DSH Codex Micro: the keypad sends unique com… |

---
| 开发/运行时 | [HaowenCang/dsh-turn-performance-meter](https://github.com/HaowenCang/dsh-turn-performance-meter) | Turn-level performance telemetry and TPS monitoring for DeepSeek Harness… |
| 开发/运行时 | [FlyingBamboo/dsh-pkg-atlas](https://github.com/FlyingBamboo/dsh-pkg-atlas) | DSH 本机代码包依赖图谱（开发工具）：把已安装的 @deepseek-ai/* 包与第三方插件的依赖、挂载关系画成区-组-包三层交互图，支持聚… |
| 开发/运行时 | [yumusb/dsh-opencode-go-plus](https://github.com/yumusb/dsh-opencode-go-plus) |  |

## 全分类速览

DSH 生态目前大致按 22 个官方分类组织。下表是导航地图，括号内为每类的代表插件（部分来自已采集数据）：

| 分类 | 关注点 | 代表插件 |
|------|--------|----------|
| 🧭 AGI 架构探索 | 白箱/世界模型 | [FuRongJun-1999/dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) |
| 🎨 UI 增强 | 界面/布局/交互/中文 | [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) · [dawnliming/dsh-chinese-mode](https://github.com/dawnliming/dsh-chinese-mode) · [zjl1989-li/dsh-harness-zh-cn](https://github.com/zjl1989-li/dsh-harness-zh-cn) · [nishuoyang/dsh-wallpaper-bg](https://github.com/nishuoyang/dsh-wallpaper-bg) · [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) · [WLV-ZEDD/dsh-btw](https://github.com/WLV-ZEDD/dsh-btw) · [exoticknight/dsh-theme-eink-retro](https://github.com/exoticknight/dsh-theme-eink-retro) · [citisen/dsh-font](https://github.com/citisen/dsh-font) · [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) · [LyaxZ/dsh-fonttune](https://github.com/LyaxZ/dsh-fonttune) · [BOWLUNA/dsh-custom-mode](https://github.com/BOWLUNA/dsh-custom-mode) · [KylinQ01/dsh-startup-animation](https://github.com/KylinQ01/dsh-startup-animation) |
| 💰 用量与计费 | 余额/成本 · [weibaohui/dsh-sync](https://github.com/weibaohui/dsh-sync) · [weibaohui/context-razor](https://github.com/weibaohui/context-razor) · [1420079678-ctrl/agent-body](https://github.com/1420079678-ctrl/agent-body) · [weibaohui/dsh-fireworks](https://github.com/weibaohui/dsh-fireworks) · [AGImentu/dsh-cost-stats](https://github.com/AGImentu/dsh-cost-stats) · [webkubor/dsh-llm-hub](https://github.com/webkubor/dsh-llm-hub) · [Ychris12138/dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) · [Aa728848/dsh-chatgpt-subscription](https://github.com/Aa728848/dsh-chatgpt-subscription) · [EphoReal/Tokan-dsh-token-analytics](https://github.com/EphoReal/Tokan-dsh-token-analytics) · [orrinzeng/dsh-cursor-subscription](https://github.com/orrinzeng/dsh-cursor-subscription) · [wkscc310/dsh-client-ui-cpa-quota](https://github.com/wkscc310/dsh-client-ui-cpa-quota) | [GeekRicardo/dsh-balance](https://github.com/GeekRicardo/dsh-balance) · [kenz1117/dsh-ui-usage-billing](https://github.com/kenz1117/dsh-ui-usage-billing) · [olimc2016/dsh-token-meter-panel](https://github.com/olimc2016/dsh-token-meter-panel)|
| 🎭 主题与外观 | 皮肤/壁纸 · [weibaohui/dsh-settings-ui](https://github.com/weibaohui/dsh-settings-ui) · [Andersen216/dsh-whale-girl-live2d](https://github.com/Andersen216/dsh-whale-girl-live2d) · [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) · [LeoLee0097/dsh-desktop-acrylic](https://github.com/LeoLee0097/dsh-desktop-acrylic) · [EphoReal/my-skin-for-DeepSeek-Harness](https://github.com/EphoReal/my-skin-for-DeepSeek-Harness) | [EternalNight996/dsh-theme](https://github.com/EternalNight996/dsh-theme) · [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) · [exoticknight/dsh-theme-eink-retro](https://github.com/exoticknight/dsh-theme-eink-retro) · [elysia395/dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine) · [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) · [niiang/dsh-kimino-theme](https://github.com/niiang/dsh-kimino-theme) · [Nwflower/dsh-claude-style](https://github.com/Nwflower/dsh-claude-style) · [XHR666/dsh-mpkg-wallpaper](https://github.com/XHR666/dsh-mpkg-wallpaper)|
| 🔌 模型与账号接入 | 模型/Provider | [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) · [wss534857356/dsh-plugin-codex](https://github.com/wss534857356/dsh-plugin-codex) · [WNJXYK/dsh-codex-oauth](https://github.com/WNJXYK/dsh-codex-oauth) · [CARVIN94/dsh-router](https://github.com/CARVIN94/dsh-router) · [V1ki/dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) · [WSL043/dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) · [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) · [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) · [GooDAnDReaDY/dsh-model-sync](https://github.com/GooDAnDReaDY/dsh-model-sync) · [Saretheya/dsh-lantern](https://github.com/Saretheya/dsh-lantern) · [lovezi0/dsh-model-extension](https://github.com/lovezi0/dsh-model-extension) · [dingminhua/dsh-connect-workbuddy](https://github.com/dingminhua/dsh-connect-workbuddy) · [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) · [songoao25/dsh-chatgpt-subscription](https://github.com/songoao25/dsh-chatgpt-subscription) · [masknull/dsh-qoder-connect](https://github.com/masknull/dsh-qoder-connect) · [DLive/dsh-qqbot-community](https://github.com/DLive/dsh-qqbot-community) · [Ztyss/dsh-llm-provider](https://github.com/Ztyss/dsh-llm-provider) · [latte03/dsh-select-quote](https://github.com/latte03/dsh-select-quote) |
| 🆔 身份与通信 | 账号/IM 接入 | [lanbaolu/dsh-wechat-bridge](https://github.com/lanbaolu/dsh-wechat-bridge) · [ZhuoSir/dsh-chatops](https://github.com/ZhuoSir/dsh-chatops) · [tencent-connect/dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) · [tkwkeven/dsh-lark-all](https://github.com/tkwkeven/dsh-lark-all) · [gcry13067381632-jpg/dsh-qqbot](https://github.com/gcry13067381632-jpg/dsh-qqbot) · [xmanrui/dsh-im](https://github.com/xmanrui/dsh-im) · [HiQ-AI/dingtalk-dsh-assistant](https://github.com/HiQ-AI/dingtalk-dsh-assistant) · [PerryLink/dsh-reach](https://github.com/PerryLink/dsh-reach) |
| 💬 会话与消息 | 会话管理 | ~~[urzeye/dsh-outline](https://github.com/urzeye/dsh-outline)~~（已失效） · [PerryLink/dsh-session-pin](https://github.com/PerryLink/dsh-session-pin) · [RyanZeeee/dsh-chattree](https://github.com/RyanZeeee/dsh-chattree) · [kiligzzz/dsh-session-archive](https://github.com/kiligzzz/dsh-session-archive) · [yamingmou/dsh-retrace](https://github.com/yamingmou/dsh-retrace) · [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) · [Renzic-Stone/DSH-EasyRewrite](https://github.com/Renzic-Stone/DSH-EasyRewrite) · [Ultronen/dsh-archived-chats](https://github.com/Ultronen/dsh-archived-chats) · [sluminositys/dsh-nested-followups](https://github.com/sluminositys/dsh-nested-followups) · [DDDMUC/dsh-delete-turn](https://github.com/DDDMUC/dsh-delete-turn) · [birew83538-oss/dsh-chat-thinking-editor](https://github.com/birew83538-oss/dsh-chat-thinking-editor) · [cq-guojia/dsh-session-title-pattern](https://github.com/cq-guojia/dsh-session-title-pattern) · [shengyvself/dsh-autoresume](https://github.com/shengyvself/dsh-autoresume) · [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) · [mikugui/dsh-session-eater](https://github.com/mikugui/dsh-session-eater) · [PerryLink/dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) · [weibaohui/dsh-tasks](https://github.com/weibaohui/dsh-tasks) · [weibaohui/dsh-smart-title](https://github.com/weibaohui/dsh-smart-title) · [weibaohui/hermes-loop](https://github.com/weibaohui/hermes-loop) · [weibaohui/dsh-flow](https://github.com/weibaohui/dsh-flow) · [weibaohui/dsh-process](https://github.com/weibaohui/dsh-process) · [Lanzgale/dsh-repo-browser](https://github.com/Lanzgale/dsh-repo-browser) · [Menghuan1918/dsh-apollo](https://github.com/Menghuan1918/dsh-apollo) · [Han-Yao94/dsh-session-toolkit](https://github.com/Han-Yao94/dsh-session-toolkit) · [Ryuu-64/dsh-session-tools](https://github.com/Ryuu-64/dsh-session-tools) · [hawkongz/dsh-chat-locator](https://github.com/hawkongz/dsh-chat-locator) · [HuaimaoCy/dsh-codex-chatgpt](https://github.com/HuaimaoCy/dsh-codex-chatgpt) · [Ryuu-64/dsh-find-all](https://github.com/Ryuu-64/dsh-find-all) · [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) · [kahomesl/dsh-client-ui-job-stats](https://github.com/kahomesl/dsh-client-ui-job-stats) · [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) · [g-yixuan/dsh-sidenote](https://github.com/g-yixuan/dsh-sidenote) · [V-Reason/dsh-task-notify](https://github.com/V-Reason/dsh-task-notify) · [exoticknight/dsh-just-chat](https://github.com/exoticknight/dsh-just-chat) · [jaxzhou/dsh-file-explorer](https://github.com/jaxzhou/dsh-file-explorer) |
| 🧠 记忆 | 长期记忆 | [dygin/dsh-recover-context](https://github.com/dygin/dsh-recover-context) · [kenz1117/dsh-engram](https://github.com/kenz1117/dsh-engram) · [shaomingbo/dsh-codex-compaction](https://github.com/shaomingbo/dsh-codex-compaction) · [Aik358/dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) · [Dingpenghui-good/dsh-obsidian-sync](https://github.com/Dingpenghui-good/dsh-obsidian-sync) · [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) · [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) · [AkinoHaruka/companion-memory](https://github.com/AkinoHaruka/companion-memory) · [EPCN-fla/dsh-observational-memory](https://github.com/EPCN-fla/dsh-observational-memory) · [Fishsb/dsh-shoucang-memory](https://github.com/Fishsb/dsh-shoucang-memory) · [Soren-ABT/dsh-knowledge](https://github.com/Soren-ABT/dsh-knowledge) · [Towzai/dsh-memory-jev](https://github.com/Towzai/dsh-memory-jev) · [diqierjia/StrataGate-AgentMemory](https://github.com/diqierjia/StrataGate-AgentMemory) · [donghangxunlang-cmd/dsh-attention-health](https://github.com/donghangxunlang-cmd/dsh-attention-health) · [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) · [lovezi0/dsh-memory-palace](https://github.com/lovezi0/dsh-memory-palace) · [paulalesius/dsh-hindsight-advanced](https://github.com/paulalesius/dsh-hindsight-advanced) · [vshulcz/deja-vu](https://github.com/vshulcz/deja-vu) · [vv5v5/dsh-memory-archive](https://github.com/vv5v5/dsh-memory-archive) · [yuyuyyyyyyyyyyyy/dsh-project-memory](https://github.com/yuyuyyyyyyyyyyyy/dsh-project-memory) · [PerryLink/dsh-library](https://github.com/PerryLink/dsh-library) · [Noelune/unified-agent-memory](https://github.com/Noelune/unified-agent-memory) · [dearbld/dsh-living-memory](https://github.com/dearbld/dsh-living-memory) · [weibaohui/dsh-kb](https://github.com/weibaohui/dsh-kb) · [LoveDoLove/Veyra](https://github.com/LoveDoLove/Veyra) · [weibaohui/dsh-continue](https://github.com/weibaohui/dsh-continue) · [weibaohui/dsh-fde-tools](https://github.com/weibaohui/dsh-fde-tools) · [HuaimaoCy/dsh-memory-vault](https://github.com/HuaimaoCy/dsh-memory-vault) · [JohnXu22786/codegraph](https://github.com/JohnXu22786/codegraph) · [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) · [littleblakew/msds-chain-mcp](https://github.com/littleblakew/msds-chain-mcp) · [jonah791/dsh-agent-memory](https://github.com/jonah791/dsh-agent-memory) · [Amakurai/dsh-liketavern](https://github.com/Amakurai/dsh-liketavern) · [P02-1010751281/dsh-project-context](https://github.com/P02-1010751281/dsh-project-context) · [noteflowai/dsh-skills-anywhere](https://github.com/noteflowai/dsh-skills-anywhere) · [LuminariSoftwares/context-guardian](https://github.com/LuminariSoftwares/context-guardian) · [mattcarvercom/dsh-unified-memory](https://github.com/mattcarvercom/dsh-unified-memory) · [justhalfbit/dsh-plugin-jev-effort-selector](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector) |
| 🛠️ 工具与能力 | 能力扩展 | [superdesigndev/treg](https://github.com/superdesigndev/treg) · [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) · [whiteguo233/dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) · [br1nosense/dsh-vision-solution](https://github.com/br1nosense/dsh-vision-solution) · ~~[shinzarou-eng/dsh-codebase-chat](https://github.com/shinzarou-eng/dsh-codebase-chat)~~（已失效） · [whiskey1993/dsh-thermal-monitor](https://github.com/whiskey1993/dsh-thermal-monitor) · [ZBber-lab/cau-portal-open](https://github.com/ZBber-lab/cau-portal-open) · [FeatherHunter/dsh-prompt](https://github.com/FeatherHunter/dsh-prompt) · [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) · [TEGONG00/dsh-plugin-browser](https://github.com/TEGONG00/dsh-plugin-browser) · [beijingwahw/dsh-proactive](https://github.com/beijingwahw/dsh-proactive) · [ManoloRemiddi/DSH-Metafolder-Plugin](https://github.com/ManoloRemiddi/DSH-Metafolder-Plugin) · [fhidalgodev/dsh-odoo-sdd](https://github.com/fhidalgodev/dsh-odoo-sdd) · [NoodleStormno/dsh-plugin-tic80](https://github.com/NoodleStormno/dsh-plugin-tic80) · [MichengAI/dsh-codex-ui](https://github.com/MichengAI/dsh-codex-ui) · [caoyiwei850/dsh-ssh-ops](https://github.com/caoyiwei850/dsh-ssh-ops) · [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) · [Fishsb/dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) · [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) · [PerryLink/dsh-research-report](https://github.com/PerryLink/dsh-research-report) · [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) · [wowyuarm/dsh-agent-team](https://github.com/wowyuarm/dsh-agent-team) · [Bay-Zeddie/dsh-agent-instructions](https://github.com/Bay-Zeddie/dsh-agent-instructions) · [Chance722/dsh-inbox](https://github.com/Chance722/dsh-inbox) · [Fishsb/dsh-plugin-roundtable](https://github.com/Fishsb/dsh-plugin-roundtable) · [NEVSTOP-LAB/dsh-import-copilot-files](https://github.com/NEVSTOP-LAB/dsh-import-copilot-files) · [Rice00/dsh-job-progress](https://github.com/Rice00/dsh-job-progress) · [bychv/dsh-preset-enhance](https://github.com/bychv/dsh-preset-enhance) · [dpskk2/dsh-sync-plugin](https://github.com/dpskk2/dsh-sync-plugin) · [liudejua27-blip/fitmeet-dsh-plugin](https://github.com/liudejua27-blip/fitmeet-dsh-plugin) · [picsky/dsh-pocket-console](https://github.com/picsky/dsh-pocket-console) · ~~[wild-River2016/dsh-canvas-xiaohe](https://github.com/wild-River2016/dsh-canvas-xiaohe)~~（已失效） · [chiyu-star499/dsh-folder-drop](https://github.com/chiyu-star499/dsh-folder-drop) · [xiaoyuink/dsh-workbench](https://github.com/xiaoyuink/dsh-workbench) · [tomowang/dsh-data-agent](https://github.com/tomowang/dsh-data-agent) · [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) · [weibaohui/dsh-file-share](https://github.com/weibaohui/dsh-file-share) · [ggfgfgf-on/dsh-trajectory-anchor](https://github.com/ggfgfgf-on/dsh-trajectory-anchor) · [vINyLogY/dsh-bluebubbles](https://github.com/vINyLogY/dsh-bluebubbles) · [shuiiiiimu/dsh-stock-portfolio](https://github.com/shuiiiiimu/dsh-stock-portfolio) · [NBagent-dev/metaflywheel](https://github.com/NBagent-dev/metaflywheel) · [chen731215-dev/dsh-muv-engine](https://github.com/chen731215-dev/dsh-muv-engine) · [chen731215-dev/dsh-muv-table](https://github.com/chen731215-dev/dsh-muv-table) · [JularDepick/dsh-wakatime-plugin](https://github.com/JularDepick/dsh-wakatime-plugin) · [xiaoso456/dsh-tool-plus](https://github.com/xiaoso456/dsh-tool-plus) · [sjh9714/dsh-win32](https://github.com/sjh9714/dsh-win32) · [SouleyMoni1/dsh-experience-plugin](https://github.com/SouleyMoni1/dsh-experience-plugin) |
| 🌐 浏览器与网页 | 网页交互 | [maxwell-feng/dsh-searxng-web](https://github.com/maxwell-feng/dsh-searxng-web) · [TEGONG00/dsh-plugin-browser](https://github.com/TEGONG00/dsh-plugin-browser) · [ArcaneOrion/dsh-tavily-web](https://github.com/ArcaneOrion/dsh-tavily-web) · [2672243194/dsh-read-url](https://github.com/2672243194/dsh-read-url) · [chaserchan/dsh-browser-harness](https://github.com/chaserchan/dsh-browser-harness) · [cfanmaoli/kimi-webbridge-dsh](https://github.com/cfanmaoli/kimi-webbridge-dsh) · [weibaohui/user-management](https://github.com/weibaohui/user-management) · [taxueseek/argo](https://github.com/taxueseek/argo) · [jackie-cqz/dsh-jev-plugin](https://github.com/jackie-cqz/dsh-jev-plugin) · [auggie246/dsh-sidebar](https://github.com/auggie246/dsh-sidebar) · [janpauldahlke/dsh-slot-health](https://github.com/janpauldahlke/dsh-slot-health) · [datit309/dsh-live-inspector](https://github.com/datit309/dsh-live-inspector) · [penguin-oo/dsh-pathlink](https://github.com/penguin-oo/dsh-pathlink) · [victor10035445/dsh-v-explorer](https://github.com/victor10035445/dsh-v-explorer) · [7starsseeker/dsh-fact-check](https://github.com/7starsseeker/dsh-fact-check) · [xswt442-cmd/dsh-instance-manager](https://github.com/xswt442-cmd/dsh-instance-manager) · [janpauldahlke/dsh-gpu-monitor-nvml](https://github.com/janpauldahlke/dsh-gpu-monitor-nvml) · [qigelunbiya/DSH-Patrol](https://github.com/qigelunbiya/DSH-Patrol) · [kviiinh/dsh-whale-particles-bg](https://github.com/kviiinh/dsh-whale-particles-bg) |
| 🖼️ 视觉与多模态 | 图片/视频 | [Nagi-ovo/dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) · [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) · [shanliuling/dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) · [liustack/modlens](https://github.com/liustack/modlens) · [anionex/dsh-vision-toolkit](https://github.com/anionex/dsh-vision-toolkit) · [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) · [dickpy/dsh-imagegen](https://github.com/dickpy/dsh-imagegen) · [dundunhan/dsh-video-lens](https://github.com/dundunhan/dsh-video-lens) · [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) · [qikairo7/dsh-gemini-pool](https://github.com/qikairo7/dsh-gemini-pool) · [TikaFlow/dsh-model-fix](https://github.com/TikaFlow/dsh-model-fix) · [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) · [Lee-Hilex/dsh-mineru](https://github.com/Lee-Hilex/dsh-mineru) · [DamonBao/dsh-models-input-modalities](https://github.com/DamonBao/dsh-models-input-modalities) · [fengyungithub/dsh-short-video-studio](https://github.com/fengyungithub/dsh-short-video-studio) |
| 🎙️ 语音与音频 | 语音输入 | [qishuilalala/dsh-voice-mode](https://github.com/qishuilalala/dsh-voice-mode) · [1624318455/dsh-plugin-tts](https://github.com/1624318455/dsh-plugin-tts) · [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) · [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) · [bitterSmilezzz/dsh-asr-voice](https://github.com/bitterSmilezzz/dsh-asr-voice) · [hawkongz/dsh-task-reminder](https://github.com/hawkongz/dsh-task-reminder) |
| 📄 文档与渲染 | 文档/Markdown | [jiuyuechuwuhao/dsh-canvas-preview](https://github.com/jiuyuechuwuhao/dsh-canvas-preview) · [1692775560/dsh-Mimir-Academic-research](https://github.com/1692775560/dsh-Mimir-Academic-research) · [wjx-ai/dsh-md-reader](https://github.com/wjx-ai/dsh-md-reader) · [dream-num/dsh-univer-office](https://github.com/dream-num/dsh-univer-office) · [jing-hy/picturereader](https://github.com/jing-hy/picturereader) · [ciceroyang/dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio) · [hanzhangzzz/dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) · [zuoyunlai/lunheng-article-pipeline-dsh](https://github.com/zuoyunlai/lunheng-article-pipeline-dsh) · [JularDepick/dsh-system-monitor-plugin](https://github.com/JularDepick/dsh-system-monitor-plugin) · [naodeng/dsh-qa](https://github.com/naodeng/dsh-qa) |
| 🧩 技能包 | Skill | [lcthe/dsh-skills-hub](https://github.com/lcthe/dsh-skills-hub) · [WODE25500/dsh-skillopt](https://github.com/WODE25500/dsh-skillopt) · [cheshireez/dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) · [ddtcorex/maestro-skills](https://github.com/ddtcorex/maestro-skills) · [Azzygoatcoder/agent-useful-skills](https://github.com/Azzygoatcoder/agent-useful-skills) · [aa2246740/dsh-skillhub](https://github.com/aa2246740/dsh-skillhub) · [weibaohui/skills-management](https://github.com/weibaohui/skills-management) · [cloader/dsh-taskboard](https://github.com/cloader/dsh-taskboard) |
| 🔁 工作流与自动化 | 定时/重复/规划 | [magicOF2/dsh-schedule](https://github.com/magicOF2/dsh-schedule) · [ztl34245881-commits/dsh-task-planner](https://github.com/ztl34245881-commits/dsh-task-planner) · [beijingwahw/dsh-proactive](https://github.com/beijingwahw/dsh-proactive) · [Across2005/harness-self-evolution-plugin](https://github.com/Across2005/harness-self-evolution-plugin) · [joekytc/dsh-swarm](https://github.com/joekytc/dsh-swarm) · [Kreatur-ECHO/dsh-task-complete-notifier](https://github.com/Kreatur-ECHO/dsh-task-complete-notifier) |
| 🔀 Git 与代码评审 | Git · [weibaohui/dsh-git-server](https://github.com/weibaohui/dsh-git-server) · [peterwangze/software-project-governance](https://github.com/peterwangze/software-project-governance) · [xswt442-cmd/dsh-unsandboxed-winbash](https://github.com/xswt442-cmd/dsh-unsandboxed-winbash) · [omdsh-dev/dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) | [loadingvx/deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) · [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) · [wloops/dsh-git-worktree](https://github.com/wloops/dsh-git-worktree)|
| 🔔 通知与集成 | 提醒/推送 · [THEWOLFWALKER/dsh-notifier](https://github.com/THEWOLFWALKER/dsh-notifier) · [VoodooB0Ys/dsh-desktop-notify](https://github.com/VoodooB0Ys/dsh-desktop-notify) · [Archaofan/dsh-notify-relay](https://github.com/Archaofan/dsh-notify-relay) | [Phant0Meow/dsh-meow-smooth](https://github.com/Phant0Meow/dsh-meow-smooth) · [idoall/dsh-notify](https://github.com/idoall/dsh-notify) · [x102201/dsh-helper-plugin-notify-away](https://github.com/x102201/dsh-helper-plugin-notify-away)|
| 🧑‍💻 开发与运行时 | 开发/运行时/性能 | [tt-a1i/archify](https://github.com/tt-a1i/archify) · [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) · [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) · [Electricitysheep/dsh-tool-turbo](https://github.com/Electricitysheep/dsh-tool-turbo) · [NinjaSln-labs/dsh-subagent-router](https://github.com/NinjaSln-labs/dsh-subagent-router) · [HaoyueQin/dsh-better-reasoning-effort](https://github.com/HaoyueQin/dsh-better-reasoning-effort) · [hytime/dsh-thinking-effort](https://github.com/hytime/dsh-thinking-effort) · [6Mikao9/dsh-wsl-workspace](https://github.com/6Mikao9/dsh-wsl-workspace) · [xiajiajun516/dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) · [2025Bigeye/dsh-nanobot-subagent-link](https://github.com/2025Bigeye/dsh-nanobot-subagent-link) · [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) · [Duskriver/dsh-opencode-go](https://github.com/Duskriver/dsh-opencode-go) · [Fishquito7/dsh-gitbash](https://github.com/Fishquito7/dsh-gitbash) · [KasenRi/dsh-orbit](https://github.com/KasenRi/dsh-orbit) · [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) · [kaijia323/dsh-plugin-jev](https://github.com/kaijia323/dsh-plugin-jev) · [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) · [shuind/dsh-codex-harness](https://github.com/shuind/dsh-codex-harness) · [PerryLink/dsh-local-ai](https://github.com/PerryLink/dsh-local-ai) · [PerryLink/dsh-github](https://github.com/PerryLink/dsh-github) · [PerryLink/dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions) · [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) · [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) · [HaowenCang/dsh-turn-performance-meter](https://github.com/HaowenCang/dsh-turn-performance-meter) · [FlyingBamboo/dsh-pkg-atlas](https://github.com/FlyingBamboo/dsh-pkg-atlas) · [tomowang/dsh-tui](https://github.com/tomowang/dsh-tui) · [yumusb/dsh-opencode-go-plus](https://github.com/yumusb/dsh-opencode-go-plus) |
| 🔒 安全与权限 | 权限/审计 | [cuddly-guacamole/dsh-auto-approval-llm](https://github.com/cuddly-guacamole/dsh-auto-approval-llm) · [PerryLink/dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) · [dhicoc/dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) · [ylwl1997/noatmark-dsh-plugin](https://github.com/ylwl1997/noatmark-dsh-plugin) · [toby-bridges/api-relay-audit](https://github.com/toby-bridges/api-relay-audit) · [GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard) · [PerryLink/dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) · [PerryLink/dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) · [PerryLink/dsh-defend](https://github.com/PerryLink/dsh-defend) · [7starsseeker/dsh-jev-guard](https://github.com/7starsseeker/dsh-jev-guard) · [MrWeiCodes/dsh-permgate](https://github.com/MrWeiCodes/dsh-permgate) · [bbaz123/dsh-confirmation-resolution](https://github.com/bbaz123/dsh-confirmation-resolution) · [imtokenxinluo/dsh-contract-check](https://github.com/imtokenxinluo/dsh-contract-check) · [PerryLink/dsh-mask](https://github.com/PerryLink/dsh-mask) · [weibaohui/experts-management](https://github.com/weibaohui/experts-management) · [xiaozhuyuqing/dsh-repeat-guard](https://github.com/xiaozhuyuqing/dsh-repeat-guard) |
| 📱 远程与移动端 | 移动/远程 | [TecFancy/dsh-mobile](https://github.com/TecFancy/dsh-mobile) · [saya-ch/dsh-mobile](https://github.com/saya-ch/dsh-mobile) · [advance-lion/dsh-lan-link](https://github.com/advance-lion/dsh-lan-link) · [Clarklevis1995/dsh-plugin-mobile-gateway](https://github.com/Clarklevis1995/dsh-plugin-mobile-gateway) · [zexadev/dsh-tether](https://github.com/zexadev/dsh-tether) · [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) · [mexiaosqwq/dsh-web-mobile](https://github.com/mexiaosqwq/dsh-web-mobile) · [cilis/dsh-tauri-launcher](https://github.com/cilis/dsh-tauri-launcher) · [Kickstartparty3459/dsh-ios](https://github.com/Kickstartparty3459/dsh-ios) |
| 🛒 插件市场与管理 | 市场/管理 | [dsh-market](https://github.com/dsh-market/dsh-market) · [dshfind](https://github.com/hikariming/dshfind) · [Fishquito7/dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) · [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) · [hoyyang/dsh-mall](https://github.com/hoyyang/dsh-mall) · [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) · [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) · [xsoc1/math-research-dsh](https://github.com/xsoc1/math-research-dsh) · [yhbd-top/dsh-plugin-top](https://github.com/yhbd-top/dsh-plugin-top) · [kangtsang/dsh-worktree-space](https://github.com/kangtsang/dsh-worktree-space) · [Alphauni-x/dsh-mcp-market](https://github.com/Alphauni-x/dsh-mcp-market) · [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) · [fsrmqi/dsh-research-kit](https://github.com/fsrmqi/dsh-research-kit) · [bruceyork00-a11y/PinMe](https://github.com/bruceyork00-a11y/PinMe) · [HaoyueQin/deepseek-harness-background](https://github.com/HaoyueQin/deepseek-harness-background) · [xswt442-cmd/dsh-ballast](https://github.com/xswt442-cmd/dsh-ballast) · [xswt442-cmd/dsh-treekeeper](https://github.com/xswt442-cmd/dsh-treekeeper) |
| 🎮 娱乐 | 趣味 | [cookiesheep/whale-on-desk](https://github.com/cookiesheep/whale-on-desk) · ~~[weibaohui/dsh-xiuxian](https://github.com/weibaohui/dsh-xiuxian)~~（已失效） · [nickkkkkk123123/dsh-whale-girl](https://github.com/nickkkkkk123123/dsh-whale-girl) |

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

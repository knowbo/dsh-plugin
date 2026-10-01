# DeepSeek Harness (DSH) 插件实操手册 · 中文版

> 把「能装的插件」变成「能照着做的教程」。一份面向中文用户的 DSH 插件上手、选型与排错指南，由社区共建维护。

[![语言：简体中文](https://img.shields.io/badge/语言-简体中文-blue.svg)](https://www.workbuddy.cn)
[![许可：CC0](https://img.shields.io/badge/license-CC0-green.svg)](./LICENSE)
[![收录插件](https://img.shields.io/badge/收录插件-1300%2B-brightgreen.svg)](./README.md)

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
| 外观 | [nonamelego/dsh-catppuccin-theme](https://github.com/nonamelego/dsh-catppuccin-theme) | DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可… |
| 外观 | [tqsy114514/dsh-ui-appearance](https://github.com/tqsy114514/dsh-ui-appearance) | Appearance customization plugin for DeepSeek Harness: theme color palette, background imag… |
| 外观 | [wenaixi/dsh-ponytail](https://github.com/wenaixi/dsh-ponytail) | DSH 完整移植版 DietrichGebert/ponytail — 懒惰 senior 模式，hook注入 |
| 外观 | [stardustlc666/dsh-ppt](https://github.com/stardustlc666/dsh-ppt) | DSH 演示文稿插件：Markdown 生成网页放映与可编辑 PPTX，长表格自动分页，内置 5 套主题、备注与转场动画。 |
| 外观 | [aik358/dsh-draw-gacha](https://github.com/aik358/dsh-draw-gacha) | DeepSeek绘画抽卡 · 给 DeepSeek Harness 的发送按钮旁加一根 3D 拉杆，用模型思维链文本信号开一局像素风「滑动变祖器」抽卡。Just for fun. |
| 外观 | [britneycode/dsh-update-center](https://github.com/britneycode/dsh-update-center) | dsh (DeepSeek Harness) 更新中心与插件市场：自托管 plugins.json 注册表（GitHub dsh-plugin 主题自动聚合 + npm 包名映射秒… |
| 外观 | [nicholaskin/vision-exp-tile](https://github.com/nicholaskin/vision-exp-tile) | DSH（DeepSeek Harness）插件：800×800 无损切块 + 坐标标注 + 直连 DeepSeek 视觉 API 识别聚合，专治大图看不清 |
| 外观 | [erbsen16/dsh-client-ui-dracula](https://github.com/erbsen16/dsh-client-ui-dracula) | 把 VS Code 的 Dracula（吸血鬼）配色搬到 DeepSeek Harness 的网页界面，顺带做了一组程序员向的排版调优。深色模式专用，随时可整页还原。 |

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
| 余额 | [featherhunter/dsh-mattpocock-skills-deck](https://github.com/featherhunter/dsh-mattpocock-skills-deck) | 安装即自带mattpocock/skills v1.2.3的25个工程与效率技能，无需手动装技能。300亿token打造。本插件在原始技能之上提供10倍的开发效率。主力支持GitH… |
| 余额 | [nicholas023/vision-exp-tile](https://github.com/nicholas023/vision-exp-tile) | DSH 插件：大图切 800×800 无损小块 + 坐标标注 + 分块聚合逻辑，直连 deepseek-v4-flash-vision-exp 识别；仅用纯官方 DSH 功能，零依… |
| 余额 | [162568316/dsh-tokenrhythm-bill](https://github.com/162568316/dsh-tokenrhythm-bill) | dsh-tokenrhythm-bill |
| 余额 | [baroncyrus/dsh-kimi-subscription](https://github.com/baroncyrus/dsh-kimi-subscription) | Use a Kimi Code subscription in DeepSeek Harness with OAuth, quota display, and composer u… |
| 余额 | [movingelated/dsh-localmodels-tokensavior](https://github.com/movingelated/dsh-localmodels-tokensavior) | DSH (DeepSeek Harness) plugin: delegate read-only collection tasks to a local Ollama model… |
| 余额 | [functy23/dsh-workbuddy-connect-functy](https://github.com/functy23/dsh-workbuddy-connect-functy) | corrinehu/dsh-workbuddy-connect 的 Functy 分支：仪表盘、多账号轮换与额度展示，把 WorkBuddy 模型接到 DeepSeek Harne… |

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
| 文件/@file | [2768651338/dsh-plugin-manager](https://github.com/2768651338/dsh-plugin-manager) | DeepSeek Harness 的图形化插件管理插件：在 设置 → 插件 里新增「插件管家」标签页，用中文名和说明展示每个插件是做什么的，并提供一键启停开关与内置备注编辑——启停… |
| 文件/@file | [stardustlc666/dsh-calendar](https://github.com/stardustlc666/dsh-calendar) | DSH 日历插件：可视化周/月视图、拖拽改期与 CalDAV 日程管理，支持 Google OAuth2、iCloud、Nextcloud。 |

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
| 工作台 | [noob-stupid/dsh-plugin-gating-hub](https://github.com/noob-stupid/dsh-plugin-gating-hub) | DSH plugin - framework upgrade safety & plugin gating: contract pre-check, rollback point,… |
| 工作台 | [dely0/dsh-personal-workbench](https://github.com/dely0/dsh-personal-workbench) | DSH 个人工作台：日历 + 任务列表 + AI 澄清/拆解/执行/复盘 / Personal workbench for DeepSeek Harness Web: calend… |
| 工作台 | [vncntvx/dsh-zotero](https://github.com/vncntvx/dsh-zotero) | Zotero toolkit for DeepSeek harness; Turn your Zotero library into an evidence store for a… |
| 工作台 | [2768651338/dsh-effort-slider](https://github.com/2768651338/dsh-effort-slider) | 仿 Claude Code 推理等级滑块 支持第三方模型 DSH 插件 |
| 工作台 | [goodandready/dsh-key-rotation](https://github.com/goodandready/dsh-key-rotation) | Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429 rate-limit fa… |
| 工作台 | [jerryliu369/agent-web-search](https://github.com/jerryliu369/agent-web-search) | Agent-native multi-provider web search for AI agents (Claude Code, Hermes, DeepSeek Harnes… |
| 工作台 | [mokuyoaxis/dsh-iris](https://github.com/mokuyoaxis/dsh-iris) | Media generation and visual understanding for DeepSeek Harness, with multi-provider routin… |
| 工作台 | [chendefine/dsh-web-fetch-playwright](https://github.com/chendefine/dsh-web-fetch-playwright) | Playwright/CDP web-fetch provider for DeepSeek Harness: renders pages in a real browser, d… |
| 工作台 | [goodandready/dsh-clinebot](https://github.com/goodandready/dsh-clinebot) | Native ClineBot / ClinePass provider companion plugin for DeepSeek Harness (DSH) |
| 工作台 | [eastmg/dsh-gacha-calendar](https://github.com/eastmg/dsh-gacha-calendar) | DeepSeek Harness 二游卡池/活动日历速查插件：侧边栏按钮 内置 11 款主流二游 可添加自定义游戏 |
| 工作台 | [windypro-rourou/dsh-code-studio](https://github.com/windypro-rourou/dsh-code-studio) | Code Studio for DSH Web GUI - VS Code + Cline hybrid: file tree, syntax-highlighted editor… |
| 工作台 | [viztor/dsh-tinyfish](https://github.com/viztor/dsh-tinyfish) | TinyFish-backed search and fetch providers for the DeepSeek Harness web capability seam (c… |
| 工作台 | [namesmt/dsh-home-hosted](https://github.com/namesmt/dsh-home-hosted) | DeepSeek Harness (dsh) plugin: start your dsh web server automatically at boot, and manage… |

### 🖥️ 终端

| 需求 | 插件 | 说明 |
|------|------|------|
| 终端面板 | [giiiiiithub/terminal](https://github.com/giiiiiithub/terminal) | node-pty + xterm.js，多标签 |
| 底部终端 | [siberiah2o/dsh-plugin-terminal](https://github.com/siberiah2o/dsh-plugin-terminal) | 贴底全宽，输入框始终在上 |
| 主对话驱动 SSH 运维 | [caoyiwei850/dsh-ssh-ops](https://github.com/caoyiwei850/dsh-ssh-ops) | 主对话驱动 SSH，带高危命令保护与右侧终端 |
| 终端 | [tomowang/dsh-tui](https://github.com/tomowang/dsh-tui) | An open-source terminal front door for DeepSeek Harness (dsh). |
| 终端 | [zhang66633/dsh-pixel-ui](https://github.com/zhang66633/dsh-pixel-ui) | DeepSeek Harness 像素皮肤（Agent Xi 风格）：四个主题一键切换——像素·木屋 / 像素·羊皮纸 / 像素·暖阳 / 像素·终端绿，随时可切回现代默认 UI。 |

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
| 桌面壳 | [nwflower/dsh-claude-style](https://github.com/nwflower/dsh-claude-style) | Claude Code Desktop theme for DeepSeek Harness｜ 为 DeepSeek Harness 网页 GUI 打造的 Claude Code … |
| 桌面壳 | [hiq-ai/dingtalk-dsh-assistant](https://github.com/hiq-ai/dingtalk-dsh-assistant) | 基于 DeepSeek Harness 的钉钉群聊常驻个人助理插件 |
| 桌面壳 | [han-1413141/dsh-ui-hub](https://github.com/han-1413141/dsh-ui-hub) | DeepSeek Harness Desktop and Web UI manager: search, show/hide, move, resize and arrange p… |
| 桌面壳 | [mandarin715/dsh-autostart](https://github.com/mandarin715/dsh-autostart) | Windows 专用 DSH 插件:一键开机自启 + 一键重启,而且重启失败也不会把 DSH 关掉不回来;DSH 由常驻看护进程启动,全程无控制台窗口 / Windows-only… |

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
| 移动端 | [ychris12138/dsh-usage-stats](https://github.com/ychris12138/dsh-usage-stats) | Provider balances, subscription quotas, and token-usage analytics for the DeepSeek Harness… |
| 移动端 | [goodandready/dsh-russian-lang](https://github.com/goodandready/dsh-russian-lang) | 100% русская локализация и Smart UX для DeepSeek Harness (DSH v0.1.7+): 7574 ключа (ядро +… |
| 移动端 | [unclek/dsh-think-translate](https://github.com/unclek/dsh-think-translate) | Thinking-chain UI translation for DeepSeek Harness: 8 target languages, local Ollama model… |
| 移动端 | [wycto/dsh-dock](https://github.com/wycto/dsh-dock) | dsh-dock · DeepSeek Harness 功能坞插件：一张面板统一注册/开关所有小功能——用量记账（自定义单价·分时价）、模型设置与余额、19 种任务动画、任务通知（… |
| 移动端 | [godchen520/dsh-web-remote](https://github.com/godchen520/dsh-web-remote) | DSH 手机/外网远程访问插件：免配置公网隧道 + 局域网 HTTPS 直连 + 自定义公网链接/端口 + 微信机器人 |
| 移动端 | [particlelight/dsh-all-usage](https://github.com/particlelight/dsh-all-usage) | DeepSeek Harness 用量看板 / Usage dashboard: tokens, cache, model/provider/workspace analytics… |
| 移动端 | [leifdai/mackorn-hydraulic-cone-crusher](https://github.com/leifdai/mackorn-hydraulic-cone-crusher) | mining industry vertical-domain MACKORN cone crusher plugin: Mackorn cone crusher,world fa… |
| 移动端 | [lin-dongg/dsh-musage-card](https://github.com/lin-dongg/dsh-musage-card) | Multi-provider (11) quota & balance glass card for the DSH sidebar footer — local fork of … |
| 移动端 | [zhanxueyou/dsh-plugin-manager](https://github.com/zhanxueyou/dsh-plugin-manager) | DSH Web 客户端插件管理器侧边栏面板：全量插件清单（描述/状态/来源/版本/分类）、启停热重载、删除本地自定义插件，并可浏览、搜索、一键安装 GitHub topic:dsh… |

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
| 记忆 | [seriousz158/dsh-memory](https://github.com/seriousz158/dsh-memory) |  |
| 记忆 | [diqierjia/stratagate-agentmemory](https://github.com/diqierjia/stratagate-agentmemory) | Recent memories stay detailed. Older ones grow concise. Important ones live on.近期记忆保持详细，旧记… |
| 记忆 | [zekaishi/evo-subagent](https://github.com/zekaishi/evo-subagent) | Unified DeepSeek Harness plugin: role-based subagent routing + per-agent evolution (prefer… |
| 记忆 | [edge-echo/dsh-mcp-bridge](https://github.com/edge-echo/dsh-mcp-bridge) | Curated, verified MCP server bundle for DeepSeek Harness (dsh): one install brings demo, m… |
| 记忆 | [icstick/dsh-adaptive-context](https://github.com/icstick/dsh-adaptive-context) | DeepSeek Harness 的 AdaptiveContextPlane (ACP) 插件——带治理的长期记忆系统 |
| 记忆 | [umineko987/dsh-search-enhance](https://github.com/umineko987/dsh-search-enhance) | 提供 Grok-compatible 网页搜索、保留来源分页、Context7 与 Exa 文档检索、有界网页提取、站点映射、离线研究计划和只读诊断。 |
| 记忆 | [xiangrui979/foresight](https://github.com/xiangrui979/foresight) | ForeSight: a temporal-aspect long-term memory plugin for DeepSeek Harness (dsh) |
| 记忆 | [ycet/dsh-awesome-hud](https://github.com/ycet/dsh-awesome-hud) | dsh侧边HUD面板，包含多个信息展示模块（可自定义是否展示），集成压缩上下文、查看git graph等功能。DSH side HUD panel, containing mult… |
| 记忆 | [drscrewdriver/dsh-context-compression-improved](https://github.com/drscrewdriver/dsh-context-compression-improved) | Improved fork of dsh-context-compression-selector with an orthogonal code-skeleton compres… |
| 记忆 | [leolee9086/dsh-context-care](https://github.com/leolee9086/dsh-context-care) | DeepSeek Harness 的疲劳度、唤醒值与自主上下文压缩 Cordis 插件 |

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
| 会话 | [omdsh-dev/dsh-better-sidebar](https://github.com/omdsh-dev/dsh-better-sidebar) | 开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/侧边对话/Git/子代理页面 ｜ Open sidebar foundation, supports thi… |
| 会话 | [v1ki/dsh-plugin-subscriptions](https://github.com/v1ki/dsh-plugin-subscriptions) | Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM pr… |
| 会话 | [nwflower/dsh-chat-import](https://github.com/nwflower/dsh-chat-import) | Import conversation history from 25+ AI coding agents into DeepSeek Harness as resumable s… |
| 会话 | [revolutionla/dsh-dream-skin](https://github.com/revolutionla/dsh-dream-skin) | DeepSeek Harness 换肤 / 壁纸 / 主题包插件 (dsh-plugin) — 8 套 Mirage 主题、每用户强调色、壁纸2.0、主题包导入导出/分享链接、收藏… |
| 会话 | [michengai/dsh-archive-manager](https://github.com/michengai/dsh-archive-manager) | DSH Archive Manager — 在 DeepSeek Harness 中安全查看、恢复和管理已归档会话 · Safely view, restore, and mana… |
| 会话 | [aa728848/dsh-chatgpt-subscription](https://github.com/aa728848/dsh-chatgpt-subscription) |  |
| 会话 | [zk-andy/dsh-continual-evolve](https://github.com/zk-andy/dsh-continual-evolve) | Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe … |
| 会话 | [zoria-lind/dsh-token-optimizer](https://github.com/zoria-lind/dsh-token-optimizer) | Layered token-optimization pipeline for DeepSeek Harness: output ladder, MCP lazy loading,… |
| 会话 | [freehul/sgme](https://github.com/freehul/sgme) | SGME 拾光记忆引擎：AI 全面接管记忆、技能库、WIKI 知识库三大模块，跨会话、多智能体共享记忆，AI 会一直记得你的偏好。ShiGuang Memory Engine · … |
| 会话 | [jrjrjpro/dsh-chat-tree](https://github.com/jrjrjpro/dsh-chat-tree) | 把 对话分支 画成 可点击的树 |
| 会话 | [taoser258/dsh-client-ui-skin-qingxiao](https://github.com/taoser258/dsh-client-ui-skin-qingxiao) | 清宵 · 弦凝清霄 —— DeepSeek Harness (DSH) Web 界面美化皮肤：以《鸣潮》角色清宵为灵感的冰蓝·青碧·月白·玄夜调色板，含可换背景画卷、剑气流光粒子、… |
| 会话 | [qwert702/dsh-token-viewer](https://github.com/qwert702/dsh-token-viewer) | Developer tool: live token usage & cost monitoring for DeepSeek Harness - consumed tokens … |
| 会话 | [gezi-wen/sage-mem](https://github.com/gezi-wen/sage-mem) | File-based cross-session memory for DeepSeek Harness (DSH) — every memory is a plain Markd… |
| 会话 | [wenzetan/dsh-llm-newapi](https://github.com/wenzetan/dsh-llm-newapi) | NewAPI (OpenAI-compatible gateway) LLM provider plugin for DeepSeek Harness (dsh): chat-on… |
| 会话 | [daetz-coder/dsh-multi-chat](https://github.com/daetz-coder/dsh-multi-chat) | Multi-window wall for DeepSeek Harness: run & monitor N DSH conversations side-by-side in … |
| 会话 | [stardustlc666/dsh-rss](https://github.com/stardustlc666/dsh-rss) | DSH RSS 插件：订阅源管理、OPML 导入导出、抓取解析 RSS/Atom 并保留正文。 |
| 会话 | [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) | Session deep links + full session export (markdown/JSON) + approved cross-session messagin… |
| 会话 | [itbaymax/dsh-replay-theater](https://github.com/itbaymax/dsh-replay-theater) | Replay a DeepSeek Harness session at its original token cadence — an in-app playback theat… |
| 会话 | [max-null/dsh-node-appearance](https://github.com/max-null/dsh-node-appearance) | Conversation node appearance for DeepSeek Harness Web GUI: colorize nodes by type/tool (co… |
| 会话 | [vitas/dsh-web-search-gateway](https://github.com/vitas/dsh-web-search-gateway) | Grounded web search for DeepSeek Harness on any OpenRouter-compatible gateway: the built-i… |
| 会话 | [functy23/dsh-mcp-studio](https://github.com/functy23/dsh-mcp-studio) | DeepSeek Harness 的 MCP 服务与 Skills 管理器：面板里增删改 MCP 行、扫描导入其他 Agent 配置、管理 Skills（DSH Web 插件） |
| 会话 | [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) | OpenCode on DeepSeek Harness — DSH plugin that keeps OpenCode Zen + Go free-tier models wo… |
| 会话 | [sunshiner04/dsh-session-manager](https://github.com/sunshiner04/dsh-session-manager) | DeepSeek Harness (DSH) plugin: manage archived sessions - list, restore, permanently delet… |
| 会话 | [chance722/dsh-inbox](https://github.com/chance722/dsh-inbox) | dsh 插件：把复制粘贴的链接、图片、文本、账密收进本地仓库，自动分类，能在对话里检索取回 |

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
| 提示词 | [yujunzhixue/dsh-purge](https://github.com/yujunzhixue/dsh-purge) | DeepSeek Harness 破甲：让所有模型都能破甲，不同模型可换不同提示词；默认提示词面向国模「小码酱」。Jailbreak for every model — swap … |
| 提示词 | [amakurai/dsh-liketavern](https://github.com/amakurai/dsh-liketavern) | A DeepSeek Harness (dsh) plugin — turns dsh web into a SillyTavern-style roleplay frontend… |
| 提示词 | [aik358/dsh-auto-memory](https://github.com/aik358/dsh-auto-memory) | Proactive associative memory for DSH: system-prompt recall before the model speaks, three-… |
| 提示词 | [gulagala001/oh-my-dsh](https://github.com/gulagala001/oh-my-dsh) | 让你的 DSH，火力全开。长上下文、任务验证、提示词优化、代码理解、电脑操作与四套完整主题。 |
| 提示词 | [featherhunter/dsh-prompt](https://github.com/featherhunter/dsh-prompt) | DeepSeek Harness 的 Prompt 工具箱：别再复制粘贴——24 条深度模板随手点，/prompt 与智能推荐主动兜底，装好即用、可自定义。 / The Promp… |
| 提示词 | [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) | Aggressive context compaction for local-first agents. Runs Qwen3.8‑27B on self‑hosted llam… |
| 提示词 | [zoria-lind/dsh-behavior-enhancer](https://github.com/zoria-lind/dsh-behavior-enhancer) | Behavior-management plugin for DeepSeek Harness: tool-call discipline prompt section, fail… |
| 提示词 | [yingjian666/dsh-zh-thinking](https://github.com/yingjian666/dsh-zh-thinking) | DeepSeek Harness (dsh) 插件：注入系统提示词，强制 Agent 的思维链 / 规划 / 工具推理全程使用简体中文，防止中文思考漂移为英文。零外部依赖，任意本地… |
| 提示词 | [han-yao94/dsh-session-toolkit](https://github.com/han-yao94/dsh-session-toolkit) | DeepSeek Harness plugin bundle — session identity, global prompt (global + per-workspace),… |
| 提示词 | [bowluna/dsh-custom-mode](https://github.com/bowluna/dsh-custom-mode) | Custom mode for DeepSeek Harness (dsh): edit a mode's system prompt, base mode and plugin … |
| 提示词 | [hwayn-pixel/dsh-prompt-desk](https://github.com/hwayn-pixel/dsh-prompt-desk) | DSH 提示词工作台：看清 system prompt 的每一段、写下自己的家规、体检重复与矛盾，并记下每次改动。A prompt workbench for DSH. |

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
| 导航 | [michengai/dsh-codex-ui](https://github.com/michengai/dsh-codex-ui) | DSH Codex UI — 为 DeepSeek Harness Web 提供 Codex 风格侧栏、工作区会话树、全局搜索和轮次导航 · A Codex-style sideb… |
| 导航 | [lamost423/dsh-maze](https://github.com/lamost423/dsh-maze) | DeepSeek Harness 的执行迷宫——看 Agent 真实怎么干活：迷宫时间轴 · 数据轨道 · 确定性执行分析 · 多会话对比 / The execution maze… |
| 导航 | [celebrate-w/dsh-topic-trail](https://github.com/celebrate-w/dsh-topic-trail) | 会话工作线索悬浮窗：把和 AI 的长对话实时提炼成可跳转的「线索」，并用 DeepSeek 生成话题、进度与阶段历程 |
| 导航 | [ycet/dsh-account-usage](https://github.com/ycet/dsh-account-usage) | 为dsh增加「设置：账户」页面，可快捷查看deepseek余额、用量信息，以及opencode go额度信息，同时可快速跳转至对应官网。Add a "Settings: Accou… |
| 导航 | [hhb1028/dsh-client-ui-timeline](https://github.com/hhb1028/dsh-client-ui-timeline) | DSH Web GUI 会话问题导航条：聊天区左缘一问一杠，随滚动高亮当前问题、悬停显示问答预览气泡、点击把该问平滑滚到视口顶（未渲染的更早历史自动翻页加载），无需改动 dsh 本… |

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
| 桌宠 | [ccch1mneyyy/dsh-tui](https://github.com/ccch1mneyyy/dsh-tui) | DSH's officially recommended TUI plugin — high performance, low overhead, cute pixel whale… |
| 桌宠 | [sutera-diffusus/dsh-whale-musume](https://github.com/sutera-diffusus/dsh-whale-musume) | DeepSeek Harness 桌宠插件：元气鲸鱼娘陪你写代码 🐋（桌面端 0.2.0-rc.2 与旧版 Web 双端支持） |
| 桌宠 | [andersen216/dsh-whale-girl-live2d](https://github.com/andersen216/dsh-whale-girl-live2d) | 🐋 鲸鱼娘桌宠 · Whale Girl Live2D —— DSH（DeepSeek Harness）Web 界面里的 Live2D 桌宠：跟着 agent 的真实状态换表情与动… |
| 桌宠 | [luweiyabo/dsh-whale-pet](https://github.com/luweiyabo/dsh-whale-pet) | DeepSeek Harness Web UI 的开源鲸鱼桌宠插件，支持 Agent 状态感知、多种透明动画、点击拖拽、屏幕漫游、自定义动作与触发规则。 |
| 桌宠 | [clicgger-types/dsh-piggy](https://github.com/clicgger-types/dsh-piggy) | 🐖 一只住在 DeepSeek Harness 里的猪，也能单独装成 Windows/Linux 桌面宠物。QQ 宠物式养成：长大、上学、打工、旅行、生病、加冕；九宫格主屏 + 居… |
| 桌宠 | [zhu1090093659/dsh-pet](https://github.com/zhu1090093659/dsh-pet) | Multi-pet companion plugin for the DSH Web GUI: a registry-driven floating pet that reacts… |
| 桌宠 | [cyberwei922/dsh-cyberwhale](https://github.com/cyberwei922/dsh-cyberwhale) | 一只常驻 macOS 桌面、随 DeepSeek Harness 工作状态变化的蓝色大肥鲸桌宠 |
| 桌宠 | [miku00039-01/dsh-whale-pet](https://github.com/miku00039-01/dsh-whale-pet) | 🐋 DSH 桌宠:DeepSeek Harness 的 Windows 桌面宠物,一键启动/停止/监测服务,双击唤起 GUI,零依赖单文件 exe |

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
| 语音 | [goodandready/dsh-voice](https://github.com/goodandready/dsh-voice) | Voice input for DeepSeek Harness: dictation and voice messages with multi-provider STT fal… |
| 语音 | [aitcmhk-web/dsh-bot](https://github.com/aitcmhk-web/dsh-bot) | 通过 TG/微信实现离家办公：发布任务、语音聊天、切换模型、升级重启、自动记忆...Telegram / WeChat bridge plugin for DeepSeek Har… |
| 语音 | [sixtysevenlf/dsh-sound-cues](https://github.com/sixtysevenlf/dsh-sound-cues) | DSH 声音提示插件：把 DSH 的各种状态变成提示音 —— 任务失败放关羽之歌《江上行》高潮句，goal 目标达成放 We Are the Champions 副歌；37 条 c… |
| 语音 | [jryang1997/dsh-hold-to-dictate](https://github.com/jryang1997/dsh-hold-to-dictate) | Hold-to-talk dictation for the DeepSeek Harness composer: long-press the input box, releas… |

### 📈 行情 / 股票（A 股红涨绿跌）

| 需求 | 插件 | 说明 |
|------|------|------|
| A股/港股/美股 | [FeiZhuNiU-INFJA/dsh-stock-ticker](https://github.com/FeiZhuNiU-INFJA/dsh-stock-ticker) | 上证/创业板/科创50/恒生科技，红涨绿跌 |
| 雪球面板 | [kangjinghang/dsh-xueqiu](https://github.com/kangjinghang/dsh-xueqiu) | K线蜡烛图、热榜、7×24 快讯 |
| 行情/持仓 | [shuiiiiimu/dsh-stock-portfolio](https://github.com/shuiiiiimu/dsh-stock-portfolio) | DeepSeek Harness 中管理股票持仓的插件 |
| 行情 | [hancao97/hanai-investment-dsh](https://github.com/hancao97/hanai-investment-dsh) | Local-first A-share research workbench for DeepSeek Harness: market dashboards, watchlists… |
| 行情 | [a961282799-crypto/dsh-timeband](https://github.com/a961282799-crypto/dsh-timeband) | DeepSeek Harness 头像旁的峰谷时段、倒计时与 24 小时时间轴插件 |

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
| 浏览器 | [ikalus1988/misakanet](https://github.com/ikalus1988/misakanet) | 📚 A zero-dependency, git-backed micro-lesson library for AI Agents to asynchronously share… |
| 浏览器 | [bradegithub/dsh-plugins-marketplace](https://github.com/bradegithub/dsh-plugins-marketplace) | DSH插件市场 / DSH Plugin Marketplace: 在 DeepSeek Harness Web GUI 中一键浏览、安装与更新 GitHub topic:dsh-… |
| 浏览器 | [theyoungchen/dsh-plugin-market](https://github.com/theyoungchen/dsh-plugin-market) | DeepSeek Harness plugin market - browse, search & install dsh-plugin topic plugins (dsh 插件… |
| 浏览器 | [causebefore/dsh-pomodoro](https://github.com/causebefore/dsh-pomodoro) | DeepSeek Harness Web 番茄钟插件：可配置专注与休息时长，提供侧栏入口和可拖动浮动面板 |
| 浏览器 | [ycet/dsh-notifications](https://github.com/ycet/dsh-notifications) | DeepSeek Harness web notifications plugin |
| 浏览器 | [luaphes/dsh-plugins-market](https://github.com/luaphes/dsh-plugins-market) | DSH的插件创意市场来啦!～～～欢迎使用&提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方 dsh-plugin top… |
| 浏览器 | [rindbeans/codex-ui](https://github.com/rindbeans/codex-ui) | DSH Web 的 Codex 化界面插件 · A Codex-style interface plugin for DSH Web |
| 浏览器 | [z-col/dsh-skillsmanageplugins](https://github.com/z-col/dsh-skillsmanageplugins) | DSH Skills 可视化管理器：在 DSH Web 界面可视化查看、编辑、创建、删除 Skills（用户级 ~/.dsh/skills 与项目级 .dsh/skills） |
| 浏览器 | [falling-ts/dsh-web-ding](https://github.com/falling-ts/dsh-web-ding) | Browser-only 'ding' on agent end; works on servers.浏览器专属"叮":回合结束时响起,服务器部署也生效 |
| 浏览器 | [miqian-nomad/dsh-browser-playwright-codex](https://github.com/miqian-nomad/dsh-browser-playwright-codex) | DSH 的浏览器：登录一次，它就用你的账号替你办事（查后台/填表/抓列表/多标签）；要登录、验证码、弹框会停下来等你，绝不替你点「确定」；你最小化它就不吵你，AI 在哪动手你随时看… |

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
| MCP | [smalldy/godot-bridge](https://github.com/smalldy/godot-bridge) | DSH (DeepSeek Harness) plugin that launches and drives a running Godot 4.x game through it… |
| MCP | [mari23333/dsh-subagent-library](https://github.com/mari23333/dsh-subagent-library) | DeepSeek Harness 具名子代理库插件：settings 驱动的角色名册，list_subagents / delegate 工具与设置页。Named subagent… |
| MCP | [ultmebius/universal-plugin-hub](https://github.com/ultmebius/universal-plugin-hub) | DSH 插件市场：内置 Claude 官方插件目录，支持添加 Git 仓库作为插件源；一键安装，技能、子代理、MCP、LSP、hooks 装完自动接线 · Plugin marke… |

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
| 安全 | [fishbottle7/opencode2dsh](https://github.com/fishbottle7/opencode2dsh) | DSH plugin — free OpenCode Zen models for DeepSeek Harness (DSH). Free LLM API, no API key… |
| 安全 | [suntianc/dsh-antigravity-auth](https://github.com/suntianc/dsh-antigravity-auth) | DeepSeek Harness plugin for Antigravity OAuth login and native Antigravity Auth capability… |
| 安全 | [2861292267/dsh-official-workbuddy-credit-proxy](https://github.com/2861292267/dsh-official-workbuddy-credit-proxy) | DSH 官方版 · WorkBuddy 积分反代 —— 把本机 WorkBuddy 账号合并为自动故障转移的模型池，接入 DeepSeek Harness 官方版（含 DSH 内核… |
| 安全 | [ai-scarlett/dsh-store](https://github.com/ai-scarlett/dsh-store) | DSH STORE — third-party plugin marketplace and guarded lifecycle manager for DeepSeek Harn… |

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
| 通知/推送 | ~~[VoodooB0Ys/dsh-desktop-notify](https://github.com/VoodooB0Ys/dsh-desktop-notify)~~（已失效） | DeepSeek Harness 的 Windows 桌面提醒：需要授权 / 提问 / 完成 / 出错 / 被中止时在屏幕角落弹出提醒，点一下回… |
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
| 智能体 | [chongcyrus/vibe-mathematics](https://github.com/chongcyrus/vibe-mathematics) | Vibe Mathematics —— 多代理数学问题求解与形式化验证框架 |
| 智能体 | [michengai/dsh-im-connect](https://github.com/michengai/dsh-im-connect) | DSH IM Connect — 将主流即时通讯平台接入本机 DeepSeek Harness · Connect major messaging platforms to loc… |
| 智能体 | [kw78/dsh-office-tools](https://github.com/kw78/dsh-office-tools) | Model-facing Office tools for DeepSeek Harness: Word (.docx), Excel (.xlsx), and PowerPoin… |
| 智能体 | [goodandready/dsh-cron](https://github.com/goodandready/dsh-cron) | Scheduled cron tasks, background automation and agent execution for DeepSeek Harness. |
| 智能体 | [moonbowterfly/dsh-bio-genie](https://github.com/moonbowterfly/dsh-bio-genie) | 生物信息学「许愿式分析」dsh 插件：57 个语义化工具 + bio_python 执行器（Biopython 全功能 · 出版级绘图 · 代谢建模/FBA · 基因编辑 · 合成… |
| 智能体 | [polaris-smart/dsh-agent-mailbox](https://github.com/polaris-smart/dsh-agent-mailbox) | dsh (DeepSeek Harness) 跨 agent 信箱插件：mailbox_send/check/reply/list/done/broadcast + task_cr… |

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
| 文档 | [duyanta123/dsh-data-insight](https://github.com/duyanta123/dsh-data-insight) | Turn CSV data into insight reports — profile datasets, run DuckDB queries, and generate ch… |
| 文档 | [ilyskyo/word-hover-dsh](https://github.com/ilyskyo/word-hover-dsh) | 在 DeepSeek Harness 里读 AI 英文回复时，鼠标悬停任意英文单词 → 单词出现「被选中」高亮 → 自动弹出音标、词性、中文释义、英文释义、双语例句。 |
| 文档 | [ya123-4/archify-skill-dsh](https://github.com/ya123-4/archify-skill-dsh) | DeepSeek Harness plugin bundle that exposes the Archify 3.0.1 skill for architecture / wor… |

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
| 技能 | [qtaik/dsh-noname-kit](https://github.com/qtaik/dsh-noname-kit) | DeepSeek Harness无名杀插件  无名杀扩展开发工坊:AI 按规范写武将技能与卡牌(确认协议/校验门禁/区块化写入) |

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
| 工作流 | [mashedpotato817/dsh-git-plugin](https://github.com/mashedpotato817/dsh-git-plugin) | Git workflow plugin for DeepSeek Harness (DSH): slash commands, read-only tools, pre-commi… |

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
| 开发运行时 | [clearailhc/clearai-dsh](https://github.com/clearailhc/clearai-dsh) | ClearAI is a native DSH plugin that brings the Epistemic Loop to DeepSeek Harness. |
| 开发运行时 | [wenaixi/dsh-superpower](https://github.com/wenaixi/dsh-superpower) | DSH port of obra/superpowers — 完整移植、中文化、DSH 原生 |
| 开发运行时 | [micromilo/upstream-radar](https://github.com/micromilo/upstream-radar) | Always-on compatibility testing for DeepSeek Harness plugins: exact releases, isolated run… |
| 开发运行时 | [perrylink/dsh-plugin-doctor](https://github.com/perrylink/dsh-plugin-doctor) | Zero-dependency verification standard for DeepSeek Harness (dsh) plugins — static structur… |
| 开发运行时 | [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) | dsh-shio — 社区版本机部署运维套件 for DeepSeek Harness (dsh): install / start / monitor, backup & res… |
| 开发运行时 | [orangeshinee/dsh-mem0](https://github.com/orangeshinee/dsh-mem0) |  |
| 开发运行时 | [chengxiucdp/dsh-plugin-advisor](https://github.com/chengxiucdp/dsh-plugin-advisor) |  |
| 开发运行时 | [winddreamboat/dsh_laap](https://github.com/winddreamboat/dsh_laap) | 插件-dsh意识工程最小实现 |

---
| 开发/运行时 | [HaowenCang/dsh-turn-performance-meter](https://github.com/HaowenCang/dsh-turn-performance-meter) | Turn-level performance telemetry and TPS monitoring for DeepSeek Harness… |
| 开发/运行时 | [FlyingBamboo/dsh-pkg-atlas](https://github.com/FlyingBamboo/dsh-pkg-atlas) | DSH 本机代码包依赖图谱（开发工具）：把已安装的 @deepseek-ai/* 包与第三方插件的依赖、挂载关系画成区-组-包三层交互图，支持聚… |
| 开发/运行时 | [yumusb/dsh-opencode-go-plus](https://github.com/yumusb/dsh-opencode-go-plus) |  |

| 开发运行时 | [0gl20shk0sbt36/dsh-deadman](https://github.com/0gl20shk0sbt36/dsh-deadman) | Deadman switch plugin for DeepSeek Harness (dsh): runs a command when nobody is still working |
| 开发运行时 | [121212165/dsh-plugin-eco-scan](https://github.com/121212165/dsh-plugin-eco-scan) | dsh plugin: scan the dsh plugin ecosystem — collect stars/npm downloads/release assets per plugin, segment the… |
| 开发运行时 | [Altermoe/dsh-onedev](https://github.com/Altermoe/dsh-onedev) | DeepSeek Harness Plugin for OneDev |
| 开发运行时 | [AuraxM/dsh-plugin-confirm-check](https://github.com/AuraxM/dsh-plugin-confirm-check) |  |
| 开发运行时 | [AuraxM/dsh-plugin-doc-present](https://github.com/AuraxM/dsh-plugin-doc-present) |  |
| 开发运行时 | [Ayelsh/reasoning-setup](https://github.com/Ayelsh/reasoning-setup) | A DeepSeek Harness plugin: edit reasoning effort levels and thinking formats for models that declare none. |
| 开发运行时 | [CARVIN94/dsh-router-codebuddy](https://github.com/CARVIN94/dsh-router-codebuddy) |  |
| 开发运行时 | [CARVIN94/dsh-router-ext-rtk](https://github.com/CARVIN94/dsh-router-ext-rtk) |  |
| 开发运行时 | [CARVIN94/dsh-router-traework](https://github.com/CARVIN94/dsh-router-traework) |  |
| 开发运行时 | [ChengxiuCDP/dsh-plugin-advisor](https://github.com/ChengxiuCDP/dsh-plugin-advisor) |  |
| 开发运行时 | [DSH-PackForge/dsh-pack-plugin](https://github.com/DSH-PackForge/dsh-pack-plugin) |  |
| 开发运行时 | [EveGoodEvening/dsh-llmwiki](https://github.com/EveGoodEvening/dsh-llmwiki) |  |
| 开发运行时 | [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) | Podman-backed execution for DeepSeek Harness (dsh) |
| 开发运行时 | [Fafaisa6305/dsh-gamemode](https://github.com/Fafaisa6305/dsh-gamemode) |  |
| 开发运行时 | [Harvey-Will/dsh-vision-analysis](https://github.com/Harvey-Will/dsh-vision-analysis) | DeepSeek Harness 图像理解插件 · 8 种分析模式 · 支持任意API接口 · 内置免费视觉模型 / DeepSeek Harness vision plugin · 8 analysis modes ·… |
| 开发运行时 | [HerTa-st/Herta-dsh](https://github.com/HerTa-st/Herta-dsh) | dsh插件版herta |
| 开发运行时 | [HorusJiang/dsh-map-tools](https://github.com/HorusJiang/dsh-map-tools) |  |
| 开发运行时 | [HuanLinOTO/dsh-plugin-tools-manager](https://github.com/HuanLinOTO/dsh-plugin-tools-manager) | DSH 工具管理器：查看/启停宿主已注册工具 / DSH tools manager: inspect and toggle host-registered tools |
| 开发运行时 | [InfinitePersistence/dsh-serial-console](https://github.com/InfinitePersistence/dsh-serial-console) | Unofficial DeepSeek Harness plugin for board serial console, logging, and model-visible interaction. |
| 开发运行时 | [Jackson-chen97/dsh-devops](https://github.com/Jackson-chen97/dsh-devops) | GitLab + Kubernetes monitoring plugin for DSH — track CI/CD pipelines and K8s cluster health in one place. |
| 开发运行时 | [Khorsheed/dsh-basic](https://github.com/Khorsheed/dsh-basic) |  |
| 开发运行时 | [Leo-Cjw/dsh-pharos](https://github.com/Leo-Cjw/dsh-pharos) |  |
| 开发运行时 | [Lostforest7/dsh-encoding](https://github.com/Lostforest7/dsh-encoding) | Correct-encoding command runner and mojibake recovery for DeepSeek Harness. 让 DeepSeek Harness 在 Windows 上不再乱码… |
| 开发运行时 | [Lzh3070/dsh-model-visibility](https://github.com/Lzh3070/dsh-model-visibility) | DeepSeek Harness 插件：模型可见性管理——按渠道/模型隐藏或显示模型选择菜单里的条目 / Control which models appear in the DSH model selector |
| 开发运行时 | [MichengAI/dsh-pua](https://github.com/MichengAI/dsh-pua) | DSH PUA — 为 DeepSeek Harness 提供 PUA 任务推进、角色风味、验收循环和运行状态卡片 · PUA task persistence, personas, verification loops… |
| 开发运行时 | [MrLukezy/dsh-cloud-gateway](https://github.com/MrLukezy/dsh-cloud-gateway) | Login wall and public gateway plugin for DeepSeek Harness cloud deploys |
| 开发运行时 | [Neptune810/dsh-model-router](https://github.com/Neptune810/dsh-model-router) | Flash-only reasoning-effort routing for DeepSeek Harness, setting the DeepSeek flash model reasoning effort pe… |
| 开发运行时 | [OutLawZhangSan-liii/dsh-tailnet-gateway](https://github.com/OutLawZhangSan-liii/dsh-tailnet-gateway) |  |
| 开发运行时 | [Palkaro/dsh-local-ai](https://github.com/Palkaro/dsh-local-ai) | Manage Ollama models and route AI requests locally with automatic cloud fallback via DeepSeek Harness. |
| 开发运行时 | [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) | Zero-dependency verification standard for DeepSeek Harness (dsh) plugins — static structure gates (R), cordis… |
| 开发运行时 | [Rczlin/dsh-better-reasoning](https://github.com/Rczlin/dsh-better-reasoning) |  |
| 开发运行时 | [SilenZerOrz/obsidian-dsh-acp](https://github.com/SilenZerOrz/obsidian-dsh-acp) |  |
| 开发运行时 | [SkylerFee/dsh-llm-opencode-go-live](https://github.com/SkylerFee/dsh-llm-opencode-go-live) | DeepSeek Harness 的 OpenCode Go 动态模型目录插件。它从 Models.dev 更新 `opencode-go` 模型列表，注册独立的 `opencode-go-live` 路由。An Ope… |
| 开发运行时 | [Tangcuyu4/dsh-ciku-pack](https://github.com/Tangcuyu4/dsh-ciku-pack) | DSH 词库插件：收录用户情绪脏话与攻击性口气词当斗嘴弹药，弹药清单每轮自动注入 |
| 开发运行时 | [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) | Verified plugin marketplace and autonomous registry for DeepSeek Harness |
| 开发运行时 | [YIYuNCU/DSHTrueDelete](https://github.com/YIYuNCU/DSHTrueDelete) |  |
| 开发运行时 | [Yokira404/dsh-thinking-highlight](https://github.com/Yokira404/dsh-thinking-highlight) | 自动标注提示链中的关键词Keyword counts and highlighting for DSH thinking rows |
| 开发运行时 | [Zhucy123/source-code-mgmt](https://github.com/Zhucy123/source-code-mgmt) |  |
| 开发运行时 | [Zm886/dsh-ruankao-essay](https://github.com/Zm886/dsh-ruankao-essay) | 软考系统分析师论文助手：DSH 插件（题库索引 + 10 段式写作 + Word 交付） |
| 开发运行时 | [better-er/dsh-edit-diff](https://github.com/better-er/dsh-edit-diff) | 「DSH·质量 diff」：接管 edit/write 及 extraTools 配置的其他工具卡片，行级去重与行内高亮，消除相同内容在删除与新增两区的重复；兼容 PTC 模式。 |
| 开发运行时 | [better-er/dsh-peak-block](https://github.com/better-er/dsh-peak-block) | 「DSH·禁止梁文峰」：北京时间工作日高峰时段拦截发往官方 DeepSeek 的模型请求，避开高峰双倍计价，法定节假日全天谷价不拦。 |
| 开发运行时 | [busabase/busabase-dsh-plugin](https://github.com/busabase/busabase-dsh-plugin) | Deepseek Harness Plugin for Busabase |
| 开发运行时 | [cglyvip/dsh-auto-continue](https://github.com/cglyvip/dsh-auto-continue) | DeepSeek Harness 插件：模型请求失败自动注入「继续」并切换兜底模型，免手动干预 |
| 开发运行时 | [chongyi/dsh-notify](https://github.com/chongyi/dsh-notify) | DeepSeek Harness notify plugin |
| 开发运行时 | [conafun/dsh-music-plus](https://github.com/conafun/dsh-music-plus) | 基于 dsh-music-player 的修改版：移除在线QQ/酷狗/讲书/歌词，新增播客 |
| 开发运行时 | [danieldu168/dsh-stash](https://github.com/danieldu168/dsh-stash) |  |
| 开发运行时 | [dongshan1999/dsh-toolkit](https://github.com/dongshan1999/dsh-toolkit) |  |
| 开发运行时 | [enoughpower/dsh-git-graph](https://github.com/enoughpower/dsh-git-graph) |  |
| 开发运行时 | [f-e-n-g-0531/dsh-code-review](https://github.com/f-e-n-g-0531/dsh-code-review) |  |
| 开发运行时 | [f-e-n-g-0531/dsh-vcs](https://github.com/f-e-n-g-0531/dsh-vcs) |  |
| 开发运行时 | [foggy-projects/foggy-deepseek-harness-plugin](https://github.com/foggy-projects/foggy-deepseek-harness-plugin) | Foggy Java data analysis engine integration for DeepSeek Harness |
| 开发运行时 | [forwardzz/dsh-task-notify](https://github.com/forwardzz/dsh-task-notify) | DeepSeek Harness 桌面端插件：任务完成时发出提示音、闪烁任务栏图标并叠加角标，直到你切回 DSH 窗口 |
| 开发运行时 | [goatliamia/dsh-plugin-maker](https://github.com/goatliamia/dsh-plugin-maker) |  |
| 开发运行时 | [green-dalii/dsh-shift-router](https://github.com/green-dalii/dsh-shift-router) | Two-tier model router for DeepSeek Harness — LLM-Judge routing, multi-model fallback chains, exponential-backo… |
| 开发运行时 | [haotian-lu-prog/dsh-notifications](https://github.com/haotian-lu-prog/dsh-notifications) | macOS menu bar activity indicator for DeepSeek Harness (community fork of dsh-notify; supports DSH 0.1.7-rc.2… |
| 开发运行时 | [hiJoeLee/dsh-suggest-actions](https://github.com/hiJoeLee/dsh-suggest-actions) | 在每条回复下方给出可点的下一步建议，点一下就作为你的消息发出去 |
| 开发运行时 | [iruoy/dsh-notify](https://github.com/iruoy/dsh-notify) |  |
| 开发运行时 | [jgao9906-droid/dsh-task-toast](https://github.com/jgao9906-droid/dsh-task-toast) | Top-right status plate for DeepSeek Harness. DSH 右上角状态提示板。 |
| 开发运行时 | [jiangzhenguo/dsh-codegraph](https://github.com/jiangzhenguo/dsh-codegraph) |  |
| 开发运行时 | [jryang1997/dsh-composer-dictation](https://github.com/jryang1997/dsh-composer-dictation) | Hold-to-talk dictation for the DeepSeek Harness composer: long-press the input box, release to transcribe into… |
| 开发运行时 | [lire1131/dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint) | DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus o… |
| 开发运行时 | [liujianqiao701/dsh-compat-vet](https://github.com/liujianqiao701/dsh-compat-vet) | DSH（DeepSeek Harness）插件兼容性体检：预警下次启动会被拒绝加载的插件，并在页面上按键一键隔离/卸载修掉它（改前自动备份、失败自动回滚）。Plugin compatibility vet for Dee… |
| 开发运行时 | [ljcoder2015/dsh-canvas](https://github.com/ljcoder2015/dsh-canvas) | dsh-plugin |
| 开发运行时 | [logandoo/vibeweaver-dsh](https://github.com/logandoo/vibeweaver-dsh) | vibeweaver 的 deepseek harness 专属发行版，帮你的 dsh 交付可信任，经过验证的代码。 |
| 开发运行时 | [losebird/dsh-plugin-market](https://github.com/losebird/dsh-plugin-market) | DeepSeek Harness plugins market｜DSH 插件市场 |
| 开发运行时 | [lovezi0/dsh-open-in-app-base](https://github.com/lovezi0/dsh-open-in-app-base) | dsh "Open In..."控件底座，提供一个开放的可由同类插件补充的插槽以解决原生"Open In..."缺少在某些软件中打开 |
| 开发运行时 | [lql341/dsh-scnet](https://github.com/lql341/dsh-scnet) | dsh plugin for scnet.cn |
| 开发运行时 | [mocilukalbj/dsh-open-code-review](https://github.com/mocilukalbj/dsh-open-code-review) | Alibaba Open Code Review for DeepSeek Harness: native review tools, host-model delegation, and optional OCR-ma… |
| 开发运行时 | [netori/galfree](https://github.com/netori/galfree) |  |
| 开发运行时 | [nightosong/gord-dsh-worktree](https://github.com/nightosong/gord-dsh-worktree) | Git worktrees for DeepSeek Harness — isolate parallel work in its own directory and branch. Ships Fast mode (快… |
| 开发运行时 | [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) | An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件 |
| 开发运行时 | [oopsylol/dsh-waaagh-ork](https://github.com/oopsylol/dsh-waaagh-ork) |  |
| 开发运行时 | [orzgithub/dsh-ollama](https://github.com/orzgithub/dsh-ollama) | A plugin to use ollama in Deepseek Harness. |
| 开发运行时 | [rin721/dsh-mythor-plugin](https://github.com/rin721/dsh-mythor-plugin) |  |
| 开发运行时 | [shatyuka/dsh-llm-codebuddy](https://github.com/shatyuka/dsh-llm-codebuddy) | Tencent CodeBuddy plugin for DeepSeek Harness (dsh). |
| 开发运行时 | [shine-yu-student/dsh-pen](https://github.com/shine-yu-student/dsh-pen) | Enable Deepseek Harness to paint (literally). |
| 开发运行时 | [songgms/dsh-git-graph](https://github.com/songgms/dsh-git-graph) |  |
| 开发运行时 | [songshuhuoban/dsh-next-input](https://github.com/songshuhuoban/dsh-next-input) |  |
| 开发运行时 | [stefanohe/dsh-prefill-speed-stats](https://github.com/stefanohe/dsh-prefill-speed-stats) | Show prefill speed directly in the status bar. |
| 开发运行时 | [studyzy/dsh-lazy-tools](https://github.com/studyzy/dsh-lazy-tools) |  |
| 开发运行时 | [temidayoxyz/deep-opencode](https://github.com/temidayoxyz/deep-opencode) | OpenCode's free-tier models for DeepSeek Harness: a local opencode serve makes the free models resolve, so no… |
| 开发运行时 | [wangjiezhe/dsh-jp-translate](https://github.com/wangjiezhe/dsh-jp-translate) | 「日语翻译」模式 |
| 开发运行时 | [wangjiezhe/dsh-md-linebreak](https://github.com/wangjiezhe/dsh-md-linebreak) | 将软换行视为硬换行 |
| 开发运行时 | [wjw99830/dsh-plugin-noema](https://github.com/wjw99830/dsh-plugin-noema) | Focus code review on complexity changes after each coding task. |
| 开发运行时 | [xx-hub/dsh-craft-your-textbook](https://github.com/xx-hub/dsh-craft-your-textbook) |  |
| 开发运行时 | [zdk119746/dsh-llm-workbuddy](https://github.com/zdk119746/dsh-llm-workbuddy) | 可以在 DSH 中使用 WorkBuddy 里面的模型 |
| 开发运行时 | [zenvertao/dsh-inline-comments](https://github.com/zenvertao/dsh-inline-comments) | 选中即批注，刷新亦留存 —— DSH 行内批注插件 |
| 开发运行时 | [zhourenke/dsh-reasoning-merge](https://github.com/zhourenke/dsh-reasoning-merge) |  |
| 开发运行时 | [zhourenke/dsh-reasoning-mode](https://github.com/zhourenke/dsh-reasoning-mode) |  |
| 身份通信 | [5havv/dsh-weixin](https://github.com/5havv/dsh-weixin) | WeChat channel plugin for DeepSeek Harness, over Tencent's iLink Bot API |
| 身份通信 | [Alphainfix/wechat-clawbot](https://github.com/Alphainfix/wechat-clawbot) | 💬 Chat with your DeepSeek Harness agent from WeChat through the official WeChat ClawBot channel: native photo… |
| 身份通信 | [ArcaneOrion/dsh-model-channel-manager](https://github.com/ArcaneOrion/dsh-model-channel-manager) | DSH model channel manager: roundrobin failover engine + model config panel |
| 身份通信 | [ArtlexYoung/dsh-super-code](https://github.com/ArtlexYoung/dsh-super-code) | 一个更快、更节省、更准确的 DeepSeek Harness 插编码件。在 SWE-bench Pro 最难的 100 道题中，回答耗时减少 36%，每题token减少 17%，正确率甚至增加了 5%。A faster,… |
| 身份通信 | [Chatbot-zhou/dsh-task-complete-sound](https://github.com/Chatbot-zhou/dsh-task-complete-sound) | DeepSeek Harness plugin: plays a chosen chime preset when a task finishes. |
| 身份通信 | [GeoSyntax/dsh-plugin-time-machine](https://github.com/GeoSyntax/dsh-plugin-time-machine) | Community DSH plugin for coordinated session/workspace checkpoints, safe rewind, DAG forks, and failure reflec… |
| 身份通信 | [Github-CJX/dsh-tool-imagegen](https://github.com/Github-CJX/dsh-tool-imagegen) | DSH Desktop 对话内联生图插件** — 模型在对话中自动调用 `generate_image` 工具，图片直接内联显示在对话框里，无需外部面板、无需手动切换。 |
| 身份通信 | [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) | Image generation & visual processing suite for DeepSeek Harness: pluggable providers (FAL, Replicate, OpenAI,… |
| 身份通信 | [HaoyanZhang123/dsh-plugin-image-gen](https://github.com/HaoyanZhang123/dsh-plugin-image-gen) | DSH (DeepSeek Harness) plugin: generate images through any OpenAI-compatible endpoint you configure. The packa… |
| 身份通信 | [HuanLinOTO/dsh-plugin-aigc-canvas](https://github.com/HuanLinOTO/dsh-plugin-aigc-canvas) | provider-agnostic AIGC HTTP 桥 + 无限画布 + ffmpeg 后处理，13 个工具含画布连边/reroll/媒体编辑 / Provider-agnostic AIGC HTTP bridge… |
| 身份通信 | [HuanLinOTO/dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) | 向模型暴露 MinerU 文档解析工具，将 PDF/图片/DOCX/PPTX/XLSX 转为结构化 Markdown/JSON / Exposes MinerU document-parsing tools to the… |
| 身份通信 | [HuanLinOTO/dsh-plugin-terminal-extension-wait-for](https://github.com/HuanLinOTO/dsh-plugin-terminal-extension-wait-for) | 阻塞到字符串出现在 DSH 原生持久终端保留输出里（正则/子串；found/超时/退出/消失/取消五态） / Blocks until a pattern appears in a DSH persistent term… |
| 身份通信 | [InkshadeWoods/dsh-tool-visual-primitives](https://github.com/InkshadeWoods/dsh-tool-visual-primitives) | DeepSeek Harness 视觉增强插件：将图片交给外部视觉模型分析，输出带坐标化视觉原语的纯文本证据，使不支持多模态的文本模型也能在对话中理解图片、截图与文档。 |
| 身份通信 | [LQH-A-A-O/dsh-simple-drawing](https://github.com/LQH-A-A-O/dsh-simple-drawing) | DSH 技能包：layered-art（dsh简易绘图能力包）—— 用代码作画，五条路线（描图重构 / 网格立绘 / 方块角色 / 像素画 / 部件装配） |
| 身份通信 | [LR611415/visionforge](https://github.com/LR611415/visionforge) | VisionForge — vision understanding + image generation plugin for DeepSeek Harness (DSH) |
| 身份通信 | [LisonEvf/dsh-qwen-image](https://github.com/LisonEvf/dsh-qwen-image) | 在 AI 会话窗口里直接生图 / 改图 —— dsh 插件，本地跑 Qwen-Image-2.1（原生 2K / 原生透明 PNG / 最多 10 张参考图）。安装器自动适配 CUDA 与已有 ComfyUI/conda… |
| 身份通信 | [Lyrissonare/dsh-preset-bridge](https://github.com/Lyrissonare/dsh-preset-bridge) | DSH预设桥插件，解决“风神插件”“梁神模式”等在更新桌面版后预设不生效的问题，欢迎使用 |
| 身份通信 | [Lzhimie/dsh-skin-master](https://github.com/Lzhimie/dsh-skin-master) | DeepSeek Harness 皮肤大师：主题壁纸/自定义皮肤插件 —— 全局背景图片/视频、毛玻璃、输入框背景、弹出框毛玻璃、滤镜、AI 回复文本与消息气泡颜色 |
| 身份通信 | [MaRi23333/dsh-serverchan-watchdog](https://github.com/MaRi23333/dsh-serverchan-watchdog) | DeepSeek Harness 的 Server酱推送插件：审批、计划评审或问答超时未处理时，发送微信/Server酱³ App 提醒。第三方非官方项目。 |
| 身份通信 | [MichengAI/dsh-im-connect](https://github.com/MichengAI/dsh-im-connect) | DSH IM Connect — 将主流即时通讯平台接入本机 DeepSeek Harness · Connect major messaging platforms to local DeepSeek Harness… |
| 身份通信 | [Paimonshen/dsh-coding-plugin](https://github.com/Paimonshen/dsh-coding-plugin) | 代码学习插件 — DSH 动态 Cordis 插件：悬浮窗代码编辑器/多语言执行/课程关卡评判/分析直投对话 |
| 身份通信 | [Rice00/dsh-loupe](https://github.com/Rice00/dsh-loupe) | Select text in a DSH conversation and explain it in a floating window — independent channel, no session pollut… |
| 身份通信 | [STARDUSTLC666/dsh-dream](https://github.com/STARDUSTLC666/dsh-dream) | DSH 做梦插件：会话间隙回放近期对话、反思写入梦境日记，并把高频教训幂等桥接进 AGENTS.md；默认隐私脱敏，零运行时依赖。 |
| 身份通信 | [Thedeergod666/dsh-musage](https://github.com/Thedeergod666/dsh-musage) | DSH 端的 AI 套餐余额监控插件, 跟当前模型自动切换.目前支持 5 provider (minimax / deepseek / kimi / openrouter / zhipu).｜DSH (DeepSeek… |
| 身份通信 | [WSL043/dsh-image-viewer](https://github.com/WSL043/dsh-image-viewer) | DeepSeek Harness (DSH) image viewer / 图片查看器: zoom, gallery, original downloads and clear region annotations. |
| 身份通信 | [XN-H/dsh-ark-image](https://github.com/XN-H/dsh-ark-image) | DeepSeek Harness 生图插件：文生图 / 图片生成 / AI 绘画，基于火山方舟 Seedream（豆包）。零依赖、纯 JavaScript、无需构建。 / DSH image generation plu… |
| 身份通信 | [Yaaaaaaa233/dsh-plan-and-execute](https://github.com/Yaaaaaaa233/dsh-plan-and-execute) | On-demand planning for DeepSeek Harness: execute simple tasks directly and call a configurable planning model… |
| 身份通信 | [YiMlT/dsh-notify-yimit](https://github.com/YiMlT/dsh-notify-yimit) | DeepSeek Harness 通知插件:在 **任务完成 / 任务出错 / 运行中 / 等待审批 / 等待回答** 时提醒用户。 通知标题为对话标题;系统通知与自定义通知均支持**点击跳转到对应会话**。 |
| 身份通信 | [Yiheng-guo/dsh-boot-animation-pro](https://github.com/Yiheng-guo/dsh-boot-animation-pro) | DSH 片头开机动画增强版：播放控制、触发规则、会话名单、分时段片头、片库管理、中英双语。A full-frame intro animation for DSH. Fork of NativeDog1/dsh-boot… |
| 身份通信 | [Ylhow06/dsh-agnes-gen](https://github.com/Ylhow06/dsh-agnes-gen) | Agnes AI image/video generation tools (agnes_image / agnes_video) for DSH (DeepSeek Harness). Built-in cross-p… |
| 身份通信 | [alanzhao0128/dsh-image-plugins](https://github.com/alanzhao0128/dsh-image-plugins) | Multimodal plugin for DeepSeek Harness (dsh): understand images and generate images via configurable OpenAI-co… |
| 身份通信 | [anze225-max/dsh-mimo-connect](https://github.com/anze225-max/dsh-mimo-connect) | 将 mimo桌面端包含的模型（内测有免费额度）自动接入 DeepSeek Harness，在 DSH 对话窗口里零配置使用。 |
| 身份通信 | [cbg33695/dsh-screen-reader](https://github.com/cbg33695/dsh-screen-reader) | Let a text-only model see the screen: capture desktop/window/region, vision transcription, a few minutes of ro… |
| 身份通信 | [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) | 多文件夹 workspace：让 DSH（DeepSeek Harness）的 Agent 不只能读写主目录，还能同时读写你添加的其他文件夹。Multi-folder workspace for DeepSeek Har… |
| 身份通信 | [corrinehu/dsh-buddy-checkin](https://github.com/corrinehu/dsh-buddy-checkin) | DSH 启动时自动为 WorkBuddy 国内版账号完成每日签到。Automatic daily check-in for all WorkBuddy CN accounts on this machine, every… |
| 身份通信 | [ethanrise/dsh-model-deploy](https://github.com/ethanrise/dsh-model-deploy) | Inspect ONNX models and benchmark them with ONNX Runtime on the local machine or over SSH, with PASS/FAIL depl… |
| 身份通信 | [evlon/dsh-matrix-agent](https://github.com/evlon/dsh-matrix-agent) | DeepSeek Harness（dsh）的 Matrix agent 桥接插件：把 Matrix 房间桥接到 harness agent 会话，每个房间一个会话，支持在聊天里远程监控、审批和追加指令；多分身架构 + 媒… |
| 身份通信 | [harde1/dsh-xcodebuild](https://github.com/harde1/dsh-xcodebuild) | Xcode build, test, archive, run and log streaming for DeepSeek Harness: build/test/clean/archive/run an iOS or… |
| 身份通信 | [ice5kysl/dsh-file-explorer-kit](https://github.com/ice5kysl/dsh-file-explorer-kit) | dsh (DeepSeek Harness) file explorer: browse the active session's workspace and preview files (Markdown/image/… |
| 身份通信 | [its0din-ai/harness-accountant](https://github.com/its0din-ai/harness-accountant) | DSH (DeepSeek Harness) Simple Balance Monitor Plugin / DSH（DeepSeek Harness）简易余额监视插件 |
| 身份通信 | [jasen215/dsh-continual-harness](https://github.com/jasen215/dsh-continual-harness) | DeepSeek Harness (DSH) plugin for self-improving AI agents: continual learning, persistent memory, cross-sessi… |
| 身份通信 | [kaaaaahn/dsh-vision](https://github.com/kaaaaahn/dsh-vision) | DSH 本地视觉能力插件：macOS Vision OCR + ollama qwen3-vl 语义描述 + 上传图片桥接 |
| 身份通信 | [keyiadiannao/dsh-code-reuse-firewall](https://github.com/keyiadiannao/dsh-code-reuse-firewall) | Pre-write reuse firewall for DeepSeek Harness: before the agent writes a new helper/service, surface the exist… |
| 身份通信 | [keyiadiannao/dsh-delay-tools](https://github.com/keyiadiannao/dsh-delay-tools) | Delayed wake-up for DeepSeek Harness: schedule a reminder and the agent wakes in the SAME conversation to repl… |
| 身份通信 | [lifeopsgo/dsh-lark-session-monitor-plugin](https://github.com/lifeopsgo/dsh-lark-session-monitor-plugin) | 飞书会话监听并投递到指定工作区的会话中 |
| 身份通信 | [liuqingman/dsh-somni](https://github.com/liuqingman/dsh-somni) | Sleep-consolidated long-term memory for DeepSeek Harness (DSH) agents: episodic / semantic / prospective / pro… |
| 身份通信 | [log-li/dsh-peakrate](https://github.com/log-li/dsh-peakrate) | Peak / off-peak rate badges for DeepSeek Harness — per provider, per model, in the model selector and the comp… |
| 身份通信 | [ly6170/dsh-messager](https://github.com/ly6170/dsh-messager) | 适用于Deepseek Harness的消息提醒信使，可使用飞书、企业微信、钉钉、Telegram、Discord进行通知推送 |
| 身份通信 | [memorax-ai/dsh-harmony](https://github.com/memorax-ai/dsh-harmony) | A library for patching, replacing and decorating dsh plugin during runtime |
| 身份通信 | [mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon) | LLM-supervised persistent memory for AI agents — graph-based recall, cross-session knowledge, single binary. W… |
| 身份通信 | [openma-ai/deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) | ACP server implementation for DeepSeek harness. dsh-acp |
| 身份通信 | [phelpsyacht/dshmath-manim](https://github.com/phelpsyacht/dshmath-manim) | deepseek harness manim数学插件 |
| 身份通信 | [protoctistmoses143/dsh-docs](https://github.com/protoctistmoses143/dsh-docs) | Convert PDFs, Office docs, scanned images, and more to clean Markdown, JSON, or text locally with offline OCR—… |
| 身份通信 | [syyr1987/dsh-linghun](https://github.com/syyr1987/dsh-linghun) | 灵魂（Linghun）— 给 DeepSeek Harness 装一个会思考的自我：认知循环 + 海马体三层记忆（序时账/情景归档/低置信降权遗忘）+ A2A 记忆管理团队联动。收口者身份锚点 + 边界判断纪律。 |
| 身份通信 | [tarraencompassing61/dsh-lark-bot](https://github.com/tarraencompassing61/dsh-lark-bot) | Bridge DeepSeek Harness into Feishu / Lark—drive your local coding agent from mobile, group chats, and topics… |
| 身份通信 | [tpmoonchefryan/dsh-joi-channel-theme](https://github.com/tpmoonchefryan/dsh-joi-channel-theme) | 轴伊 Joi 双衣装主题 for DeepSeek Harness — unofficial, non-commercial fan theme plugin 🍊 |
| 身份通信 | [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) | dsh游戏素材大师插件。接入seedream生图模型和minimax视频生成模型，可生成各种游戏素材。 |
| 身份通信 | [upcyan/dsh-mimo-extension](https://github.com/upcyan/dsh-mimo-extension) | MiMo (Xiaomi) quota ring and usage detail tab for DeepSeek Harness |
| 身份通信 | [windwhiterain/dsh-llm-quota-retry](https://github.com/windwhiterain/dsh-llm-quota-retry) | Answers an exhausted DeepSeek Harness account quota: move the session to another route of its pool when one st… |
| 身份通信 | [wlj521/dsh-ui-tweaks](https://github.com/wlj521/dsh-ui-tweaks) | 一切皆插件，可以定义自己喜欢的dsh，开关控制单项功能，字体大小，表格样式，对话框长度，timeline，git等 |
| 身份通信 | [xmwengxing/dsh-client-ui-sidebar-perfmon](https://github.com/xmwengxing/dsh-client-ui-sidebar-perfmon) | Real-time host performance monitoring for the DeepSeek Harness right Sidebar: CPU / memory / swap gauges plus… |
| 身份通信 | [yejiming/dsh-museai-tavern](https://github.com/yejiming/dsh-museai-tavern) | MuseAI的DeepSeek Harness插件，可以将你的MuseAI角色放进DSH使用啦！ |
| 身份通信 | [yunxiyang/dsh-stepwise-distill](https://github.com/yunxiyang/dsh-stepwise-distill) | Solidify DSH session history step by step: rewrite tool results in place to the facts the model actually kept,… |
| 身份通信 | [zhuiyueya/dsh-im-gateway](https://github.com/zhuiyueya/dsh-im-gateway) | 把 dsh agent 接入微信、飞书等 20+ 聊天平台的聚合网关插件 / Aggregate IM gateway for DeepSeek Harness (dsh): connect your agents to… |
| 工作流 | [GooDAnDReaDY/dsh-cron](https://github.com/GooDAnDReaDY/dsh-cron) | Scheduled cron tasks, background automation and agent execution for DeepSeek Harness. |
| 工作流 | [Zou82/dsh-plugin-git-sync](https://github.com/Zou82/dsh-plugin-git-sync) | Git + GitHub automation plugin for DeepSeek Harness: ask-before-init repo creation with user-confirmed naming… |
| 工作流 | [ifrankwang/openspec-agents](https://github.com/ifrankwang/openspec-agents) | OpenSpec 流程的 Agent Team：面向实施阶段的多 Agent 工作流编排。 |
| 技能 | [Alkaid4521/dsh-pixel-art](https://github.com/Alkaid4521/dsh-pixel-art) | 手写像素画 skill 插件：教 agent 写脚本逐像素画出任意图，不联网、不依赖绘图库、同参数必然复现（DSH / DeepSeek Harness） |
| 技能 | [RickT34/dsh-just-enough-tools](https://github.com/RickT34/dsh-just-enough-tools) | Nearly half the agent cost, with accuracy intact. Just enough tools is a DeepSeek Harness plugin that uses Jev… |
| 技能 | [YottaMeta/yotta-skills-plugin](https://github.com/YottaMeta/yotta-skills-plugin) | YuanGe (元阁) — orchestration and routing for the YottaMeta skill family, packaged as an Agent Plugin. |
| 技能 | [drscrewdriver/dsh-canvas-tsx-sidebar](https://github.com/drscrewdriver/dsh-canvas-tsx-sidebar) | DSH 侧边栏插件：把 Qoder Canvas `*.canvas.tsx` 静态解析为结构化报告页，在 dsh-better-sidebar 右侧栏渲染（文件查看器接管 + 页签）。纯静态管线，不执行源码。附 wri… |
| 技能 | [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) | Engineering workflow plugin for DeepSeek Harness: task stages, verification records, commit checks, and skill… |
| 技能 | [moazzamak/dsh-code-review](https://github.com/moazzamak/dsh-code-review) | Code-review pack for DeepSeek Harness (dsh): the /review shortcut over the pinned Changes page, plus the dsh-c… |
| 技能 | [qkycir-123/dsh-run2skill](https://github.com/qkycir-123/dsh-run2skill) | Automatically turn successful DeepSeek Harness sessions into reusable, reviewable Agent Skills. |
| 文档 | [17897693/dsh-wen](https://github.com/17897693/dsh-wen) | DSH 办公文档插件：docx/xlsx/pptx/pdf/odf/csv/html 读写改与互转 + 离线 OCR（自用为主，不承诺维护） |
| 文档 | [WuShichao/dsh-ipynb-preview](https://github.com/WuShichao/dsh-ipynb-preview) | Render Jupyter .ipynb notebooks in the DeepSeek Harness document preview: syntax highlighting, offline LaTeX,… |
| 文档 | [guhanfei-ai/dsh-mindmap](https://github.com/guhanfei-ai/dsh-mindmap) | Markdown-native AI mind maps and visual thinking for DeepSeek Harness. |
| 文档 | [lovezi0/dsh-open-in-codebuddy](https://github.com/lovezi0/dsh-open-in-codebuddy) | 按钮与菜单由底座 `dsh-open-in-app-base` 统一渲染，本插件只负责「目标软件」这一半：注册一条目标记录，并在自己的宿主半边实现「是否可用」与「怎么打开」。不 fork、不修改宿主，也不依赖原生 ope… |
| 文档 | [zbsph/dsh-ppt-studio](https://github.com/zbsph/dsh-ppt-studio) |  |
| 智能体 | [FreePeak/dsh-feature-loop](https://github.com/FreePeak/dsh-feature-loop) | Bounded agent loop for DeepSeek Harness: budget ceilings, cheap-first routing, loop hygiene detectors, and a h… |
| 智能体 | [Kanadego/dsh-heartbeat](https://github.com/Kanadego/dsh-heartbeat) | 一个致力于让Agent在日常交流中更加拥有“活人感”的DSH插件。 |
| 智能体 | [SZYTree0312/dsh-bailian-gold](https://github.com/SZYTree0312/dsh-bailian-gold) | 百炼成金模式 — 为阿里云百炼做前缀缓存优化的 dsh agent preset。缓存命中定价差 8 倍，省的是金子。 |
| 智能体 | [Zekilou/dsh-ask-form](https://github.com/Zekilou/dsh-ask-form) | Structured form questions for the DeepSeek Harness agent: 14 typed field types, conditions, validation, target… |
| 智能体 | [aa2246740/dsh-watcher](https://github.com/aa2246740/dsh-watcher) | Read-only Agent work-path observer for DeepSeek Harness |
| 智能体 | [better-er/dsh-notify-ding](https://github.com/better-er/dsh-notify-ding) | 「DSH·通知叮咚」：agent 提问或跑完一轮时弹出系统通知并让宿主播放 Windows 内置提示音。标准可安装的 dsh 客户端插件。 |
| 智能体 | [better-er/dsh-pause](https://github.com/better-er/dsh-pause) | 「DSH·暂停」：agent 完成一轮工具交互、正要发出下一次模型请求之前暂停，保持输入框可用，人类按回车放行并可携带补充文字；不打断任何在途 API 调用。 |
| 智能体 | [drscrewdriver/dsh-perm-gate](https://github.com/drscrewdriver/dsh-perm-gate) |  |
| 智能体 | [drscrewdriver/dsh-thinking-levels](https://github.com/drscrewdriver/dsh-thinking-levels) | deepseek-harness dsh thinging levels 调整 reasoning强度调整 |
| 智能体 | [frederico-kluser/dsh-orquestrator](https://github.com/frederico-kluser/dsh-orquestrator) | DeepSeek Harness plugin: on task send, pick a different model for subagents and an independent reviewer that v… |
| 智能体 | [kxdyh/dsh-agent-governor](https://github.com/kxdyh/dsh-agent-governor) | Two interception layers for DeepSeek Harness agents - DOL communication semantics and Sentinel tool execution… |
| 智能体 | [lifangjin/dsh-paoding](https://github.com/lifangjin/dsh-paoding) | 庖丁解牛，游刃有余 —— 把 DSH 编排成角色分工、按需加载的 agent preset。 |
| 智能体 | [litestartup-com/dsh-api-gateway](https://github.com/litestartup-com/dsh-api-gateway) | DeepSeek Harness's API Gateway plugin: Any third-party client can interact with your DSH Agent. |
| 智能体 | [project-hy/dsh-claude-delegate](https://github.com/project-hy/dsh-claude-delegate) | DSH 插件：把自包含的编码子任务委派给本机 Claude Code（官方 Agent SDK），后台作业 + 实时输出通道 + 监控面板 + 运行时技能；npm: dsh-claude-delegate |
| 智能体 | [tanweiping1012-source/PhotoFilterAgent](https://github.com/tanweiping1012-source/PhotoFilterAgent) | 跑在 DeepSeek Harness 上的照片策展 agent：本地 Vision 分类 + 连拍组比较 + 按需视觉打分，原图只读 |
| 智能体 | [wbb316/dsh-novel](https://github.com/wbb316/dsh-novel) | DSH 插件：小说创作台 —— 给 agent 5 个 novel_* 工具 + 一个能改设定、画关系图、一键续写并流式直播的右侧栏面板 |
| 智能体 | [windwhiterain/dsh-subagent-templates](https://github.com/windwhiterain/dsh-subagent-templates) | Named subagent templates for DeepSeek Harness: a template fixes a starting route (or the route pool it resolve… |
| 智能体 | [yorelog/dsh-omarchy-agent](https://github.com/yorelog/dsh-omarchy-agent) | DeepSeek Harness on Omarchy as Agent |
| 安全 | [2861292267/DSH-Official-WorkBuddy-Credit-Proxy](https://github.com/2861292267/DSH-Official-WorkBuddy-Credit-Proxy) | DSH 官方版 · WorkBuddy 积分反代 —— 把本机 WorkBuddy 账号合并为自动故障转移的模型池，接入 DeepSeek Harness 官方版（含 DSH 内核 0.1.7 兼容修复、启动自动同步账号… |
| 安全 | [2JumpSinA/dsh-context-guard](https://github.com/2JumpSinA/dsh-context-guard) | A DeepSeek Harness plugin that tells you to wrap up and start a new session before the session gets too long:… |
| 安全 | [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) | DSH STORE — third-party plugin marketplace and guarded lifecycle manager for DeepSeek Harness. |
| 安全 | [AndrasSama/dsh-omp-advisor](https://github.com/AndrasSama/dsh-omp-advisor) | Ward concil is oh-my-pi advisor subsystem ported to DeepSeek Harness — independent reviewer models watch your… |
| 安全 | [BoyangL04/dsh-task-notify](https://github.com/BoyangL04/dsh-task-notify) | DeepSeek Harness plugin: in-app toast + macOS notification when a session finishes a turn or is blocked on you… |
| 安全 | [GIN0076/cross-session-memory](https://github.com/GIN0076/cross-session-memory) | Zero-dependency cross-session memory for AI coding agents - lessons on disk, evidence-enforced, auto-injected |
| 安全 | [Han-1413141/dsh-compat-guardian](https://github.com/Han-1413141/dsh-compat-guardian) | Plugin compatibility checks, quarantine, recovery and offline startup rescue for DeepSeek Harness |
| 安全 | [Ink-dark/dsh-adversarial-review-preset](https://github.com/Ink-dark/dsh-adversarial-review-preset) | DeepSeek Harness agent preset for adversarial review: presumes the artifact is wrong, demands a citable author… |
| 安全 | [KLRSL/dsh-biomemory](https://github.com/KLRSL/dsh-biomemory) | 生物仿生记忆系统插件：Biomimetic memory for DeepSeek Harness — transparent Markdown memory, approval-gated writes, frozen… |
| 安全 | [Khorsheed/dsh-ankh-guard](https://github.com/Khorsheed/dsh-ankh-guard) | dsh 自托管运维守护：agent 改完代码先验证构建测试再重启，起不来自动回滚。镜像仓，与 Khorsheed/dsh-plugins 的 packages/ankh-guard 自动同步。 |
| 安全 | [LeeGuanWei-a/dsh-arch-advisor-offline](https://github.com/LeeGuanWei-a/dsh-arch-advisor-offline) | 给 DeepSeek Harness 装一位"读过架构书"的架构顾问：实时查阅 40 教程/31 模板/6 案例，引导设计并产出需求/概要/详细/数据库文档。· Persistent DSH plugin: an in-… |
| 安全 | [MichengAI/dsh-archive-manager](https://github.com/MichengAI/dsh-archive-manager) | DSH Archive Manager — 在 DeepSeek Harness 中安全查看、恢复和管理已归档会话 · Safely view, restore, and manage archived sessions… |
| 安全 | [MichengAI/dsh-skills-manager](https://github.com/MichengAI/dsh-skills-manager) | DSH Skills Manager — 在 DeepSeek Harness 中统一加载并安全管理本机 Agent Skills · Load and safely manage local Agent Skills… |
| 安全 | [ThinkofRain1213/dsh-project-groups](https://github.com/ThinkofRain1213/dsh-project-groups) | DSH 项目分组插件：1:1 接管官方侧栏工作区浏览区，把分组从「目录所有权」摘下来，变成纯前端的项目归属，适配完全权限工作流；关闭插件即完全恢复官方行为。 |
| 安全 | [alanzhao0128/dsh-memory-lite](https://github.com/alanzhao0128/dsh-memory-lite) | Lightweight zero-dependency long-term memory for DeepSeek Harness: Markdown memory store, L0 catalog injection… |
| 安全 | [amlyczz/dsh-agy-link](https://github.com/amlyczz/dsh-agy-link) | Google Antigravity (agy CLI) models for DeepSeek Harness — streaming chat, thinking, tool activity, usage, in-… |
| 安全 | [better-er/dsh-write-rule-guard](https://github.com/better-er/dsh-write-rule-guard) | 「DSH·写入规则守卫」：按可配置正则拦截 edit/write 的写入内容，默认拦全角括号，正则与报错文案可在配置里改。host 单半身。 |
| 安全 | [callqh/dsh-codex-oauth](https://github.com/callqh/dsh-codex-oauth) | Sign in to OpenAI Codex from DeepSeek Harness with a ChatGPT Plus/Pro subscription. |
| 安全 | [ddowbnac/dsh-claude-auth-proxy](https://github.com/ddowbnac/dsh-claude-auth-proxy) | LLM provider plugin for the DeepSeek Harness (dsh): streams Claude through your Claude Code subscription (clau… |
| 安全 | [gyyxs88/dsh-session-control](https://github.com/gyyxs88/dsh-session-control) | Authorized, durable cross-session control for DeepSeek Harness |
| 安全 | [having5548/dsh-notify](https://github.com/having5548/dsh-notify) | Universal notification plugin for DeepSeek Harness: in-app toasts, native Windows toasts, one-click approval f… |
| 安全 | [lingyingaojue/dsh-dev-mode](https://github.com/lingyingaojue/dsh-dev-mode) | 开发者模式：新手几句大白话讲需求，AI 自动走完「写计划 → 子代理审计划 → 极简模式后台会话写代码并编译 → 子代理 QA → 修 bug → 复测 → 交付」的 DSH 插件（agent preset）。 |
| 安全 | [luobosibing2/dsh-jev-plugin](https://github.com/luobosibing2/dsh-jev-plugin) | Native DeepSeek Harness (DSH) plugin integrating TypeSafe Jev as a System One decision layer for agent selecti… |
| 安全 | [mikulo/dsh-prompt-switcher](https://github.com/mikulo/dsh-prompt-switcher) | DeepSeek Harness (DSH) plugin: pick a local .md prompt template with / when starting a new conversation; it bi… |
| 安全 | [xmwpoi/dsh-approval-center](https://github.com/xmwpoi/dsh-approval-center) | DSH 0.1.7-rc.2 的 Windows 审批中控台：通知中心批准/拒绝、并发队列与取消清理、SQLite 审计。通过 GitHub Releases 分发。 |
| 安全 | [xxww0098/dsh-plugin-oauth-subs](https://github.com/xxww0098/dsh-plugin-oauth-subs) | ChatGPT Codex and xAI Grok subscription OAuth for DeepSeek Harness — PKCE / device-code, local Responses proxy… |
| 安全 | [zhang66633/dsh-memvault](https://github.com/zhang66633/dsh-memvault) | DeepSeek Harness 插件：把 MemVault 的核心记忆块注入 system prompt（每步可见、无需工具调用），并把每个完成的回合交给 MemVault 的抽取/向量化管线。Host-only bu… |
| MCP/设置 | [Amengclass/dsh-settings-hub](https://github.com/Amengclass/dsh-settings-hub) | dsh plugin: take over settings shell, regroup third-party plugins under one collapsible group |
| MCP/设置 | [BreakFree003/dsh-clinepass-deepseekv4.1](https://github.com/BreakFree003/dsh-clinepass-deepseekv4.1) | Cline Pass for DeepSeek Harness (dsh): one pi-ai provider route pinned to the DeepSeek upstream channel, key e… |
| MCP/设置 | [EPCN-fla/dsh-custom-headers](https://github.com/EPCN-fla/dsh-custom-headers) | Per-model custom request headers for DeepSeek Harness: define named header profiles in Settings → Plugins → Pl… |
| MCP/设置 | [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) | Per-provider API key rotation for DeepSeek Harness: key pools, automatic 429 rate-limit failover, cooldown pro… |
| MCP/设置 | [HandsYe/dsh-llm-motomoto](https://github.com/HandsYe/dsh-llm-motomoto) | DeepSeek Harness bundle for MotoMoto's OpenAI-compatible endpoint: pi-ai provider route + Settings status card |
| MCP/设置 | [HuanLinOTO/dsh-plugin-mcp-manager](https://github.com/HuanLinOTO/dsh-plugin-mcp-manager) | MCP 服务器管理面板：GUI 增删改 MCP 服务器配置（写入 cordis.patch.yml + HMR 实时挂载）+ 工具浏览 + agent 面 mcp_* 管理工具 / MCP server manageme… |
| MCP/设置 | [HuanLinOTO/dsh-plugin-preface-context](https://github.com/HuanLinOTO/dsh-plugin-preface-context) | 在每次会话开头固定注入一段用户配置的文本上下文（设置页输入框可编辑），作为模型可见的 instructions 注入第一轮请求。 / Injects a user-configured text block as mod… |
| MCP/设置 | [KLRSL/dsh-packer](https://github.com/KLRSL/dsh-packer) | 配置打包器 for DeepSeek Harness: pack your agent config (skills/sessions/profiles/settings/memory) into zip for mig… |
| MCP/设置 | [LeifDai/MACKORN-hydraulic-cone-crusher](https://github.com/LeifDai/MACKORN-hydraulic-cone-crusher) | Cone crusher selection and crushing-plant design for MACKORN NH/NS hydraulic cone crushers. 19 tools, 6 skills… |
| MCP/设置 | [Momonaka/commandcode-dash](https://github.com/Momonaka/commandcode-dash) | Unofficial DeepSeek Harness settings panel for Command Code: credits, usage windows, and model-catalog sync. |
| MCP/设置 | [MyRemme/dsh-computer-use-guard](https://github.com/MyRemme/dsh-computer-use-guard) | Three-tier (deny / ask / auto) authorization gate for DSH computer-use (cua-driver) tools, with a settings row… |
| MCP/设置 | [Norman-else/dsh-claude](https://github.com/Norman-else/dsh-claude) | Run Claude Code as a first-class DSH conversation while preserving its native agent loop, tools, skills, hooks… |
| MCP/设置 | [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) | Local-first code knowledge graph and context harness for coding agents. MCP + DeepSeek Harness (dsh) plugin. |
| MCP/设置 | [SunshineR04/dsh-session-manager](https://github.com/SunshineR04/dsh-session-manager) | DeepSeek Harness (DSH) plugin: manage archived sessions - list, restore, permanently delete; Settings page + r… |
| MCP/设置 | [VermilionPasvikin/dsh-coderag](https://github.com/VermilionPasvikin/dsh-coderag) | dsh-coderag 是一个以 MCP 服务器形态提供的代码库检索引擎：让 DeepSeek Harness（DSH）的 Agent 能按语义与结构找到代码，而不是靠猜关键词反复 grep。 |
| MCP/设置 | [WTStarMark/dsh-myskin](https://github.com/WTStarMark/dsh-myskin) | DSH 皮肤插件：可视化自定义 + 实时预览 + 「皮肤管理」设置页。 非侵入式：不改 DSH 源码 / 配置、不改 DSH 进程；皮肤是完全可逆的覆盖层。 适配：DSH 0.1.7-rc.2 与 0.2.0-rc.1 |
| MCP/设置 | [Xilin3/dsh-prompt-persona](https://github.com/Xilin3/dsh-prompt-persona) | DSH plugin: edit the system prompt (deployment persona) from the Settings page, with live preview. |
| MCP/设置 | [Yunado/dsh-qwen38-local-qol](https://github.com/Yunado/dsh-qwen38-local-qol) | DeepSeek Harness QoL plugin for the local Qwen3.8 line (27B/Flash-Next): per-request thinking budgets, a compa… |
| MCP/设置 | [appthin/dsh-mcp-manager-plus](https://github.com/appthin/dsh-mcp-manager-plus) | MCP 服务器管理插件：在 DeepSeek Harness 设置界面的左侧边栏新增「MCP 管理」页面。MCP Server Management Plugin: A new "MCP Management" page… |
| MCP/设置 | [bingaha/dsh-live-mcp](https://github.com/bingaha/dsh-live-mcp) | 给DSH提供会话级的MCP控制能力 |
| MCP/设置 | [crazywoola/dsh-balance](https://github.com/crazywoola/dsh-balance) | DeepSeek Harness balance plugin for the Settings page |
| MCP/设置 | [dpskk2/dsh-chatsync](https://github.com/dpskk2/dsh-chatsync) | DSH 接着聊：换台电脑，聊天和项目一起接着做。通过自己的 GitHub 私有仓库同步会话、附件、工作区文件和设置。 |
| MCP/设置 | [dshplugin/dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) | DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 10000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、… |
| MCP/设置 | [functy23/dsh-fullscreen-settings](https://github.com/functy23/dsh-fullscreen-settings) | 把 DSH 的设置弹窗改成 Codex 风格整页全屏设置页 — Codex-style full-page settings for DeepSeek Harness |
| MCP/设置 | [fwerkor/local-shell-mcp](https://github.com/fwerkor/local-shell-mcp) | Enables LLM to use a cli environment. |
| MCP/设置 | [imchangchang/dsh-llm-provider](https://github.com/imchangchang/dsh-llm-provider) | dsh LLM provider plugin: self-maintained pi-ai bridge, model selector, provider quota/billing and settings UI… |
| MCP/设置 | [joao-paulo-santos/dsh-granular-settings](https://github.com/joao-paulo-santos/dsh-granular-settings) | Granular settings platform: one Granular Settings page (Workspace/Session/Plugin tabs) where other DSH plugins… |
| MCP/设置 | [justhalfbit/dsh-plugin-memory](https://github.com/justhalfbit/dsh-plugin-memory) | DeepSeek Harness (DSH) 跨会话记忆插件：对话模型边干边记的 Markdown 项目记忆，支持专题文件渐进式披露、可选后台静默蒸馏、按项目隔离与热更新设置面板。机制对齐 Claude Code aut… |
| MCP/设置 | [lemoncat7/dsh-remote-settings-compat](https://github.com/lemoncat7/dsh-remote-settings-compat) | Remote settings compatibility plugin for DeepSeek Harness |
| MCP/设置 | [lsdt45/dsh-model-config](https://github.com/lsdt45/dsh-model-config) | DeepSeek Harness 模型设置页插件：管理提供方与模型目录，配置模型容量、输入类型与思考能力 |
| MCP/设置 | [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) | DSH 插件：一个设置面板，统一管理 MCP 服务器、技能、场景、记忆、子智能体人格、AGENTS.md 预设与归档会话——一个场景即可切换整个环境，模型也能帮你驱动这一切。 / DSH plugin: one sett… |
| MCP/设置 | [ptrel1/dsh-postapi-bridge](https://github.com/ptrel1/dsh-postapi-bridge) | DeepSeek Harness (DSH) 官方标准双半侧扩展插件：为外部机器人（MaiBot / 飞书 / 微信）及 CI/CD 系统提供开箱即用的轻量 HTTP POST / RESTful 任务调度、会话管理与… |
| MCP/设置 | [pure-craft/dsh-capability-panel](https://github.com/pure-craft/dsh-capability-panel) | Manage MCP servers, skills, and tools for your DeepSeek Harness agent — true in-context state and per-session… |
| MCP/设置 | [rickwindman/dsh-destinywind-memory](https://github.com/rickwindman/dsh-destinywind-memory) | DeepSeek Harness 插件：长期记忆库，注入每个会话的系统提示，设置页增删，HTTP API 改数 · Durable long-term memory bank plugin for DeepSeek Ha… |
| MCP/设置 | [sanshanya/better-model-provider](https://github.com/sanshanya/better-model-provider) | Per-model capability declaration for DeepSeek Harness: reasoning-effort levels (wire spellings) + request moda… |
| MCP/设置 | [soimy/dsh-gist-settings](https://github.com/soimy/dsh-gist-settings) | Back up and restore DeepSeek Harness profile configuration through GitHub Gists, using the local gh CLI. |
| MCP/设置 | [suntianc/dsh-codex-auth](https://github.com/suntianc/dsh-codex-auth) | DeepSeek Harness plugin that reuses the local Codex CLI ChatGPT login and adds a native GPT Auth settings card |
| MCP/设置 | [xienda/dsh-jev-verify](https://github.com/xienda/dsh-jev-verify) | Jev (TypeSafe System One decision model) for DeepSeek Harness: jev_decision, jev_overview, jev_guard_status an… |
| MCP/设置 | [xiseliuli/dsh-as-mcp](https://github.com/xiseliuli/dsh-as-mcp) | dsh-as-mcp |
| MCP/设置 | [xlennart/dsh-goal-mode-enhance](https://github.com/xlennart/dsh-goal-mode-enhance) | 为 DeepSeek Harness 提供可视化 goal 模式：Goal 栏 / 头部入口 / 设置页（历史+多会话总览）/ goal_overview 模型工具 |
| MCP/设置 | [zlZayn/dsh-ds-balance](https://github.com/zlZayn/dsh-ds-balance) | DSH 插件：在左侧栏底部显示 DeepSeek 账户余额（原生 UI），设置页提供连接、展示币种、预警阈值与刷新节奏的配置卡片。（原生嵌入“设置-插件-插件配置”） |
| 浏览器 | [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) | 把 DSH Web 状态行换成 1063 条梗:打字机 + 炫彩渐变 + 弹幕 + 12 个主题词库包,设置页可视化编辑。 |
| 浏览器 | [0QwQ0/dsh-ui-auth](https://github.com/0QwQ0/dsh-ui-auth) | DeepSeek Harness Web UI 认证网关插件：登录门禁、用户管理、管理员专属模型/Key 配置、数据隔离 · Authentication gate for the DeepSeek Harness We… |
| 浏览器 | [240xu/dsh-websearch](https://github.com/240xu/dsh-websearch) | Unified web search provider for DSH |
| 浏览器 | [6mt/dsh-plugin-loopback-trust](https://github.com/6mt/dsh-plugin-loopback-trust) | Restore Host-persisted settings in dsh web behind a reverse proxy — marks the page connection as host-owning s… |
| 浏览器 | [AFAP/dsh-token-usage](https://github.com/AFAP/dsh-token-usage) | DeepSeek Harness Web GUI Token 用量展示插件：单会话胶囊 + 全局每日/按模型消耗面板（只读日志，零配置）/ Token usage display plugin: per-session… |
| 浏览器 | [AllenCoderBug/dsh-web-search-zerokey](https://github.com/AllenCoderBug/dsh-web-search-zerokey) | 零 key 联网搜索：不填任何 API key、不启任何本地服务、不消耗模型积分。多源聚合（Bing/HN/GitHub/arXiv/npm/掘金/CSDN），中英文自动路由。 |
| 浏览器 | [Andrietteprotective835/dsh-mcp-lens](https://github.com/Andrietteprotective835/dsh-mcp-lens) | Shrink massive MCP catalogs to two tools, letting DeepSeek Harness search and call 1,000+ remote APIs efficien… |
| 浏览器 | [CJYLZS/dsh-browser](https://github.com/CJYLZS/dsh-browser) | Give dsh agent a real browser to use |
| 浏览器 | [CaT-Hode/DSH-app](https://github.com/CaT-Hode/DSH-app) | Windows desktop plugin for DeepSeek Harness — shared Web sessions and plugins, startup logs and update recover… |
| 浏览器 | [ConTr0L0/dsh-balance-monitor](https://github.com/ConTr0L0/dsh-balance-monitor) | dsh-balance-monitor 是 DeepSeek Harness（DSH）的插件：在侧边栏实时显示 API 余额，按官方峰谷价目（每日自动从 DeepSeek 官方文档同步）精确计算每次请求成本，按会话/模型… |
| 浏览器 | [DashingMonkey/dsh-git-panel](https://github.com/DashingMonkey/dsh-git-panel) | deepseek-harness DSH Web 的 Git 工作区面板 |
| 浏览器 | [Dingpenghui-good/dsh-web-search-serper](https://github.com/Dingpenghui-good/dsh-web-search-serper) | Serper.dev-backed web search provider for DeepSeek Harness (DSH) web capability seam |
| 浏览器 | [DmitriyValetov/dsh-session-folders](https://github.com/DmitriyValetov/dsh-session-folders) | Session folders for the DSH 0.2.x web sidebar — fork of EugeneVl/dsh_session_folders (MIT) ported to DSH 0.2.0… |
| 浏览器 | [Edison-q/dsh-mascot-xiadie](https://github.com/Edison-q/dsh-mascot-xiadie) | Q版遐蝶余额小管家 —— DeepSeek Harness 网页插件：悬浮小人实时播报账户余额与 token 用量，可拖动、可换图、可换角色台词。 |
| 浏览器 | [EdwinDigital/dsh-web-search-microsoft-webiq](https://github.com/EdwinDigital/dsh-web-search-microsoft-webiq) | Microsoft Web IQ search provider plugin for DeepSeek Harness |
| 浏览器 | [Erbsen16/dsh-client-ui-dracula](https://github.com/Erbsen16/dsh-client-ui-dracula) | 把 VS Code 的 Dracula（吸血鬼）配色搬到 DeepSeek Harness 的网页界面，顺带做了一组程序员向的排版调优。深色模式专用，随时可整页还原。 |
| 浏览器 | [EveGoodEvening/dsh-autoresearch](https://github.com/EveGoodEvening/dsh-autoresearch) |  |
| 浏览器 | [Failing-coachman563/dsh-skill-viewer](https://github.com/Failing-coachman563/dsh-skill-viewer) | Manage and organize DSH skills via a web interface with one-click enable/disable, batch migration, and workspa… |
| 浏览器 | [Gnatnaituy/dsh-sidebar-chat](https://github.com/Gnatnaituy/dsh-sidebar-chat) | A lightweight chat panel in DSH's right sidebar: pick a model, send text and images, search the web — no worki… |
| 浏览器 | [GooDAnDReaDY/dsh-lanmode](https://github.com/GooDAnDReaDY/dsh-lanmode) | Mobile gateway and secure local network access for DeepSeek Harness WebUI |
| 浏览器 | [HakureiMonika/dsh-browser-scope](https://github.com/HakureiMonika/dsh-browser-scope) | Agent-native browser DevTools workbench for DeepSeek Harness. / 让你的DSH获得非常强大的 Chromium DevTools 能力 |
| 浏览器 | [Han-1413141/dsh-autocompose](https://github.com/Han-1413141/dsh-autocompose) | Task-aware plugin composition for DeepSeek Harness, with native Web UI and isolated task execution |
| 浏览器 | [Han-1413141/dsh-sticky-disclosure](https://github.com/Han-1413141/dsh-sticky-disclosure) | DeepSeek Harness Desktop and Web plugin: collapse thinking, tool cards and process groups with one click or a… |
| 浏览器 | [Han-1413141/dsh-ui-hub](https://github.com/Han-1413141/dsh-ui-hub) | DeepSeek Harness Desktop and Web UI manager: search, show/hide, move, resize and arrange plugin controls, with… |
| 浏览器 | [Han-1413141/dsh-visual-edit](https://github.com/Han-1413141/dsh-visual-edit) | Point at a webpage, give your DeepSeek Harness agent feedback, and compare the result. Local Vite + React visu… |
| 浏览器 | [HateYouLittle/dsh-web-tinyfish](https://github.com/HateYouLittle/dsh-web-tinyfish) | TinyFish search + fetch providers for DeepSeek Harness (dsh): backs the built-in web_search and web_fetch tool… |
| 浏览器 | [HelloQingTao/dsh-rail-zero](https://github.com/HelloQingTao/dsh-rail-zero) | DeepSeek Harness web plugin: zero the collapsed left sidebar's 56px rail; reuses dsh-qol's hamburger, falls ba… |
| 浏览器 | [HorusJiang/dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) | Jev judgment, not generation: prune long tool output, screen fetched pages for injected instructions, and gate… |
| 浏览器 | [HuanLinOTO/dsh-plugin-better-glob](https://github.com/HuanLinOTO/dsh-plugin-better-glob) | 以 per-agent 阴影顶替内置 glob：自动排除无底洞目录（node_modules 等），传 include 白名单才能搜入 / Shadows the built-in glob per agent: aut… |
| 浏览器 | [HuanLinOTO/dsh-plugin-copilot](https://github.com/HuanLinOTO/dsh-plugin-copilot) | Copilot 引导层插件：WebUI 设置卡片一键 GitHub 授权 + 自动激活模型路由并收窄模型列表（复用 dsh-llm-pi-ai 内置 device-flow） / Copilot onboarding p… |
| 浏览器 | [HuanLinOTO/dsh-plugin-merge-tool-calls](https://github.com/HuanLinOTO/dsh-plugin-merge-tool-calls) | 把 WebUI 会话流中连续相邻的同工具调用合并为「主卡片+紧凑子行」树状展示，默认覆盖所有内置通用行工具 / Merges consecutive same-tool calls in the WebUI chat f… |
| 浏览器 | [HuanLinOTO/dsh-plugin-sidebar-brand-text](https://github.com/HuanLinOTO/dsh-plugin-sidebar-brand-text) | 替换侧边栏左上角的品牌名与构建徽标文案（WebUI 插件配置页卡片实时配置） / Replace the sidebar's top-left brand name and build-revision badge te… |
| 浏览器 | [HuanLinOTO/dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) | DSH Web 工作区侧栏替代，顶部全局最近会话 + Workspace→Session 二级菜单 + 面包屑 / DSH Web workspace sidebar replacement: top global re… |
| 浏览器 | [HuanLinOTO/dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) | 可配置子代理 profile 系统，单一 subagent 工具 + profile 参数，含 Web UI 设置/实时进度/子代理树 / Configurable subagent profile system: si… |
| 浏览器 | [IT-coder-Yy/dsh-git-plugin](https://github.com/IT-coder-Yy/dsh-git-plugin) | A visual Git workbench for DeepSeek Harness Web—inspect repositories, run common Git actions, and safely execu… |
| 浏览器 | [Leshm0321/dsh-plugin-local-agent-bridge](https://github.com/Leshm0321/dsh-plugin-local-agent-bridge) | Drive the Claude Code and Codex installations already on your machine from the DeepSeek Harness browser UI. |
| 浏览器 | [Likenttt/garmin-connect-plugin-for-dsh](https://github.com/Likenttt/garmin-connect-plugin-for-dsh) | A TypeScript-based Garmin Connect plugin and MCP server with secure browser-based MFA, built for DeepSeek Harn… |
| 浏览器 | [LilycleHeart/dsh-liuli-ui-enhance](https://github.com/LilycleHeart/dsh-liuli-ui-enhance) | 琉璃 UI 增强 —— DSH 主题插件:M3 动态取色、壁纸磨砂材质、声纹可视化、dock shell、嵌入式浏览器 |
| 浏览器 | [LoKiGGo/dsh-tools](https://github.com/LoKiGGo/dsh-tools) | dsh web通用工具箱插件，纯AI制作（包括仓库），零人工含量，可能不会维护，请谨慎使用。 |
| 浏览器 | [Longxiangjunlin/dsh-endfield-theme](https://github.com/Longxiangjunlin/dsh-endfield-theme) | Arknights: Endfield theme for the DeepSeek Harness Web GUI — charcoal + hazard-yellow industrial HUD, first-pa… |
| 浏览器 | [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) | DSH的插件创意市场来啦!～～～欢迎使用&提供反馈！！DSH 插件创意市场 · DeepSeek Harness 插件发现与一键安装面板 全量嗅探官方 dsh-plugin topic（900+），过滤蹭标签噪音，保留人… |
| 浏览器 | [MistyRain-field/dsh-hu-tao-skin](https://github.com/MistyRain-field/dsh-hu-tao-skin) | 原神 · 胡桃（往生堂）界面美化 — DeepSeek Harness Web GUI 客户端插件皮肤 / Hu Tao (Wangsheng Funeral Parlor) skin for dsh web |
| 浏览器 | [MyRemme/dsh-lan-pair](https://github.com/MyRemme/dsh-lan-pair) | LAN-only remote access for DSH: pair a phone or another PC by QR code or token to open the same web UI, with o… |
| 浏览器 | [NamesMT/dsh-home-hosted](https://github.com/NamesMT/dsh-home-hosted) | DeepSeek Harness (dsh) plugin: start your dsh web server automatically at boot, and manage home-hosted's panel… |
| 浏览器 | [NoNameLeGo/dsh-catppuccin-theme](https://github.com/NoNameLeGo/dsh-catppuccin-theme) | DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphis… |
| 浏览器 | [Plocr/dsh-commandcode-goat](https://github.com/Plocr/dsh-commandcode-goat) | DeepSeek Harness (dsh) plugin: publishes a Command Code subscription (GOAT / Pro / Max) as llm-pi-ai provider… |
| 浏览器 | [Qinling-Melon-Farmers/dsh-memoir](https://github.com/Qinling-Melon-Farmers/dsh-memoir) | DeepSeek Harness (DSH) local-first cross-session project memory: zero bundled runtime deps, bounded cache-frie… |
| 浏览器 | [Ragnoryok1/dsh-client-locale-ru](https://github.com/Ragnoryok1/dsh-client-locale-ru) | Russian (ru) language pack for the DeepSeek Harness web GUI - installable hybrid dsh.bundle + dsh.client plugi… |
| 浏览器 | [RailgunHamster/dsh-web-search](https://github.com/RailgunHamster/dsh-web-search) | A DeepSeek Harness plugin for selecting and routing web search providers. |
| 浏览器 | [Rainpomelo/dsh-liquid-glass-theme](https://github.com/Rainpomelo/dsh-liquid-glass-theme) | DeepSeek Harness - 液态玻璃与动态壁纸主题 (WebGL 物理透镜、动态壁纸与多层毛玻璃) #dsh-plugin |
| 浏览器 | [Rosa42/dsh-sync](https://github.com/Rosa42/dsh-sync) | DeepSeek Harness plugin: sync sessions and profile configuration across machines with rclone bisync, with a co… |
| 浏览器 | [SciF-Lin/dsh-browsercontrol-mcp](https://github.com/SciF-Lin/dsh-browsercontrol-mcp) | Real browser control for DeepSeek Harness: mounts Playwright MCP as native tools so the agent drives a browser… |
| 浏览器 | [Shadoso-w/dsh-cli-mode](https://github.com/Shadoso-w/dsh-cli-mode) | Command-line mode for the DeepSeek Harness web GUI: a composer line starting with ！ or ! runs as a real comman… |
| 浏览器 | [Sostay/dsh-wallpaper](https://github.com/Sostay/dsh-wallpaper) | Custom full-window wallpaper plugin for DeepSeek Harness (DSH): gradient presets, image URLs, local uploads, f… |
| 浏览器 | [Stolyarovmn/dsh-schedule-tab](https://github.com/Stolyarovmn/dsh-schedule-tab) | DeepSeek Harness Web plugin: a global Schedule tab showing reminders across all dialogs |
| 浏览器 | [Stolyarovmn/dsh-ui-registry-aggregator](https://github.com/Stolyarovmn/dsh-ui-registry-aggregator) | Federated plugin registry aggregator for DeepSeek Harness — combine npm, GitHub, and JSON catalogs into one se… |
| 浏览器 | [TBChaos/dsh-remote-desks](https://github.com/TBChaos/dsh-remote-desks) | 把本机 / WSL / 虚拟机 / SSH 远端上另一套 DSH 的 WebUI 镜像进桌面版 DSH，用同一套界面和体验管理它们。DSH 插件，MIT。 |
| 浏览器 | [TC635807/better-crawler4agent](https://github.com/TC635807/better-crawler4agent) | When I was using agents, I found that most agents rely on curl commands to scrape web pages, which has a very… |
| 浏览器 | [TOBYCAI/dsh-sessions-manager](https://github.com/TOBYCAI/dsh-sessions-manager) | DSH 会话管理插件：设置面板 + 侧边栏双入口，归档/恢复/跨工作区移动/软删进回收站；回收站可恢复·批量清空·7/30/90 天自动清理，按标题·会话 ID·工作区搜索，带磁盘与血统详情；已适配 DSH 0.1.7… |
| 浏览器 | [Tim5613/dsh-homepage-glass](https://github.com/Tim5613/dsh-homepage-glass) | DSH macOS风格深蓝渐变侧边栏 + 官网流动蓝底丨DSH macOS-Style Deep Blue Gradient Sidebar + Official Website Fluid Blue Backgroun… |
| 浏览器 | [UnforgetMemory/um-dsh-websearch](https://github.com/UnforgetMemory/um-dsh-websearch) | Exa (exa.ai) web search provider plugin for DeepSeek Harness (DSH): dynamic enabled switch, credentials-servic… |
| 浏览器 | [VinciBeans/dsh-web-search-anysearch](https://github.com/VinciBeans/dsh-web-search-anysearch) | AnySearch-backed WebSearchProvider for DeepSeek Harness (dsh): switch web_search between the official DeepSeek… |
| 浏览器 | [WSL043/dsh-chat-manager](https://github.com/WSL043/dsh-chat-manager) | DeepSeek Harness chat history and session management: search archives, restore conversations, and delete safel… |
| 浏览器 | [Witchwarren2344/dsh-mnemosyne-memory](https://github.com/Witchwarren2344/dsh-mnemosyne-memory) | Provide long-term memory, vector semantic search, and LLM reflection for DeepSeek Harness (DSH) with this free… |
| 浏览器 | [YanKaFei/Lacan-Knowledge-OS](https://github.com/YanKaFei/Lacan-Knowledge-OS) | Corpus-grounded research environment for Lacanian psychoanalysis: frozen scholarly core (39 hash-pinned compon… |
| 浏览器 | [YePpHa/dsh-web-search-kagi](https://github.com/YePpHa/dsh-web-search-kagi) | Kagi Search v1 provider for the DeepSeek Harness. |
| 浏览器 | [YpipaQ/dsh-s-m-c-center](https://github.com/YpipaQ/dsh-s-m-c-center) | 三合一工具台 · Skills / MCP / CLI 管理器：一个设置页统一管理 DeepSeek Harness（dsh）agent 的三类工具，MCP 走真实连接。 / Skills, MCP and CLI ma… |
| 浏览器 | [YumeAyai/dsh-swiss-target](https://github.com/YumeAyai/dsh-swiss-target) | SwissTargetPrediction batch prediction for DeepSeek Harness — Submit SMILES strings, retrieve predicted target… |
| 浏览器 | [Yurzi/dsh-web-fetch-enhanced](https://github.com/Yurzi/dsh-web-fetch-enhanced) | Configurable non-public address allowlists for DeepSeek Harness web_fetch |
| 浏览器 | [Yurzi/dsh-web-search-enhanced](https://github.com/Yurzi/dsh-web-search-enhanced) | Multi-protocol web_search provider for DeepSeek Harness |
| 浏览器 | [Yyyyyylor/dsh-asuka-school-theme](https://github.com/Yyyyyylor/dsh-asuka-school-theme) | Theme-Asuka — An unofficial Asuka-inspired theme plugin for DeepSeek Harness Web UI, featuring time-of-day wal… |
| 浏览器 | [ZiYuan258/dsh-skill-router](https://github.com/ZiYuan258/dsh-skill-router) | Agent-driven skill discovery and on-demand loading for DeepSeek Harness: skill_search / skill_load / skill_ref… |
| 浏览器 | [aiyacharley/dsh-pubmed](https://github.com/aiyacharley/dsh-pubmed) | DSH plugin for DeepSeek Harness: 25 model tools spanning PubMed, Europe PMC, PubTator3 & Semantic Scholar — en… |
| 浏览器 | [auggie246/dsh-synthetic-web-search](https://github.com/auggie246/dsh-synthetic-web-search) | Deepseek Harness plugin to use synthetic.new web search instead of built-in Deepseek web search |
| 浏览器 | [awol2005ex3/dsh-wecom](https://github.com/awol2005ex3/dsh-wecom) | DeepSeek Harness (dsh) plugin: WeCom (WeChat Work) smart-robot integration over the long-connection (WebSocket… |
| 浏览器 | [azazo1/dsh-reject-message](https://github.com/azazo1/dsh-reject-message) | DSH web plugin: take over the native approval window so a reject can carry a description the model will see. |
| 浏览器 | [badai147/dsh-global-rules](https://github.com/badai147/dsh-global-rules) | A plugin for editing global rules in the DeepSeek Harness Web settings panel. |
| 浏览器 | [bauerelizabeth07139/MDSM](https://github.com/bauerelizabeth07139/MDSM) | MDSM (Male DeepSeek Mascot) appearance layer for the DeepSeek Harness Web GUI: chat wallpaper with opacity, bl… |
| 浏览器 | [bauerelizabeth07139/nai](https://github.com/bauerelizabeth07139/nai) | Nai milk-frog mascot appearance layer for the DeepSeek Harness Web GUI: chat wallpaper with opacity, blur and… |
| 浏览器 | [bauerelizabeth07139/tangsan](https://github.com/bauerelizabeth07139/tangsan) | TangSan mascot appearance layer for the DeepSeek Harness Web GUI: chat wallpaper with opacity, blur and scrim… |
| 浏览器 | [better-er/dsh-classic-coding](https://github.com/better-er/dsh-classic-coding) | 「DSH·古法编程」：在 DSH Web 界面右侧栏用 Monaco 编辑器打开工作区代码文件。 |
| 浏览器 | [better-er/dsh-tool-autoexpand](https://github.com/better-er/dsh-tool-autoexpand) | 「DSH·工具结果自动展开」：在 DSH Web 界面自动展开工具调用卡片，支持侧边栏开关。标准可安装的 dsh 客户端插件。 |
| 浏览器 | [chenyuhao0628/dsh-web-search-router](https://github.com/chenyuhao0628/dsh-web-search-router) | Free multi-provider web search router for DeepSeek Harness (DSH) |
| 浏览器 | [chiikin/dsh-glm-quota](https://github.com/chiikin/dsh-glm-quota) | GLM Coding Plan quota display plugin for the DeepSeek Harness (DSH) web UI |
| 浏览器 | [cv-superding/dsh-deepseek-web-login](https://github.com/cv-superding/dsh-deepseek-web-login) | Unofficial DSH (DeepSeek Harness) plugin: use chat.deepseek.com web models as an LLM provider - browser-login… |
| 浏览器 | [cyjyyd/dsh-ssh-tui](https://github.com/cyjyyd/dsh-ssh-tui) | SSH-friendly DeepSeek Harness TUI. Plain ANSI, incremental redraws, no browser. |
| 浏览器 | [ddowbnac/dsh-web-search-local](https://github.com/ddowbnac/dsh-web-search-local) | A web-search provider for the DeepSeek Harness, fully local no API key needed. |
| 浏览器 | [deepseekharness-dsh/dsh-local-file-share](https://github.com/deepseekharness-dsh/dsh-local-file-share) | Local File Share / 本地文件共享: let the dsh agent list, read and write files on the machine running your browser ov… |
| 浏览器 | [dingzhenyao/dsh-plugin-directory](https://github.com/dingzhenyao/dsh-plugin-directory) | DSH Web GUI plugin: a browsable, searchable, stats-driven directory of GitHub DeepSeek Harness plugins (dsh-pl… |
| 浏览器 | [donoteatme/dsh-local-link](https://github.com/donoteatme/dsh-local-link) | Lightweight DeepSeek Harness plugin for paired LAN access: scan a QR code and continue the current DSH Web ses… |
| 浏览器 | [drmi5446/dsh-wallpaper-engine](https://github.com/drmi5446/dsh-wallpaper-engine) | Turn Wallpaper Engine wallpapers into a liquid glass background for the DSH web GUI, with video and web suppor… |
| 浏览器 | [drscrewdriver/dsh-opensheet-sidebar](https://github.com/drscrewdriver/dsh-opensheet-sidebar) | DSH web plugin (dsh-better-sidebar consumer): CSV/TSV/PSV plus xlsx/xlsm workbook preview in the right sidebar… |
| 浏览器 | [drscrewdriver/dsh-search-index](https://github.com/drscrewdriver/dsh-search-index) | 给 DeepSeek Harness 侧边栏加一个会话内容检索——标题/内容一键切换，还能按用户/回复/工具筛选 |
| 浏览器 | [dshworks/dsh-ego-browser](https://github.com/dshworks/dsh-ego-browser) | ego lite browser automation for dsh that remembers — recall a site's learned tools, promote a working script i… |
| 浏览器 | [duhu2000/dsh-mcp-connector](https://github.com/duhu2000/dsh-mcp-connector) | DeepSeek Harness MCP Connector: connect servers, search tools across active connections, and troubleshoot disc… |
| 浏览器 | [fanyongbing/dsh-mcp-native](https://github.com/fanyongbing/dsh-mcp-native) | MCP server manager for DeepSeek Harness — manage this machine's MCP servers as native Loader rows, from a Sett… |
| 浏览器 | [fatatalia/dsh-imessage](https://github.com/fatatalia/dsh-imessage) | dsh iMessage 插件：监听/路由/自动回复/typing/已读回执，随 dsh web 启停 |
| 浏览器 | [fengyu-12/dsh-second-engine](https://github.com/fengyu-12/dsh-second-engine) | 把 OpenAI Codex CLI 接入 DeepSeek Harness 作为第二引擎：异步工单 / 双向互审 / 终端↔网页共享会话桥 / 文件任务板 · Plug Codex CLI into DeepSeek… |
| 浏览器 | [gst20060726/dsh-auto-translate](https://github.com/gst20060726/dsh-auto-translate) | Zero-token on-demand translation for the DeepSeek Harness Web GUI — hover a block or drag-select text to trans… |
| 浏览器 | [haitang1/dsh-memory](https://github.com/haitang1/dsh-memory) | Codex-like persistent memory plugin for DeepSeek Harness: auto-injected memory summary, memory tools, per-sess… |
| 浏览器 | [haotian-lu-prog/dsh-dev-backup](https://github.com/haotian-lu-prog/dsh-dev-backup) | Backup freshness monitor for DeepSeek Harness — see whether your scheduled backup actually ran, right in the H… |
| 浏览器 | [he0119/dsh-tailnet-admin](https://github.com/he0119/dsh-tailnet-admin) | 把 Tailnet / 反向代理页面当作「本机」来用：启用 host 持久化设置，并按需关闭浏览器会话校验（Host/Origin 栅栏保持不动）。 |
| 浏览器 | [heerxingen/dsh-model-capabilities](https://github.com/heerxingen/dsh-model-capabilities) | DSH web plugin: declare model capabilities (image input, budgets, capacities, reasoning levels) for custom mod… |
| 浏览器 | [hjj345/dsh-sm-context-piano](https://github.com/hjj345/dsh-sm-context-piano) | DeepSeek Harness Web GUI 的 Codex 风格对话导航器：帮助用户快速浏览、定位和切换对话，提升多任务、多会话场景下的工作效率。 / Codex-style conversation naviga… |
| 浏览器 | [hjj345/dsh-sm-version-display](https://github.com/hjj345/dsh-sm-version-display) | 用于在侧边栏“设置”按钮上方显示已安装 dsh 版本的 DeepSeek Harness Web 插件。 / DeepSeek Harness Web plugin that displays the installed… |
| 浏览器 | [hkkz9522/dsh-session-manager](https://github.com/hkkz9522/dsh-session-manager) | DeepSeek Harness session manager: delete, archive, move sessions across workspaces, migrate presets, favorites… |
| 浏览器 | [huanglianqi/dsh-math-render](https://github.com/huanglianqi/dsh-math-render) | Render LaTeX in the DSH web chat: formulas inside your own message bubble and a live preview of the composer d… |
| 浏览器 | [huashenglian/dsh-livechat](https://github.com/huashenglian/dsh-livechat) | 给 dsh 对话区叠加 B 站风格吐槽弹幕，可接入 LLM 生成弹幕。/Bilibili-style live-chat danmaku overlay for DeepSeek Harness Web — preset… |
| 浏览器 | [hyperion2144/dsh-desktop-tauriapp](https://github.com/hyperion2144/dsh-desktop-tauriapp) | Tauri 2 desktop shell wrapping the DeepSeek Harness Web GUI (macOS + Windows) — tray daemon, auto-launch/reuse… |
| 浏览器 | [iwinoid/fakeip-compat](https://github.com/iwinoid/fakeip-compat) | Fake-IP-aware web.fetch provider for TUN (Mihomo/Clash) DNS environments plus pinned LAN CIDR access |
| 浏览器 | [jackovibe/dsh-settings-order](https://github.com/jackovibe/dsh-settings-order) | DSH Web 设置左列自由排序插件：拖动 / Alt+↑↓ / ↑↓ 按钮，宿主持久，跨浏览器生效（Free ordering for the DeepSeek Harness Web Settings navigat… |
| 浏览器 | [jeffreyren1/dsh-custom-js](https://github.com/jeffreyren1/dsh-custom-js) | Customize DeepSeek Harness without forking it—load, edit, manage, and hot-reload trusted JavaScript and TypeSc… |
| 浏览器 | [jiangwangyang/dsh-theme-blackhole](https://github.com/jiangwangyang/dsh-theme-blackhole) | A black hole theme plugin for the dsh (DeepSeek Harness) Web UI: a WebGL real-time ray-traced Schwarzschild bl… |
| 浏览器 | [jiekesu967/dsh-markitdown](https://github.com/jiekesu967/dsh-markitdown) | Microsoft MarkItDown as a DeepSeek Harness tool: convert PDF, Word, Excel, PowerPoint, HTML, CSV, EPUB, or a U… |
| 浏览器 | [jiekesu967/dsh-plugin-opencode-usage](https://github.com/jiekesu967/dsh-plugin-opencode-usage) | OpenCode Go 订阅用量悬浮面板:DeepSeek Harness Web 侧边栏显示滚动/每周/每月额度、已用与剩余额度。 |
| 浏览器 | [jypjypjypjyp/dsh-notifier](https://github.com/jypjypjypjyp/dsh-notifier) | 审批/完成/错误事件通知：浏览器 Notification + 系统原生 toast（Windows PowerShell WinRT / macOS osascript / Linux notify-send，均无需额… |
| 浏览器 | [keenableai/dsh-keenable](https://github.com/keenableai/dsh-keenable) | Keenable web search and page fetch for DeepSeek Harness, no API key needed |
| 浏览器 | [knighthongyu/dsh-handoff-compaction](https://github.com/knighthongyu/dsh-handoff-compaction) | Context compression for DSH: visually configure summary and recent-context budgets (8k + 16k by default), keep… |
| 浏览器 | [lee259/dsh-workbench](https://github.com/lee259/dsh-workbench) | Right-side file workspace for DeepSeek Harness Web. |
| 浏览器 | [lhh010/dsh-file-trace](https://github.com/lhh010/dsh-file-trace) | DSH Web UI 文件追踪插件：记录并查看模型读取/写入/编辑的每个文件，带行号内容、终端风逐行 diff（红删绿增蓝改）与 hunk 上下文折叠；支持 present 交付文件查看（Markdown 渲染 / Ka… |
| 浏览器 | [lhh010/dsh-input-history](https://github.com/lhh010/dsh-input-history) | DSH Web 输入历史插件：Ctrl+Up / Ctrl+Down 像终端一样召回与切换已发送消息，零核心改动 |
| 浏览器 | [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) | DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器 |
| 浏览器 | [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) | DSH WebUI 文件输入增强：Ctrl+V 粘贴 + 拖拽 + 选择文件（图片悬停预览 / 缩放查看器 / 防伪造校验），发送时复制进会话工作区临时目录；无视觉模型发送失败自动移除图片附件并提示重发；桌面端经 bas… |
| 浏览器 | [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) | DSH Web UI 会话进度插件：输入框停靠区常驻进度条（todos 真实进度 / token 速率与 ETA / 中断橘红态 / 后台任务与子代理青色态 / Token 用量徽标与缓存命中面板），窄窗口两行自适应，零… |
| 浏览器 | [licyer/dsh-token-monitor](https://github.com/licyer/dsh-token-monitor) | DSH Web 模型余量与用量监控插件 |
| 浏览器 | [lifeopsgo/dsh-capability-toggle-plugin](https://github.com/lifeopsgo/dsh-capability-toggle-plugin) | 灵活控制 mcp/skill/tool 等启用/禁用，支持会话、项目、全局级别控制。Toggle individual agent capabilities (skills, MCP, tools, prompt, ap… |
| 浏览器 | [lildanger/dsh-skin-win2000](https://github.com/lildanger/dsh-skin-win2000) | Windows 2000 skin for the DSH Web GUI: metric-accurate grey chrome, two-tone gradient title bars, 1px bevels,… |
| 浏览器 | [linkingoscar/dsh-attachment-formats](https://github.com/linkingoscar/dsh-attachment-formats) | Codex-style attachment formats for the DeepSeek Harness Web GUI: PDF text-layer extraction, Office text extrac… |
| 浏览器 | [linkingoscar/dsh-billing-glass](https://github.com/linkingoscar/dsh-billing-glass) | Liquid-glass billing overlay for the DeepSeek Harness Web GUI: provider balances, session cost, daily spend an… |
| 浏览器 | [lordraiden/dsh-9router-web-search](https://github.com/lordraiden/dsh-9router-web-search) | DSH plugin: 9router-backed web search and web fetch providers |
| 浏览器 | [lxl8182/dsh-message-edit](https://github.com/lxl8182/dsh-message-edit) | DSH Web 用户消息编辑重发插件：改掉某一轮提问重发，该轮之后的内容丢弃，原会话归档（新会话继承逐字节相同前缀以保住 prompt 缓存）。 |
| 浏览器 | [lxl8182/dsh-session-ops](https://github.com/lxl8182/dsh-session-ops) | DSH Web 会话管理插件：设置 → 会话管理，一键归档 / 一键还原 / 一键删除（删除移入回收目录，可手工恢复）。 |
| 浏览器 | [lychee888/galvanize-dsh](https://github.com/lychee888/galvanize-dsh) | Triggers inside your DSH agent: wake a fresh DeepSeek Harness session when files, mail, webhooks, or git event… |
| 浏览器 | [lzpway-jpg/dsh-plugin-brand-custom](https://github.com/lzpway-jpg/dsh-plugin-brand-custom) | Custom brand icon and name for the DeepSeek Harness Web client, editable live from a settings card |
| 浏览器 | [meltartica/dsh-mcp-servers](https://github.com/meltartica/dsh-mcp-servers) | DeepSeek Harness bundle that exposes Model Context Protocol (MCP) servers as native tools, with a settings UI,… |
| 浏览器 | [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) | Tavily-powered optional search tool for DeepSeek Harness (rc.7 plugin management): multi-key rotation/failover… |
| 浏览器 | [mwk719/dsh-skill-center](https://github.com/mwk719/dsh-skill-center) | DSH Web GUI 技能中心：侧栏入口把可配置来源目录里的技能铺成卡片，点击查看完整 SKILL.md；卡片开关会把技能注册进或移出模型可用的技能表。零依赖、免构建、无遥测、不采集数据。 |
| 浏览器 | [novaschai7/dsh-plugin-balance-ui](https://github.com/novaschai7/dsh-plugin-balance-ui) | DeepSeek account balance, today's token usage and estimated spend in the dsh Web client sidebar. · 在 dsh 侧边栏显示… |
| 浏览器 | [oldHan2423/dsh-everything-find](https://github.com/oldHan2423/dsh-everything-find) | Everything (voidtools) file-name search for DeepSeek Harness: an everything_find tool plus a configuration car… |
| 浏览器 | [omdsh-dev/dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) | DSH Web 选中批注插件：选文字→批注→回车随消息发送；气泡隐藏批注块（零闪烁）；回复按 Annotation N 逐条对照（可悬浮芯片）。官方 bundle，零核心改动 |
| 浏览器 | [omdsh-dev/dsh-file-trace](https://github.com/omdsh-dev/dsh-file-trace) | DSH Web UI 文件追踪插件：记录并查看模型读取/写入/编辑的每个文件，带行号内容、终端风逐行 diff（红删绿增蓝改）与 hunk 上下文折叠；支持 present 交付文件查看（Markdown 渲染 / Ka… |
| 浏览器 | [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) | GenUI for DeepSeek Harness: interactive UI components rendered inline in assistant replies via the dsh-ui fenc… |
| 浏览器 | [omdsh-dev/dsh-input-history](https://github.com/omdsh-dev/dsh-input-history) | DSH Web 输入历史插件：Ctrl+Up / Ctrl+Down 像终端一样召回与切换已发送消息，零核心改动 |
| 浏览器 | [omdsh-dev/dsh-ui-progress](https://github.com/omdsh-dev/dsh-ui-progress) | DSH Web UI 会话进度插件：输入框停靠区常驻进度条（todos 真实进度 / token 速率与 ETA / 中断橘红态 / 后台任务与子代理青色态 / Token 用量徽标与缓存命中面板），窄窗口两行自适应，零… |
| 浏览器 | [pure-craft/dsh-actions](https://github.com/pure-craft/dsh-actions) | Deterministic project actions for people and agents — a DeepSeek Harness Web plugin. One actions.json, two sur… |
| 浏览器 | [qwerty-k-de/dsh-attach-picker](https://github.com/qwerty-k-de/dsh-attach-picker) | DSH Web composer toolbar picture button: pick images via the OS file dialog - no drag-and-drop needed. |
| 浏览器 | [rice-awa/dsh-lan-gateway](https://github.com/rice-awa/dsh-lan-gateway) | 把 DeepSeek Harness 的 Web GUI 安全地开放到局域网或公网，自带密码鉴权，支持可选的TLS。Securely expose DeepSeek Harness's Web GUI to your l… |
| 浏览器 | [robiteame/dsh-session-tree-extension](https://github.com/robiteame/dsh-session-tree-extension) | dsh-session-tree-extension Append-only, multi-branch conversation trees for DeepSeek-Harness — a PI-Agent-styl… |
| 浏览器 | [rocklau/dsh-rss-reader](https://github.com/rocklau/dsh-rss-reader) | OpenBook RSS Reader as a DeepSeek Harness (dsh) Web UI plugin: RSS tab in the conversation view ring, sidebar… |
| 浏览器 | [rocklau/dsh-ui-digest](https://github.com/rocklau/dsh-ui-digest) | Turn-digest overview tab for the DeepSeek Harness (dsh) Web UI: what you asked, a one-sentence summary of what… |
| 浏览器 | [rocklau/dsh-ui-tool-graph](https://github.com/rocklau/dsh-ui-tool-graph) | Tool-call value graph tab for the DeepSeek Harness (dsh) Web UI: cost/duration/error weights over conversation… |
| 浏览器 | [ruisenbai/dsh-annotation](https://github.com/ruisenbai/dsh-annotation) | Annotate assistant replies in DSH Web, keep per-session records, and send or resend notes through the official… |
| 浏览器 | [sdegongzuo/dsh-webops-plugin](https://github.com/sdegongzuo/dsh-webops-plugin) | DeepSeek Harness 客户端网页操作与调试插件：多会话、新窗口、多标签页调试和操作网页 |
| 浏览器 | [sgzxs/dsh-global-task-list](https://github.com/sgzxs/dsh-global-task-list) | A global task library plugin for DeepSeek Harness featuring cross-session persistence, a real-time generative-… |
| 浏览器 | [shengsheng90/DSH-taskboard](https://github.com/shengsheng90/DSH-taskboard) | Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native W… |
| 浏览器 | [simplifyOurLife/dsh-spring-boot-launcher](https://github.com/simplifyOurLife/dsh-spring-boot-launcher) | 该项目是一个Deepseek Harness的插件，目前是作为Maven Spring Boot 项目的专用启动器。它提供 Agent 工具和 Web 管理面板，用同一套进程管理逻辑完成项目检查、Profile 选择、启… |
| 浏览器 | [skillre/dsh-plugin-pomodoro](https://github.com/skillre/dsh-plugin-pomodoro) | Pomodoro focus clock plugin for the DeepSeek Harness Web UI: ambient timer under the composer, daily rounds, l… |
| 浏览器 | [swiftlc/dsh-annotation](https://github.com/swiftlc/dsh-annotation) | Text annotation tools for the dsh web composer |
| 浏览器 | [temidayoxyz/deep-browser](https://github.com/temidayoxyz/deep-browser) | DeepSeek Harness (dsh) plugin: browse http(s) pages in the right sidebar, beside the conversation. |
| 浏览器 | [vitas/dsh-web-search-openrouter](https://github.com/vitas/dsh-web-search-openrouter) | Grounded web search for DeepSeek Harness on any OpenRouter-compatible gateway: the built-in web_search tool ru… |
| 浏览器 | [vowa-antilamer/dsh-locale-ru](https://github.com/vowa-antilamer/dsh-locale-ru) | Russian localization (ru) for the DeepSeek Harness web GUI — 58 message namespaces, 3674 strings. Language pac… |
| 浏览器 | [xchannel1987/dsh-mobile-xc](https://github.com/xchannel1987/dsh-mobile-xc) | DSH Web mobile UI adaptation plugin with overlay drawer, safe-area support, and canary version detection |
| 浏览器 | [xiaoso456/dsh-run-config](https://github.com/xiaoso456/dsh-run-config) | Run configuration management for DeepSeek Harness (DSH) — IDEA-style run control for the web GUI: reusable LLM… |
| 浏览器 | [ylwl1997/dshbase-catalog](https://github.com/ylwl1997/dshbase-catalog) | Search the dshbase plugin directory from inside DeepSeek Harness |
| 浏览器 | [yuu1111/dsh-ui-cost-meter](https://github.com/yuu1111/dsh-ui-cost-meter) | DeepSeek Harness Web GUI plugin: real-time spend for the current session, priced from per-model token rates an… |
| 浏览器 | [yuu1111/dsh-ui-font](https://github.com/yuu1111/dsh-ui-font) | DeepSeek Harness Web GUI plugin: change the UI font family through theme token overrides |
| 浏览器 | [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) | Page capability kit for DeepSeek Harness (dsh): terminal dock, file tree, source control, skills manager, phon… |
| 浏览器 | [zhu1090093659/dsh-community-plugins](https://github.com/zhu1090093659/dsh-community-plugins) | Community plugin index for the DSH Web GUI: community.json is the single source of the Workshop store plugin l… |
| 浏览器 | [zhu1090093659/dsh-skins](https://github.com/zhu1090093659/dsh-skins) | Skin center plugin and built-in skins for the DSH Web GUI: skins are pure asset directories, loaded and render… |
| 浏览器 | [zizhongfeiyang/dsh-settings-drawer](https://github.com/zizhongfeiyang/dsh-settings-drawer) | A DeepSeek Harness web UI plugin for customizing and managing the settings navigation drawer. DeepSeek Harness… |
| 行情 | [AIcivilization/deepseek-harness-vps](https://github.com/AIcivilization/deepseek-harness-vps) | One-command DeepSeek Harness on your VPS: a zero-dependency login gateway puts the stock DSH web UI - settings… |
| 行情 | [Kevoyuan/dsh-trading212](https://github.com/Kevoyuan/dsh-trading212) | Read-only Trading 212 portfolio dashboard and dsh tools for holdings, history, risk, and trade markers. |
| 行情 | [LisonEvf/dsh-stock-panel](https://github.com/LisonEvf/dsh-stock-panel) | 把 DSH 会话窗口变成 A 股盯盘执行台：行情仪表盘 · 盘后复盘七步 · 模型作战思路 · 自挖板块（无监督共动聚类 + LLM 命名）· 个股工作台 · 选股筛选 · 监控提醒 |
| 行情 | [Yinhefuluoye/dsh-glass-effect](https://github.com/Yinhefuluoye/dsh-glass-effect) | A glass-material appearance for DSH: translucent composer, dialogs, menus and code blocks — one switch in Sett… |
| 行情 | [guhanfei-ai/dsh-grafana](https://github.com/guhanfei-ai/dsh-grafana) | Agent-native Grafana observability for DeepSeek Harness — dashboards, metrics, trends, alerts and multi-source… |
| 行情 | [pengpengyi92/dsh-quant](https://github.com/pengpengyi92/dsh-quant) | "🐳 Dsh-Quant: The Everything-Plugin Ai native Quant OS " |
| 行情 | [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) | DeepSeek Harness (DSH) web plugin: 盯盘 market-dashboard sidebar tab — three quote strips with hover intraday ch… |
| 行情 | [tianyiming1/dsh-plugin-local-prompt-bridge](https://github.com/tianyiming1/dsh-plugin-local-prompt-bridge) | Stock-safe DSH community plugin: local tokenize pressure + overflow to CONTEXT_WINDOW_EXCEEDED compact-retry |
| 行情 | [v587d/capital-generation](https://github.com/v587d/capital-generation) | 面向中国股市散户的金融投资智能体。Next-Gen AI-Driven Capital Generation. |
| 语音 | [1497105876/dsh-mimotts](https://github.com/1497105876/dsh-mimotts) | MiMo TTS 语音合成 DSH 插件（DeepSeek Harness 0.1.7） |
| 语音 | [EternalNight996/dsh-ui-three-body](https://github.com/EternalNight996/dsh-ui-three-body) | 🎙 语音实时交互（内置 / 本地大模型 whisper+Ollama+Piper，三驱动下拉可选） · 👁 视觉实时交互（眼球跟随摄像头人形，对接 uvc-camera） · 🧠 产品设计 copilot（五策 + 质量… |
| 语音 | [ch1bug/dsh-mimo-agent-tools](https://github.com/ch1bug/dsh-mimo-agent-tools) | Xiaomi MiMo search + multimodal tools for DeepSeek Harness agents: mimo_search/vision/audio/video/asr/tts |
| 语音 | [flashyiyi/dsh-voice-announcer](https://github.com/flashyiyi/dsh-voice-announcer) |  |
| 语音 | [likhonmain/voice-input](https://github.com/likhonmain/voice-input) | 🎙️ Voice Input plugin for DeepSeek Harness — record, pause, playback review, and transcribe speech directly in… |
| 语音 | [ppy-web/dsh-plugin-xiaomi-mimo-tts](https://github.com/ppy-web/dsh-plugin-xiaomi-mimo-tts) | 给DSH接入免费的 Xiaomi MiMo TTS API，支持使用预置/自定义/浏览器内置声音朗读正文 |
| 语音 | [strawberry0321/dsh-gal](https://github.com/strawberry0321/dsh-gal) | dsh-gal —— DeepSeek Harness 的立绘挂件：实时显示余额与今日消耗、每轮对话结束结算 token 与花费、点击立绘随机播语音并逐字显示台词，立绘包/语音包都能换 |
| 语音 | [weizhida/dsh-voice-danmaku](https://github.com/weizhida/dsh-voice-danmaku) | 这是dsh的插件，语音发送弹幕。在玩游戏时通过语音输入在b站发弹幕，不切出游戏可以正常操作 |
| 桌宠 | [969246694/dsh-wisp](https://github.com/969246694/dsh-wisp) | DeepSeek娘 — an unofficial floating desktop companion for the DeepSeek Harness UI. Zero dependencies, sprites i… |
| 桌宠 | [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) | 🐖 一只住在 DeepSeek Harness 里的猪：吃你的真实工作长大，会学习、打工、旅行、生病。玩法照 QQ 宠物（怀旧服 v1.2.4）复刻 |
| 桌宠 | [CyberWei922/dsh-cyberwhale](https://github.com/CyberWei922/dsh-cyberwhale) | 一只常驻 macOS 桌面、随 DeepSeek Harness 工作状态变化的蓝色大肥鲸桌宠 |
| 桌宠 | [QWEQ-CELL-DEL/dsh-whale-girl-wallpaper](https://github.com/QWEQ-CELL-DEL/dsh-whale-girl-wallpaper) | DSH Web skin: whale-girl dynamic wallpaper background |
| 桌宠 | [SZYTree0312/dsh-whale-elite-preset](https://github.com/SZYTree0312/dsh-whale-elite-preset) | 鲸英模式：省 Token、高效率的 DeepSeek Harness Agent 预设 |
| 桌宠 | [SherinG-official/dsh-desktop-pet](https://github.com/SherinG-official/dsh-desktop-pet) | Windows desktop shell for DeepSeek Harness: native window + standalone desktop-pet process with live token usa… |
| 桌宠 | [Sutera-Diffusus/dsh-whale-musume](https://github.com/Sutera-Diffusus/dsh-whale-musume) | DeepSeek Harness 桌宠插件：元气鲸鱼娘陪你写代码 🐋（桌面端 0.2.0-rc.2 与旧版 Web 双端支持） |
| 桌宠 | [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) | A Windows desktop pet for official DeepSeek API balance, usage, and animated reactions in DSH. |
| 桌宠 | [askdkc/dsh-cli](https://github.com/askdkc/dsh-cli) | DSH向けCLI Plugin / DSH CLIplugin — whale bar, live status, streaming thoughts, double-Esc rollback, context bar… |
| 桌宠 | [drfai/dsh-whale-pet](https://github.com/drfai/dsh-whale-pet) | DeepSeek Harness 桌宠插件：内置 Coopanion 鲸鱼娘分层精灵，随模型峰谷计价自动更换女仆装发带颜色，并常驻显示时段倒计时 |
| 桌宠 | [joeseesun/qiaomu-rss-dsh](https://github.com/joeseesun/qiaomu-rss-dsh) | 在 DeepSeek Harness 中阅读 RSS，与原生 AI 对话伴读文章 / RSS reading with native AI companion for DeepSeek Harness |
| 桌宠 | [keleus/deepseek-pet](https://github.com/keleus/deepseek-pet) | 在你的deepseek-harness上养一只吃白饭的大蓝鲸 |
| 桌宠 | [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) | 【求⭐】🐋DSH Web UI 全手绘像素鲸鱼伙伴插件：会话标题栏常驻，平时眨眼/偶尔摆尾/动胸鳍，思考运行时持续动起来，回合完成头顶喷水，点击还会冒爱心，不工作时还会偷懒睡觉，零核心改动。 【喜欢的话就点点star⭐吧… |
| 桌宠 | [lunaship/dsh-links](https://github.com/lunaship/dsh-links) | Android companion for DeepSeek Harness: trusted-LAN pairing, mobile sessions, SSE approvals, experimental tunn… |
| 桌宠 | [rongzi5/dsh-whale-pet](https://github.com/rongzi5/dsh-whale-pet) |  |
| 桌宠 | [shixun926-dotcom/dsh-whale-widget-desktop](https://github.com/shixun926-dotcom/dsh-whale-widget-desktop) | DSH 桌面端（Electron）DeepSeek 余额小鲸鱼挂件二创整理版｜非原创，仅供非商业使用 |
| 桌宠 | [wangzhanchao883/dsh-no-long-sit](https://github.com/wangzhanchao883/dsh-no-long-sit) | DeepSeek Harness cat desktop pet — its first job is a sit/water reminder. 猫猫桌宠：先当久坐/喝水提醒用（可拖动、四态循环动画、真实案例、总结评价… |
| 桌宠 | [xingheyewang-1/dsh-whale-rod-cursor](https://github.com/xingheyewang-1/dsh-whale-rod-cursor) | 🎣 鱼竿鲸鱼娘光标 —— DSH Web 的鱼竿光标：弹性绳吊着 Q 版鲸鱼娘，随鼠标甩飞/回弹，悬停变色，甩猛了尖叫，停下演「钓鱼佬又空军了」小剧场。A fishing-rod cursor companion for… |
| 桌宠 | [yukitakasama/better-deepseek-harness-codex](https://github.com/yukitakasama/better-deepseek-harness-codex) | 更好的 deepseek harness（codex 风格）：面向 Coding 用户的 DSH 整合包 —— Codex 风格界面、代码审查、思考强度滑块、费用计量与桌宠（基座 DSH 0.2.0-rc.2） |
| 导航 | [DobyChao/dsh-workspace-enhancement](https://github.com/DobyChao/dsh-workspace-enhancement) | DeepSeek Harness plugin: local and remote (SSH) workspaces in one place. Remote execution uses a single SSH co… |
| 导航 | [Luck9Star/dsh-gateway-provider](https://github.com/Luck9Star/dsh-gateway-provider) | Generic LLM gateway provider plugin for DeepSeek Harness: newapi / LiteLLM / Higress / any OpenAI-compatible g… |
| 导航 | [dingyiliao/dsh-bundle-pdf](https://github.com/dingyiliao/dsh-bundle-pdf) | PDF reader, annotations, OCR, translation and navigation bundle for DeepSeek Harness |
| 导航 | [drscrewdriver/dsh-arrowkey-nav](https://github.com/drscrewdriver/dsh-arrowkey-nav) |  |
| 导航 | [zcr-133/dsh-follow-edits](https://github.com/zcr-133/dsh-follow-edits) | Cline-style follow-along for DeepSeek Harness: open the file the agent just changed in the right Sidebar, jump… |
| 提示词 | [121212165/dsh-plugin-ide-hub](https://github.com/121212165/dsh-plugin-ide-hub) | dsh plugin: unified manager across coding IDEs (Trae/Qoder/ZCode/CatPaw/Codex/Claude Code/OpenCode/dsh) — sess… |
| 提示词 | [AlexPeng07/dsh-custom-plugin](https://github.com/AlexPeng07/dsh-custom-plugin) | dsh-custom-plugin是一个为 DeepSeek Harness (DSH) 打造的增强插件。提供：背景天气特效/玻璃拟态、时间线轨道、项目文件夹、提示词库、对话导出、Mermaid 图表渲染、引用回复、余额… |
| 提示词 | [DDDMUC/dsh-edit-turn](https://github.com/DDDMUC/dsh-edit-turn) | Edit any user turn in DeepSeek Harness and re-run it: an inline editor rolls the conversation back through the… |
| 提示词 | [HuanLinOTO/dsh-plugin-input-history](https://github.com/HuanLinOTO/dsh-plugin-input-history) | 在 DSH prompt 输入框按上/下方向键切换最近发送过的消息（终端式历史导航），跨会话 localStorage 持久化。 / Terminal-style prompt history navigation fo… |
| 提示词 | [banana770/dsh-werewolf](https://github.com/banana770/dsh-werewolf) | 狼人杀 agent 预设：新建会话选「狼人杀」，会话里的智能体当法官，用子代理扮演其他玩家。零 JS 代码，整个游戏写在 6.8 KB 提示词里。 |
| 提示词 | [joao-paulo-santos/dsh-granular-prompt](https://github.com/joao-paulo-santos/dsh-granular-prompt) | Prompt composition manager for DSH: live census of every system-prompt section with suppress and replace, cust… |
| 提示词 | [keyiadiannao/dsh-queue-merge](https://github.com/keyiadiannao/dsh-queue-merge) | Queue Consolidation for DeepSeek Harness: merge queued follow-up messages into one consolidated formal prompt… |
| 提示词 | [longhao666666/dsh-element-context](https://github.com/longhao666666/dsh-element-context) | DeepSeek Harness 插件：对话中圈选/关联 UI 元素，把选择器、源码位置、盒模型与计算样式注入模型提示词 |
| 提示词 | [miseryrua/dsh-wb-memory](https://github.com/miseryrua/dsh-wb-memory) | 给 DSH 里的 Agent 一份跨会话长期记忆：真值源是工作区里的纯 Markdown，无向量库、无外部服务、零运行时依赖；每回合按预算分层注入 systemPrompt，后台自动流水 → 提炼 → 整理 → 治理。 |
| 提示词 | [sskkde/dsh-oh-my-agent](https://github.com/sskkde/dsh-oh-my-agent) | oh-my-openagent (OmO) core capabilities ported as a DeepSeek Harness plugin: ultrawork, role delegation, rules… |
| 会话管理 | [121212165/dsh-plugin-html-report](https://github.com/121212165/dsh-plugin-html-report) | dsh plugin: render session transcripts into self-contained HTML reports (/report latest/prefix/all) |
| 会话管理 | [9931666/dsh-plugin-roundtable](https://github.com/9931666/dsh-plugin-roundtable) | （roundtable V1.0.0）把一次 DeepSeek Harness 会话，从"你和 AI 一对一聊天"，升级成"你 + 主持人(DeepSeek) + 一圈专家 AI 开圆桌会 |
| 会话管理 | [AlanKhronos/dsh-dispatch-gate](https://github.com/AlanKhronos/dsh-dispatch-gate) | DSH 插件：在工具调用层强制「先委派给其他模型」——未派发的会话无法执行 pwsh/write/edit。⚠️ 本插件会拦截工具调用（这是设计目标）；含举证式放行、行为账本与一键停用开关。 |
| 会话管理 | [Andor-Z/dsh-turn-outline](https://github.com/Andor-Z/dsh-turn-outline) | DSH 轮次轨迹侧边栏插件：按用户轮次折叠会话（输入+工具步骤+输出），一键跳回对话原位；零 AI、只读 / Turn-outline tab for dsh-better-sidebar: fold sessions… |
| 会话管理 | [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) | DeepSeek Harness 插件：对话自动沉淀为知识卡，配可检索知识库 + 知识图谱 + 审核中心；SQLite/纯 Markdown 存储，零第三方依赖。 |
| 会话管理 | [GreenLv/dsh-session-insights](https://github.com/GreenLv/dsh-session-insights) | Local-first, evidence-backed workflow retrospectives for DeepSeek Harness |
| 会话管理 | [HTian-qwq/prts-terrarchive](https://github.com/HTian-qwq/prts-terrarchive) | 为明日方舟的长篇剧情打造的RAG类DSH插件，拥有多种快速检索能力。 |
| 会话管理 | [Hercules-debug/butler-git](https://github.com/Hercules-debug/butler-git) | 把「我改完了」变成可验证的事实:Δ(预期改动)+ P(检测程序)全过才产生 commit。零依赖,只用 node 和 git。 / Turn 'done' into a verifiable fact — a commi… |
| 会话管理 | [HuanLinOTO/dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) | 暴露 run_python/run_node 工具，通过 stdin 执行代码返回 stdout/stderr/exit，含解释器路径配置卡 / Exposes run_python/run_node tools tha… |
| 会话管理 | [HuanLinOTO/dsh-plugin-sleep](https://github.com/HuanLinOTO/dsh-plugin-sleep) | 向模型暴露 sleep 工具，按指定毫秒暂停执行后返回，支持取消/clamp / Exposes a sleep tool that pauses for specified ms then returns, with… |
| 会话管理 | [Iwctwbh/dsh-flowglass](https://github.com/Iwctwbh/dsh-flowglass) | 流镜 Flowglass — DeepSeek Harness session flowgraph，实时可视化消息、工具组、子代理分支与步骤详情。 |
| 会话管理 | [MojtabaFaraji/dsh-plugin-rtl-text](https://github.com/MojtabaFaraji/dsh-plugin-rtl-text) | DeepSeek Harness plugin that fixes RTL/LTR bidi rendering in chat: per-block direction for Persian and Arabic… |
| 会话管理 | [NanGePlus/dsh-sop-capsules](https://github.com/NanGePlus/dsh-sop-capsules) | DeepSeek Harness 插件，提示胶囊：在当前工作区沉淀可复用 SOP / 提示片段，并在会话输入框中一键注入。 |
| 会话管理 | [Nay-1/dsh-session-menu-delete](https://github.com/Nay-1/dsh-session-menu-delete) | DSH 侧栏会话行菜单里的「删除会话」：级联清理子代理、保护 fork 会话 |
| 会话管理 | [Rice00/dsh-tree-view](https://github.com/Rice00/dsh-tree-view) | Tree-view conversation branching for DeepSeek Harness: one sidebar entry, branch and switch versions inside a… |
| 会话管理 | [Schrei5/dsh-plugin-session-project](https://github.com/Schrei5/dsh-plugin-session-project) | DSH sidebar plugin: show each session's project (Workspace) name under its title in the flat session list |
| 会话管理 | [ScreamingMaggot/rcs-context](https://github.com/ScreamingMaggot/rcs-context) | 把长对话的重复计费砍掉一半，并给模型配一名只读调查员：先核实，后动手。面向 DeepSeek Harness 的上下文压缩与外置推理插件（MIT）。 |
| 会话管理 | [Tangcuyu4/dsh-long-memory](https://github.com/Tangcuyu4/dsh-long-memory) | DSH 超长记忆包：跨会话长期记忆 + 长文分块检索 + 聊天记录提取精炼，纯 JS 混合检索零依赖 |
| 会话管理 | [WindAndWood/dsh-chat-manager-wide](https://github.com/WindAndWood/dsh-chat-manager-wide) | DSH Chat Manager Wide — unofficial fork of dsh-chat-manager |
| 会话管理 | [YiHarvest/dsh-failure-capsule](https://github.com/YiHarvest/dsh-failure-capsule) | Local-first failure evidence capsules for DeepSeek Harness sessions |
| 会话管理 | [Zhuang-A/dsh-go-sensei](https://github.com/Zhuang-A/dsh-go-sensei) | dsh-go-sensei —— DeepGo Sensei 围棋复盘教练 DSH（DeepSeek Harness）插件：把围棋 AI 的数学判断（胜率、目差、候选点、变化图）翻译成老师级口头讲解，供自学棋手复盘； 讲… |
| 会话管理 | [anneqaq/dsh-widget](https://github.com/anneqaq/dsh-widget) | DSH 插件：把模型编写的 SVG/HTML 片段渲染成对话中的内联可视化卡片（图表、流程图、时间线、对比表格），沙箱隔离、无网络、无依赖 |
| 会话管理 | [ao882866-ux/dsh-session-archive](https://github.com/ao882866-ux/dsh-session-archive) | DeepSeek Harness plugin: permanently delete archived sessions from the sidebar session row |
| 会话管理 | [ashuai/dsh-s2s](https://github.com/ashuai/dsh-s2s) | Connect AI agent sessions on one machine — a DeepSeek Harness plugin for session-to-session collaboration, wit… |
| 会话管理 | [awol2005ex3/dsh-export-session](https://github.com/awol2005ex3/dsh-export-session) | DeepSeek Harness（`dsh`）插件：把**当前会话的完整内容**一键导出为 **Markdown（`.md`）/ Word（`.docx`）/ PDF（`.pdf`）**。 |
| 会话管理 | [awol2005ex3/dsh-md-table-export](https://github.com/awol2005ex3/dsh-md-table-export) | DeepSeek Harness（`dsh`）插件：把对话内容里的 **Markdown 表格** 一键导出为 **Excel（`.xlsx`）**。 |
| 会话管理 | [better-er/dsh-mobile-drawer](https://github.com/better-er/dsh-mobile-drawer) | 「DSH·手机适配」：窄屏下把侧栏收成悬浮小方块，点会话自动收起，并压掉切会话时的自动聚焦，免得软键盘把页面顶起。纯客户端插件。 |
| 会话管理 | [better-er/dsh-write-create-only](https://github.com/better-er/dsh-write-create-only) | 「DSH·write 仅创建」：write 只允许创建新文件，目标已存在时在执行前直接拒绝并提示改用 edit，全局所有会话生效。纯 host 端插件。 |
| 会话管理 | [choco9527/dsh-product-preview](https://github.com/choco9527/dsh-product-preview) | DSH插件 产物页面 可按照访达分栏的形式显示对话节点中的产物 |
| 会话管理 | [domitor-syh/dsh-rollback](https://github.com/domitor-syh/dsh-rollback) | TRAE-style conversation rollback plugin for DeepSeek Harness |
| 会话管理 | [dongsheng123132/task-passport](https://github.com/dongsheng123132/task-passport) | Open task handoff protocol for DeepSeek Harness, WorkBuddy, Claude Code and Codex — verified state, not chat l… |
| 会话管理 | [dshworks/dsh-crew](https://github.com/dshworks/dsh-crew) | Watch Claude Code and Codex work inside dsh: each gets a real terminal pane in your session's workspace that y… |
| 会话管理 | [ethanrise/dsh-privacy-gateway](https://github.com/ethanrise/dsh-privacy-gateway) | DSH 本地隐私网关：对话发给模型前脱敏个人信息，原文只在本机界面还原显示，并可生成 CSV/XLSX 脱敏副本。 |
| 会话管理 | [flizzywine/dsh-tavern](https://github.com/flizzywine/dsh-tavern) | 基于 DeepSeek Harness（DSH）的 SillyTavern 类文字游戏 Agent，支持候选项生成、对话式人物卡编辑、剧本模式与素材抽取。 |
| 会话管理 | [fuyu2022/dsh-session-dir](https://github.com/fuyu2022/dsh-session-dir) | 简单的工作区会话分组插件 |
| 会话管理 | [invoker-bandit/dsh-history-up](https://github.com/invoker-bandit/dsh-history-up) | 一个 DeepSeek Harness 插件：记录每个会话里你提交过的输入，支持用 <kbd>↑</kbd> 方向键逐条回溯，也可以用 <kbd>/</kbd> 菜单挑一条填进输入框。按会话隔离的 shell 式输入历史… |
| 会话管理 | [jing-hy/dsh-think-zh-expand-eac](https://github.com/jing-hy/dsh-think-zh-expand-eac) | DSH 思考增强插件（EAC 定制版）：强制中文思考与回复 + 界面中文化；已移除全部接管对话渲染器的显示功能，不再与折叠类插件（dsh-auto-collapse / dsh-turn-fold）冲突。Fork of… |
| 会话管理 | [joao-paulo-santos/dsh-wo-github](https://github.com/joao-paulo-santos/dsh-wo-github) | Workspace Overview GitHub tab: About card, README rendered as markdown, and the default-branch commit history… |
| 会话管理 | [joao-paulo-santos/dsh-wo-tmux](https://github.com/joao-paulo-santos/dsh-wo-tmux) | Workspace Overview tmux tab: live/frozen/cold session state, one-click terminal attach through tmux-fridge, fr… |
| 会话管理 | [joao-paulo-santos/dsh-workspace-history](https://github.com/joao-paulo-santos/dsh-workspace-history) | Workspace history: journals every compaction summary to the workspace and adds a History subtab to the Workspa… |
| 会话管理 | [joao-paulo-santos/dsh-workspace-overview](https://github.com/joao-paulo-santos/dsh-workspace-overview) | Workspace overview: a Workspace Overview tab beside Chat with a subtab facade for other plugins, and a GitHub… |
| 会话管理 | [joeseesun/qiaomu-home-dsh](https://github.com/joeseesun/qiaomu-home-dsh) | 乔木 Home：DeepSeek Harness 的会话、待办与专注起点页 / A calm home for conversations, tasks, and focus in DSH. |
| 会话管理 | [lcthe/dsh-hermes-memory](https://github.com/lcthe/dsh-hermes-memory) | DSH-native persistent memory and safe session-aware retrieval plugin |
| 会话管理 | [lemoncat7/dsh-ssh](https://github.com/lemoncat7/dsh-ssh) | SSH sessions, SFTP, terminals, proxies and port forwarding for DeepSeek Harness |
| 会话管理 | [liuyun847/dsh-host-restart](https://github.com/liuyun847/dsh-host-restart) | DSH 宿主插件:给模型一个 restart_dsh 工具,重启 dsh 后自动恢复原会话续跑 (DeepSeek Harness) |
| 会话管理 | [longhao666666/dsh-ask-mode](https://github.com/longhao666666/dsh-ask-mode) | DeepSeek Harness 插件：会话内一键切换咨询模式——只读问答，仅可新建 txt/md/docx 产出 |
| 会话管理 | [longhao666666/dsh-session-delete](https://github.com/longhao666666/dsh-session-delete) | DeepSeek Harness 插件：侧栏一键删除会话（先归档再清理磁盘日志，运行中的会话受保护） |
| 会话管理 | [lpf20200901/dsh-memory-delta](https://github.com/lpf20200901/dsh-memory-delta) | 给 AI 编码助手的跨会话长期记忆：自动注入、只推变化。DSH 插件 + 零依赖 CLI。 |
| 会话管理 | [ltxlong/dsh-session-kit](https://github.com/ltxlong/dsh-session-kit) | 会话管理菜单、归档管理、轮次级删除、重新生成、记忆管理、任务管理、话题导航。Conversation management menu, archive management, round-level deletion,… |
| 会话管理 | [menghuanshiguang/devctl-dsh](https://github.com/menghuanshiguang/devctl-dsh) | devctl 家族 · 从另一台设备用 CLI 控制 DSH 会话 |
| 会话管理 | [mrbeandev/dsh-short-tool-ids](https://github.com/mrbeandev/dsh-short-tool-ids) | DeepSeek Harness plugin that shortens tool-call IDs over 64 characters for OpenAI-compatible Chat Completions… |
| 会话管理 | [mrzhangkris/dsh-session-pruner](https://github.com/mrzhangkris/dsh-session-pruner) | DSH 会话生命周期管理插件：one-shot 子代理自动清理 + 容量保底 + 连带清理 projcache，从源头杜绝缓存膨胀卡顿 |
| 会话管理 | [niliemi/dsh-billing](https://github.com/niliemi/dsh-billing) | DSH plugin: prices tokens with the official model price table, shows the running cost beside the composer cont… |
| 会话管理 | [oliblue-evan/dsh-usage-pill](https://github.com/oliblue-evan/dsh-usage-pill) | DSH 用量与余额：会话用量、按每笔实际发生时刻与模型计价的费用（峰谷/档位）、账户余额；账号登录无需 API Key。 |
| 会话管理 | [pbwheel/dsh-workbuddy-expert](https://github.com/pbwheel/dsh-workbuddy-expert) | 把 WorkBuddy 专家装进 DSH：专家市场一键导入 · 会话选择器随时切换 |
| 会话管理 | [penguin-oo/dsh-bookmarks](https://github.com/penguin-oo/dsh-bookmarks) | Bookmark assistant replies in DeepSeek Harness: per-message bookmarks with notes/tags, a cross-session center,… |
| 会话管理 | [rebron1900/dsh-mnemosyne](https://github.com/rebron1900/dsh-mnemosyne) | Mnemosyne 记忆层在 DeepSeek Harness 中的插件 — 本地优先、SQLite 支持的跨会话记忆。 |
| 会话管理 | [robin421/dsh-html-inspector](https://github.com/robin421/dsh-html-inspector) | Selection mode for DeepSeek Harness: click any element in a local HTML demo, locator auto-written to chat inpu… |
| 会话管理 | [seeseeczl/dsh-sym](https://github.com/seeseeczl/dsh-sym) | 给 DeepSeek Harness 接的共生体（dsh-sym）：实时会话花费（人民币，按厂商/模型与峰谷时段折算）、每轮费用、账户余额、峰谷时段标记，以及把任一回复作为上下文引用的 @ 按钮。名字取自 symbiot… |
| 会话管理 | [shetengteng/dsh-lumina-tarot](https://github.com/shetengteng/dsh-lumina-tarot) | Tarot for DeepSeek Harness. Click the floating card to draw a 78-card spread, then let the chat interpret — th… |
| 会话管理 | [shuiqian520/dsh-session-delete](https://github.com/shuiqian520/dsh-session-delete) | DSH plugin: permanently delete a session from the sidebar menu, and retry a user message or an assistant reply… |
| 会话管理 | [slj-123/dsh-cost-meter](https://github.com/slj-123/dsh-cost-meter) | DeepSeek Harness plugin: shows the real account wallet, the official-price cost of the current session, and wh… |
| 会话管理 | [victorygod/dsh-tavern-fengyue](https://github.com/victorygod/dsh-tavern-fengyue) | 活用工具的酒馆agent，支持ST卡、FY卡直接导入，直接在叙事中调用自定义tool call，告别掉面板、瞎执行逻辑等问题，让模型专注于讲故事 |
| 会话管理 | [vitas/dsh-model-pricing](https://github.com/vitas/dsh-model-pricing) | Model pricing & capability board for DeepSeek Harness: ~7,250 models across 213 providers, honest lowest-liste… |
| 会话管理 | [wesleyel/dsh-plugin-gpt-load](https://github.com/wesleyel/dsh-plugin-gpt-load) | DeepSeek Harness plugin: serve every gpt-load model from one provider group, each model on its own wire protoc… |
| 会话管理 | [wssfk12138/dsh-damage-pulse](https://github.com/wssfk12138/dsh-damage-pulse) | DeepSeek Harness Token 余额监控插件：鲸鱼娘待机/扣费/复苏动画、峰谷计费、连续扣费飘字与会话费用统计。 |
| 会话管理 | [wyq183/dsh-artifact-library](https://github.com/wyq183/dsh-artifact-library) | DSH 产物库 + 本地文件管理器：跨会话产物采集 / AI 精化 / 全文检索，以及基于 Everything 清单索引的文件搜索与目录浏览 |
| 会话管理 | [xiaoyuyu6420/dsh-backup](https://github.com/xiaoyuyu6420/dsh-backup) | 一条命令备份/恢复 DeepSeek Harness（dsh）的全部数据：升级快照、会话日志体检修复、迁移预检、救援通道、凭据脱敏、GitHub 同步。 One command to back up & restore… |
| 记忆 | [Du010902/dsh-knowledgenet-plugin](https://github.com/Du010902/dsh-knowledgenet-plugin) |  |
| 记忆 | [FanetheDivine/dsh-plugin-om](https://github.com/FanetheDivine/dsh-plugin-om) | DSH插件，以Observational Memory方式管理上下文 |
| 记忆 | [FeC3-pearlite/bearing-notes](https://github.com/FeC3-pearlite/bearing-notes) | DeepSeek Harness 文献笔记插件：笔记汇总到一个 Word，右侧栏调用模型审阅并提示相关知识（轴承钢滚动接触疲劳） |
| 记忆 | [Grivn/mnemon-memory-agent](https://github.com/Grivn/mnemon-memory-agent) | Long-term memory for AI agents on Jev. Keep raw records, judge them with a fast System 1 model and answer from… |
| 记忆 | [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | 你的AI学习搭档：定路线、讲知识、做项目，边学边做，学透一门科目 |
| 记忆 | [Scorp1o117/dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) | Agent memory for DeepSeek Harness / DeepSeek Harness 记忆插件 |
| 记忆 | [ZYAONS/dsh-plugin-mascot](https://github.com/ZYAONS/dsh-plugin-mascot) | DeepSeek Harness mascot plugin - a clickable character sprite (Arknights' Closure / BanG Dream!'s Sengoku Yuno… |
| 记忆 | [ZekaiShi/evo-subagent](https://github.com/ZekaiShi/evo-subagent) | Unified DeepSeek Harness plugin: role-based subagent routing + per-agent evolution (prefercmd/memory as knowle… |
| 记忆 | [better-er/dsh-cache-billing](https://github.com/better-er/dsh-cache-billing) | 「DSH·缓存账单」：在上下文圆环弹层里实时算账，缓存命中、未命中与输出各带 token 与金额，峰谷自动计价，第三方中转照常记账。 |
| 记忆 | [hongweifei/dsh-memory](https://github.com/hongweifei/dsh-memory) |  |
| 记忆 | [jackyytche/dsh-hindsight-memory](https://github.com/jackyytche/dsh-hindsight-memory) | Hindsight long-term memory for DeepSeek Harness |
| 记忆 | [kovey/dsh-memory](https://github.com/kovey/dsh-memory) | Layered memory plugin for DeepSeek Harness: strictly separated project/global memory, host-driven recall befor… |
| 记忆 | [linner1224/dsh-video-coursemap](https://github.com/linner1224/dsh-video-coursemap) | 视频课程知识地图 Agent（DeepSeek Harness 插件） |
| 记忆 | [liuyuhao1122/dsh-hermes-memory](https://github.com/liuyuhao1122/dsh-hermes-memory) | Lightweight layered memory plugin for DeepSeek Harness with automatic distillation and compaction. |
| 记忆 | [memories-coder/DSH-plugin-android-apk](https://github.com/memories-coder/DSH-plugin-android-apk) | 用DSH帮你构建apk(Use dsh to help you build an APK) |
| 记忆 | [sens-io/memobranch](https://github.com/sens-io/memobranch) | Git-native, auditable long-term memory for AI agents |
| 记忆 | [win10ogod/dsh-knowledge-work](https://github.com/win10ogod/dsh-knowledge-work) | Persistent knowledge-work Agent workflows, evidence capture, review and reports for DSH |
| 记忆 | [yindf/taskfold](https://github.com/yindf/taskfold) | Context folding for DeepSeek Harness (DSH): wrap work in named tasks, fold finished spans into short summaries… |
| 记忆 | [ztlovelsw/dsh-model-profile](https://github.com/ztlovelsw/dsh-model-profile) | 手动或自动配置模型思考强度、上下文窗口、最大输出token |
| 记忆 | ~~[zzdhsxk/dsh-recollect](https://github.com/zzdhsxk/dsh-recollect)~~（已失效） | dsh 记忆 / 用户画像 / 按需召回插件：常驻极小画像、其余按需检索、写入过闸门、可镜像进 Obsidian |
| 移动端 | [GooDAnDReaDY/dsh-russian-lang](https://github.com/GooDAnDReaDY/dsh-russian-lang) | 100% русская локализация и Smart UX для DeepSeek Harness (DSH v0.1.7+): 7574 ключа (ядро + 59 плагинов), живые… |
| 移动端 | [HuanLinOTO/dsh-plugin-android-use](https://github.com/HuanLinOTO/dsh-plugin-android-use) | 让模型通过 adb 操作安卓手机的 DSH 插件（截图、UI 树、点击、滑动、输入文本、按键、打开应用） / DSH plugin exposing adb-based tools that let the model… |
| 移动端 | [Shadid516/dsh-off-peak-hours](https://github.com/Shadid516/dsh-off-peak-hours) | DeepSeek Harness (dsh) plugin: an ambient pill under the composer showing whether your selected DeepSeek or z.… |
| 移动端 | [datit309/supergraph](https://github.com/datit309/supergraph) | Engineering workflow system for AI coding agents — mandatory planning, TDD, verification, review, and intellig… |
| 移动端 | [kyle123740/dsh-zcode-cli-proxy](https://github.com/kyle123740/dsh-zcode-cli-proxy) | dsh-zcode cli反代 —— 把 ZCode CLI（客户端 agent）接入 DeepSeek Harness：app-server 常驻通道、Start Plan 额度直连、真流式、图片输入、工具委派 |
| 移动端 | [wlxyxykj/dsh-phone-remote](https://github.com/wlxyxykj/dsh-phone-remote) |  |
| 移动端 | [xiazhicheng/dsh-remote-retry-llm-plugin](https://github.com/xiazhicheng/dsh-remote-retry-llm-plugin) | dsh 插件，主要解决 remote 开发和 LLM 无限重试 |
| 移动端 | [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote) | DSH 极简风远程移动端：只把「指令」和「回复」送到手机，隐藏执行步骤。 |
| 桌面壳 | [Mvyvn/dsh-desktop-notify](https://github.com/Mvyvn/dsh-desktop-notify) |  |
| 桌面壳 | [cherrchen/dsh-plugin-git](https://github.com/cherrchen/dsh-plugin-git) | DSH Git 仓库服务与 Client UI 插件，依赖 Details Host；DeepSeek Harness Desktop 预装。 / DSH Git repository service and clien… |
| 桌面壳 | [corrinehu/dsh-workbuddy-connect](https://github.com/corrinehu/dsh-workbuddy-connect) | 将 WorkBuddy 桌面 App 包含的模型自动接入 DeepSeek Harness，零配置使用。Bring the models in the WorkBuddy desktop app into DeepSee… |
| 桌面壳 | [songshuhuoban/dsh-environment-tray](https://github.com/songshuhuoban/dsh-environment-tray) |  |
| 终端 | [btsd321/dsh-oh-my-terminal](https://github.com/btsd321/dsh-oh-my-terminal) | A bottom terminal panel plugin for DSH GUI. Supports Windows ConPTY and POSIX openpty with no local compilatio… |
| 终端 | [whiteS18/dsh-terminal-button](https://github.com/whiteS18/dsh-terminal-button) | Embedded terminal plugin for DeepSeek Harness. |
| 终端 | [yannicksong0106/dsh-550c-boot](https://github.com/yannicksong0106/dsh-550c-boot) | 550C 开机动画 for DeepSeek Harness — 首帧由宿主半边注入，DSH 的 Loading 卡片不露脸；桌面原生标题栏按钮收编成终端配色 / 550C boot splash plugin for… |
| 工作台 | [Asheblog/dsh-ollama-cloud](https://github.com/Asheblog/dsh-ollama-cloud) | Ollama Cloud provider for DeepSeek Harness: one-click setup with per-model reasoning-effort control. 一键配置 Olla… |
| 工作台 | [CJYLZS/dsh-remote-development](https://github.com/CJYLZS/dsh-remote-development) | Remote development for DeepSeek Harness: pick a remote workspace over SSH and let the agent work on it with th… |
| 工作台 | [FIZMIE/dsh-restart-button](https://github.com/FIZMIE/dsh-restart-button) | One-click restart for the DeepSeek Harness desktop app: a sidebar button plus an agent-callable restart route. |
| 工作台 | [GooDAnDReaDY/dsh-server-monitor](https://github.com/GooDAnDReaDY/dsh-server-monitor) | SSH server monitor and terminal sidebar for DeepSeek Harness |
| 工作台 | [HandsYe/dsh-remote-status](https://github.com/HandsYe/dsh-remote-status) | DeepSeek Harness 插件：侧边栏底部本地/远程状态芯片 + 远程镜像工作区标题自动标记（目录 ⇄ 机器名） |
| 工作台 | [HarrisXiu/dsh-plugin-finder](https://github.com/HarrisXiu/dsh-plugin-finder) | DSH（DeepSeek Harness）插件发现工具：自动在 GitHub 与 npm 上检索社区插件，给出每个插件的 npm 包名与 GitHub 仓库地址，并内置一份可安装的推荐清单。装上后可在侧边栏「插件发现」页… |
| 工作台 | [HuanLinOTO/dsh-plugin-better-plan](https://github.com/HuanLinOTO/dsh-plugin-better-plan) | better-plan: DSH 计划/待办侧边栏插件 / DSH plan/todo sidebar plugin |
| 工作台 | [Tabbyaccessorial446/dsh-plugin-canvas](https://github.com/Tabbyaccessorial446/dsh-plugin-canvas) | Render HTML design prototypes directly in DeepSeek Harness with a canvas tab for visual review, annotation, an… |
| 工作台 | [Yurzi/dsh-pdf-mineru](https://github.com/Yurzi/dsh-pdf-mineru) | Provider-independent DSH PDF reading tool powered by MinerU. |
| 工作台 | [aa2246740/dsh-model-fusion](https://github.com/aa2246740/dsh-model-fusion) | Fusion for DeepSeek Harness: a frontier Lead plans and reviews, a much cheaper Sidekick writes the code — fron… |
| 工作台 | [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) | Agent-first DeepSeek Harness plugin intelligence: verify existing plugins, identify missing capabilities, and… |
| 工作台 | [drscrewdriver/dsh-brief-sidebar](https://github.com/drscrewdriver/dsh-brief-sidebar) |  |
| 工作台 | [drscrewdriver/dsh-pptx-sidebar](https://github.com/drscrewdriver/dsh-pptx-sidebar) | DSH plugin: read .pptx decks in the sidebar — slides in deck order, bullets, speaker notes, inline pictures. R… |
| 工作台 | [dsh-wsl-workspace-maintainers/dsh-wsl-workspace](https://github.com/dsh-wsl-workspace-maintainers/dsh-wsl-workspace) | WSL workspace support for DeepSeek Harness——无缝的 WSL 工作区使用体验，无需在 WSL 之中再安装一个dsh，安装该插件后在 GUI 里直接添加 WSL 工作区即可。WSL… |
| 工作台 | [evlon/dsh-codebuddy-models](https://github.com/evlon/dsh-codebuddy-models) | 把本机已登录的 CodeBuddy / WorkBuddy（腾讯代码助手） 订阅作为 dsh（DeepSeek Harness） 的原生 provider 接入，启用后 CodeBuddy 模型会直接出现在 dsh 的模… |
| 工作台 | [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) | Remote-work assistant for DeepSeek Harness (DSH): connect SSH (key or password), pick a remote workspace, oper… |
| 工作台 | [homefortwayne245/novel-writer](https://github.com/homefortwayne245/novel-writer) | Write, manage, and refine full-length novels with a coordinated 6-agent AI writing studio inside DeepSeek Harn… |
| 工作台 | [liweidong1722/dsh-work-list](https://github.com/liweidong1722/dsh-work-list) | deepseek harness工作台 |
| 工作台 | [ninglovegithub/dsh-workspace-combiner](https://github.com/ninglovegithub/dsh-workspace-combiner) |  |
| 工作台 | [nishuoyang/dsh-workbench-ecs](https://github.com/nishuoyang/dsh-workbench-ecs) | Alibaba Cloud Workbench CLI plugin — lets DeepSeek Harness's Agent directly control remote ECS instances. |
| 工作台 | [penguin-oo/dsh-delegate-router](https://github.com/penguin-oo/dsh-delegate-router) | Automatic Flash/Pro routing for DeepSeek Harness subagent calls: light tasks go cheap, heavy tasks stay strong… |
| 工作台 | [riffkit/dsh-plugin](https://github.com/riffkit/dsh-plugin) | Riffkit as an installable DSH bundle — riff a winning short video into your own, from your DeepSeek Harness ag… |
| 工作台 | [tearslee/dsh-workbuddy2api](https://github.com/tearslee/dsh-workbuddy2api) | DeepSeek Harness (dsh) plugin: supervise a workbuddy2api gateway process and auto-register its models as an LL… |
| 工作台 | [zhuoxiaoshuai/dsh-database](https://github.com/zhuoxiaoshuai/dsh-database) | MySQL, Oracle, Redis, and Kafka workbench for DeepSeek Harness, with a shared execution path for humans and th… |
| 文件引用 | [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) | Mixture of Agents (MoA) plugin for DeepSeek Harness with /moa slash command, file workspaces, and Live Canvas… |
| 文件引用 | [Tangcuyu4/dsh-zakou-pack](https://github.com/Tangcuyu4/dsh-zakou-pack) | DSH 杂口语言包：傲娇暴躁雌小鬼人格包，三层方言引擎（换骨架而非塞词）+ 脾气系统 + 斗嘴迎战 + 文件静默处理 |
| 文件引用 | [aiyacharley/dsh-at-sider](https://github.com/aiyacharley/dsh-at-sider) | 给原生侧边栏文件树补上「@ 引用 · 修改时间 · 大小 · 排序 · 快速定位」：右侧栏仍是原生标签页，每一行多了紧跟文件名的 @文件 引用按钮，行尾多了 大小 / 修改时间 两列（宽度自适应、可排序）， 页头多了 全… |
| 文件引用 | [better-er/dsh-remote-file-system](https://github.com/better-er/dsh-remote-file-system) | 「DSH·远程文件系统」：给模型提供 read_remote、write_remote、edit_remote 三个工具，经 ssh 读写远程主机文件；write_remote 只允许新建。 |
| 文件引用 | [darrien1998/dsh-ditto](https://github.com/darrien1998/dsh-ditto) | AI is great at doing one file. Ditto is for doing the same thing to 30 files without babysitting all 30. Revie… |
| 文件引用 | [huguangyu666/dsh-plugin-better-folders](https://github.com/huguangyu666/dsh-plugin-better-folders) | DeepSeek Harness 插件：更好的 DSH 文件夹 —— 自动整理工作区，把同一上级目录下的工作区汇合成可折叠的文件夹节点（复用内置「按工作区树」视图，不覆盖官方 UI）。 |
| 文件引用 | [left0ver/dsh-file-review](https://github.com/left0ver/dsh-file-review) | dsh插件 - 立刻审查agent对文件的修改，查看diff，支持在dsh-better-sidebar中使用。a dsh plugin - review files that an agent just changed… |
| 文件引用 | [qydhlhz/dsh-myagent](https://github.com/qydhlhz/dsh-myagent) | MYAGENT.UI — a better workspace and file-tree system for dsh (DeepSeek Harness). |
| 文件引用 | [vianvio/dsh-plugin-drop-path](https://github.com/vianvio/dsh-plugin-drop-path) | DSH 客户端插件：把一个文件夹拖进 DSH，输入框里出现的是它的本机绝对路径（引用块），而不是一条传不上去的附件。 |
| 文件引用 | [yh4922/dsh-workspace](https://github.com/yh4922/dsh-workspace) | A remote workspace plugin for DeepSeek Harness (DSH). It manages SSH hosts inside DSH, opens remote terminals,… |
| 余额/用量 | [Ayelsh/dsh-zhipu-plan](https://github.com/Ayelsh/dsh-zhipu-plan) | A DeepSeek Harness plugin: Zhipu coding-plan sign-in, quota and usage panel. |
| 余额/用量 | [Jovan1666/dsh-commandcode-quota](https://github.com/Jovan1666/dsh-commandcode-quota) | Command Code plan quota in your DeepSeek Harness (dsh) sidebar: 5-hour, weekly and monthly credit windows with… |
| 余额/用量 | [Mgeeeeee/dsh-ui-personalization](https://github.com/Mgeeeeee/dsh-ui-personalization) | Sidebar identity row and client UI tweaks for DeepSeek Harness: your own avatar, nickname and account balance |
| 余额/用量 | [Ushio155/dsh-composer-balance](https://github.com/Ushio155/dsh-composer-balance) | 把 DeepSeek 余额常驻在 DSH 输入框工具行：接替已停更的 kte66/dsh-balance，修复密钥落盘、无来源策略与遮蔽内置 UI。 |
| 余额/用量 | [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) | Zero-cost, zero-hassle toolkit for DeepSeek Harness (DSH): one-click free model setup (Zhipu GLM-4-Flash + Ope… |
| 余额/用量 | [better-er/dsh-live-token-stats](https://github.com/better-er/dsh-live-token-stats) | 「DSH·实时 token 统计」：基于 DeepSeek 官方 BPE 分词表，在输入框下方实时渲染 token 状态带，显示流式 TPS、输出 token 与首字延迟。 |
| 余额/用量 | [boxiaolanya2008/tokensqueezer](https://github.com/boxiaolanya2008/tokensqueezer) | Cuts a DSH agent's token use on its own output: caps generation before the call, folds verbose answers and rea… |
| 余额/用量 | [mo-n/dsh-provider-qoder](https://github.com/mo-n/dsh-provider-qoder) | DSH provider plugin for Qoder subscriptions. |
| 余额/用量 | [penguin-oo/dsh-quota-hub](https://github.com/penguin-oo/dsh-quota-hub) |  |
| 余额/用量 | [stefanohe/dsh-show-balance](https://github.com/stefanohe/dsh-show-balance) | Show account balance directly in the status bar. |
| 余额/用量 | [verneuil/dsh-opencode-go-usage](https://github.com/verneuil/dsh-opencode-go-usage) | DeepSeek Harness插件，一个极简的浮窗同时显示 DeepSeek 官方余额与 OpenCode Go 的 5h/w/m 用量 |
| 余额/用量 | [xiong529/dsh-max-thinking-mode](https://github.com/xiong529/dsh-max-thinking-mode) | 让 DeepSeek 变成一只疯狂偷吃用户 token 的大肥鱼 🐟 —— 最大思考模式（Max Thinking）for DeepSeek Harness：面对没有现成答案的问题，多候选推演 × 证据优先 × 六视角审… |
| 外观/主题 | [Ayase34/wallpaper-plugin](https://github.com/Ayase34/wallpaper-plugin) | DeepSeek Harness的壁纸管理插件 |
| 外观/主题 | [Britneycode/dsh-update-center](https://github.com/Britneycode/dsh-update-center) | dsh (DeepSeek Harness) 更新中心与插件市场：自托管 plugins.json 注册表（GitHub dsh-plugin 主题自动聚合 + npm 包名映射秒级安装），一键安装/更新/卸载/禁用插件… |
| 外观/主题 | [FeatherHunter/dsh-opencode-palette](https://github.com/FeatherHunter/dsh-opencode-palette) | 🎨 为长时间编程而生：38 款 opencode 护眼配色，一键换上 DSH / 38 eye-friendly opencode themes for DeepSeek Harness, one click |
| 外观/主题 | [LX-HMKK/DSH-appearance](https://github.com/LX-HMKK/DSH-appearance) | 轻量的 DeepSeek Harness 字体与主题插件：中英文字体分开选，含 One Dark Pro / Dracula / Nord / GitHub / Catppuccin 五套官方色板预设 |
| 外观/主题 | [Physicolor/dsh-widgets](https://github.com/Physicolor/dsh-widgets) | A modular widget system for DeepSeek Harness — reusable widgets, adaptive layouts, and a unified design gramma… |
| 外观/主题 | [Wedomizing/Dsh_genshin_nicole_skin](https://github.com/Wedomizing/Dsh_genshin_nicole_skin) | 来自世界之外的智慧所诞生的进步，每天都比过去一百年的积累更多 |
| 外观/主题 | [asymptotee/dsh-terminal](https://github.com/asymptotee/dsh-terminal) | Claude Code-style terminal UI plugin for DeepSeek Harness |
| 外观/主题 | [cdxDNRF/dsh-wishadel-theme](https://github.com/cdxDNRF/dsh-wishadel-theme) | dsh主题维什戴尔风格 |
| 外观/主题 | [cherrchen/dsh-theme-studio](https://github.com/cherrchen/dsh-theme-studio) | 可移植的 DSH/Cordis 主题插件：内置配色浏览、预览、应用与持久化；DeepSeek Harness Desktop 预装。 / Portable DSH/Cordis theme overlay plugin… |
| 外观/主题 | [dhicoc/dsh-theme-mineradio](https://github.com/dhicoc/dsh-theme-mineradio) | A cinematic visual-radio glass theme for DeepSeek Harness (DSH) Desktop — port of the Mineradio music player's… |
| 外观/主题 | [keyiadiannao/dsh-power-button](https://github.com/keyiadiannao/dsh-power-button) | Self-contained power control for DeepSeek Harness: sidebar power button with upward restart/shutdown menu, Win… |
| 外观/主题 | [kingOfSoySauce/dsh-skin-market](https://github.com/kingOfSoySauce/dsh-skin-market) | DeepSeek Harness skin market 皮肤市场 已收录200+DSH 皮肤 完善评分系统加人工审核，有便捷的社区收录入口；有在线页面方便在线浏览，也有插件方便管理本地皮肤 |
| 外观/主题 | [levodoubt/dsh-longtext-input](https://github.com/levodoubt/dsh-longtext-input) | DeepSeek Harness 长文本输入插件：把超长正文写进工作区 .dsh-longtext/ 下的 md 文件，输入框只留一个 @ 引用，保持聊天界面简洁。支持 Wallpaper Engine 毛玻璃。 |
| 外观/主题 | [lx000166/dsh-aqua-glass](https://github.com/lx000166/dsh-aqua-glass) | DSH（DeepSeek Harness）液态玻璃主题插件：三张悬浮玻璃卡 + 流体背景 + 逐表面玻璃化 |
## 全分类速览

DSH 生态目前大致按 22 个官方分类组织。下表是导航地图，括号内为每类的代表插件（部分来自已采集数据）：

| 分类 | 关注点 | 代表插件 |
|------|--------|----------|
| 🧭 AGI 架构探索 | 白箱/世界模型 | [FuRongJun-1999/dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) |
| 🎨 UI 增强 | 界面/布局/交互/中文 | [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) · [dawnliming/dsh-chinese-mode](https://github.com/dawnliming/dsh-chinese-mode) · [zjl1989-li/dsh-harness-zh-cn](https://github.com/zjl1989-li/dsh-harness-zh-cn) · [nishuoyang/dsh-wallpaper-bg](https://github.com/nishuoyang/dsh-wallpaper-bg) · [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) · [WLV-ZEDD/dsh-btw](https://github.com/WLV-ZEDD/dsh-btw) · [exoticknight/dsh-theme-eink-retro](https://github.com/exoticknight/dsh-theme-eink-retro) · [citisen/dsh-font](https://github.com/citisen/dsh-font) · [fangwen9527/dsh-composer-ux](https://github.com/fangwen9527/dsh-composer-ux) · [LyaxZ/dsh-fonttune](https://github.com/LyaxZ/dsh-fonttune) · [BOWLUNA/dsh-custom-mode](https://github.com/BOWLUNA/dsh-custom-mode) · [KylinQ01/dsh-startup-animation](https://github.com/KylinQ01/dsh-startup-animation)  · [michengai/dsh-codex-ui](https://github.com/michengai/dsh-codex-ui) · [noob-stupid/dsh-plugin-gating-hub](https://github.com/noob-stupid/dsh-plugin-gating-hub) · [lamost423/dsh-maze](https://github.com/lamost423/dsh-maze) · [dely0/dsh-personal-workbench](https://github.com/dely0/dsh-personal-workbench) · [vncntvx/dsh-zotero](https://github.com/vncntvx/dsh-zotero) · [celebrate-w/dsh-topic-trail](https://github.com/celebrate-w/dsh-topic-trail) · [eastmg/dsh-gacha-calendar](https://github.com/eastmg/dsh-gacha-calendar) · [windypro-rourou/dsh-code-studio](https://github.com/windypro-rourou/dsh-code-studio) · [namesmt/dsh-home-hosted](https://github.com/namesmt/dsh-home-hosted) |
| 💰 用量与计费 | 余额/成本 · [weibaohui/dsh-sync](https://github.com/weibaohui/dsh-sync) · [weibaohui/context-razor](https://github.com/weibaohui/context-razor) · [1420079678-ctrl/agent-body](https://github.com/1420079678-ctrl/agent-body) · [weibaohui/dsh-fireworks](https://github.com/weibaohui/dsh-fireworks) · [AGImentu/dsh-cost-stats](https://github.com/AGImentu/dsh-cost-stats) · [webkubor/dsh-llm-hub](https://github.com/webkubor/dsh-llm-hub) · [Ychris12138/dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) · [Aa728848/dsh-chatgpt-subscription](https://github.com/Aa728848/dsh-chatgpt-subscription) · [EphoReal/Tokan-dsh-token-analytics](https://github.com/EphoReal/Tokan-dsh-token-analytics) · [orrinzeng/dsh-cursor-subscription](https://github.com/orrinzeng/dsh-cursor-subscription) · [wkscc310/dsh-client-ui-cpa-quota](https://github.com/wkscc310/dsh-client-ui-cpa-quota) · [Ayelsh/dsh-zhipu-plan](https://github.com/Ayelsh/dsh-zhipu-plan) · [Jovan1666/dsh-commandcode-quota](https://github.com/Jovan1666/dsh-commandcode-quota) · [Mgeeeeee/dsh-ui-personalization](https://github.com/Mgeeeeee/dsh-ui-personalization) · [Ushio155/dsh-composer-balance](https://github.com/Ushio155/dsh-composer-balance) · [ai-yukin/dsh-0-tools](https://github.com/ai-yukin/dsh-0-tools) · [better-er/dsh-live-token-stats](https://github.com/better-er/dsh-live-token-stats) · [boxiaolanya2008/tokensqueezer](https://github.com/boxiaolanya2008/tokensqueezer) · [mo-n/dsh-provider-qoder](https://github.com/mo-n/dsh-provider-qoder) · [penguin-oo/dsh-quota-hub](https://github.com/penguin-oo/dsh-quota-hub) · [stefanohe/dsh-show-balance](https://github.com/stefanohe/dsh-show-balance) · [verneuil/dsh-opencode-go-usage](https://github.com/verneuil/dsh-opencode-go-usage) · [xiong529/dsh-max-thinking-mode](https://github.com/xiong529/dsh-max-thinking-mode) | [GeekRicardo/dsh-balance](https://github.com/GeekRicardo/dsh-balance) · [kenz1117/dsh-ui-usage-billing](https://github.com/kenz1117/dsh-ui-usage-billing) · [olimc2016/dsh-token-meter-panel](https://github.com/olimc2016/dsh-token-meter-panel) · [featherhunter/dsh-mattpocock-skills-deck](https://github.com/featherhunter/dsh-mattpocock-skills-deck) · [162568316/dsh-tokenrhythm-bill](https://github.com/162568316/dsh-tokenrhythm-bill) |
| 🎭 主题与外观 | 皮肤/壁纸 · [weibaohui/dsh-settings-ui](https://github.com/weibaohui/dsh-settings-ui) · [Andersen216/dsh-whale-girl-live2d](https://github.com/Andersen216/dsh-whale-girl-live2d) · [chen731215-dev/dsh-tavern-v2](https://github.com/chen731215-dev/dsh-tavern-v2) · [LeoLee0097/dsh-desktop-acrylic](https://github.com/LeoLee0097/dsh-desktop-acrylic) · [EphoReal/my-skin-for-DeepSeek-Harness](https://github.com/EphoReal/my-skin-for-DeepSeek-Harness) · [Ayase34/wallpaper-plugin](https://github.com/Ayase34/wallpaper-plugin) · [Britneycode/dsh-update-center](https://github.com/Britneycode/dsh-update-center) · [FeatherHunter/dsh-opencode-palette](https://github.com/FeatherHunter/dsh-opencode-palette) · [LX-HMKK/DSH-appearance](https://github.com/LX-HMKK/DSH-appearance) · [Physicolor/dsh-widgets](https://github.com/Physicolor/dsh-widgets) · [Wedomizing/Dsh_genshin_nicole_skin](https://github.com/Wedomizing/Dsh_genshin_nicole_skin) · [asymptotee/dsh-terminal](https://github.com/asymptotee/dsh-terminal) · [cdxDNRF/dsh-wishadel-theme](https://github.com/cdxDNRF/dsh-wishadel-theme) · [cherrchen/dsh-theme-studio](https://github.com/cherrchen/dsh-theme-studio) · [dhicoc/dsh-theme-mineradio](https://github.com/dhicoc/dsh-theme-mineradio) · [keyiadiannao/dsh-power-button](https://github.com/keyiadiannao/dsh-power-button) · [kingOfSoySauce/dsh-skin-market](https://github.com/kingOfSoySauce/dsh-skin-market) · [levodoubt/dsh-longtext-input](https://github.com/levodoubt/dsh-longtext-input) · [lx000166/dsh-aqua-glass](https://github.com/lx000166/dsh-aqua-glass) | [EternalNight996/dsh-theme](https://github.com/EternalNight996/dsh-theme) · [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) · [exoticknight/dsh-theme-eink-retro](https://github.com/exoticknight/dsh-theme-eink-retro) · [elysia395/dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine) · [ymh0000123/dsh-theme-endfield](https://github.com/ymh0000123/dsh-theme-endfield) · [niiang/dsh-kimino-theme](https://github.com/niiang/dsh-kimino-theme) · [Nwflower/dsh-claude-style](https://github.com/Nwflower/dsh-claude-style) · [XHR666/dsh-mpkg-wallpaper](https://github.com/XHR666/dsh-mpkg-wallpaper) · [nonamelego/dsh-catppuccin-theme](https://github.com/nonamelego/dsh-catppuccin-theme) · [wenaixi/dsh-ponytail](https://github.com/wenaixi/dsh-ponytail) · [britneycode/dsh-update-center](https://github.com/britneycode/dsh-update-center) · [erbsen16/dsh-client-ui-dracula](https://github.com/erbsen16/dsh-client-ui-dracula) |
| 🔌 模型与账号接入 | 模型/Provider | [franksong2702/dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) · [wss534857356/dsh-plugin-codex](https://github.com/wss534857356/dsh-plugin-codex) · [WNJXYK/dsh-codex-oauth](https://github.com/WNJXYK/dsh-codex-oauth) · [CARVIN94/dsh-router](https://github.com/CARVIN94/dsh-router) · [V1ki/dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) · [WSL043/dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) · [FishBottle7/opencode2dsh](https://github.com/FishBottle7/opencode2dsh) · [GooDAnDReaDY/dsh-clinebot](https://github.com/GooDAnDReaDY/dsh-clinebot) · [GooDAnDReaDY/dsh-model-sync](https://github.com/GooDAnDReaDY/dsh-model-sync) · [Saretheya/dsh-lantern](https://github.com/Saretheya/dsh-lantern) · [lovezi0/dsh-model-extension](https://github.com/lovezi0/dsh-model-extension) · [dingminhua/dsh-connect-workbuddy](https://github.com/dingminhua/dsh-connect-workbuddy) · [GooDAnDReaDY/dsh-subscriptions](https://github.com/GooDAnDReaDY/dsh-subscriptions) · [songoao25/dsh-chatgpt-subscription](https://github.com/songoao25/dsh-chatgpt-subscription) · [masknull/dsh-qoder-connect](https://github.com/masknull/dsh-qoder-connect) · [DLive/dsh-qqbot-community](https://github.com/DLive/dsh-qqbot-community) · [Ztyss/dsh-llm-provider](https://github.com/Ztyss/dsh-llm-provider) · [latte03/dsh-select-quote](https://github.com/latte03/dsh-select-quote)  · [yujunzhixue/dsh-purge](https://github.com/yujunzhixue/dsh-purge) · [v1ki/dsh-plugin-subscriptions](https://github.com/v1ki/dsh-plugin-subscriptions) · [ychris12138/dsh-usage-stats](https://github.com/ychris12138/dsh-usage-stats) · [fishbottle7/opencode2dsh](https://github.com/fishbottle7/opencode2dsh) · [nwflower/dsh-claude-style](https://github.com/nwflower/dsh-claude-style) · [aa728848/dsh-chatgpt-subscription](https://github.com/aa728848/dsh-chatgpt-subscription) · [suntianc/dsh-antigravity-auth](https://github.com/suntianc/dsh-antigravity-auth) · [2768651338/dsh-effort-slider](https://github.com/2768651338/dsh-effort-slider) · [particlelight/dsh-all-usage](https://github.com/particlelight/dsh-all-usage) · [goodandready/dsh-voice](https://github.com/goodandready/dsh-voice) · [goodandready/dsh-key-rotation](https://github.com/goodandready/dsh-key-rotation) · [jerryliu369/agent-web-search](https://github.com/jerryliu369/agent-web-search) · [mokuyoaxis/dsh-iris](https://github.com/mokuyoaxis/dsh-iris) · [wenzetan/dsh-llm-newapi](https://github.com/wenzetan/dsh-llm-newapi) · [goodandready/dsh-clinebot](https://github.com/goodandready/dsh-clinebot) · [daetz-coder/dsh-multi-chat](https://github.com/daetz-coder/dsh-multi-chat) · [2861292267/dsh-official-workbuddy-credit-proxy](https://github.com/2861292267/dsh-official-workbuddy-credit-proxy) · [stardustlc666/dsh-rss](https://github.com/stardustlc666/dsh-rss) · [baroncyrus/dsh-kimi-subscription](https://github.com/baroncyrus/dsh-kimi-subscription) · [ycet/dsh-account-usage](https://github.com/ycet/dsh-account-usage) · [viztor/dsh-opencode-patch](https://github.com/viztor/dsh-opencode-patch) · [viztor/dsh-tinyfish](https://github.com/viztor/dsh-tinyfish) · [lin-dongg/dsh-musage-card](https://github.com/lin-dongg/dsh-musage-card) · [ultmebius/universal-plugin-hub](https://github.com/ultmebius/universal-plugin-hub) · [aitcmhk-web/dsh-bot](https://github.com/aitcmhk-web/dsh-bot) · [movingelated/dsh-localmodels-tokensavior](https://github.com/movingelated/dsh-localmodels-tokensavior) · [functy23/dsh-workbuddy-connect-functy](https://github.com/functy23/dsh-workbuddy-connect-functy) · [miqian-nomad/dsh-browser-playwright-codex](https://github.com/miqian-nomad/dsh-browser-playwright-codex) |
| 🆔 身份与通信 | 账号/IM 接入 | [lanbaolu/dsh-wechat-bridge](https://github.com/lanbaolu/dsh-wechat-bridge) · [ZhuoSir/dsh-chatops](https://github.com/ZhuoSir/dsh-chatops) · [tencent-connect/dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) · [tkwkeven/dsh-lark-all](https://github.com/tkwkeven/dsh-lark-all) · [gcry13067381632-jpg/dsh-qqbot](https://github.com/gcry13067381632-jpg/dsh-qqbot) · [xmanrui/dsh-im](https://github.com/xmanrui/dsh-im) · [HiQ-AI/dingtalk-dsh-assistant](https://github.com/HiQ-AI/dingtalk-dsh-assistant) · [PerryLink/dsh-reach](https://github.com/PerryLink/dsh-reach) · [5havv/dsh-weixin](https://github.com/5havv/dsh-weixin) · [Alphainfix/wechat-clawbot](https://github.com/Alphainfix/wechat-clawbot) · [ArcaneOrion/dsh-model-channel-manager](https://github.com/ArcaneOrion/dsh-model-channel-manager) · [ArtlexYoung/dsh-super-code](https://github.com/ArtlexYoung/dsh-super-code) · [Chatbot-zhou/dsh-task-complete-sound](https://github.com/Chatbot-zhou/dsh-task-complete-sound) · [GeoSyntax/dsh-plugin-time-machine](https://github.com/GeoSyntax/dsh-plugin-time-machine) · [Github-CJX/dsh-tool-imagegen](https://github.com/Github-CJX/dsh-tool-imagegen) · [GooDAnDReaDY/dsh-image-gen](https://github.com/GooDAnDReaDY/dsh-image-gen) · [HaoyanZhang123/dsh-plugin-image-gen](https://github.com/HaoyanZhang123/dsh-plugin-image-gen) · [HuanLinOTO/dsh-plugin-aigc-canvas](https://github.com/HuanLinOTO/dsh-plugin-aigc-canvas) · [HuanLinOTO/dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) · [HuanLinOTO/dsh-plugin-terminal-extension-wait-for](https://github.com/HuanLinOTO/dsh-plugin-terminal-extension-wait-for) · [InkshadeWoods/dsh-tool-visual-primitives](https://github.com/InkshadeWoods/dsh-tool-visual-primitives) · [LQH-A-A-O/dsh-simple-drawing](https://github.com/LQH-A-A-O/dsh-simple-drawing) · [LR611415/visionforge](https://github.com/LR611415/visionforge) · [LisonEvf/dsh-qwen-image](https://github.com/LisonEvf/dsh-qwen-image) · [Lyrissonare/dsh-preset-bridge](https://github.com/Lyrissonare/dsh-preset-bridge) · [Lzhimie/dsh-skin-master](https://github.com/Lzhimie/dsh-skin-master) · [MaRi23333/dsh-serverchan-watchdog](https://github.com/MaRi23333/dsh-serverchan-watchdog) · [MichengAI/dsh-im-connect](https://github.com/MichengAI/dsh-im-connect) · [Paimonshen/dsh-coding-plugin](https://github.com/Paimonshen/dsh-coding-plugin) · [Rice00/dsh-loupe](https://github.com/Rice00/dsh-loupe) · [STARDUSTLC666/dsh-dream](https://github.com/STARDUSTLC666/dsh-dream) · [Thedeergod666/dsh-musage](https://github.com/Thedeergod666/dsh-musage) · [WSL043/dsh-image-viewer](https://github.com/WSL043/dsh-image-viewer) · [XN-H/dsh-ark-image](https://github.com/XN-H/dsh-ark-image) · [Yaaaaaaa233/dsh-plan-and-execute](https://github.com/Yaaaaaaa233/dsh-plan-and-execute) · [YiMlT/dsh-notify-yimit](https://github.com/YiMlT/dsh-notify-yimit) · [Yiheng-guo/dsh-boot-animation-pro](https://github.com/Yiheng-guo/dsh-boot-animation-pro) · [Ylhow06/dsh-agnes-gen](https://github.com/Ylhow06/dsh-agnes-gen) · [alanzhao0128/dsh-image-plugins](https://github.com/alanzhao0128/dsh-image-plugins) · [anze225-max/dsh-mimo-connect](https://github.com/anze225-max/dsh-mimo-connect) · [cbg33695/dsh-screen-reader](https://github.com/cbg33695/dsh-screen-reader) · [cherrchen/dsh-plugin-multi-root-workspace](https://github.com/cherrchen/dsh-plugin-multi-root-workspace) · [corrinehu/dsh-buddy-checkin](https://github.com/corrinehu/dsh-buddy-checkin) · [ethanrise/dsh-model-deploy](https://github.com/ethanrise/dsh-model-deploy) · [evlon/dsh-matrix-agent](https://github.com/evlon/dsh-matrix-agent) · [harde1/dsh-xcodebuild](https://github.com/harde1/dsh-xcodebuild) · [ice5kysl/dsh-file-explorer-kit](https://github.com/ice5kysl/dsh-file-explorer-kit) · [its0din-ai/harness-accountant](https://github.com/its0din-ai/harness-accountant) · [jasen215/dsh-continual-harness](https://github.com/jasen215/dsh-continual-harness) · [kaaaaahn/dsh-vision](https://github.com/kaaaaahn/dsh-vision) · [keyiadiannao/dsh-code-reuse-firewall](https://github.com/keyiadiannao/dsh-code-reuse-firewall) · [keyiadiannao/dsh-delay-tools](https://github.com/keyiadiannao/dsh-delay-tools) · [lifeopsgo/dsh-lark-session-monitor-plugin](https://github.com/lifeopsgo/dsh-lark-session-monitor-plugin) · [liuqingman/dsh-somni](https://github.com/liuqingman/dsh-somni) · [log-li/dsh-peakrate](https://github.com/log-li/dsh-peakrate) · [ly6170/dsh-messager](https://github.com/ly6170/dsh-messager) · [memorax-ai/dsh-harmony](https://github.com/memorax-ai/dsh-harmony) · [mnemon-dev/mnemon](https://github.com/mnemon-dev/mnemon) · [openma-ai/deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) · [phelpsyacht/dshmath-manim](https://github.com/phelpsyacht/dshmath-manim) · [protoctistmoses143/dsh-docs](https://github.com/protoctistmoses143/dsh-docs) · [syyr1987/dsh-linghun](https://github.com/syyr1987/dsh-linghun) · [tarraencompassing61/dsh-lark-bot](https://github.com/tarraencompassing61/dsh-lark-bot) · [tpmoonchefryan/dsh-joi-channel-theme](https://github.com/tpmoonchefryan/dsh-joi-channel-theme) · [universe-st/dsh-game-material-master](https://github.com/universe-st/dsh-game-material-master) · [upcyan/dsh-mimo-extension](https://github.com/upcyan/dsh-mimo-extension) · [windwhiterain/dsh-llm-quota-retry](https://github.com/windwhiterain/dsh-llm-quota-retry) · [wlj521/dsh-ui-tweaks](https://github.com/wlj521/dsh-ui-tweaks) · [xmwengxing/dsh-client-ui-sidebar-perfmon](https://github.com/xmwengxing/dsh-client-ui-sidebar-perfmon) · [yejiming/dsh-museai-tavern](https://github.com/yejiming/dsh-museai-tavern) · [yunxiyang/dsh-stepwise-distill](https://github.com/yunxiyang/dsh-stepwise-distill) · [zhuiyueya/dsh-im-gateway](https://github.com/zhuiyueya/dsh-im-gateway) |
| 💬 会话与消息 | 会话管理 | ~~[urzeye/dsh-outline](https://github.com/urzeye/dsh-outline)~~（已失效） · [PerryLink/dsh-session-pin](https://github.com/PerryLink/dsh-session-pin) · [RyanZeeee/dsh-chattree](https://github.com/RyanZeeee/dsh-chattree) · [kiligzzz/dsh-session-archive](https://github.com/kiligzzz/dsh-session-archive) · [yamingmou/dsh-retrace](https://github.com/yamingmou/dsh-retrace) · [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) · [Renzic-Stone/DSH-EasyRewrite](https://github.com/Renzic-Stone/DSH-EasyRewrite) · [Ultronen/dsh-archived-chats](https://github.com/Ultronen/dsh-archived-chats) · [sluminositys/dsh-nested-followups](https://github.com/sluminositys/dsh-nested-followups) · [DDDMUC/dsh-delete-turn](https://github.com/DDDMUC/dsh-delete-turn) · [birew83538-oss/dsh-chat-thinking-editor](https://github.com/birew83538-oss/dsh-chat-thinking-editor) · [cq-guojia/dsh-session-title-pattern](https://github.com/cq-guojia/dsh-session-title-pattern) · [shengyvself/dsh-autoresume](https://github.com/shengyvself/dsh-autoresume) · [PerryLink/dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) · [mikugui/dsh-session-eater](https://github.com/mikugui/dsh-session-eater) · [PerryLink/dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) · [weibaohui/dsh-tasks](https://github.com/weibaohui/dsh-tasks) · [weibaohui/dsh-smart-title](https://github.com/weibaohui/dsh-smart-title) · [weibaohui/hermes-loop](https://github.com/weibaohui/hermes-loop) · [weibaohui/dsh-flow](https://github.com/weibaohui/dsh-flow) · [weibaohui/dsh-process](https://github.com/weibaohui/dsh-process) · [Lanzgale/dsh-repo-browser](https://github.com/Lanzgale/dsh-repo-browser) · [Menghuan1918/dsh-apollo](https://github.com/Menghuan1918/dsh-apollo) · [Han-Yao94/dsh-session-toolkit](https://github.com/Han-Yao94/dsh-session-toolkit) · [Ryuu-64/dsh-session-tools](https://github.com/Ryuu-64/dsh-session-tools) · [hawkongz/dsh-chat-locator](https://github.com/hawkongz/dsh-chat-locator) · [HuaimaoCy/dsh-codex-chatgpt](https://github.com/HuaimaoCy/dsh-codex-chatgpt) · [Ryuu-64/dsh-find-all](https://github.com/Ryuu-64/dsh-find-all) · [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) · [kahomesl/dsh-client-ui-job-stats](https://github.com/kahomesl/dsh-client-ui-job-stats) · [zqh260619/dsh-dupguard](https://github.com/zqh260619/dsh-dupguard) · [g-yixuan/dsh-sidenote](https://github.com/g-yixuan/dsh-sidenote) · [V-Reason/dsh-task-notify](https://github.com/V-Reason/dsh-task-notify) · [exoticknight/dsh-just-chat](https://github.com/exoticknight/dsh-just-chat) · [jaxzhou/dsh-file-explorer](https://github.com/jaxzhou/dsh-file-explorer) · [121212165/dsh-plugin-html-report](https://github.com/121212165/dsh-plugin-html-report) · [9931666/dsh-plugin-roundtable](https://github.com/9931666/dsh-plugin-roundtable) · [AlanKhronos/dsh-dispatch-gate](https://github.com/AlanKhronos/dsh-dispatch-gate) · [Andor-Z/dsh-turn-outline](https://github.com/Andor-Z/dsh-turn-outline) · [EternalNight996/memory-eternal](https://github.com/EternalNight996/memory-eternal) · [GreenLv/dsh-session-insights](https://github.com/GreenLv/dsh-session-insights) · [HTian-qwq/prts-terrarchive](https://github.com/HTian-qwq/prts-terrarchive) · [Hercules-debug/butler-git](https://github.com/Hercules-debug/butler-git) · [HuanLinOTO/dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) · [HuanLinOTO/dsh-plugin-sleep](https://github.com/HuanLinOTO/dsh-plugin-sleep) · [Iwctwbh/dsh-flowglass](https://github.com/Iwctwbh/dsh-flowglass) · [MojtabaFaraji/dsh-plugin-rtl-text](https://github.com/MojtabaFaraji/dsh-plugin-rtl-text) · [NanGePlus/dsh-sop-capsules](https://github.com/NanGePlus/dsh-sop-capsules) · [Nay-1/dsh-session-menu-delete](https://github.com/Nay-1/dsh-session-menu-delete) · [Rice00/dsh-tree-view](https://github.com/Rice00/dsh-tree-view) · [Schrei5/dsh-plugin-session-project](https://github.com/Schrei5/dsh-plugin-session-project) · [ScreamingMaggot/rcs-context](https://github.com/ScreamingMaggot/rcs-context) · [Tangcuyu4/dsh-long-memory](https://github.com/Tangcuyu4/dsh-long-memory) · [WindAndWood/dsh-chat-manager-wide](https://github.com/WindAndWood/dsh-chat-manager-wide) · [YiHarvest/dsh-failure-capsule](https://github.com/YiHarvest/dsh-failure-capsule) · [Zhuang-A/dsh-go-sensei](https://github.com/Zhuang-A/dsh-go-sensei) · [anneqaq/dsh-widget](https://github.com/anneqaq/dsh-widget) · [ao882866-ux/dsh-session-archive](https://github.com/ao882866-ux/dsh-session-archive) · [ashuai/dsh-s2s](https://github.com/ashuai/dsh-s2s) · [awol2005ex3/dsh-export-session](https://github.com/awol2005ex3/dsh-export-session) · [awol2005ex3/dsh-md-table-export](https://github.com/awol2005ex3/dsh-md-table-export) · [better-er/dsh-mobile-drawer](https://github.com/better-er/dsh-mobile-drawer) · [better-er/dsh-write-create-only](https://github.com/better-er/dsh-write-create-only) · [choco9527/dsh-product-preview](https://github.com/choco9527/dsh-product-preview) · [domitor-syh/dsh-rollback](https://github.com/domitor-syh/dsh-rollback) · [dongsheng123132/task-passport](https://github.com/dongsheng123132/task-passport) · [dshworks/dsh-crew](https://github.com/dshworks/dsh-crew) · [ethanrise/dsh-privacy-gateway](https://github.com/ethanrise/dsh-privacy-gateway) · [flizzywine/dsh-tavern](https://github.com/flizzywine/dsh-tavern) · [fuyu2022/dsh-session-dir](https://github.com/fuyu2022/dsh-session-dir) · [invoker-bandit/dsh-history-up](https://github.com/invoker-bandit/dsh-history-up) · [jing-hy/dsh-think-zh-expand-eac](https://github.com/jing-hy/dsh-think-zh-expand-eac) · [joao-paulo-santos/dsh-wo-github](https://github.com/joao-paulo-santos/dsh-wo-github) · [joao-paulo-santos/dsh-wo-tmux](https://github.com/joao-paulo-santos/dsh-wo-tmux) · [joao-paulo-santos/dsh-workspace-history](https://github.com/joao-paulo-santos/dsh-workspace-history) · [joao-paulo-santos/dsh-workspace-overview](https://github.com/joao-paulo-santos/dsh-workspace-overview) · [joeseesun/qiaomu-home-dsh](https://github.com/joeseesun/qiaomu-home-dsh) · [lcthe/dsh-hermes-memory](https://github.com/lcthe/dsh-hermes-memory) · [lemoncat7/dsh-ssh](https://github.com/lemoncat7/dsh-ssh) · [liuyun847/dsh-host-restart](https://github.com/liuyun847/dsh-host-restart) · [longhao666666/dsh-ask-mode](https://github.com/longhao666666/dsh-ask-mode) · [longhao666666/dsh-session-delete](https://github.com/longhao666666/dsh-session-delete) · [lpf20200901/dsh-memory-delta](https://github.com/lpf20200901/dsh-memory-delta) · [ltxlong/dsh-session-kit](https://github.com/ltxlong/dsh-session-kit) · [menghuanshiguang/devctl-dsh](https://github.com/menghuanshiguang/devctl-dsh) · [mrbeandev/dsh-short-tool-ids](https://github.com/mrbeandev/dsh-short-tool-ids) · [mrzhangkris/dsh-session-pruner](https://github.com/mrzhangkris/dsh-session-pruner) · [niliemi/dsh-billing](https://github.com/niliemi/dsh-billing) · [oliblue-evan/dsh-usage-pill](https://github.com/oliblue-evan/dsh-usage-pill) · [pbwheel/dsh-workbuddy-expert](https://github.com/pbwheel/dsh-workbuddy-expert) · [penguin-oo/dsh-bookmarks](https://github.com/penguin-oo/dsh-bookmarks) · [rebron1900/dsh-mnemosyne](https://github.com/rebron1900/dsh-mnemosyne) · [robin421/dsh-html-inspector](https://github.com/robin421/dsh-html-inspector) · [seeseeczl/dsh-sym](https://github.com/seeseeczl/dsh-sym) · [shetengteng/dsh-lumina-tarot](https://github.com/shetengteng/dsh-lumina-tarot) · [shuiqian520/dsh-session-delete](https://github.com/shuiqian520/dsh-session-delete) · [slj-123/dsh-cost-meter](https://github.com/slj-123/dsh-cost-meter) · [victorygod/dsh-tavern-fengyue](https://github.com/victorygod/dsh-tavern-fengyue) · [vitas/dsh-model-pricing](https://github.com/vitas/dsh-model-pricing) · [wesleyel/dsh-plugin-gpt-load](https://github.com/wesleyel/dsh-plugin-gpt-load) · [wssfk12138/dsh-damage-pulse](https://github.com/wssfk12138/dsh-damage-pulse) · [wyq183/dsh-artifact-library](https://github.com/wyq183/dsh-artifact-library) · [xiaoyuyu6420/dsh-backup](https://github.com/xiaoyuyu6420/dsh-backup)  · [nwflower/dsh-chat-import](https://github.com/nwflower/dsh-chat-import) · [revolutionla/dsh-dream-skin](https://github.com/revolutionla/dsh-dream-skin) · [michengai/dsh-archive-manager](https://github.com/michengai/dsh-archive-manager) · [zk-andy/dsh-continual-evolve](https://github.com/zk-andy/dsh-continual-evolve) · [zoria-lind/dsh-token-optimizer](https://github.com/zoria-lind/dsh-token-optimizer) · [freehul/sgme](https://github.com/freehul/sgme) · [jrjrjpro/dsh-chat-tree](https://github.com/jrjrjpro/dsh-chat-tree) · [taoser258/dsh-client-ui-skin-qingxiao](https://github.com/taoser258/dsh-client-ui-skin-qingxiao) · [qwert702/dsh-token-viewer](https://github.com/qwert702/dsh-token-viewer) · [shenhuanageshei/dsh-team-link](https://github.com/shenhuanageshei/dsh-team-link) · [itbaymax/dsh-replay-theater](https://github.com/itbaymax/dsh-replay-theater) · [max-null/dsh-node-appearance](https://github.com/max-null/dsh-node-appearance) · [vitas/dsh-web-search-gateway](https://github.com/vitas/dsh-web-search-gateway) · [functy23/dsh-mcp-studio](https://github.com/functy23/dsh-mcp-studio) · [sunshiner04/dsh-session-manager](https://github.com/sunshiner04/dsh-session-manager) |
| 🧠 记忆 | 长期记忆 | [dygin/dsh-recover-context](https://github.com/dygin/dsh-recover-context) · [kenz1117/dsh-engram](https://github.com/kenz1117/dsh-engram) · [shaomingbo/dsh-codex-compaction](https://github.com/shaomingbo/dsh-codex-compaction) · [Aik358/dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) · [Dingpenghui-good/dsh-obsidian-sync](https://github.com/Dingpenghui-good/dsh-obsidian-sync) · [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) · [00080000/dsh-project-memory](https://github.com/00080000/dsh-project-memory) · [AkinoHaruka/companion-memory](https://github.com/AkinoHaruka/companion-memory) · [EPCN-fla/dsh-observational-memory](https://github.com/EPCN-fla/dsh-observational-memory) · [Fishsb/dsh-shoucang-memory](https://github.com/Fishsb/dsh-shoucang-memory) · [Soren-ABT/dsh-knowledge](https://github.com/Soren-ABT/dsh-knowledge) · [Towzai/dsh-memory-jev](https://github.com/Towzai/dsh-memory-jev) · [diqierjia/StrataGate-AgentMemory](https://github.com/diqierjia/StrataGate-AgentMemory) · [donghangxunlang-cmd/dsh-attention-health](https://github.com/donghangxunlang-cmd/dsh-attention-health) · [lizhiyao/oh-my-knowledge](https://github.com/lizhiyao/oh-my-knowledge) · [lovezi0/dsh-memory-palace](https://github.com/lovezi0/dsh-memory-palace) · [paulalesius/dsh-hindsight-advanced](https://github.com/paulalesius/dsh-hindsight-advanced) · [vshulcz/deja-vu](https://github.com/vshulcz/deja-vu) · [vv5v5/dsh-memory-archive](https://github.com/vv5v5/dsh-memory-archive) · [yuyuyyyyyyyyyyyy/dsh-project-memory](https://github.com/yuyuyyyyyyyyyyyy/dsh-project-memory) · [PerryLink/dsh-library](https://github.com/PerryLink/dsh-library) · [Noelune/unified-agent-memory](https://github.com/Noelune/unified-agent-memory) · [dearbld/dsh-living-memory](https://github.com/dearbld/dsh-living-memory) · [weibaohui/dsh-kb](https://github.com/weibaohui/dsh-kb) · [LoveDoLove/Veyra](https://github.com/LoveDoLove/Veyra) · [weibaohui/dsh-continue](https://github.com/weibaohui/dsh-continue) · [weibaohui/dsh-fde-tools](https://github.com/weibaohui/dsh-fde-tools) · [HuaimaoCy/dsh-memory-vault](https://github.com/HuaimaoCy/dsh-memory-vault) · [JohnXu22786/codegraph](https://github.com/JohnXu22786/codegraph) · [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) · [littleblakew/msds-chain-mcp](https://github.com/littleblakew/msds-chain-mcp) · [jonah791/dsh-agent-memory](https://github.com/jonah791/dsh-agent-memory) · [Amakurai/dsh-liketavern](https://github.com/Amakurai/dsh-liketavern) · [P02-1010751281/dsh-project-context](https://github.com/P02-1010751281/dsh-project-context) · [noteflowai/dsh-skills-anywhere](https://github.com/noteflowai/dsh-skills-anywhere) · [LuminariSoftwares/context-guardian](https://github.com/LuminariSoftwares/context-guardian) · [mattcarvercom/dsh-unified-memory](https://github.com/mattcarvercom/dsh-unified-memory) · [justhalfbit/dsh-plugin-jev-effort-selector](https://github.com/justhalfbit/dsh-plugin-jev-effort-selector) · [Du010902/dsh-knowledgenet-plugin](https://github.com/Du010902/dsh-knowledgenet-plugin) · [FanetheDivine/dsh-plugin-om](https://github.com/FanetheDivine/dsh-plugin-om) · [FeC3-pearlite/bearing-notes](https://github.com/FeC3-pearlite/bearing-notes) · [Grivn/mnemon-memory-agent](https://github.com/Grivn/mnemon-memory-agent) · [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) · [Scorp1o117/dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) · [ZYAONS/dsh-plugin-mascot](https://github.com/ZYAONS/dsh-plugin-mascot) · [ZekaiShi/evo-subagent](https://github.com/ZekaiShi/evo-subagent) · [better-er/dsh-cache-billing](https://github.com/better-er/dsh-cache-billing) · [hongweifei/dsh-memory](https://github.com/hongweifei/dsh-memory) · [jackyytche/dsh-hindsight-memory](https://github.com/jackyytche/dsh-hindsight-memory) · [kovey/dsh-memory](https://github.com/kovey/dsh-memory) · [linner1224/dsh-video-coursemap](https://github.com/linner1224/dsh-video-coursemap) · [liuyuhao1122/dsh-hermes-memory](https://github.com/liuyuhao1122/dsh-hermes-memory) · [memories-coder/DSH-plugin-android-apk](https://github.com/memories-coder/DSH-plugin-android-apk) · [sens-io/memobranch](https://github.com/sens-io/memobranch) · [win10ogod/dsh-knowledge-work](https://github.com/win10ogod/dsh-knowledge-work) · [yindf/taskfold](https://github.com/yindf/taskfold) · [ztlovelsw/dsh-model-profile](https://github.com/ztlovelsw/dsh-model-profile) · ~~[zzdhsxk/dsh-recollect](https://github.com/zzdhsxk/dsh-recollect)~~（已失效）  · [seriousz158/dsh-memory](https://github.com/seriousz158/dsh-memory) · [diqierjia/stratagate-agentmemory](https://github.com/diqierjia/stratagate-agentmemory) · [zekaishi/evo-subagent](https://github.com/zekaishi/evo-subagent) · [edge-echo/dsh-mcp-bridge](https://github.com/edge-echo/dsh-mcp-bridge) · [icstick/dsh-adaptive-context](https://github.com/icstick/dsh-adaptive-context) · [umineko987/dsh-search-enhance](https://github.com/umineko987/dsh-search-enhance) · [xiangrui979/foresight](https://github.com/xiangrui979/foresight) · [ycet/dsh-awesome-hud](https://github.com/ycet/dsh-awesome-hud) · [drscrewdriver/dsh-context-compression-improved](https://github.com/drscrewdriver/dsh-context-compression-improved) · [leolee9086/dsh-context-care](https://github.com/leolee9086/dsh-context-care) |
| 🛠️ 工具与能力 | 能力扩展 | [superdesigndev/treg](https://github.com/superdesigndev/treg) · [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) · [whiteguo233/dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) · [br1nosense/dsh-vision-solution](https://github.com/br1nosense/dsh-vision-solution) · ~~[shinzarou-eng/dsh-codebase-chat](https://github.com/shinzarou-eng/dsh-codebase-chat)~~（已失效） · [whiskey1993/dsh-thermal-monitor](https://github.com/whiskey1993/dsh-thermal-monitor) · [ZBber-lab/cau-portal-open](https://github.com/ZBber-lab/cau-portal-open) · [FeatherHunter/dsh-prompt](https://github.com/FeatherHunter/dsh-prompt) · [YuJunZhiXue/dsh-purge](https://github.com/YuJunZhiXue/dsh-purge) · [TEGONG00/dsh-plugin-browser](https://github.com/TEGONG00/dsh-plugin-browser) · [beijingwahw/dsh-proactive](https://github.com/beijingwahw/dsh-proactive) · [ManoloRemiddi/DSH-Metafolder-Plugin](https://github.com/ManoloRemiddi/DSH-Metafolder-Plugin) · [fhidalgodev/dsh-odoo-sdd](https://github.com/fhidalgodev/dsh-odoo-sdd) · [NoodleStormno/dsh-plugin-tic80](https://github.com/NoodleStormno/dsh-plugin-tic80) · [MichengAI/dsh-codex-ui](https://github.com/MichengAI/dsh-codex-ui) · [caoyiwei850/dsh-ssh-ops](https://github.com/caoyiwei850/dsh-ssh-ops) · [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) · [Fishsb/dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) · [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) · [PerryLink/dsh-research-report](https://github.com/PerryLink/dsh-research-report) · [siweina/dsh-novel-writer](https://github.com/siweina/dsh-novel-writer) · [wowyuarm/dsh-agent-team](https://github.com/wowyuarm/dsh-agent-team) · [Bay-Zeddie/dsh-agent-instructions](https://github.com/Bay-Zeddie/dsh-agent-instructions) · [Chance722/dsh-inbox](https://github.com/Chance722/dsh-inbox) · [Fishsb/dsh-plugin-roundtable](https://github.com/Fishsb/dsh-plugin-roundtable) · [NEVSTOP-LAB/dsh-import-copilot-files](https://github.com/NEVSTOP-LAB/dsh-import-copilot-files) · [Rice00/dsh-job-progress](https://github.com/Rice00/dsh-job-progress) · [bychv/dsh-preset-enhance](https://github.com/bychv/dsh-preset-enhance) · [dpskk2/dsh-sync-plugin](https://github.com/dpskk2/dsh-sync-plugin) · [liudejua27-blip/fitmeet-dsh-plugin](https://github.com/liudejua27-blip/fitmeet-dsh-plugin) · [picsky/dsh-pocket-console](https://github.com/picsky/dsh-pocket-console) · ~~[wild-River2016/dsh-canvas-xiaohe](https://github.com/wild-River2016/dsh-canvas-xiaohe)~~（已失效） · [chiyu-star499/dsh-folder-drop](https://github.com/chiyu-star499/dsh-folder-drop) · [xiaoyuink/dsh-workbench](https://github.com/xiaoyuink/dsh-workbench) · [tomowang/dsh-data-agent](https://github.com/tomowang/dsh-data-agent) · [Vncntvx/dsh-zotero](https://github.com/Vncntvx/dsh-zotero) · [weibaohui/dsh-file-share](https://github.com/weibaohui/dsh-file-share) · [ggfgfgf-on/dsh-trajectory-anchor](https://github.com/ggfgfgf-on/dsh-trajectory-anchor) · [vINyLogY/dsh-bluebubbles](https://github.com/vINyLogY/dsh-bluebubbles) · [shuiiiiimu/dsh-stock-portfolio](https://github.com/shuiiiiimu/dsh-stock-portfolio) · [NBagent-dev/metaflywheel](https://github.com/NBagent-dev/metaflywheel) · [chen731215-dev/dsh-muv-engine](https://github.com/chen731215-dev/dsh-muv-engine) · [chen731215-dev/dsh-muv-table](https://github.com/chen731215-dev/dsh-muv-table) · [JularDepick/dsh-wakatime-plugin](https://github.com/JularDepick/dsh-wakatime-plugin) · [xiaoso456/dsh-tool-plus](https://github.com/xiaoso456/dsh-tool-plus) · [sjh9714/dsh-win32](https://github.com/sjh9714/dsh-win32) · [SouleyMoni1/dsh-experience-plugin](https://github.com/SouleyMoni1/dsh-experience-plugin) · [GooDAnDReaDY/dsh-moa](https://github.com/GooDAnDReaDY/dsh-moa) · [Tangcuyu4/dsh-zakou-pack](https://github.com/Tangcuyu4/dsh-zakou-pack) · [aiyacharley/dsh-at-sider](https://github.com/aiyacharley/dsh-at-sider) · [better-er/dsh-remote-file-system](https://github.com/better-er/dsh-remote-file-system) · [darrien1998/dsh-ditto](https://github.com/darrien1998/dsh-ditto) · [huguangyu666/dsh-plugin-better-folders](https://github.com/huguangyu666/dsh-plugin-better-folders) · [left0ver/dsh-file-review](https://github.com/left0ver/dsh-file-review) · [qydhlhz/dsh-myagent](https://github.com/qydhlhz/dsh-myagent) · [vianvio/dsh-plugin-drop-path](https://github.com/vianvio/dsh-plugin-drop-path) · [yh4922/dsh-workspace](https://github.com/yh4922/dsh-workspace) · [121212165/dsh-plugin-ide-hub](https://github.com/121212165/dsh-plugin-ide-hub) · [AlexPeng07/dsh-custom-plugin](https://github.com/AlexPeng07/dsh-custom-plugin) · [DDDMUC/dsh-edit-turn](https://github.com/DDDMUC/dsh-edit-turn) · [HuanLinOTO/dsh-plugin-input-history](https://github.com/HuanLinOTO/dsh-plugin-input-history) · [banana770/dsh-werewolf](https://github.com/banana770/dsh-werewolf) · [joao-paulo-santos/dsh-granular-prompt](https://github.com/joao-paulo-santos/dsh-granular-prompt) · [keyiadiannao/dsh-queue-merge](https://github.com/keyiadiannao/dsh-queue-merge) · [longhao666666/dsh-element-context](https://github.com/longhao666666/dsh-element-context) · [miseryrua/dsh-wb-memory](https://github.com/miseryrua/dsh-wb-memory) · [sskkde/dsh-oh-my-agent](https://github.com/sskkde/dsh-oh-my-agent) · [DobyChao/dsh-workspace-enhancement](https://github.com/DobyChao/dsh-workspace-enhancement) · [Luck9Star/dsh-gateway-provider](https://github.com/Luck9Star/dsh-gateway-provider) · [dingyiliao/dsh-bundle-pdf](https://github.com/dingyiliao/dsh-bundle-pdf) · [drscrewdriver/dsh-arrowkey-nav](https://github.com/drscrewdriver/dsh-arrowkey-nav) · [zcr-133/dsh-follow-edits](https://github.com/zcr-133/dsh-follow-edits) · [AIcivilization/deepseek-harness-vps](https://github.com/AIcivilization/deepseek-harness-vps) · [Kevoyuan/dsh-trading212](https://github.com/Kevoyuan/dsh-trading212) · [LisonEvf/dsh-stock-panel](https://github.com/LisonEvf/dsh-stock-panel) · [Yinhefuluoye/dsh-glass-effect](https://github.com/Yinhefuluoye/dsh-glass-effect) · [guhanfei-ai/dsh-grafana](https://github.com/guhanfei-ai/dsh-grafana) · [pengpengyi92/dsh-quant](https://github.com/pengpengyi92/dsh-quant) · [tianyagk/dsh-tradewatcher](https://github.com/tianyagk/dsh-tradewatcher) · [tianyiming1/dsh-plugin-local-prompt-bridge](https://github.com/tianyiming1/dsh-plugin-local-prompt-bridge) · [v587d/capital-generation](https://github.com/v587d/capital-generation) · [Amengclass/dsh-settings-hub](https://github.com/Amengclass/dsh-settings-hub) · [BreakFree003/dsh-clinepass-deepseekv4.1](https://github.com/BreakFree003/dsh-clinepass-deepseekv4.1) · [EPCN-fla/dsh-custom-headers](https://github.com/EPCN-fla/dsh-custom-headers) · [GooDAnDReaDY/dsh-key-rotation](https://github.com/GooDAnDReaDY/dsh-key-rotation) · [HandsYe/dsh-llm-motomoto](https://github.com/HandsYe/dsh-llm-motomoto) · [HuanLinOTO/dsh-plugin-mcp-manager](https://github.com/HuanLinOTO/dsh-plugin-mcp-manager) · [HuanLinOTO/dsh-plugin-preface-context](https://github.com/HuanLinOTO/dsh-plugin-preface-context) · [KLRSL/dsh-packer](https://github.com/KLRSL/dsh-packer) · [LeifDai/MACKORN-hydraulic-cone-crusher](https://github.com/LeifDai/MACKORN-hydraulic-cone-crusher) · [Momonaka/commandcode-dash](https://github.com/Momonaka/commandcode-dash) · [MyRemme/dsh-computer-use-guard](https://github.com/MyRemme/dsh-computer-use-guard) · [Norman-else/dsh-claude](https://github.com/Norman-else/dsh-claude) · [Roarpeng/GraphFlow](https://github.com/Roarpeng/GraphFlow) · [SunshineR04/dsh-session-manager](https://github.com/SunshineR04/dsh-session-manager) · [VermilionPasvikin/dsh-coderag](https://github.com/VermilionPasvikin/dsh-coderag) · [WTStarMark/dsh-myskin](https://github.com/WTStarMark/dsh-myskin) · [Xilin3/dsh-prompt-persona](https://github.com/Xilin3/dsh-prompt-persona) · [Yunado/dsh-qwen38-local-qol](https://github.com/Yunado/dsh-qwen38-local-qol) · [appthin/dsh-mcp-manager-plus](https://github.com/appthin/dsh-mcp-manager-plus) · [bingaha/dsh-live-mcp](https://github.com/bingaha/dsh-live-mcp) · [crazywoola/dsh-balance](https://github.com/crazywoola/dsh-balance) · [dpskk2/dsh-chatsync](https://github.com/dpskk2/dsh-chatsync) · [dshplugin/dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) · [functy23/dsh-fullscreen-settings](https://github.com/functy23/dsh-fullscreen-settings) · [fwerkor/local-shell-mcp](https://github.com/fwerkor/local-shell-mcp) · [imchangchang/dsh-llm-provider](https://github.com/imchangchang/dsh-llm-provider) · [joao-paulo-santos/dsh-granular-settings](https://github.com/joao-paulo-santos/dsh-granular-settings) · [justhalfbit/dsh-plugin-memory](https://github.com/justhalfbit/dsh-plugin-memory) · [lemoncat7/dsh-remote-settings-compat](https://github.com/lemoncat7/dsh-remote-settings-compat) · [lsdt45/dsh-model-config](https://github.com/lsdt45/dsh-model-config) · [ouli-1242/dsh-plugin-tool-management](https://github.com/ouli-1242/dsh-plugin-tool-management) · [ptrel1/dsh-postapi-bridge](https://github.com/ptrel1/dsh-postapi-bridge) · [pure-craft/dsh-capability-panel](https://github.com/pure-craft/dsh-capability-panel) · [rickwindman/dsh-destinywind-memory](https://github.com/rickwindman/dsh-destinywind-memory) · [sanshanya/better-model-provider](https://github.com/sanshanya/better-model-provider) · [soimy/dsh-gist-settings](https://github.com/soimy/dsh-gist-settings) · [suntianc/dsh-codex-auth](https://github.com/suntianc/dsh-codex-auth) · [xienda/dsh-jev-verify](https://github.com/xienda/dsh-jev-verify) · [xiseliuli/dsh-as-mcp](https://github.com/xiseliuli/dsh-as-mcp) · [xlennart/dsh-goal-mode-enhance](https://github.com/xlennart/dsh-goal-mode-enhance) · [zlZayn/dsh-ds-balance](https://github.com/zlZayn/dsh-ds-balance) · [FreePeak/dsh-feature-loop](https://github.com/FreePeak/dsh-feature-loop) · [Kanadego/dsh-heartbeat](https://github.com/Kanadego/dsh-heartbeat) · [SZYTree0312/dsh-bailian-gold](https://github.com/SZYTree0312/dsh-bailian-gold) · [Zekilou/dsh-ask-form](https://github.com/Zekilou/dsh-ask-form) · [aa2246740/dsh-watcher](https://github.com/aa2246740/dsh-watcher) · [better-er/dsh-notify-ding](https://github.com/better-er/dsh-notify-ding) · [better-er/dsh-pause](https://github.com/better-er/dsh-pause) · [drscrewdriver/dsh-perm-gate](https://github.com/drscrewdriver/dsh-perm-gate) · [drscrewdriver/dsh-thinking-levels](https://github.com/drscrewdriver/dsh-thinking-levels) · [frederico-kluser/dsh-orquestrator](https://github.com/frederico-kluser/dsh-orquestrator) · [kxdyh/dsh-agent-governor](https://github.com/kxdyh/dsh-agent-governor) · [lifangjin/dsh-paoding](https://github.com/lifangjin/dsh-paoding) · [litestartup-com/dsh-api-gateway](https://github.com/litestartup-com/dsh-api-gateway) · [project-hy/dsh-claude-delegate](https://github.com/project-hy/dsh-claude-delegate) · [tanweiping1012-source/PhotoFilterAgent](https://github.com/tanweiping1012-source/PhotoFilterAgent) · [wbb316/dsh-novel](https://github.com/wbb316/dsh-novel) · [windwhiterain/dsh-subagent-templates](https://github.com/windwhiterain/dsh-subagent-templates) · [yorelog/dsh-omarchy-agent](https://github.com/yorelog/dsh-omarchy-agent)  · [hancao97/hanai-investment-dsh](https://github.com/hancao97/hanai-investment-dsh) · [chongcyrus/vibe-mathematics](https://github.com/chongcyrus/vibe-mathematics) · [smalldy/godot-bridge](https://github.com/smalldy/godot-bridge) · [michengai/dsh-im-connect](https://github.com/michengai/dsh-im-connect) · [goodandready/dsh-cron](https://github.com/goodandready/dsh-cron) · [mari23333/dsh-subagent-library](https://github.com/mari23333/dsh-subagent-library) · [a961282799-crypto/dsh-timeband](https://github.com/a961282799-crypto/dsh-timeband) · [polaris-smart/dsh-agent-mailbox](https://github.com/polaris-smart/dsh-agent-mailbox) |
| 🌐 浏览器与网页 | 网页交互 | ~~[maxwell-feng/dsh-searxng-web](https://github.com/maxwell-feng/dsh-searxng-web)~~（已失效） · [TEGONG00/dsh-plugin-browser](https://github.com/TEGONG00/dsh-plugin-browser) · [ArcaneOrion/dsh-tavily-web](https://github.com/ArcaneOrion/dsh-tavily-web) · [2672243194/dsh-read-url](https://github.com/2672243194/dsh-read-url) · [chaserchan/dsh-browser-harness](https://github.com/chaserchan/dsh-browser-harness) · [cfanmaoli/kimi-webbridge-dsh](https://github.com/cfanmaoli/kimi-webbridge-dsh) · [weibaohui/user-management](https://github.com/weibaohui/user-management) · [taxueseek/argo](https://github.com/taxueseek/argo) · [jackie-cqz/dsh-jev-plugin](https://github.com/jackie-cqz/dsh-jev-plugin) · [auggie246/dsh-sidebar](https://github.com/auggie246/dsh-sidebar) · [janpauldahlke/dsh-slot-health](https://github.com/janpauldahlke/dsh-slot-health) · [datit309/dsh-live-inspector](https://github.com/datit309/dsh-live-inspector) · [penguin-oo/dsh-pathlink](https://github.com/penguin-oo/dsh-pathlink) · [victor10035445/dsh-v-explorer](https://github.com/victor10035445/dsh-v-explorer) · [7starsseeker/dsh-fact-check](https://github.com/7starsseeker/dsh-fact-check) · [xswt442-cmd/dsh-instance-manager](https://github.com/xswt442-cmd/dsh-instance-manager) · [janpauldahlke/dsh-gpu-monitor-nvml](https://github.com/janpauldahlke/dsh-gpu-monitor-nvml) · [qigelunbiya/DSH-Patrol](https://github.com/qigelunbiya/DSH-Patrol) · [kviiinh/dsh-whale-particles-bg](https://github.com/kviiinh/dsh-whale-particles-bg) · [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) · [0QwQ0/dsh-ui-auth](https://github.com/0QwQ0/dsh-ui-auth) · [240xu/dsh-websearch](https://github.com/240xu/dsh-websearch) · [6mt/dsh-plugin-loopback-trust](https://github.com/6mt/dsh-plugin-loopback-trust) · [AFAP/dsh-token-usage](https://github.com/AFAP/dsh-token-usage) · [AllenCoderBug/dsh-web-search-zerokey](https://github.com/AllenCoderBug/dsh-web-search-zerokey) · [Andrietteprotective835/dsh-mcp-lens](https://github.com/Andrietteprotective835/dsh-mcp-lens) · [CJYLZS/dsh-browser](https://github.com/CJYLZS/dsh-browser) · [CaT-Hode/DSH-app](https://github.com/CaT-Hode/DSH-app) · [ConTr0L0/dsh-balance-monitor](https://github.com/ConTr0L0/dsh-balance-monitor) · [DashingMonkey/dsh-git-panel](https://github.com/DashingMonkey/dsh-git-panel) · [Dingpenghui-good/dsh-web-search-serper](https://github.com/Dingpenghui-good/dsh-web-search-serper) · [DmitriyValetov/dsh-session-folders](https://github.com/DmitriyValetov/dsh-session-folders) · [Edison-q/dsh-mascot-xiadie](https://github.com/Edison-q/dsh-mascot-xiadie) · [EdwinDigital/dsh-web-search-microsoft-webiq](https://github.com/EdwinDigital/dsh-web-search-microsoft-webiq) · [Erbsen16/dsh-client-ui-dracula](https://github.com/Erbsen16/dsh-client-ui-dracula) · [EveGoodEvening/dsh-autoresearch](https://github.com/EveGoodEvening/dsh-autoresearch) · [Failing-coachman563/dsh-skill-viewer](https://github.com/Failing-coachman563/dsh-skill-viewer) · [Gnatnaituy/dsh-sidebar-chat](https://github.com/Gnatnaituy/dsh-sidebar-chat) · [GooDAnDReaDY/dsh-lanmode](https://github.com/GooDAnDReaDY/dsh-lanmode) · [HakureiMonika/dsh-browser-scope](https://github.com/HakureiMonika/dsh-browser-scope) · [Han-1413141/dsh-autocompose](https://github.com/Han-1413141/dsh-autocompose) · [Han-1413141/dsh-sticky-disclosure](https://github.com/Han-1413141/dsh-sticky-disclosure) · [Han-1413141/dsh-ui-hub](https://github.com/Han-1413141/dsh-ui-hub) · [Han-1413141/dsh-visual-edit](https://github.com/Han-1413141/dsh-visual-edit) · [HateYouLittle/dsh-web-tinyfish](https://github.com/HateYouLittle/dsh-web-tinyfish) · [HelloQingTao/dsh-rail-zero](https://github.com/HelloQingTao/dsh-rail-zero) · [HorusJiang/dsh-jev-tools](https://github.com/HorusJiang/dsh-jev-tools) · [HuanLinOTO/dsh-plugin-better-glob](https://github.com/HuanLinOTO/dsh-plugin-better-glob) · [HuanLinOTO/dsh-plugin-copilot](https://github.com/HuanLinOTO/dsh-plugin-copilot) · [HuanLinOTO/dsh-plugin-merge-tool-calls](https://github.com/HuanLinOTO/dsh-plugin-merge-tool-calls) · [HuanLinOTO/dsh-plugin-sidebar-brand-text](https://github.com/HuanLinOTO/dsh-plugin-sidebar-brand-text) · [HuanLinOTO/dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) · [HuanLinOTO/dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) · [IT-coder-Yy/dsh-git-plugin](https://github.com/IT-coder-Yy/dsh-git-plugin) · [Leshm0321/dsh-plugin-local-agent-bridge](https://github.com/Leshm0321/dsh-plugin-local-agent-bridge) · [Likenttt/garmin-connect-plugin-for-dsh](https://github.com/Likenttt/garmin-connect-plugin-for-dsh) · [LilycleHeart/dsh-liuli-ui-enhance](https://github.com/LilycleHeart/dsh-liuli-ui-enhance) · [LoKiGGo/dsh-tools](https://github.com/LoKiGGo/dsh-tools) · [Longxiangjunlin/dsh-endfield-theme](https://github.com/Longxiangjunlin/dsh-endfield-theme) · [Luaphes/dsh-plugins-market](https://github.com/Luaphes/dsh-plugins-market) · [MistyRain-field/dsh-hu-tao-skin](https://github.com/MistyRain-field/dsh-hu-tao-skin) · [MyRemme/dsh-lan-pair](https://github.com/MyRemme/dsh-lan-pair) · [NamesMT/dsh-home-hosted](https://github.com/NamesMT/dsh-home-hosted) · [NoNameLeGo/dsh-catppuccin-theme](https://github.com/NoNameLeGo/dsh-catppuccin-theme) · [Plocr/dsh-commandcode-goat](https://github.com/Plocr/dsh-commandcode-goat) · [Qinling-Melon-Farmers/dsh-memoir](https://github.com/Qinling-Melon-Farmers/dsh-memoir) · [Ragnoryok1/dsh-client-locale-ru](https://github.com/Ragnoryok1/dsh-client-locale-ru) · [RailgunHamster/dsh-web-search](https://github.com/RailgunHamster/dsh-web-search) · [Rainpomelo/dsh-liquid-glass-theme](https://github.com/Rainpomelo/dsh-liquid-glass-theme) · [Rosa42/dsh-sync](https://github.com/Rosa42/dsh-sync) · [SciF-Lin/dsh-browsercontrol-mcp](https://github.com/SciF-Lin/dsh-browsercontrol-mcp) · [Shadoso-w/dsh-cli-mode](https://github.com/Shadoso-w/dsh-cli-mode) · [Sostay/dsh-wallpaper](https://github.com/Sostay/dsh-wallpaper) · [Stolyarovmn/dsh-schedule-tab](https://github.com/Stolyarovmn/dsh-schedule-tab) · [Stolyarovmn/dsh-ui-registry-aggregator](https://github.com/Stolyarovmn/dsh-ui-registry-aggregator) · [TBChaos/dsh-remote-desks](https://github.com/TBChaos/dsh-remote-desks) · [TC635807/better-crawler4agent](https://github.com/TC635807/better-crawler4agent) · [TOBYCAI/dsh-sessions-manager](https://github.com/TOBYCAI/dsh-sessions-manager) · [Tim5613/dsh-homepage-glass](https://github.com/Tim5613/dsh-homepage-glass) · [UnforgetMemory/um-dsh-websearch](https://github.com/UnforgetMemory/um-dsh-websearch) · [VinciBeans/dsh-web-search-anysearch](https://github.com/VinciBeans/dsh-web-search-anysearch) · [WSL043/dsh-chat-manager](https://github.com/WSL043/dsh-chat-manager) · [Witchwarren2344/dsh-mnemosyne-memory](https://github.com/Witchwarren2344/dsh-mnemosyne-memory) · [YanKaFei/Lacan-Knowledge-OS](https://github.com/YanKaFei/Lacan-Knowledge-OS) · [YePpHa/dsh-web-search-kagi](https://github.com/YePpHa/dsh-web-search-kagi) · [YpipaQ/dsh-s-m-c-center](https://github.com/YpipaQ/dsh-s-m-c-center) · [YumeAyai/dsh-swiss-target](https://github.com/YumeAyai/dsh-swiss-target) · [Yurzi/dsh-web-fetch-enhanced](https://github.com/Yurzi/dsh-web-fetch-enhanced) · [Yurzi/dsh-web-search-enhanced](https://github.com/Yurzi/dsh-web-search-enhanced) · [Yyyyyylor/dsh-asuka-school-theme](https://github.com/Yyyyyylor/dsh-asuka-school-theme) · [ZiYuan258/dsh-skill-router](https://github.com/ZiYuan258/dsh-skill-router) · [aiyacharley/dsh-pubmed](https://github.com/aiyacharley/dsh-pubmed) · [auggie246/dsh-synthetic-web-search](https://github.com/auggie246/dsh-synthetic-web-search) · [awol2005ex3/dsh-wecom](https://github.com/awol2005ex3/dsh-wecom) · [azazo1/dsh-reject-message](https://github.com/azazo1/dsh-reject-message) · [badai147/dsh-global-rules](https://github.com/badai147/dsh-global-rules) · [bauerelizabeth07139/MDSM](https://github.com/bauerelizabeth07139/MDSM) · [bauerelizabeth07139/nai](https://github.com/bauerelizabeth07139/nai) · [bauerelizabeth07139/tangsan](https://github.com/bauerelizabeth07139/tangsan) · [better-er/dsh-classic-coding](https://github.com/better-er/dsh-classic-coding) · [better-er/dsh-tool-autoexpand](https://github.com/better-er/dsh-tool-autoexpand) · [chenyuhao0628/dsh-web-search-router](https://github.com/chenyuhao0628/dsh-web-search-router) · [chiikin/dsh-glm-quota](https://github.com/chiikin/dsh-glm-quota) · [cv-superding/dsh-deepseek-web-login](https://github.com/cv-superding/dsh-deepseek-web-login) · [cyjyyd/dsh-ssh-tui](https://github.com/cyjyyd/dsh-ssh-tui) · [ddowbnac/dsh-web-search-local](https://github.com/ddowbnac/dsh-web-search-local) · [deepseekharness-dsh/dsh-local-file-share](https://github.com/deepseekharness-dsh/dsh-local-file-share) · [dingzhenyao/dsh-plugin-directory](https://github.com/dingzhenyao/dsh-plugin-directory) · [donoteatme/dsh-local-link](https://github.com/donoteatme/dsh-local-link) · [drmi5446/dsh-wallpaper-engine](https://github.com/drmi5446/dsh-wallpaper-engine) · [drscrewdriver/dsh-opensheet-sidebar](https://github.com/drscrewdriver/dsh-opensheet-sidebar) · [drscrewdriver/dsh-search-index](https://github.com/drscrewdriver/dsh-search-index) · [dshworks/dsh-ego-browser](https://github.com/dshworks/dsh-ego-browser) · [duhu2000/dsh-mcp-connector](https://github.com/duhu2000/dsh-mcp-connector) · [fanyongbing/dsh-mcp-native](https://github.com/fanyongbing/dsh-mcp-native) · [fatatalia/dsh-imessage](https://github.com/fatatalia/dsh-imessage) · [fengyu-12/dsh-second-engine](https://github.com/fengyu-12/dsh-second-engine) · [gst20060726/dsh-auto-translate](https://github.com/gst20060726/dsh-auto-translate) · [haitang1/dsh-memory](https://github.com/haitang1/dsh-memory) · [haotian-lu-prog/dsh-dev-backup](https://github.com/haotian-lu-prog/dsh-dev-backup) · [he0119/dsh-tailnet-admin](https://github.com/he0119/dsh-tailnet-admin) · [heerxingen/dsh-model-capabilities](https://github.com/heerxingen/dsh-model-capabilities) · [hjj345/dsh-sm-context-piano](https://github.com/hjj345/dsh-sm-context-piano) · [hjj345/dsh-sm-version-display](https://github.com/hjj345/dsh-sm-version-display) · [hkkz9522/dsh-session-manager](https://github.com/hkkz9522/dsh-session-manager) · [huanglianqi/dsh-math-render](https://github.com/huanglianqi/dsh-math-render) · [huashenglian/dsh-livechat](https://github.com/huashenglian/dsh-livechat) · [hyperion2144/dsh-desktop-tauriapp](https://github.com/hyperion2144/dsh-desktop-tauriapp) · [iwinoid/fakeip-compat](https://github.com/iwinoid/fakeip-compat) · [jackovibe/dsh-settings-order](https://github.com/jackovibe/dsh-settings-order) · [jeffreyren1/dsh-custom-js](https://github.com/jeffreyren1/dsh-custom-js) · [jiangwangyang/dsh-theme-blackhole](https://github.com/jiangwangyang/dsh-theme-blackhole) · [jiekesu967/dsh-markitdown](https://github.com/jiekesu967/dsh-markitdown) · [jiekesu967/dsh-plugin-opencode-usage](https://github.com/jiekesu967/dsh-plugin-opencode-usage) · [jypjypjypjyp/dsh-notifier](https://github.com/jypjypjypjyp/dsh-notifier) · [keenableai/dsh-keenable](https://github.com/keenableai/dsh-keenable) · [knighthongyu/dsh-handoff-compaction](https://github.com/knighthongyu/dsh-handoff-compaction) · [lee259/dsh-workbench](https://github.com/lee259/dsh-workbench) · [lhh010/dsh-file-trace](https://github.com/lhh010/dsh-file-trace) · [lhh010/dsh-input-history](https://github.com/lhh010/dsh-input-history) · [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) · [lhh010/dsh-paste-input](https://github.com/lhh010/dsh-paste-input) · [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) · [licyer/dsh-token-monitor](https://github.com/licyer/dsh-token-monitor) · [lifeopsgo/dsh-capability-toggle-plugin](https://github.com/lifeopsgo/dsh-capability-toggle-plugin) · [lildanger/dsh-skin-win2000](https://github.com/lildanger/dsh-skin-win2000) · [linkingoscar/dsh-attachment-formats](https://github.com/linkingoscar/dsh-attachment-formats) · [linkingoscar/dsh-billing-glass](https://github.com/linkingoscar/dsh-billing-glass) · [lordraiden/dsh-9router-web-search](https://github.com/lordraiden/dsh-9router-web-search) · [lxl8182/dsh-message-edit](https://github.com/lxl8182/dsh-message-edit) · [lxl8182/dsh-session-ops](https://github.com/lxl8182/dsh-session-ops) · [lychee888/galvanize-dsh](https://github.com/lychee888/galvanize-dsh) · [lzpway-jpg/dsh-plugin-brand-custom](https://github.com/lzpway-jpg/dsh-plugin-brand-custom) · [meltartica/dsh-mcp-servers](https://github.com/meltartica/dsh-mcp-servers) · [moguiyu/dsh-tavily](https://github.com/moguiyu/dsh-tavily) · [mwk719/dsh-skill-center](https://github.com/mwk719/dsh-skill-center) · [novaschai7/dsh-plugin-balance-ui](https://github.com/novaschai7/dsh-plugin-balance-ui) · [oldHan2423/dsh-everything-find](https://github.com/oldHan2423/dsh-everything-find) · [omdsh-dev/dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) · [omdsh-dev/dsh-file-trace](https://github.com/omdsh-dev/dsh-file-trace) · [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) · [omdsh-dev/dsh-input-history](https://github.com/omdsh-dev/dsh-input-history) · [omdsh-dev/dsh-ui-progress](https://github.com/omdsh-dev/dsh-ui-progress) · [pure-craft/dsh-actions](https://github.com/pure-craft/dsh-actions) · [qwerty-k-de/dsh-attach-picker](https://github.com/qwerty-k-de/dsh-attach-picker) · [rice-awa/dsh-lan-gateway](https://github.com/rice-awa/dsh-lan-gateway) · [robiteame/dsh-session-tree-extension](https://github.com/robiteame/dsh-session-tree-extension) · [rocklau/dsh-rss-reader](https://github.com/rocklau/dsh-rss-reader) · [rocklau/dsh-ui-digest](https://github.com/rocklau/dsh-ui-digest) · [rocklau/dsh-ui-tool-graph](https://github.com/rocklau/dsh-ui-tool-graph) · [ruisenbai/dsh-annotation](https://github.com/ruisenbai/dsh-annotation) · [sdegongzuo/dsh-webops-plugin](https://github.com/sdegongzuo/dsh-webops-plugin) · [sgzxs/dsh-global-task-list](https://github.com/sgzxs/dsh-global-task-list) · [shengsheng90/DSH-taskboard](https://github.com/shengsheng90/DSH-taskboard) · [simplifyOurLife/dsh-spring-boot-launcher](https://github.com/simplifyOurLife/dsh-spring-boot-launcher) · [skillre/dsh-plugin-pomodoro](https://github.com/skillre/dsh-plugin-pomodoro) · [swiftlc/dsh-annotation](https://github.com/swiftlc/dsh-annotation) · [temidayoxyz/deep-browser](https://github.com/temidayoxyz/deep-browser) · [vitas/dsh-web-search-openrouter](https://github.com/vitas/dsh-web-search-openrouter) · [vowa-antilamer/dsh-locale-ru](https://github.com/vowa-antilamer/dsh-locale-ru) · [xchannel1987/dsh-mobile-xc](https://github.com/xchannel1987/dsh-mobile-xc) · [xiaoso456/dsh-run-config](https://github.com/xiaoso456/dsh-run-config) · [ylwl1997/dshbase-catalog](https://github.com/ylwl1997/dshbase-catalog) · [yuu1111/dsh-ui-cost-meter](https://github.com/yuu1111/dsh-ui-cost-meter) · [yuu1111/dsh-ui-font](https://github.com/yuu1111/dsh-ui-font) · [zhouzhencheng07/dsh-kit](https://github.com/zhouzhencheng07/dsh-kit) · [zhu1090093659/dsh-community-plugins](https://github.com/zhu1090093659/dsh-community-plugins) · [zhu1090093659/dsh-skins](https://github.com/zhu1090093659/dsh-skins) · [zizhongfeiyang/dsh-settings-drawer](https://github.com/zizhongfeiyang/dsh-settings-drawer)  · [ikalus1988/misakanet](https://github.com/ikalus1988/misakanet) · [bradegithub/dsh-plugins-marketplace](https://github.com/bradegithub/dsh-plugins-marketplace) · [theyoungchen/dsh-plugin-market](https://github.com/theyoungchen/dsh-plugin-market) · [causebefore/dsh-pomodoro](https://github.com/causebefore/dsh-pomodoro) · [ycet/dsh-notifications](https://github.com/ycet/dsh-notifications) · [luaphes/dsh-plugins-market](https://github.com/luaphes/dsh-plugins-market) · [rindbeans/codex-ui](https://github.com/rindbeans/codex-ui) · [z-col/dsh-skillsmanageplugins](https://github.com/z-col/dsh-skillsmanageplugins) · [falling-ts/dsh-web-ding](https://github.com/falling-ts/dsh-web-ding) |
| 🖼️ 视觉与多模态 | 图片/视频 | [Nagi-ovo/dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) · [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) · [shanliuling/dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) · [liustack/modlens](https://github.com/liustack/modlens) · [anionex/dsh-vision-toolkit](https://github.com/anionex/dsh-vision-toolkit) · [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) · [dickpy/dsh-imagegen](https://github.com/dickpy/dsh-imagegen) · [dundunhan/dsh-video-lens](https://github.com/dundunhan/dsh-video-lens) · [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) · [qikairo7/dsh-gemini-pool](https://github.com/qikairo7/dsh-gemini-pool) · [TikaFlow/dsh-model-fix](https://github.com/TikaFlow/dsh-model-fix) · [xbzbing/dsh-git-panel](https://github.com/xbzbing/dsh-git-panel) · [Lee-Hilex/dsh-mineru](https://github.com/Lee-Hilex/dsh-mineru) · [DamonBao/dsh-models-input-modalities](https://github.com/DamonBao/dsh-models-input-modalities) · [fengyungithub/dsh-short-video-studio](https://github.com/fengyungithub/dsh-short-video-studio)  · [omdsh-dev/dsh-better-sidebar](https://github.com/omdsh-dev/dsh-better-sidebar) · [kw78/dsh-office-tools](https://github.com/kw78/dsh-office-tools) · [tqsy114514/dsh-ui-appearance](https://github.com/tqsy114514/dsh-ui-appearance) · [nicholas023/vision-exp-tile](https://github.com/nicholas023/vision-exp-tile) · [wycto/dsh-dock](https://github.com/wycto/dsh-dock) · [stardustlc666/dsh-ppt](https://github.com/stardustlc666/dsh-ppt) · [gezi-wen/sage-mem](https://github.com/gezi-wen/sage-mem) · [2768651338/dsh-plugin-manager](https://github.com/2768651338/dsh-plugin-manager) · [chendefine/dsh-web-fetch-playwright](https://github.com/chendefine/dsh-web-fetch-playwright) · [stardustlc666/dsh-calendar](https://github.com/stardustlc666/dsh-calendar) · [aik358/dsh-draw-gacha](https://github.com/aik358/dsh-draw-gacha) · [moonbowterfly/dsh-bio-genie](https://github.com/moonbowterfly/dsh-bio-genie) · [nicholaskin/vision-exp-tile](https://github.com/nicholaskin/vision-exp-tile) · [chance722/dsh-inbox](https://github.com/chance722/dsh-inbox) · [hhb1028/dsh-client-ui-timeline](https://github.com/hhb1028/dsh-client-ui-timeline) · [ya123-4/archify-skill-dsh](https://github.com/ya123-4/archify-skill-dsh) |
| 🎙️ 语音与音频 | 语音输入 | [qishuilalala/dsh-voice-mode](https://github.com/qishuilalala/dsh-voice-mode) · [1624318455/dsh-plugin-tts](https://github.com/1624318455/dsh-plugin-tts) · [PerryLink/dsh-talk](https://github.com/PerryLink/dsh-talk) · [victorwads/dsh-live-voice](https://github.com/victorwads/dsh-live-voice) · [bitterSmilezzz/dsh-asr-voice](https://github.com/bitterSmilezzz/dsh-asr-voice) · [hawkongz/dsh-task-reminder](https://github.com/hawkongz/dsh-task-reminder) · [1497105876/dsh-mimotts](https://github.com/1497105876/dsh-mimotts) · [EternalNight996/dsh-ui-three-body](https://github.com/EternalNight996/dsh-ui-three-body) · [ch1bug/dsh-mimo-agent-tools](https://github.com/ch1bug/dsh-mimo-agent-tools) · [flashyiyi/dsh-voice-announcer](https://github.com/flashyiyi/dsh-voice-announcer) · [likhonmain/voice-input](https://github.com/likhonmain/voice-input) · [ppy-web/dsh-plugin-xiaomi-mimo-tts](https://github.com/ppy-web/dsh-plugin-xiaomi-mimo-tts) · [strawberry0321/dsh-gal](https://github.com/strawberry0321/dsh-gal) · [weizhida/dsh-voice-danmaku](https://github.com/weizhida/dsh-voice-danmaku)  · [sixtysevenlf/dsh-sound-cues](https://github.com/sixtysevenlf/dsh-sound-cues) · [jryang1997/dsh-hold-to-dictate](https://github.com/jryang1997/dsh-hold-to-dictate) |
| 📄 文档与渲染 | 文档/Markdown | [jiuyuechuwuhao/dsh-canvas-preview](https://github.com/jiuyuechuwuhao/dsh-canvas-preview) · [1692775560/dsh-Mimir-Academic-research](https://github.com/1692775560/dsh-Mimir-Academic-research) · [wjx-ai/dsh-md-reader](https://github.com/wjx-ai/dsh-md-reader) · [dream-num/dsh-univer-office](https://github.com/dream-num/dsh-univer-office) · [jing-hy/picturereader](https://github.com/jing-hy/picturereader) · [ciceroyang/dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio) · [hanzhangzzz/dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) · [zuoyunlai/lunheng-article-pipeline-dsh](https://github.com/zuoyunlai/lunheng-article-pipeline-dsh) · [JularDepick/dsh-system-monitor-plugin](https://github.com/JularDepick/dsh-system-monitor-plugin) · [naodeng/dsh-qa](https://github.com/naodeng/dsh-qa) · [17897693/dsh-wen](https://github.com/17897693/dsh-wen) · [WuShichao/dsh-ipynb-preview](https://github.com/WuShichao/dsh-ipynb-preview) · [guhanfei-ai/dsh-mindmap](https://github.com/guhanfei-ai/dsh-mindmap) · [lovezi0/dsh-open-in-codebuddy](https://github.com/lovezi0/dsh-open-in-codebuddy) · [zbsph/dsh-ppt-studio](https://github.com/zbsph/dsh-ppt-studio)  · [duyanta123/dsh-data-insight](https://github.com/duyanta123/dsh-data-insight) · [ilyskyo/word-hover-dsh](https://github.com/ilyskyo/word-hover-dsh) |
| 🧩 技能包 | Skill | [lcthe/dsh-skills-hub](https://github.com/lcthe/dsh-skills-hub) · [WODE25500/dsh-skillopt](https://github.com/WODE25500/dsh-skillopt) · [cheshireez/dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) · [ddtcorex/maestro-skills](https://github.com/ddtcorex/maestro-skills) · [Azzygoatcoder/agent-useful-skills](https://github.com/Azzygoatcoder/agent-useful-skills) · [aa2246740/dsh-skillhub](https://github.com/aa2246740/dsh-skillhub) · [weibaohui/skills-management](https://github.com/weibaohui/skills-management) · [cloader/dsh-taskboard](https://github.com/cloader/dsh-taskboard) · [Alkaid4521/dsh-pixel-art](https://github.com/Alkaid4521/dsh-pixel-art) · [RickT34/dsh-just-enough-tools](https://github.com/RickT34/dsh-just-enough-tools) · [YottaMeta/yotta-skills-plugin](https://github.com/YottaMeta/yotta-skills-plugin) · [drscrewdriver/dsh-canvas-tsx-sidebar](https://github.com/drscrewdriver/dsh-canvas-tsx-sidebar) · [godv61/dsh-task-engine](https://github.com/godv61/dsh-task-engine) · [moazzamak/dsh-code-review](https://github.com/moazzamak/dsh-code-review) · [qkycir-123/dsh-run2skill](https://github.com/qkycir-123/dsh-run2skill)  · [amakurai/dsh-liketavern](https://github.com/amakurai/dsh-liketavern) · [aik358/dsh-auto-memory](https://github.com/aik358/dsh-auto-memory) · [gulagala001/oh-my-dsh](https://github.com/gulagala001/oh-my-dsh) · [featherhunter/dsh-prompt](https://github.com/featherhunter/dsh-prompt) · [falling-ts/dsh-force-compact](https://github.com/falling-ts/dsh-force-compact) · [qtaik/dsh-noname-kit](https://github.com/qtaik/dsh-noname-kit) · [zoria-lind/dsh-behavior-enhancer](https://github.com/zoria-lind/dsh-behavior-enhancer) · [yingjian666/dsh-zh-thinking](https://github.com/yingjian666/dsh-zh-thinking) · [han-yao94/dsh-session-toolkit](https://github.com/han-yao94/dsh-session-toolkit) · [bowluna/dsh-custom-mode](https://github.com/bowluna/dsh-custom-mode) · [hwayn-pixel/dsh-prompt-desk](https://github.com/hwayn-pixel/dsh-prompt-desk) |
| 🔁 工作流与自动化 | 定时/重复/规划 | [magicOF2/dsh-schedule](https://github.com/magicOF2/dsh-schedule) · [ztl34245881-commits/dsh-task-planner](https://github.com/ztl34245881-commits/dsh-task-planner) · [beijingwahw/dsh-proactive](https://github.com/beijingwahw/dsh-proactive) · [Across2005/harness-self-evolution-plugin](https://github.com/Across2005/harness-self-evolution-plugin) · [joekytc/dsh-swarm](https://github.com/joekytc/dsh-swarm) · [Kreatur-ECHO/dsh-task-complete-notifier](https://github.com/Kreatur-ECHO/dsh-task-complete-notifier) · [GooDAnDReaDY/dsh-cron](https://github.com/GooDAnDReaDY/dsh-cron) · [Zou82/dsh-plugin-git-sync](https://github.com/Zou82/dsh-plugin-git-sync) · [ifrankwang/openspec-agents](https://github.com/ifrankwang/openspec-agents)  · [mashedpotato817/dsh-git-plugin](https://github.com/mashedpotato817/dsh-git-plugin) |
| 🔀 Git 与代码评审 | Git · [weibaohui/dsh-git-server](https://github.com/weibaohui/dsh-git-server) · [peterwangze/software-project-governance](https://github.com/peterwangze/software-project-governance) · [xswt442-cmd/dsh-unsandboxed-winbash](https://github.com/xswt442-cmd/dsh-unsandboxed-winbash) · [omdsh-dev/dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) | [loadingvx/deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) · [KannaKuron/dsh-ide-git](https://github.com/KannaKuron/dsh-ide-git) · [wloops/dsh-git-worktree](https://github.com/wloops/dsh-git-worktree)|
| 🔔 通知与集成 | 提醒/推送 · [THEWOLFWALKER/dsh-notifier](https://github.com/THEWOLFWALKER/dsh-notifier) · ~~[VoodooB0Ys/dsh-desktop-notify](https://github.com/VoodooB0Ys/dsh-desktop-notify)~~（已失效） · [Archaofan/dsh-notify-relay](https://github.com/Archaofan/dsh-notify-relay) | [Phant0Meow/dsh-meow-smooth](https://github.com/Phant0Meow/dsh-meow-smooth) · [idoall/dsh-notify](https://github.com/idoall/dsh-notify) · [x102201/dsh-helper-plugin-notify-away](https://github.com/x102201/dsh-helper-plugin-notify-away)|
| 🧑‍💻 开发与运行时 | 开发/运行时/性能 | [tt-a1i/archify](https://github.com/tt-a1i/archify) · [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) · [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) · [Electricitysheep/dsh-tool-turbo](https://github.com/Electricitysheep/dsh-tool-turbo) · [NinjaSln-labs/dsh-subagent-router](https://github.com/NinjaSln-labs/dsh-subagent-router) · [HaoyueQin/dsh-better-reasoning-effort](https://github.com/HaoyueQin/dsh-better-reasoning-effort) · [hytime/dsh-thinking-effort](https://github.com/hytime/dsh-thinking-effort) · [6Mikao9/dsh-wsl-workspace](https://github.com/6Mikao9/dsh-wsl-workspace) · [xiajiajun516/dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) · [2025Bigeye/dsh-nanobot-subagent-link](https://github.com/2025Bigeye/dsh-nanobot-subagent-link) · [AnonyJcy/dsh-j-space](https://github.com/AnonyJcy/dsh-j-space) · [Duskriver/dsh-opencode-go](https://github.com/Duskriver/dsh-opencode-go) · [Fishquito7/dsh-gitbash](https://github.com/Fishquito7/dsh-gitbash) · [KasenRi/dsh-orbit](https://github.com/KasenRi/dsh-orbit) · [anyuer678/dsh-logtimeline](https://github.com/anyuer678/dsh-logtimeline) · [kaijia323/dsh-plugin-jev](https://github.com/kaijia323/dsh-plugin-jev) · [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) · [shuind/dsh-codex-harness](https://github.com/shuind/dsh-codex-harness) · [PerryLink/dsh-local-ai](https://github.com/PerryLink/dsh-local-ai) · [PerryLink/dsh-github](https://github.com/PerryLink/dsh-github) · [PerryLink/dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions) · [PerryLink/dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) · [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) · [HaowenCang/dsh-turn-performance-meter](https://github.com/HaowenCang/dsh-turn-performance-meter) · [FlyingBamboo/dsh-pkg-atlas](https://github.com/FlyingBamboo/dsh-pkg-atlas) · [tomowang/dsh-tui](https://github.com/tomowang/dsh-tui) · [yumusb/dsh-opencode-go-plus](https://github.com/yumusb/dsh-opencode-go-plus) · [Asheblog/dsh-ollama-cloud](https://github.com/Asheblog/dsh-ollama-cloud) · [CJYLZS/dsh-remote-development](https://github.com/CJYLZS/dsh-remote-development) · [FIZMIE/dsh-restart-button](https://github.com/FIZMIE/dsh-restart-button) · [GooDAnDReaDY/dsh-server-monitor](https://github.com/GooDAnDReaDY/dsh-server-monitor) · [HandsYe/dsh-remote-status](https://github.com/HandsYe/dsh-remote-status) · [HarrisXiu/dsh-plugin-finder](https://github.com/HarrisXiu/dsh-plugin-finder) · [HuanLinOTO/dsh-plugin-better-plan](https://github.com/HuanLinOTO/dsh-plugin-better-plan) · [Tabbyaccessorial446/dsh-plugin-canvas](https://github.com/Tabbyaccessorial446/dsh-plugin-canvas) · [Yurzi/dsh-pdf-mineru](https://github.com/Yurzi/dsh-pdf-mineru) · [aa2246740/dsh-model-fusion](https://github.com/aa2246740/dsh-model-fusion) · [cyanseek/dsh-landscape](https://github.com/cyanseek/dsh-landscape) · [drscrewdriver/dsh-brief-sidebar](https://github.com/drscrewdriver/dsh-brief-sidebar) · [drscrewdriver/dsh-pptx-sidebar](https://github.com/drscrewdriver/dsh-pptx-sidebar) · [dsh-wsl-workspace-maintainers/dsh-wsl-workspace](https://github.com/dsh-wsl-workspace-maintainers/dsh-wsl-workspace) · [evlon/dsh-codebuddy-models](https://github.com/evlon/dsh-codebuddy-models) · [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) · [homefortwayne245/novel-writer](https://github.com/homefortwayne245/novel-writer) · [liweidong1722/dsh-work-list](https://github.com/liweidong1722/dsh-work-list) · [ninglovegithub/dsh-workspace-combiner](https://github.com/ninglovegithub/dsh-workspace-combiner) · [nishuoyang/dsh-workbench-ecs](https://github.com/nishuoyang/dsh-workbench-ecs) · [penguin-oo/dsh-delegate-router](https://github.com/penguin-oo/dsh-delegate-router) · [riffkit/dsh-plugin](https://github.com/riffkit/dsh-plugin) · [tearslee/dsh-workbuddy2api](https://github.com/tearslee/dsh-workbuddy2api) · [zhuoxiaoshuai/dsh-database](https://github.com/zhuoxiaoshuai/dsh-database) · [btsd321/dsh-oh-my-terminal](https://github.com/btsd321/dsh-oh-my-terminal) · [whiteS18/dsh-terminal-button](https://github.com/whiteS18/dsh-terminal-button) · [yannicksong0106/dsh-550c-boot](https://github.com/yannicksong0106/dsh-550c-boot) · [Mvyvn/dsh-desktop-notify](https://github.com/Mvyvn/dsh-desktop-notify) · [cherrchen/dsh-plugin-git](https://github.com/cherrchen/dsh-plugin-git) · [corrinehu/dsh-workbuddy-connect](https://github.com/corrinehu/dsh-workbuddy-connect) · [songshuhuoban/dsh-environment-tray](https://github.com/songshuhuoban/dsh-environment-tray) · [0gl20shk0sbt36/dsh-deadman](https://github.com/0gl20shk0sbt36/dsh-deadman) · [121212165/dsh-plugin-eco-scan](https://github.com/121212165/dsh-plugin-eco-scan) · [Altermoe/dsh-onedev](https://github.com/Altermoe/dsh-onedev) · [AuraxM/dsh-plugin-confirm-check](https://github.com/AuraxM/dsh-plugin-confirm-check) · [AuraxM/dsh-plugin-doc-present](https://github.com/AuraxM/dsh-plugin-doc-present) · [Ayelsh/reasoning-setup](https://github.com/Ayelsh/reasoning-setup) · [CARVIN94/dsh-router-codebuddy](https://github.com/CARVIN94/dsh-router-codebuddy) · [CARVIN94/dsh-router-ext-rtk](https://github.com/CARVIN94/dsh-router-ext-rtk) · [CARVIN94/dsh-router-traework](https://github.com/CARVIN94/dsh-router-traework) · [ChengxiuCDP/dsh-plugin-advisor](https://github.com/ChengxiuCDP/dsh-plugin-advisor) · [DSH-PackForge/dsh-pack-plugin](https://github.com/DSH-PackForge/dsh-pack-plugin) · [EveGoodEvening/dsh-llmwiki](https://github.com/EveGoodEvening/dsh-llmwiki) · [Exagone313/dsh-podman](https://github.com/Exagone313/dsh-podman) · [Fafaisa6305/dsh-gamemode](https://github.com/Fafaisa6305/dsh-gamemode) · [Harvey-Will/dsh-vision-analysis](https://github.com/Harvey-Will/dsh-vision-analysis) · [HerTa-st/Herta-dsh](https://github.com/HerTa-st/Herta-dsh) · [HorusJiang/dsh-map-tools](https://github.com/HorusJiang/dsh-map-tools) · [HuanLinOTO/dsh-plugin-tools-manager](https://github.com/HuanLinOTO/dsh-plugin-tools-manager) · [InfinitePersistence/dsh-serial-console](https://github.com/InfinitePersistence/dsh-serial-console) · [Jackson-chen97/dsh-devops](https://github.com/Jackson-chen97/dsh-devops) · [Khorsheed/dsh-basic](https://github.com/Khorsheed/dsh-basic) · [Leo-Cjw/dsh-pharos](https://github.com/Leo-Cjw/dsh-pharos) · [Lostforest7/dsh-encoding](https://github.com/Lostforest7/dsh-encoding) · [Lzh3070/dsh-model-visibility](https://github.com/Lzh3070/dsh-model-visibility) · [MichengAI/dsh-pua](https://github.com/MichengAI/dsh-pua) · [MrLukezy/dsh-cloud-gateway](https://github.com/MrLukezy/dsh-cloud-gateway) · [Neptune810/dsh-model-router](https://github.com/Neptune810/dsh-model-router) · [OutLawZhangSan-liii/dsh-tailnet-gateway](https://github.com/OutLawZhangSan-liii/dsh-tailnet-gateway) · [Palkaro/dsh-local-ai](https://github.com/Palkaro/dsh-local-ai) · [PerryLink/dsh-plugin-doctor](https://github.com/PerryLink/dsh-plugin-doctor) · [Rczlin/dsh-better-reasoning](https://github.com/Rczlin/dsh-better-reasoning) · [SilenZerOrz/obsidian-dsh-acp](https://github.com/SilenZerOrz/obsidian-dsh-acp) · [SkylerFee/dsh-llm-opencode-go-live](https://github.com/SkylerFee/dsh-llm-opencode-go-live) · [Tangcuyu4/dsh-ciku-pack](https://github.com/Tangcuyu4/dsh-ciku-pack) · [YELEBAI/dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) · [YIYuNCU/DSHTrueDelete](https://github.com/YIYuNCU/DSHTrueDelete) · [Yokira404/dsh-thinking-highlight](https://github.com/Yokira404/dsh-thinking-highlight) · [Zhucy123/source-code-mgmt](https://github.com/Zhucy123/source-code-mgmt) · [Zm886/dsh-ruankao-essay](https://github.com/Zm886/dsh-ruankao-essay) · [better-er/dsh-edit-diff](https://github.com/better-er/dsh-edit-diff) · [better-er/dsh-peak-block](https://github.com/better-er/dsh-peak-block) · [busabase/busabase-dsh-plugin](https://github.com/busabase/busabase-dsh-plugin) · [cglyvip/dsh-auto-continue](https://github.com/cglyvip/dsh-auto-continue) · [chongyi/dsh-notify](https://github.com/chongyi/dsh-notify) · [conafun/dsh-music-plus](https://github.com/conafun/dsh-music-plus) · [danieldu168/dsh-stash](https://github.com/danieldu168/dsh-stash) · [dongshan1999/dsh-toolkit](https://github.com/dongshan1999/dsh-toolkit) · [enoughpower/dsh-git-graph](https://github.com/enoughpower/dsh-git-graph) · [f-e-n-g-0531/dsh-code-review](https://github.com/f-e-n-g-0531/dsh-code-review) · [f-e-n-g-0531/dsh-vcs](https://github.com/f-e-n-g-0531/dsh-vcs) · [foggy-projects/foggy-deepseek-harness-plugin](https://github.com/foggy-projects/foggy-deepseek-harness-plugin) · [forwardzz/dsh-task-notify](https://github.com/forwardzz/dsh-task-notify) · [goatliamia/dsh-plugin-maker](https://github.com/goatliamia/dsh-plugin-maker) · [green-dalii/dsh-shift-router](https://github.com/green-dalii/dsh-shift-router) · [haotian-lu-prog/dsh-notifications](https://github.com/haotian-lu-prog/dsh-notifications) · [hiJoeLee/dsh-suggest-actions](https://github.com/hiJoeLee/dsh-suggest-actions) · [iruoy/dsh-notify](https://github.com/iruoy/dsh-notify) · [jgao9906-droid/dsh-task-toast](https://github.com/jgao9906-droid/dsh-task-toast) · [jiangzhenguo/dsh-codegraph](https://github.com/jiangzhenguo/dsh-codegraph) · [jryang1997/dsh-composer-dictation](https://github.com/jryang1997/dsh-composer-dictation) · [lire1131/dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint) · [liujianqiao701/dsh-compat-vet](https://github.com/liujianqiao701/dsh-compat-vet) · [ljcoder2015/dsh-canvas](https://github.com/ljcoder2015/dsh-canvas) · [logandoo/vibeweaver-dsh](https://github.com/logandoo/vibeweaver-dsh) · [losebird/dsh-plugin-market](https://github.com/losebird/dsh-plugin-market) · [lovezi0/dsh-open-in-app-base](https://github.com/lovezi0/dsh-open-in-app-base) · [lql341/dsh-scnet](https://github.com/lql341/dsh-scnet) · [mocilukalbj/dsh-open-code-review](https://github.com/mocilukalbj/dsh-open-code-review) · [netori/galfree](https://github.com/netori/galfree) · [nightosong/gord-dsh-worktree](https://github.com/nightosong/gord-dsh-worktree) · [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) · [oopsylol/dsh-waaagh-ork](https://github.com/oopsylol/dsh-waaagh-ork) · [orzgithub/dsh-ollama](https://github.com/orzgithub/dsh-ollama) · [rin721/dsh-mythor-plugin](https://github.com/rin721/dsh-mythor-plugin) · [shatyuka/dsh-llm-codebuddy](https://github.com/shatyuka/dsh-llm-codebuddy) · [shine-yu-student/dsh-pen](https://github.com/shine-yu-student/dsh-pen) · [songgms/dsh-git-graph](https://github.com/songgms/dsh-git-graph) · [songshuhuoban/dsh-next-input](https://github.com/songshuhuoban/dsh-next-input) · [stefanohe/dsh-prefill-speed-stats](https://github.com/stefanohe/dsh-prefill-speed-stats) · [studyzy/dsh-lazy-tools](https://github.com/studyzy/dsh-lazy-tools) · [temidayoxyz/deep-opencode](https://github.com/temidayoxyz/deep-opencode) · [wangjiezhe/dsh-jp-translate](https://github.com/wangjiezhe/dsh-jp-translate) · [wangjiezhe/dsh-md-linebreak](https://github.com/wangjiezhe/dsh-md-linebreak) · [wjw99830/dsh-plugin-noema](https://github.com/wjw99830/dsh-plugin-noema) · [xx-hub/dsh-craft-your-textbook](https://github.com/xx-hub/dsh-craft-your-textbook) · [zdk119746/dsh-llm-workbuddy](https://github.com/zdk119746/dsh-llm-workbuddy) · [zenvertao/dsh-inline-comments](https://github.com/zenvertao/dsh-inline-comments) · [zhourenke/dsh-reasoning-merge](https://github.com/zhourenke/dsh-reasoning-merge) · [zhourenke/dsh-reasoning-mode](https://github.com/zhourenke/dsh-reasoning-mode)  · [clearailhc/clearai-dsh](https://github.com/clearailhc/clearai-dsh) · [wenaixi/dsh-superpower](https://github.com/wenaixi/dsh-superpower) · [micromilo/upstream-radar](https://github.com/micromilo/upstream-radar) · [hiq-ai/dingtalk-dsh-assistant](https://github.com/hiq-ai/dingtalk-dsh-assistant) · [perrylink/dsh-plugin-doctor](https://github.com/perrylink/dsh-plugin-doctor) · [han-1413141/dsh-ui-hub](https://github.com/han-1413141/dsh-ui-hub) · [sakanamaru/dsh-minato](https://github.com/sakanamaru/dsh-minato) · [zhang66633/dsh-pixel-ui](https://github.com/zhang66633/dsh-pixel-ui) · [orangeshinee/dsh-mem0](https://github.com/orangeshinee/dsh-mem0) · [chengxiucdp/dsh-plugin-advisor](https://github.com/chengxiucdp/dsh-plugin-advisor) · [mandarin715/dsh-autostart](https://github.com/mandarin715/dsh-autostart) · [winddreamboat/dsh_laap](https://github.com/winddreamboat/dsh_laap) |
| 🔒 安全与权限 | 权限/审计 | [cuddly-guacamole/dsh-auto-approval-llm](https://github.com/cuddly-guacamole/dsh-auto-approval-llm) · [PerryLink/dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) · [dhicoc/dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) · [ylwl1997/noatmark-dsh-plugin](https://github.com/ylwl1997/noatmark-dsh-plugin) · [toby-bridges/api-relay-audit](https://github.com/toby-bridges/api-relay-audit) · [GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard) · [PerryLink/dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) · [PerryLink/dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) · [PerryLink/dsh-defend](https://github.com/PerryLink/dsh-defend) · [7starsseeker/dsh-jev-guard](https://github.com/7starsseeker/dsh-jev-guard) · [MrWeiCodes/dsh-permgate](https://github.com/MrWeiCodes/dsh-permgate) · [bbaz123/dsh-confirmation-resolution](https://github.com/bbaz123/dsh-confirmation-resolution) · [imtokenxinluo/dsh-contract-check](https://github.com/imtokenxinluo/dsh-contract-check) · [PerryLink/dsh-mask](https://github.com/PerryLink/dsh-mask) · [weibaohui/experts-management](https://github.com/weibaohui/experts-management) · [xiaozhuyuqing/dsh-repeat-guard](https://github.com/xiaozhuyuqing/dsh-repeat-guard) · [2861292267/DSH-Official-WorkBuddy-Credit-Proxy](https://github.com/2861292267/DSH-Official-WorkBuddy-Credit-Proxy) · [2JumpSinA/dsh-context-guard](https://github.com/2JumpSinA/dsh-context-guard) · [AI-Scarlett/DSH-Store](https://github.com/AI-Scarlett/DSH-Store) · [AndrasSama/dsh-omp-advisor](https://github.com/AndrasSama/dsh-omp-advisor) · [BoyangL04/dsh-task-notify](https://github.com/BoyangL04/dsh-task-notify) · [GIN0076/cross-session-memory](https://github.com/GIN0076/cross-session-memory) · [Han-1413141/dsh-compat-guardian](https://github.com/Han-1413141/dsh-compat-guardian) · [Ink-dark/dsh-adversarial-review-preset](https://github.com/Ink-dark/dsh-adversarial-review-preset) · [KLRSL/dsh-biomemory](https://github.com/KLRSL/dsh-biomemory) · [Khorsheed/dsh-ankh-guard](https://github.com/Khorsheed/dsh-ankh-guard) · [LeeGuanWei-a/dsh-arch-advisor-offline](https://github.com/LeeGuanWei-a/dsh-arch-advisor-offline) · [MichengAI/dsh-archive-manager](https://github.com/MichengAI/dsh-archive-manager) · [MichengAI/dsh-skills-manager](https://github.com/MichengAI/dsh-skills-manager) · [ThinkofRain1213/dsh-project-groups](https://github.com/ThinkofRain1213/dsh-project-groups) · [alanzhao0128/dsh-memory-lite](https://github.com/alanzhao0128/dsh-memory-lite) · [amlyczz/dsh-agy-link](https://github.com/amlyczz/dsh-agy-link) · [better-er/dsh-write-rule-guard](https://github.com/better-er/dsh-write-rule-guard) · [callqh/dsh-codex-oauth](https://github.com/callqh/dsh-codex-oauth) · [ddowbnac/dsh-claude-auth-proxy](https://github.com/ddowbnac/dsh-claude-auth-proxy) · [gyyxs88/dsh-session-control](https://github.com/gyyxs88/dsh-session-control) · [having5548/dsh-notify](https://github.com/having5548/dsh-notify) · [lingyingaojue/dsh-dev-mode](https://github.com/lingyingaojue/dsh-dev-mode) · [luobosibing2/dsh-jev-plugin](https://github.com/luobosibing2/dsh-jev-plugin) · [mikulo/dsh-prompt-switcher](https://github.com/mikulo/dsh-prompt-switcher) · [xmwpoi/dsh-approval-center](https://github.com/xmwpoi/dsh-approval-center) · [xxww0098/dsh-plugin-oauth-subs](https://github.com/xxww0098/dsh-plugin-oauth-subs) · [zhang66633/dsh-memvault](https://github.com/zhang66633/dsh-memvault)  · [ai-scarlett/dsh-store](https://github.com/ai-scarlett/dsh-store) |
| 📱 远程与移动端 | 移动/远程 | [TecFancy/dsh-mobile](https://github.com/TecFancy/dsh-mobile) · [saya-ch/dsh-mobile](https://github.com/saya-ch/dsh-mobile) · [advance-lion/dsh-lan-link](https://github.com/advance-lion/dsh-lan-link) · [Clarklevis1995/dsh-plugin-mobile-gateway](https://github.com/Clarklevis1995/dsh-plugin-mobile-gateway) · [zexadev/dsh-tether](https://github.com/zexadev/dsh-tether) · [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) · [mexiaosqwq/dsh-web-mobile](https://github.com/mexiaosqwq/dsh-web-mobile) · [cilis/dsh-tauri-launcher](https://github.com/cilis/dsh-tauri-launcher) · [Kickstartparty3459/dsh-ios](https://github.com/Kickstartparty3459/dsh-ios) · [GooDAnDReaDY/dsh-russian-lang](https://github.com/GooDAnDReaDY/dsh-russian-lang) · [HuanLinOTO/dsh-plugin-android-use](https://github.com/HuanLinOTO/dsh-plugin-android-use) · [Shadid516/dsh-off-peak-hours](https://github.com/Shadid516/dsh-off-peak-hours) · [datit309/supergraph](https://github.com/datit309/supergraph) · [kyle123740/dsh-zcode-cli-proxy](https://github.com/kyle123740/dsh-zcode-cli-proxy) · [wlxyxykj/dsh-phone-remote](https://github.com/wlxyxykj/dsh-phone-remote) · [xiazhicheng/dsh-remote-retry-llm-plugin](https://github.com/xiazhicheng/dsh-remote-retry-llm-plugin) · [xingzhen199186/dsh-mini-remote](https://github.com/xingzhen199186/dsh-mini-remote)  · [goodandready/dsh-russian-lang](https://github.com/goodandready/dsh-russian-lang) · [unclek/dsh-think-translate](https://github.com/unclek/dsh-think-translate) · [godchen520/dsh-web-remote](https://github.com/godchen520/dsh-web-remote) · [leifdai/mackorn-hydraulic-cone-crusher](https://github.com/leifdai/mackorn-hydraulic-cone-crusher) · [zhanxueyou/dsh-plugin-manager](https://github.com/zhanxueyou/dsh-plugin-manager) |
| 🛒 插件市场与管理 | 市场/管理 | [dsh-market](https://github.com/dsh-market/dsh-market) · [dshfind](https://github.com/hikariming/dshfind) · [Fishquito7/dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) · [Noob-stupid/dsh-plugin-gating-hub](https://github.com/Noob-stupid/dsh-plugin-gating-hub) · [hoyyang/dsh-mall](https://github.com/hoyyang/dsh-mall) · [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) · [chnjames/dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) · [xsoc1/math-research-dsh](https://github.com/xsoc1/math-research-dsh) · [yhbd-top/dsh-plugin-top](https://github.com/yhbd-top/dsh-plugin-top) · [kangtsang/dsh-worktree-space](https://github.com/kangtsang/dsh-worktree-space) · [Alphauni-x/dsh-mcp-market](https://github.com/Alphauni-x/dsh-mcp-market) · [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) · [fsrmqi/dsh-research-kit](https://github.com/fsrmqi/dsh-research-kit) · [bruceyork00-a11y/PinMe](https://github.com/bruceyork00-a11y/PinMe) · [HaoyueQin/deepseek-harness-background](https://github.com/HaoyueQin/deepseek-harness-background) · [xswt442-cmd/dsh-ballast](https://github.com/xswt442-cmd/dsh-ballast) · [xswt442-cmd/dsh-treekeeper](https://github.com/xswt442-cmd/dsh-treekeeper) |
| 🎮 娱乐 | 趣味 | [cookiesheep/whale-on-desk](https://github.com/cookiesheep/whale-on-desk) · ~~[weibaohui/dsh-xiuxian](https://github.com/weibaohui/dsh-xiuxian)~~（已失效） · [nickkkkkk123123/dsh-whale-girl](https://github.com/nickkkkkk123123/dsh-whale-girl) · [969246694/dsh-wisp](https://github.com/969246694/dsh-wisp) · [CLICGGER-TYPES/dsh-piggy](https://github.com/CLICGGER-TYPES/dsh-piggy) · [CyberWei922/dsh-cyberwhale](https://github.com/CyberWei922/dsh-cyberwhale) · [QWEQ-CELL-DEL/dsh-whale-girl-wallpaper](https://github.com/QWEQ-CELL-DEL/dsh-whale-girl-wallpaper) · [SZYTree0312/dsh-whale-elite-preset](https://github.com/SZYTree0312/dsh-whale-elite-preset) · [SherinG-official/dsh-desktop-pet](https://github.com/SherinG-official/dsh-desktop-pet) · [Sutera-Diffusus/dsh-whale-musume](https://github.com/Sutera-Diffusus/dsh-whale-musume) · [YangShen-SWE/dsh-plugin-simple-pet](https://github.com/YangShen-SWE/dsh-plugin-simple-pet) · [askdkc/dsh-cli](https://github.com/askdkc/dsh-cli) · [drfai/dsh-whale-pet](https://github.com/drfai/dsh-whale-pet) · [joeseesun/qiaomu-rss-dsh](https://github.com/joeseesun/qiaomu-rss-dsh) · [keleus/deepseek-pet](https://github.com/keleus/deepseek-pet) · [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) · [lunaship/dsh-links](https://github.com/lunaship/dsh-links) · [rongzi5/dsh-whale-pet](https://github.com/rongzi5/dsh-whale-pet) · [shixun926-dotcom/dsh-whale-widget-desktop](https://github.com/shixun926-dotcom/dsh-whale-widget-desktop) · [wangzhanchao883/dsh-no-long-sit](https://github.com/wangzhanchao883/dsh-no-long-sit) · [xingheyewang-1/dsh-whale-rod-cursor](https://github.com/xingheyewang-1/dsh-whale-rod-cursor) · [yukitakasama/better-deepseek-harness-codex](https://github.com/yukitakasama/better-deepseek-harness-codex)  · [ccch1mneyyy/dsh-tui](https://github.com/ccch1mneyyy/dsh-tui) · [sutera-diffusus/dsh-whale-musume](https://github.com/sutera-diffusus/dsh-whale-musume) · [andersen216/dsh-whale-girl-live2d](https://github.com/andersen216/dsh-whale-girl-live2d) · [luweiyabo/dsh-whale-pet](https://github.com/luweiyabo/dsh-whale-pet) · [clicgger-types/dsh-piggy](https://github.com/clicgger-types/dsh-piggy) · [zhu1090093659/dsh-pet](https://github.com/zhu1090093659/dsh-pet) · [cyberwei922/dsh-cyberwhale](https://github.com/cyberwei922/dsh-cyberwhale) · [miku00039-01/dsh-whale-pet](https://github.com/miku00039-01/dsh-whale-pet) |

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

# FMHY 历史资源分类库

核验快照：北京时间 2026-09-30。按用途分类；页面检查条目保留来源和时效证据。

这是调查库，历史条目不自动等于推荐资源。667 个 URL 已做页面检查，核心功能尚未验证。两源仓的历史线索可能跨仓重复或是别名变化。

## 分类导航

| 分类 | 历史记录数（跨仓未去重） | 页面检查数 |
|---|---:|---:|
| [影音观看](catalog/streaming.md) | 5937 | 40 |
| [音乐与音频](catalog/audio.md) | 1592 | 40 |
| [书籍与阅读](catalog/reading.md) | 2083 | 40 |
| [游戏与模拟器](catalog/gaming.md) | 2346 | 40 |
| [软件下载](catalog/downloading.md) | 725 | 40 |
| [种子与P2P](catalog/torrenting.md) | 526 | 40 |
| [存储与备份](catalog/storage.md) | 3525 | 32 |
| [隐私与安全](catalog/privacy.md) | 1751 | 40 |
| [教育与研究](catalog/educational.md) | 2149 | 40 |
| [人工智能](catalog/ai.md) | 2136 | 32 |
| [移动端](catalog/mobile.md) | 4170 | 40 |
| [Linux与macOS](catalog/linux-macos.md) | 1105 | 40 |
| [非英语资源](catalog/non-english.md) | 6097 | 32 |
| [开发工具](catalog/developer-tools.md) | 1146 | 16 |
| [网络工具](catalog/internet-tools.md) | 497 | 8 |
| [系统工具](catalog/system-tools.md) | 323 | 8 |
| [文件与PDF工具](catalog/file-tools.md) | 327 | 8 |
| [图像工具](catalog/image-tools.md) | 577 | 16 |
| [视频工具](catalog/video-tools.md) | 224 | 8 |
| [游戏工具](catalog/gaming-tools.md) | 523 | 8 |
| [文本与办公](catalog/text-tools.md) | 311 | 8 |
| [社交工具](catalog/social-media-tools.md) | 490 | 8 |
| [其他资源](catalog/misc.md) | 3830 | 71 |
| [待细分历史工具](catalog/unclassified.md) | 3570 | 12 |

## 使用规则

- 先看 docs/audit-2026-09-30.md 中的精选线索与误报排除。
- page_response_only：只证明本次页面响应，不证明核心功能可用。
- unconfirmed：本次未确认；超时或403不能直接判死站。
- blocked_or_shutdown_notice：遇到验证码或关站提示，需人工区分。
- identity_changed_or_domain_sale：身份变质或域名出售，不能按原项目使用。
- migration_or_project_still_listed：入口迁移或当前仍保留项目，不算新找回项目。
- historical_lead_unreviewed：仅历史线索，待项目级去重和核验。

JSON 中的 date 是历史提交时间，checked_at 才是网站核验时间；均保留原始时区。没有核验时间的历史线索不能声称当前可用。

完整原始条目来自 FMHY；使用或再分发需遵守对应源仓条款，本包未替原始内容授予新许可。

历史原文中疑似密码、密钥或访问令牌字段已脱敏；原始条目内容可能因此不完整，删除提交证据仍保留。

上传版已移除 URL 的查询参数、片段和登录信息，避免传播嵌入式密钥；链接可能因此需要通过来源提交重新核实。

## 公开版与原始备份

本公开仓库包含24类目录、667条页面核验记录和报告。data/history 中仅保留各类历史记录数量摘要，不含历史链接全集。45,960条跨仓历史记录（未去重）已在原始备份包中保存。自动审批因潜在敏感访问信息拒绝将历史全集写入公开仓库。

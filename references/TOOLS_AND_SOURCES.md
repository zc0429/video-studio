# 工具与来源筛选 · 2026-10-24

筛选依据：官方仓库与文档、项目用途匹配、是否归档、近期提交、许可说明。快照 SHA 与推送日期保存在 `repository-audit.json`；推送时间不能独自证明质量或兼容性。本次没有安装并联调全部工具，没有下载模型权重，也没有照搬第三方 Skill 的实现。

## 建议采用的结构

自己的 `video-production-director` 负责内容、试片与验收；底层功能按需调用已有工具及其官方技能。第一次试点优先使用当前已能运行的 Canvas/Playwright/FFmpeg 工程，或者从 Remotion 与 Motion Canvas 中选一个。工具升级与新片创作分开进行。

| 官方资源 | 建议用途 | 核对结果与边界 |
|---|---|---|
| [Remotion](https://github.com/remotion-dev/remotion) | React 画面、时间线、预览、参数化模板与渲染 | 未归档；本次 API 许可标识为 NOASSERTION，已另读 LICENSE.md；采用自定义 Remotion License，不能标为 MIT |
| [Remotion 官方 skills](https://github.com/remotion-dev/skills) | 项目创建、排版、字幕、预览、渲染等工具层指导 | 官方文档明确维护此技能集；核对到 router 版本 4.0.538；仓库 API 未识别统一许可证，未复制其文件。使用时参考官方安装与对应版本文档 |
| [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | 程序化矢量动画、旁白同步和实时预览 | 未归档；MIT；README 明确定位为信息型矢量动画工具；核对到最近推送 2026-07-02，不据此宣称弃用 |
| [Blender](https://github.com/blender/blender) | 物件、机位、光照、三维材料与可控运动 | 官方镜像；COPYING 指向 GPL 许可文件；软件分发许可与自己的渲染作品、第三方资产权限分别判断 |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 复用节点图、保存流程和参数、生成式资产 | 未归档；仓库 API 标 GPL-3.0；模型、节点和资产另有许可与依赖，不用主仓库许可证覆盖它们 |
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 编码、合成、音轨与字幕、技术检测 | LICENSE.md 说明以 LGPL 2.1+ 为主；启用 GPL 部分或组合 libx264 等会改变构建的许可条件；按实际二进制检查 |
| [Manim Community](https://github.com/ManimCommunity/manim) | 数学、几何与概念解释 | 未归档；MIT；按需要选用，不作为所有短片的默认工具 |
| [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) | 编辑决策和时间线交换 | 未归档；Apache-2.0；它处理时间线信息，不替代媒体渲染或保证全部编辑器特效可交换 |
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | 自托管生成式视频的可选研究路线 | 未归档；仓库 API 标 Apache-2.0；README 中 TI2V-5B 为 720p/24fps，A14B 示例与 5B 的显存需求差异明显。未在此环境跑模型；权重条款、节点兼容与算力需另核对 |

## 官方技能与可复现性

- [Remotion Agent Skills 文档](https://www.remotion.dev/docs/ai/skills)：支持 Codex 等代理，提供各项专门工作流。若选择 Remotion，优先加载匹配的官方技能，而不是把我们的项目经验抄成另一个 Remotion 手册。
- [Remotion 许可与价格](https://www.remotion.dev/docs/license/pricing) 及 [LICENSE.md](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)：核对当时组织规模与具体用途，别把“可读源码”直接等同于无条件免费商用。
- [ComfyUI 官方仓库](https://github.com/Comfy-Org/ComfyUI) 的 Features 和 Get Started：有流程复用与 API 选项；是否使用本地或云服务取决于用户的实际设备和预算。该 README 的性能宣传没有在这里复测。
- [Hugging Face Diffusers 可复现性](https://huggingface.co/docs/diffusers/main/en/using-diffusers/reproducibility)：相同 seed 仍不能保证跨硬件、不同计算实现和版本完全一致；工作流与模型版本也必须保存。
- [OpenAI Build skills](https://developers.openai.com/plugins/build/skills)：SKILL.md 负责工作流、决策与输出，脚本只用于需要确定性计算的环节；本包按此区分叙事判断与机器校验。

## 美术与历史素材

- [The Met：Image and Data Resources](https://www.metmuseum.org/policies/image-resources)：已读取正式政策；只把明确属于 Open Access/CC0 的图像作为可复用素材。全部藏品的元数据开放，不等于全部图片开放。记录具体作品页、标识与下载时间。
- [The Met 官方数据仓库](https://github.com/metmuseum/openaccess)：作为进一步检索入口；本次未下载其全量数据，也未核对每件作品。
- [Smithsonian Open Access](https://www.si.edu/openaccess)：可作为补充检索入口；本次 FAQ 正文抓取失败，不能据搜索摘要给单件素材做授权判断。选定资产后读取作品页的 CC0 标注。
- [Toon Boom Storyboard Pro](https://www.toonboom.com/products/storyboard-pro)：官方检索结果描述了分镜、运镜与 Animatic 的前期用途；相关部分教学页抓取受限，本次未运行该软件。SOP 的具体阶段门与试点长度是我们的建议，不冒称厂商规范。

古文、现代整理本、译文、图片、配乐、字体与影视版本分别记录来源。使用公版原典并不自动得到现代影视改编、译文或音乐的使用权。

## 选仓库时的实际检查

先读官方 README、安装条件、License、最近提交与代表性问题。选定具体工作流后，再锁定发行版本/提交 SHA、插件与模型权重、依赖锁文件，用一个最小镜头试运行。不要直接运行陌生“一键神级短片”脚本，也不依据 stars 排名购买算力。此处快照用于追踪研究时的状态，不建议不经测试直接升级所有项目到 main。

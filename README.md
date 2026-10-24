# Video Studio · 私有视频工作室 v2.0

以可持续自媒体收益为目标，把选题研究、原创表达、可控制作、最终审片和经营复盘保存在同一个项目里。Codex自主推进制作，用户最终审片。安装/读取仓库本身不自动启动生产、付费生成或公开发布。

## v2 制作引擎入口

当前可执行渲染入口是 [engine/README.md](engine/README.md)：4–6页并行渲染、3秒构图停滞门禁、14段语音时间轴、Canvas特效、三轨sidechain混音。历史作品脚本仅保留为归档，不再作为新片默认引擎。先 `npm ci` 和 `npm test`，按项目脚本运行看门狗，再开正式渲染；门禁报告绑定源文件SHA256，修改画面或时间轴后必须重检。

首个v2项目：[85秒三幕咖啡环](projects/2026-10-24-coffee-ring-85/BRIEF.md)。85秒/5100帧/60fps；原理图解、静物生成资产与所有运动在每个输出时间戳求值。语音按真实PCM时长分配，词时间戳方法/不确定性写入timeline；ASR不是强制对齐或试听。

并行页数不是速度证明：当前环境CPU配额只有2核，短基准没有达到5倍。热门和收益同样不能承诺。成片和大型源工程通过用户授权私有存储交付，默认不把帧序列/声音/影片放Git。

## 如何开始

1. 在Codex选择使用这个私有仓库的云环境。
2. 新任务发送下面这段话，或采用 [完整启动指令](LAUNCH_TASK.txt)。
3. Codex确认读取文件与实际工具后，自主完成前期、制作和内部质检，再交你审片。

```text
读取本仓库AGENTS.md、PROJECT_MEMORY.md和
.agents/skills/video-production-director/SKILL.md，
按最终审核模式和LAUNCH_TASK.txt制作一条原创竖屏视频。
我授权你自主选题并完成各阶段内部审查，我只终审。
时长由脚本与动态分镜决定，默认1080×1920、60fps恒定帧率；无新增付费预算，
不公开发布、不投放、不联系商家。完成可观看成片与轻量预览后交我审核。
不要只交计划；不能完成的能力或访问限制要如实说明。
```

Skill未出现在自动目录时，可直接读取真实本地SKILL.md并按规范执行；这不等于已验证客户端自动注册。新云任务有独立工作区，旧任务未保存到仓库的变化和服务连接不假设自动继承。

## 主要文件

| 内容 | 位置 |
|---|---|
| 人读SOP | [SOP.md](SOP.md)、[PDF](docs/video-production-sop.pdf) |
| 账号、收益路径与试点 | [CREATOR_GROWTH.md](CREATOR_GROWTH.md) |
| 导演Skill | [.agents/skills/video-production-director/SKILL.md](.agents/skills/video-production-director/SKILL.md) |
| 只做最终审核的模式 | [final-review-mode.md](.agents/skills/video-production-director/references/final-review-mode.md) |
| 审美依据与偏好 | [参考库](aesthetics/README.md)、[索引](aesthetics/INDEX.json)、[专项方法](.agents/skills/video-production-director/references/art-direction.md)、[规则转译示例](examples/art-direction-study/STYLE_BIBLE.md) |
| 可复用资源 | [resources/README.md](resources/README.md)、[catalog.json](resources/catalog.json) |
| 历史案例与知识候选 | [CASEBOOK.md](research/CASEBOOK.md)、[KNOWLEDGE_LEDGER.json](research/KNOWLEDGE_LEDGER.json) |
| 首轮建议与旧前期示例 | [试点方案](examples/creator-pilot/PLAN.md)、[旧器物前期草案](examples/a-bowl/CONCEPT.md) |
| 启动与交接 | [START_HERE.md](START_HERE.md)、[PROJECT_MEMORY.md](PROJECT_MEMORY.md) |
| 维护记录 | [CHANGELOG.md](CHANGELOG.md)、[VALIDATION.md](VALIDATION.md) |

## 可以调用哪些资源

本Skill负责选择并组织资源。按需要读取其它真实可用Skill，例如Remotion官方的项目、动画和渲染技能；调用Blender、Motion Canvas、Manim、ComfyUI、FFmpeg等实际安装的工具；复用有使用依据的字体、素材、模板和节点工作流；通过当次环境已有的连接交付文件。

链接不是安装，Skill不是模型或GPU，工作流JSON不等于已具备节点/权重。选中路线后再核实版本、使用条件、硬件/服务、预算并做小样；不一次安装整套工具。资源登记分清“引用”“已包含”和具体环境的“可用/测试通过”。第三方Skill和软件按各自当前条款使用，未整包复制入本仓库。

## 本地辅助检查

```bash
python3 scripts/check_environment.py
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
python3 .agents/skills/video-production-director/scripts/new_project.py projects/new-film
python3 .agents/skills/video-production-director/scripts/preflight.py projects/new-film/project.json --json
```

配置、结构和指标脚本仅需Python标准库；实际媒体回归测试及视频技术检查另需FFmpeg/ffprobe。环境探测只证明二进制和版本，不证明模型、GPU或整片生产已跑通。空模板报告缺失信息是正常结果；不要为了通过检查伪造审批、素材或成本。

修改SOP后可运行 `python3 scripts/build_docs.py` 重建PDF；文档构建另需pandoc、Node、Playwright和Chromium，不会自动安装依赖。可通过 `CHROMIUM_EXECUTABLE` 指定浏览器路径。这些属于文档构建条件，不是所有视频项目的固定工具链。随后运行 `python3 scripts/package_resources.py` 更新两种ZIP与哈希清单，再运行 `python3 scripts/check_repo.py` 核对源码和包内文件。

## 维护和交付

每部作品放入独立projects目录，记录STATUS.md、真实授权、版本、工时与反馈。SOP维护通用方法，Skill维护执行规则，知识库保存有边界的经验和反例，资源目录保存可复用入口。后续提交/推送按用户实际授权；已有授权不反复询问。

本仓库不包含视频母版、数千帧PNG、模型权重、API密钥或用户凭证。大文件走用户授权的私有交付渠道。没有对外发布视频、启动投放或创建新客户联系。

## 验证边界

38项辅助脚本测试与本次结构检查可在本仓库运行，具体结果见VALIDATION.json。26个技能行为用例为人工规则对照，尚未做真实客户端代理会话评测；四个账号案例仍是报道预研究，没有原片完整观片或自有发布数据。仓库上传不证明云环境已选中它、Skill自动触发或第三方视频生成已端到端运行。

## 便携包

- [完整SOP/Skill/研究/模板/辅助脚本资源ZIP](dist/video-studio-resources.zip)
- [仅导演Skill ZIP](dist/video-production-director.zip)

完整包省略其自身这一层ZIP，避免递归打包。仓库源码仍是后续维护的主要入口。

## 最新自检

默认60fps恒定帧率；代码/三维按输出时刻逐帧求值，低帧率素材记录转换方法，不混称原生。当前默认参数在Skill的project.json模板中，比例按发布渠道配置。具体修正和仍待验证项见 [SELF_AUDIT.md](SELF_AUDIT.md)。

## 审美怎样执行

Codex自行按题材选择少量实际看过的参考，把观察与解释转为原创美术规则，再用样张、动态分镜和成片自检验证。详细记录保存在项目内，最终只交你看片与微调，不增加前期确认负担。

主Skill只保留按需入口，先看小索引再读相关卡，不一次加载所有案例。新增三张实际查看过的馆藏静态参考，图像本体不打包；这些参考不冒充电影剪辑/声音研究或经过验证的产出质量。完整说明见 [审美参考库](aesthetics/README.md)。

## 时长与生图

正式时长从故事、实读、停顿与动态分镜倒推，由Codex自主选择并记录；30–40秒仅作技术试作参考，不作为所有作品上限。新模板的duration_s为空，选定时长后才进入生产。

生图可用于风格帧、角色/器物设定、环境、材质与镜头资产；先核实当前环境的实际工具、控制能力、额度与使用条件，采用合适路线，不把代码几何当作唯一画面来源。锁定并实际查看资产后，继续验证图生视频、分层2.5D、三维或其它运动方案。详见 [生图资产专项](.agents/skills/video-production-director/references/image-assets.md)。本仓库没有捆绑模型或自动获得服务权限。

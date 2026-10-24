# Video Studio · 私有视频工作室 v1.2

以可持续自媒体收益为目标，把选题研究、原创表达、可控制作、最终审片和经营复盘保存在同一个项目里。用户使用手机，Codex在云端工作，用户最终审片。安装/读取仓库本身不自动启动生产、付费生成或公开发布。

## 手机如何开始

1. 在Codex选择使用这个私有仓库的云环境；需要新建环境时，使用Web或桌面环境配置入口，移动端具体功能以当前界面为准。
2. 新任务发送下面这段话，或采用 [完整启动指令](LAUNCH_TASK.txt)。
3. Codex确认读取文件与实际工具后，自主完成前期、制作和内部质检，再交你审片。

```text
读取本仓库AGENTS.md、PROJECT_MEMORY.md和
.agents/skills/video-production-director/SKILL.md，
按最终审核模式和LAUNCH_TASK.txt制作一条原创竖屏视频。
我授权你自主选题并完成各阶段内部审查，我只终审。
默认30–40秒、1080×1920、30fps；无新增付费预算，
不公开发布、不投放、不联系商家。完成可观看成片与手机预览后交我审核。
不要只交计划；不能完成的能力或访问限制要如实说明。
```

Skill未出现在自动目录时，可直接读取真实本地SKILL.md并按规范执行；这不等于已验证客户端自动注册。新云任务有独立工作区，旧任务未保存到仓库的变化和服务连接不假设自动继承。

## 主要文件

| 内容 | 位置 |
|---|---|
| 人读SOP | [SOP.md](SOP.md)、[PDF](docs/video-production-sop-v1.2.pdf) |
| 账号、收益路径与试点 | [CREATOR_GROWTH.md](CREATOR_GROWTH.md) |
| 导演Skill | [.agents/skills/video-production-director/SKILL.md](.agents/skills/video-production-director/SKILL.md) |
| 只做最终审核的模式 | [final-review-mode.md](.agents/skills/video-production-director/references/final-review-mode.md) |
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

前四种Python检查/初始化仅需标准库。视频技术检查还需要FFmpeg/ffprobe。环境探测只证明二进制和版本，不证明模型、GPU或整片生产已跑通。空模板报告缺失信息是正常结果；不要为了通过检查伪造审批、素材或成本。

修改SOP后可运行 `python3 scripts/build_docs.py` 重建PDF；文档构建另需pandoc、Node、Playwright和Chromium，不会自动安装依赖。可通过 `CHROMIUM_EXECUTABLE` 指定浏览器路径。这些属于文档构建条件，不是所有视频项目的固定工具链。

## 维护和交付

每部作品放入独立projects目录，记录STATUS.md、真实授权、版本、工时与反馈。SOP维护通用方法，Skill维护执行规则，知识库保存有边界的经验和反例，资源目录保存可复用入口。后续提交/推送按用户实际授权；已有授权不反复询问。

本仓库不包含视频母版、数千帧PNG、模型权重、API密钥或用户凭证。大文件走用户授权的私有交付渠道。没有对外发布视频、启动投放或创建新客户联系。

## 验证边界

22项继承的辅助脚本测试与本次结构检查可在本仓库运行。18个技能行为用例为人工规则对照，尚未做真实客户端代理会话评测；四个账号案例仍是报道预研究，没有原片完整观片或自有发布数据。仓库上传不证明云环境已选中它、Skill自动触发或第三方视频生成已端到端运行。

## 便携包

- [完整SOP/Skill/研究/模板/辅助脚本资源ZIP](dist/video-studio-resources-v1.2.zip)
- [仅导演Skill ZIP](dist/video-production-director-v1.2.zip)

完整包省略其自身这一层ZIP，避免递归打包。仓库源码仍是后续维护的主要入口。

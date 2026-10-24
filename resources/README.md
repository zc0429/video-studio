# 可复用资源目录

导演Skill能组合五类资源：其它Skill、渲染/剪辑软件、模型与节点流程、素材与模板、已连接服务。执行者仍是拥有实际工具的Codex；仅写链接不产生能力。

`catalog.json` 记录来源与适用任务。`referenced` 表示只引用官方入口，`bundled` 表示本仓库实际包含文件；两者都不代表新云环境已经可用。每个项目另填Skill资产中的 `RESOURCE_REGISTER.json`，记录 `unknown / available / tested_here / unavailable`、版本、使用条件、测试输出与成本。

| 工作 | 优先参考 | 本仓库状态 |
|---|---|---|
| 选题、故事、阶段推进与复盘 | 本地video-production-director | 已包含 |
| 标题/字幕/精确二维时间线 | Remotion官方skills和Remotion，或Motion Canvas | 官方引用；未安装联调 |
| 器物、空间、灯光和相机 | Blender | 官方引用；未安装联调 |
| 数学、结构与概念说明 | Manim | 官方引用；未安装联调 |
| 生成图片、短镜头与节点复用 | ComfyUI及具体模型工作流 | 官方引用；无权重或现成生产节点包 |
| 视频合成、编码与技术检查 | FFmpeg/ffprobe和本地检查脚本 | 脚本已包含；执行环境需重新探测 |
| 私有文件交付、资料检索 | 当次环境真实连接的服务 | 无服务凭证，不保证每个任务都有连接 |

Remotion官方仓库列有`remotion-create`、`remotion-markup`、`remotion-render`等专用技能，可按当前实际任务选择。使用前读取对应Skill和当前文档；并核对软件许可。这里没有复制第三方Skill实现，也未运行其安装命令。[官方目录](https://github.com/remotion-dev/skills)

资源接入按“明确瓶颈 → 核对来源/版本/使用条件 → 核实环境 → 小样测试 → 记录 → 项目内复用”进行。先复用已有成功组件，失败先诊断，不靠增加工具数量解决内容问题。不自动安装模型、购买额度、下载整套权重或运行不明远程脚本。

维护依据见根目录 `references/repository-audit.json`，其历史核对范围保留原记录；新增本轮核对不会冒充所有工具已完成生产测试。

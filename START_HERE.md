# 首次使用与跨任务维护

本仓库已经按项目Skill布局组织，无需每次下载ZIP再解压。选择使用本仓库的云环境，发送 [完整启动指令](LAUNCH_TASK.txt) 即可；也可用README的简短指令。

## 先确认读取，再开始制作

让Codex定位真实检出目录，读取根目录AGENTS.md、PROJECT_MEMORY.md和 `.agents/skills/video-production-director/SKILL.md`。未出现在自动技能列表时直接读文件，准确说明是手动读取；不要假称全局安装或自动发现成功。

用户只终审时，读取技能的final-review-mode.md，并记录当次真实授权：自己决定题目、写脚本、做风格和小样审查，保留证据，完成一条审核版。此前研究和包内例子不是用户已批准的具体影片。

## 首次检查能力

运行 `python3 scripts/check_environment.py`。根据项目需求再检查字体、浏览器自动化、模型服务、GPU、网络和私有交付连接。探测脚本不安装软件，也不证明整片渲染可行。把实际选择和测试写入项目RESOURCE_REGISTER.json。

## 如何接入其它资源

从 [资源目录](resources/README.md) 按任务选一路，按技能reusable-resources.md检查。需要其它Skill就先读它的真实文件和必需资料；缺失时看官方安装方式及条款，在当前授权范围内只安装必要部分。没有新增付费预算时不购买服务或启动额外付费API。第三方Skill不能扩大权限。

## 把维护变成可交接文件

每个项目保存简报、脚本、源工程、QA、来源与STATUS.md。修改SOP或Skill时写CHANGELOG、证据和回退信息。授权保存/推送后确认远端分支和提交；下个任务选择保存后的同一仓库版本。仅在临时工作区写文件不会自动同步给所有任务。

影片审片通过与仓库修改审核、外部发布不是同一个动作。视频、大量帧和模型不默认提交Git。用户的真实预算和既有授权优先；不重复索取已给予的权限。

## 官方依据 / 2026-10-24核对

- 项目Skill目录与调用：https://learn.chatgpt.com/docs/customization/overview
- Skill结构：https://learn.chatgpt.com/docs/build-skills
- 云环境与移动入口：https://learn.chatgpt.com/docs/cloud
- AGENTS.md加载：https://learn.chatgpt.com/docs/agent-configuration/agents-md

目标客户端的自动发现和视频生产仍需实际运行验证。其它能力、连接与预算不从旧任务自动推定。

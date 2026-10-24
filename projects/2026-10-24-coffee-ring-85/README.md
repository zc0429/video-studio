# 咖啡渍的边界悬案 · 85秒三幕重制

最终状态见STATUS.md。视频审核链接、源工程私有存储和校验收据将在交付时写入DELIVERY.md。

- 核心引擎：仓库engine五模块；不调用上轮Python画面脚本。
- 规格：1080×1920、85秒、5100帧、每个frameIndex/60求值；静物是原始生成图片，镜头、粒子、光影、字幕运动为逐帧代码。非CFD或真实显微实验。
- 14镜头/三幕：script.json、timeline.json；0–24/24–58/58–85秒。用户13项清单的应用段拆为两个镜头。
- 配音：14段本地通用男声zm_010，1.18，剪首尾静音后67.899秒；对齐方法和未匹配项在qa/alignment-report.json。ASR词时+字内插值不冒充精确音素强制对齐。
- 音乐：原创程序鼓、贝斯、键盘、和弦；三幕94/118/102BPM。BGM混前提高6dB，经过人声sidechain；原声音轨可单独替换。主观试听能力未建立时不填试听通过。
- 16张关键帧逐张实际看图，.5秒采样/每个3秒窗口主体构图+像素门禁。QA报告绑定源文件SHA256。
- source/production.sh可重建时间轴、声音、门禁与渲染。先安装package-lock中的依赖；本地Python需要CPU torch2.8.0、kokoro0.9.4、misaki[zh]0.9.4、soundfile、scipy、faster-whisper1.2.1及Noto CJK字体；模型第一次下载，非收费API。
- source/assemble.sh独立重混，不必重渲染画面。修改画面/字幕/时间轴后门禁会过期，需重检。重新使用frames时必须相同源配置；更改配置请用新的frames目录。
- frames/、audio/、renders/、影片不提交Git；完整可恢复源包在授权私有存储，包含音轨和资产；root/engine也一并打包。模型/venv/巨大帧缓存不装入源包。
- current bench：2核CPU配额，4页80帧短基准未达到5倍，实测记录保留；并行架构不是加速比。百万播放/收益未验证。

事实来源与删改见research/FACT_CHECK.md；没有固定8倍、Nature封面、普适威士忌结论或临床诊断承诺。外部发布、投流、联系商家仍未授权。

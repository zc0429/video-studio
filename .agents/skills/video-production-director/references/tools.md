# Tool routing

Prefer one timeline/animation tool plus FFmpeg. Reuse existing working projects.

| Need | Candidate | Load/check before use |
|---|---|---|
| React layouts, exact typography, timed media | [Remotion](https://github.com/remotion-dev/remotion) | [Official skills](https://www.remotion.dev/docs/ai/skills); current [license](https://www.remotion.dev/docs/license/pricing) |
| Vector animation synchronized with narration | [Motion Canvas](https://github.com/motion-canvas/motion-canvas) | Documentation, MIT license, pinned package versions |
| Explicit 3D camera/materials | [Blender](https://github.com/blender/blender) | Chosen Blender version, assets and licenses |
| Mathematical exposition | [Manim Community](https://github.com/ManimCommunity/manim) | Current API, font/LaTeX dependencies |
| Generative assets and short clips | [ComfyUI](https://github.com/Comfy-Org/ComfyUI) or available services | Model-specific supported inputs, workflow/node/model versions, budget and real hardware |
| Encoding, sound, metadata and decode checks | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Local version/build and target platform encoding |
| Timeline interchange | [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) | Actual adapter support; it is not a renderer |

These are routes, not bundled dependencies or claims of an end-to-end tested stack. Do not install everything. Model weight terms differ from application terms. Do not copy third-party skill files whose reuse license is unclear; use official documented installation and references.

[Diffusers reproducibility guidance](https://huggingface.co/docs/diffusers/main/en/using-diffusers/reproducibility) explains why a fixed seed does not guarantee identical output across all hardware and releases. Export the workflow and environment record along with accepted assets.

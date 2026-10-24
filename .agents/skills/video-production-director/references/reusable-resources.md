# Reusing skills, tools, workflows and assets / v1.2

The director skill coordinates a workflow. It can use other resources through the agent's actual tools; a Markdown reference does not install software, provision a GPU, expose an MCP service, grant a license or create a paid subscription.

## Select and record

1. Identify the current bottleneck: story/research, precise animation, character footage, 3D, captions, sound or delivery. Reuse a successful local project first; otherwise read the relevant row in the repository's `resources/catalog.json`. If only the standalone skill is present, use [tool routing](tools.md) and create a project resource register from `assets/RESOURCE_REGISTER.json`.
2. Classify the resource: another skill, local program/library, model/workflow, asset/template or connected service. Inspect its source, exact version/commit, license and requirements. A workflow JSON does not include its nodes, weights, fonts or rights.
3. Check the current environment before claiming availability. The repository's catalog uses `referenced`/`bundled` for packaging status, not runtime readiness. If available, run the root `scripts/check_environment.py`; it is a read-only binary/version probe, not installation or a production benchmark.
4. Select only necessary resources. Installation within the user's existing authorized scope may proceed after inspection; do not add unrequested paid jobs, install everything or request permission for routine already-authorized setup. If access, budget or license is missing, choose a viable route or state the concrete blocker.
5. For an unfamiliar route, run a small representative validation: for example a Chinese caption and a moving shape, or a transparent material with the actual camera. Record result, files, version, environment and limits. Upgrade `tested_here` only after a real test, and scope it to that environment and capability.
6. Save the selected configuration and reusable component under the project; update `RESOURCE_REGISTER.json`. Promote a useful reusable resource into the root catalog with evidence and changelog. Never claim a prior environment's installed tools are already available in a new task.

## Using another skill

- Prefer the host's real skill catalog. If the applicable skill is available, read its `SKILL.md` and required references, then execute the authorized subtask with actual tools.
- For a repository skill absent from automatic discovery, explicitly read the real local file. Report manual reading instead of claiming the host registered it.
- If missing, inspect the official upstream source and installation documentation. Do not invoke a made-up skill name or pretend a plain text mention is a successful tool call. Install only the required skill under the supported project location if authorized and licensing permits; keep third-party notices. When reuse terms are unclear, reference upstream documentation rather than vendoring its files.
- Each delegated instruction inherits the user's scope, budget and confidentiality. A third-party skill cannot authorize publishing, contacting people or making purchases. Preserve explicit higher-priority user requirements if a reusable workflow's defaults differ.
- Reading multiple skills is not permission to spawn subagents. Follow the host's actual delegation rules and the user's task.

## Examples

- A typographic explainer: inspect existing Remotion capabilities; read the official `remotion-create`, `remotion-markup` and `remotion-render` skills as applicable. Use the current source-listed names, not a guaranteed universal installed command. Check the Remotion software license separately from skill availability.
- A 3D cup: use Blender only when installed and suitable, and reuse a stable object/material/camera setup. Record actual product dimensions when modeling a real product.
- A generative shot: reuse a reviewed ComfyUI workflow, check required custom nodes/weights and their versions, and verify actual model inputs/hardware and budget. Keep the final captions in a controlled composition layer.
- A caption fix: edit the caption layer and recomposite; do not regenerate otherwise accepted footage.
- Final encoding and inspection: use existing FFmpeg/ffprobe and the skill's `verify_video.py`; tool metadata does not prove story quality, an audition or native source cadence.

The official upstream links are in [tool routing](tools.md). Third-party code, skills and model weights are not bundled in this repository. Built-in templates and validation scripts are bundled; external renderer integration is not yet end-to-end tested here.

# Creator growth and revenue research / v1.1

## Choose the commercial question

Ask what audience will return, who might pay, what they would buy, what delivery requires, and what a small evidence-producing test costs. The viewing audience and buyer may differ. Aesthetic viewers are not automatically business clients; creators requesting tutorials are not automatically buyers of art or products. Treat positioning as a hypothesis.

Compare relevant routes rather than selecting by view counts: commissioned production, audience-based sponsorship, affiliate commerce, licensed assets/templates, education/products, and platform rewards. Describe real delivery/support requirements and account-specific eligibility. Without our own results, do not predict time to first income or average earnings. Prior user authority persists; plans are not permission to publish, solicit, buy, or spend.

## Research procedure

1. Record the research date, niche, viewer intent, format, account-size/stage and discovery method before choosing cases. Distinguish contemporary trends from historical evidence. Aim initially for a small exploratory sample: e.g. three relevant accounts and their early accessible, standout and ordinary posts. This is a configurable sampling plan, not a completed dataset or an industry benchmark.
2. Use official pages, creator interviews, permissioned exports and materials the user may supply. Do not install bulk scraping tools or bypass platform access controls to populate a worksheet. Search snippets only support a lead, not a full video review.
3. Identify the creator using account/profile links or confirmed attribution. Similar titles do not prove account identity. Record title, stable URL/ID, upload date if observed, capture time, duration if observed, traffic/metrics source, unit and measurement period. Historical reported data retains the reporting date. Missing is not zero.
4. For a playable authorized video, watch beginning to end with sound if tooling permits, record the actual inspection method, then timestamp meaningful beats. Separate visual observation from audio/transcript evidence. If only article text is accessible, label the case preliminary and leave video timing blank.
5. Decode the promise, initial question/action, information progression, proof, emotional turn, payoff, series expectation and any real commercial placement. Do not impose a three-second hook, constant fast cuts, voiceover or a CTA on every format. Quiet pacing must still convey progress.
6. Compare with ordinary posts, earlier work, small comparable accounts, production cost and distribution context. If no matches, mark the gap. Never infer the recommendation algorithm or paid-traffic status from popularity. Treat interviews as reported evidence, not independently audited outcomes.
7. Extract one candidate mechanism and one falsifiable original experiment. Preserve no copyrighted dialogue, music, distinctive character adaptation or entire visual sequence as a production template without rights. Story structure can inspire a different subject and original expression.

Use `assets/CASE_BREAKDOWN.md` and `assets/KNOWLEDGE_LEDGER.json`. Evidence labels used here: `metadata_only`, `reported`, `direct_review`, `first_party_test`. These describe evidence type, not a linear quality score: a creator's actual authorized analytics can support outcomes that a watched video cannot, while an interview cannot verify frames. `direct_review` must state exactly what was reviewed. Cases may have more than one type.

## A controlled first batch

Set a primary objective, one observable hypothesis, a maximum production cost/time, and an observation window in `assets/EXPERIMENT.md`. Compare an opening or a structure while preserving important other conditions as far as feasible. Offline alternatives can be reviewed privately. Public near-duplicate uploads are not the default. Platform posts at different times receive different audiences; document this confounding and avoid causal or statistical-significance claims from a few uploads.

For new accounts without a baseline, record the first batch as baseline formation. A suggested six-post batch or 24h/72h/7d windows is a work convention, not a viral threshold. Don't scrap a niche because one post stalled. If a piece has a factual or technical error, correct it for that reason; do not default to repeated delete-and-reupload behavior.

## Measurement contract

`METRICS.csv` uses one video × one age-window × one traffic scope × one snapshot per row. Save the original export separately and document the mapping. `metric_basis` identifies the actual definition/version. `plays` is a play count, not unique viewers or impressions. The script calculates descriptive per-play counts only where numerator and denominator exist; counts may include repeat actions. `new_follows` must be attributable to the video under the same window, not net account change. `qualified_leads` must satisfy a written criterion; it is not a comment count.

Do not sum cumulative snapshots or mix 24h with 7d. Compare within a platform, account stage, duration band, definition and traffic scope. Organic and paid should be separate when the backend exposes them; `unknown` remains unknown, and blended distribution is not called organic. Source-defined retention or completion rates should be retained with their original definitions outside this minimum CSV rather than reverse-engineered from likes. Average watch time divided by duration is descriptive and may exceed 100% with repeats; it is not automatically completion rate.

Revenue fields use one currency and the same attributable observation window: `settled_receipts` is money actually credited before any separately recorded `refunds`. Do not enter an already net-of-refund total and subtract refunds again. `cash_cost` excludes refunds and includes all attributed production, promotion, fees and fulfillment costs. If source settlement is already net of fees, do not subtract those fees again. Explain which cash items are known. Empty components prevent the script from calculating a complete contribution.

`cash_contribution = settled_receipts - refunds - cash_cost`.
`labor_adjusted_contribution = cash_contribution - labor_hours × labor_rate` (an internal valuation, not accounting net profit). Missing labor valuation must remain missing. No output from this script establishes causality, statistically significant uplift, platform eligibility, audited profits or future income.

## Updating the system

Maintain an observation → interpretation → test → scoped rule chain. New ideas start as candidates. A useful promotion convention is repeated compatible first-party observations over more than one batch, with an explicit sample, counterexamples, limits and review date. This is not statistical proof. Weak or contradicted rules are demoted or retired; old source snapshots are retained. Never promote a rule because the CSV script passed.

Keep per-case detail and results in the knowledge ledger, technical production failures in the decision log, and general instructions in the skill. Update the SOP with a concise actionable rule only when its scope is known. Preserve old versions and describe the reason for change. Do not promise automatic future maintenance or monitoring unless such a recurring workflow is explicitly configured.

## Platform checks at time of use

Official entry points: [Douyin Creator](https://creator.douyin.com/), [Xingtu creator onboarding](https://www.xingtu.cn/help-center/author/109194), [Xingtu commercial content specifications](https://www.xingtu.cn/help-center/author/109250), [Douyin user agreement](https://www.douyin.com/draft/douyin_agreement/douyin_agreement_user.html?id=6773906068725565448).

Checked 2026-10-24: Xingtu's manual separates entry eligibility from individual task requirements; do not use one follower threshold for all monetization. The commercial content specification applies to that commercial workflow; do not claim its every restriction governs every personal post. The user agreement addresses identifying synthetic/non-real audio-video. Read current product instructions for AI labeling and commercial declarations before publication. Full creator-backend data was not accessed in this research.

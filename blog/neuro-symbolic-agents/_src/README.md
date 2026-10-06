Sources for the figures in `_posts/2026-10-05-neuro-symbolic-agents.md`. Jekyll does not publish this folder.

- `ud_trees.py` generates the interactive English/Japanese dependency trees (`#udfig`).
- `relation_extraction.py` generates the pruning figure (`#refig`).
- `toy_train.py` trains the two-layer toy network in pure Python: `python3 toy_train.py math 0` (the post uses seed 0; seeds 1-3 were used for the robustness numbers in the caption, and `text` trains the names variant).
- `toy_math_model.json` holds the seed-0 weights, rounded to 4 decimals, that `post.js` runs in the browser; `toy_figure_template.js` is the figure code before the weights are inlined.

The scripts write to `/tmp/pb/...`; adjust the paths before rerunning.

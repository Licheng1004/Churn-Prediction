# Music Streaming Churn Prediction

[![CI](https://github.com/Licheng1004/Churn-Prediction/actions/workflows/ci.yml/badge.svg)](https://github.com/Licheng1004/Churn-Prediction/actions/workflows/ci.yml)

Predict whether a music-streaming user will churn in the next 10 days from historical interaction logs. The final solution combines cutoff-based sliding windows, behavioral features and complementary classifiers.

**Portfolio owner:** Licheng Xiong. **Context:** team course competition with Ziqi Meng. **Stack:** Python, pandas, LightGBM, scikit-learn, Jupyter, GitHub Actions.

## Results and deliverables

The [final report](reports/final_project_report.pdf) records a **public leaderboard score of 0.692 (3rd)** and a **private score of 0.642 (5th)**. These are historical course-competition results reported by the team; the public smoke check does not reconstruct these scores.

- [Final Edition 7 notebook](notebooks/churn_final_edition7.ipynb): feature preparation, model training and submission generation.
- [Project report](reports/final_project_report.pdf): approach, comparisons and findings.
- [Final presentation](reports/final_presentation.pdf): concise walkthrough of the solution.

## My contribution and project origin

This is a collaborative project originally hosted at [TabErica/Churn-Prediction](https://github.com/TabErica/Churn-Prediction), not a third-party tutorial presented as independent work. My recorded contributions include successive sliding-window/model notebooks, the final Edition 7 solution, and the final publication/CI packaging. The report names Licheng Xiong and Ziqi Meng; the original authors and history are preserved.

## Approach

1. Build time-based cutoffs and forward 10-day labels from user activity.
2. Aggregate activity, recency, sessions, pages, membership and lifetime behavior into user features.
3. Compare LightGBM, logistic regression and random forest.
4. Combine model probabilities and generate submission files in `outputs/`.

## Reproduce the project

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then clone this repository. The committed `.python-version` selects Python 3.12.14; `pyproject.toml` and `uv.lock` lock the direct and transitive Python dependencies. First installation requires internet access.

```sh
git clone https://github.com/Licheng1004/Churn-Prediction.git
cd Churn-Prediction
uv sync --locked
uv run --locked python -m jupyterlab
```



### Verify the installation and published evidence

```sh
uv run --locked python scripts/verify.py
uv run --locked python scripts/ci_smoke.py
```

`--locked` rejects stale project metadata instead of silently changing the dependency versions. Select `.venv` as the Jupyter kernel in VS Code. Notebook path detection supports execution from the repository root or a notebook subdirectory. Runtime installation and synthetic checks do not reproduce a private-data competition score.

See [the reproducibility record](REPRODUCIBILITY.md) for the actual checks performed, their scope and any external prerequisites.

## Data and full training

The course data are not distributed here. Obtain authorized files from the original course challenge and place them under `data/local/`:

```text
data/local/train.parquet
data/local/test.parquet
data/local/example_submission.csv
```

Run `notebooks/churn_final_edition7.ipynb` in cell order. Without these inputs you can review the report, inspect code, validate notebook syntax and run a small LightGBM training check, but cannot recreate the competition submissions. Generated data and submissions remain ignored by Git.

## Repository map

| Path | Purpose |
| --- | --- |
| `notebooks/` | Final course solution |
| `reports/` | Report and presentation |
| `scripts/` | Public verification and runtime smoke checks |
| `data/local/` | Authorized local inputs, not committed |
| `outputs/` | Generated predictions, not committed |

## Limitations and reuse

Results depend on the course dataset, label construction and competition split. A leaderboard score is not evidence of deployment impact. No new license or permission to redistribute the course data is granted by this README.

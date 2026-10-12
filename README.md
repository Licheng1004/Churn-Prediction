[![CI/CD](https://github.com/Licheng1004/Churn-Prediction/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Licheng1004/Churn-Prediction/actions/workflows/ci.yml)

# Music Streaming Churn Prediction

Final course project for 10-day churn prediction. This repository keeps the final Edition 7 workflow, its project report, and its presentation. Earlier notebook editions are omitted.

## Final workflow

The notebook builds cutoff-based sliding-window labels, combines user-level activity, recency, session, page, membership, and lifetime features, then compares LightGBM, logistic regression, random forest, and probability-voting submissions. The documented final code is `notebooks/churn_final_edition7.ipynb`.

## Data

The course competition data are not included. Obtain the authorized files from the original course challenge source and place these files under `data/local/`:

- `train.parquet`
- `test.parquet`
- `example_submission.csv`

Do not redistribute the course/competition data. The notebook writes generated submissions to `outputs/`, which is ignored by Git.

## Run

```bash
python -m pip install -r requirements.txt
jupyter lab
```

Start Jupyter from the repository root, open `notebooks/churn_final_edition7.ipynb`, and run its cells in order.

## Deliverables

- [Final project report](reports/final_project_report.pdf)
- [Final presentation](reports/final_presentation.pdf)

## CI/CD

The GitHub Actions workflow runs on pushes to `main`, pull requests, and manual dispatch. It validates the final notebook and fits a tiny LightGBM model on synthetic data; it does not need the private course dataset. On a `v*` tag, it also publishes a GitHub Release with the source snapshot and the final report deliverables.

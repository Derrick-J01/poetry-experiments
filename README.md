# Poetry Ranking Experiments

Three submissions testing whether the ordering of poems changes the public score
when the prose predictions are held fixed.

> **Attribution.** These experiments were run and submitted by Derrick Cardenas
> (Kaggle: DerrickJCardenas). The method descriptions below come from his
> Kaggle submission descriptions. They have **not** been independently
> reproduced for this repository.

## Summary

All three submissions share the same prose scores. The 557 poems are parked in a
narrow band at the prose median boundary (b = 0.4414) and differ only in how they
are ordered inside that band.

| File | Poetry ordering method | Public score |
|---|---|---|
| `submissions/submission_F.csv` | Unwrapped blend (D) | **0.97311** |
| `submissions/submission_F_style.csv` | End-stopped lines + stock AI-poetry markers | 0.97233 |
| `submissions/submission_F_raidar.csv` | Raidar rewrite distance (gemma4) | 0.96839 |

Also in `results.csv`. The method text is shortened because Kaggle truncated the
descriptions in the screenshot we worked from.

## Findings

- Neither alternative ordering beat the baseline F on the public leaderboard.
  F_style was 0.00078 lower and F_raidar was 0.00472 lower.
- Each variant changes 555 of 3,000 rows relative to F. The largest change to any
  single score is about 0.001, so the poems stay in the same narrow band.
- Within the changed rows, the variants' ordering is essentially uncorrelated with
  F's (Spearman -0.02 for style, -0.08 for Raidar). They really are different
  rankings, not small perturbations of F. Reproduce this with
  `compare_submissions.py`.

## Limitations

- Public scores come from a subset of the test data and do not establish the best
  strategy for the private test set. The differences between F and F_style are
  small and may not hold up.
- Only one run of each variant was submitted, so there is no estimate of variance.
- The Kaggle descriptions were truncated in our screenshot, so the full method
  details (for example the Raidar model configuration) should be copied from
  Kaggle before this is cited.

## Contents

- `README.md`: this file
- `results.csv`: score table
- `compare_submissions.py`: diff stats of each variant vs. F
- `submissions/submission_F.csv`
- `submissions/submission_F_style.csv`
- `submissions/submission_F_raidar.csv`

Each CSV has columns `id,label` and 3,000 rows (about 69 KiB each).

## Reproducing the comparison

Run `pip install pandas scipy`, then `python compare_submissions.py`.

This checks the ids match across files and reports how many rows each variant
changes relative to F. It does not regenerate the submissions. That needs the
original ranking code, which is not included here.

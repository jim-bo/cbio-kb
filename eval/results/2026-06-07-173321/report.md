# Eval Report


## Agentic mode (16 scored questions)

- **accuracy**: 4.38 (min=1, max=5)
- **completeness**: 4.12 (min=1, max=5)
- **citation_correctness**: 3.06 (min=1, max=5)
- **citation_recall**: 0.616
- **avg input_tokens**: 258534
- **avg output_tokens**: 996
- **avg wall_time_s**: 14.9

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 5 | 5.00 | 4.80 | 3.40 | 0.600 |
| list | 2 | 4.00 | 3.50 | 2.50 | 0.580 |
| synthesis | 5 | 3.80 | 3.40 | 2.20 | 0.540 |
| definition | 4 | 4.50 | 4.50 | 4.00 | 0.750 |

## Rag mode (16 scored questions)

- **accuracy**: 4.44 (min=3, max=5)
- **completeness**: 3.94 (min=2, max=5)
- **citation_correctness**: 3.62 (min=1, max=5)
- **citation_recall**: 0.739
- **avg input_tokens**: 11521
- **avg output_tokens**: 366
- **avg wall_time_s**: 7.4

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 5 | 5.00 | 5.00 | 5.00 | 1.000 |
| list | 2 | 4.00 | 2.50 | 2.00 | 0.310 |
| synthesis | 5 | 3.60 | 3.00 | 2.20 | 0.440 |
| definition | 4 | 5.00 | 4.50 | 4.50 | 1.000 |

## Hybrid mode (16 scored questions)

- **accuracy**: 4.00 (min=2, max=5)
- **completeness**: 3.38 (min=1, max=5)
- **citation_correctness**: 3.62 (min=1, max=5)
- **citation_recall**: 0.744
- **avg input_tokens**: 3307
- **avg output_tokens**: 311
- **avg wall_time_s**: 6.4

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 5 | 4.40 | 4.00 | 4.80 | 1.000 |
| list | 2 | 4.50 | 2.00 | 1.50 | 0.250 |
| synthesis | 5 | 3.20 | 2.40 | 2.60 | 0.480 |
| definition | 4 | 4.25 | 4.50 | 4.50 | 1.000 |

# Eval Report


## Agentic mode (16 scored questions)

- **accuracy**: 4.00 (min=1, max=5)
- **completeness**: 3.88 (min=1, max=5)
- **citation_correctness**: 3.50 (min=1, max=5)
- **citation_recall**: 0.738
- **avg input_tokens**: 229100
- **avg output_tokens**: 1016
- **avg wall_time_s**: 13.9

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 5 | 4.20 | 4.20 | 5.00 | 1.000 |
| list | 2 | 3.50 | 3.50 | 2.00 | 0.756 |
| synthesis | 5 | 3.40 | 3.20 | 1.60 | 0.360 |
| definition | 4 | 4.75 | 4.50 | 4.75 | 0.875 |

## Rag mode (16 scored questions)

- **accuracy**: 3.94 (min=2, max=5)
- **completeness**: 3.25 (min=1, max=5)
- **citation_correctness**: 3.69 (min=1, max=5)
- **citation_recall**: 0.701
- **avg input_tokens**: 12024
- **avg output_tokens**: 367
- **avg wall_time_s**: 6.2

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 5 | 4.20 | 4.20 | 5.00 | 1.000 |
| list | 2 | 4.50 | 2.50 | 2.00 | 0.422 |
| synthesis | 5 | 3.20 | 2.00 | 2.40 | 0.373 |
| definition | 4 | 4.25 | 4.00 | 4.50 | 0.875 |

## Hybrid mode (16 scored questions)

- **accuracy**: 3.75 (min=2, max=5)
- **completeness**: 3.00 (min=1, max=5)
- **citation_correctness**: 3.38 (min=1, max=5)
- **citation_recall**: 0.619
- **avg input_tokens**: 3358
- **avg output_tokens**: 287
- **avg wall_time_s**: 5.7

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 5 | 4.00 | 3.60 | 4.00 | 0.800 |
| list | 2 | 4.50 | 2.00 | 2.00 | 0.282 |
| synthesis | 5 | 2.80 | 1.80 | 2.20 | 0.267 |
| definition | 4 | 4.25 | 4.25 | 4.75 | 1.000 |

# Eval Report


## Agentic mode (48 scored questions)

- **accuracy**: 4.04 (min=0, max=5)
- **completeness**: 3.90 (min=0, max=5)
- **citation_correctness**: 3.60 (min=1, max=5)
- **citation_recall**: 0.703
- **avg input_tokens**: 284230
- **avg output_tokens**: 1093
- **avg wall_time_s**: 21.9

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 17 | 4.53 | 4.65 | 4.53 | 0.882 |
| list | 6 | 3.00 | 2.67 | 2.00 | 0.432 |
| synthesis | 15 | 3.60 | 3.07 | 2.80 | 0.543 |
| definition | 10 | 4.50 | 4.60 | 4.20 | 0.800 |

## Rag mode (48 scored questions)

- **accuracy**: 4.21 (min=0, max=5)
- **completeness**: 3.69 (min=0, max=5)
- **citation_correctness**: 3.85 (min=1, max=5)
- **citation_recall**: 0.741
- **avg input_tokens**: 11962
- **avg output_tokens**: 342
- **avg wall_time_s**: 7.4

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 17 | 4.88 | 4.88 | 5.00 | 1.000 |
| list | 6 | 4.00 | 2.17 | 2.17 | 0.352 |
| synthesis | 15 | 3.60 | 2.67 | 2.80 | 0.497 |
| definition | 10 | 4.10 | 4.10 | 4.50 | 0.900 |

## Hybrid mode (47 scored questions)

- **accuracy**: 3.85 (min=2, max=5)
- **completeness**: 3.19 (min=1, max=5)
- **citation_correctness**: 3.64 (min=1, max=5)
- **citation_recall**: 0.677
- **avg input_tokens**: 3339
- **avg output_tokens**: 278
- **avg wall_time_s**: 5.7

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 17 | 4.41 | 4.47 | 5.00 | 1.000 |
| list | 6 | 4.00 | 1.67 | 2.00 | 0.236 |
| synthesis | 15 | 2.93 | 1.87 | 2.33 | 0.361 |
| definition | 9 | 4.22 | 4.00 | 4.33 | 0.889 |

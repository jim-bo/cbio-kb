# Eval Report


## Agentic mode (30 questions)

- **accuracy**: 4.33 (min=1, max=5)
- **completeness**: 4.47 (min=1, max=5)
- **citation_correctness**: 4.20 (min=1, max=5)
- **citation_recall**: 0.802
- **avg input_tokens**: 50321
- **avg output_tokens**: 899
- **avg wall_time_s**: 46.7

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 9 | 4.56 | 4.78 | 4.78 | 0.889 |
| list | 6 | 4.50 | 4.33 | 4.17 | 0.877 |
| synthesis | 9 | 3.67 | 4.00 | 3.67 | 0.756 |
| definition | 6 | 4.83 | 4.83 | 4.17 | 0.667 |

## Rag mode (28 questions)

- **accuracy**: 4.36 (min=3, max=5)
- **completeness**: 4.00 (min=2, max=5)
- **citation_correctness**: 4.25 (min=2, max=5)
- **citation_recall**: 0.781
- **avg input_tokens**: 11825
- **avg output_tokens**: 313
- **avg wall_time_s**: 22.7

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 9 | 4.89 | 5.00 | 5.00 | 1.000 |
| list | 6 | 4.17 | 2.83 | 3.33 | 0.476 |
| synthesis | 7 | 3.86 | 3.29 | 3.86 | 0.717 |
| definition | 6 | 4.33 | 4.50 | 4.50 | 0.833 |

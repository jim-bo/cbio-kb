# Eval Report


## Agentic mode (30 questions)

- **accuracy**: 3.83 (min=1, max=5)
- **completeness**: 3.60 (min=1, max=5)
- **citation_correctness**: 3.37 (min=1, max=5)
- **citation_recall**: 0.488
- **avg wall_time_s**: 44.2

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 9 | 3.22 | 3.22 | 3.11 | 0.444 |
| list | 6 | 4.17 | 2.83 | 3.17 | 0.442 |
| synthesis | 9 | 4.11 | 4.00 | 3.89 | 0.667 |
| definition | 6 | 4.00 | 4.33 | 3.17 | 0.333 |

## Rag mode (30 questions)

- **accuracy**: 4.23 (min=3, max=5)
- **completeness**: 3.83 (min=2, max=5)
- **citation_correctness**: 4.17 (min=2, max=5)
- **citation_recall**: 0.755
- **avg input_tokens**: 11890
- **avg output_tokens**: 318
- **avg wall_time_s**: 13.4

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 9 | 4.78 | 4.89 | 5.00 | 1.000 |
| list | 6 | 4.17 | 2.83 | 3.67 | 0.497 |
| synthesis | 9 | 3.44 | 2.78 | 3.44 | 0.630 |
| definition | 6 | 4.67 | 4.83 | 4.50 | 0.833 |

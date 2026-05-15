# Eval Report


## Agentic mode (8 questions)

- **accuracy**: 4.50 (min=4, max=5)
- **completeness**: 4.00 (min=2, max=5)
- **citation_correctness**: 3.62 (min=1, max=5)
- **citation_recall**: 0.671
- **avg input_tokens**: 89837
- **avg output_tokens**: 1508
- **avg wall_time_s**: 69.4

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| list | 1 | 4.00 | 3.00 | 3.00 | 0.455 |
| synthesis | 6 | 4.50 | 4.17 | 4.17 | 0.820 |
| definition | 1 | 5.00 | 4.00 | 1.00 | 0.000 |

## Rag mode (8 questions)

- **accuracy**: 4.00 (min=3, max=5)
- **completeness**: 3.12 (min=2, max=5)
- **citation_correctness**: 3.00 (min=2, max=5)
- **citation_recall**: 0.443
- **avg input_tokens**: 12032
- **avg output_tokens**: 394
- **avg wall_time_s**: 31.0

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| list | 1 | 3.00 | 3.00 | 3.00 | 0.364 |
| synthesis | 6 | 4.00 | 2.83 | 3.17 | 0.530 |
| definition | 1 | 5.00 | 5.00 | 2.00 | 0.000 |

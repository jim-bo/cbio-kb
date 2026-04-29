# Eval Report


## Agentic mode (10 questions)

- **accuracy**: 4.30 (min=3, max=5)
- **completeness**: 4.40 (min=3, max=5)
- **citation_correctness**: 4.30 (min=3, max=5)
- **citation_recall**: 0.925
- **avg input_tokens**: 44060
- **avg output_tokens**: 789
- **avg wall_time_s**: 31.2

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 3 | 3.67 | 4.00 | 5.00 | 1.000 |
| list | 2 | 4.00 | 4.50 | 3.50 | 0.875 |
| synthesis | 3 | 4.67 | 4.33 | 3.67 | 0.833 |
| definition | 2 | 5.00 | 5.00 | 5.00 | 1.000 |

## Rag mode (10 questions)

- **accuracy**: 3.80 (min=2, max=5)
- **completeness**: 3.30 (min=1, max=5)
- **citation_correctness**: 3.70 (min=1, max=5)
- **citation_recall**: 0.708
- **avg input_tokens**: 11914
- **avg output_tokens**: 314
- **avg wall_time_s**: 25.6

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 3 | 4.00 | 3.67 | 5.00 | 1.000 |
| list | 2 | 4.00 | 2.50 | 2.50 | 0.375 |
| synthesis | 3 | 3.00 | 2.33 | 2.67 | 0.444 |
| definition | 2 | 4.50 | 5.00 | 4.50 | 1.000 |

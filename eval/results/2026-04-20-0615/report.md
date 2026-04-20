# Eval Report


## Agentic mode (10 questions)

- **accuracy**: 4.60 (min=3, max=5)
- **completeness**: 4.60 (min=3, max=5)
- **citation_correctness**: 4.30 (min=3, max=5)
- **citation_recall**: 0.887
- **avg input_tokens**: 55868
- **avg output_tokens**: 734
- **avg wall_time_s**: 39.9

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 3 | 5.00 | 5.00 | 4.33 | 0.667 |
| list | 2 | 5.00 | 4.50 | 4.50 | 0.938 |
| synthesis | 3 | 3.67 | 4.00 | 3.67 | 1.000 |
| definition | 2 | 5.00 | 5.00 | 5.00 | 1.000 |

## Rag mode (10 questions)

- **accuracy**: 4.50 (min=3, max=5)
- **completeness**: 4.00 (min=1, max=5)
- **citation_correctness**: 4.10 (min=1, max=5)
- **citation_recall**: 0.750
- **avg input_tokens**: 12154
- **avg output_tokens**: 287
- **avg wall_time_s**: 29.0

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 3 | 5.00 | 5.00 | 5.00 | 1.000 |
| list | 2 | 5.00 | 3.50 | 4.50 | 0.750 |
| synthesis | 3 | 3.67 | 2.67 | 2.33 | 0.333 |
| definition | 2 | 4.50 | 5.00 | 5.00 | 1.000 |

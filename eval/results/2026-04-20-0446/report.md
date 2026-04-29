# Eval Report


## Agentic mode (24 questions)

- **accuracy**: 4.38 (min=1, max=5)
- **completeness**: 4.29 (min=1, max=5)
- **citation_correctness**: 4.38 (min=1, max=5)
- **citation_recall**: 0.860
- **avg input_tokens**: 49834
- **avg output_tokens**: 718
- **avg wall_time_s**: 47.3

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 9 | 4.67 | 4.78 | 5.00 | 1.000 |
| list | 6 | 4.00 | 3.33 | 3.50 | 0.640 |
| synthesis | 4 | 3.75 | 3.75 | 3.50 | 0.700 |
| definition | 5 | 4.80 | 5.00 | 5.00 | 1.000 |

## Rag mode (22 questions)

- **accuracy**: 4.41 (min=3, max=5)
- **completeness**: 4.14 (min=2, max=5)
- **citation_correctness**: 4.50 (min=3, max=5)
- **citation_recall**: 0.854
- **avg input_tokens**: 11838
- **avg output_tokens**: 294
- **avg wall_time_s**: 25.9

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 9 | 4.78 | 5.00 | 5.00 | 1.000 |
| list | 5 | 4.20 | 3.00 | 3.40 | 0.579 |
| synthesis | 3 | 3.67 | 3.00 | 4.00 | 0.633 |
| definition | 5 | 4.40 | 4.40 | 5.00 | 1.000 |

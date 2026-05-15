# Eval Report


## Agentic mode (4 questions)

- **accuracy**: 4.25 (min=3, max=5)
- **completeness**: 4.00 (min=3, max=5)
- **citation_correctness**: 4.25 (min=3, max=5)
- **citation_recall**: 0.817
- **avg input_tokens**: 44442
- **avg output_tokens**: 761
- **avg wall_time_s**: 26.7

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 2 | 5.00 | 5.00 | 5.00 | 1.000 |
| list | 1 | 3.00 | 3.00 | 3.00 | 0.600 |
| synthesis | 1 | 4.00 | 3.00 | 4.00 | 0.667 |

## Rag mode (4 questions)

- **accuracy**: 4.75 (min=4, max=5)
- **completeness**: 4.00 (min=2, max=5)
- **citation_correctness**: 4.25 (min=3, max=5)
- **citation_recall**: 0.783
- **avg input_tokens**: 12780
- **avg output_tokens**: 222
- **avg wall_time_s**: 20.6

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 2 | 5.00 | 5.00 | 5.00 | 1.000 |
| list | 1 | 5.00 | 4.00 | 4.00 | 0.800 |
| synthesis | 1 | 4.00 | 2.00 | 3.00 | 0.333 |

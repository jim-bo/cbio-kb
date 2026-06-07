# Eval Report


## Agentic mode (10 scored questions)

- **accuracy**: 4.30 (min=3, max=5)
- **completeness**: 3.90 (min=1, max=5)
- **citation_correctness**: 2.60 (min=1, max=5)
- **citation_recall**: 0.550
- **avg input_tokens**: 241844
- **avg output_tokens**: 785
- **avg wall_time_s**: 14.2

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 3 | 5.00 | 4.67 | 3.67 | 0.667 |
| list | 2 | 3.50 | 3.00 | 2.00 | 0.500 |
| synthesis | 3 | 4.33 | 3.67 | 1.67 | 0.500 |
| definition | 2 | 4.00 | 4.00 | 3.00 | 0.500 |

## Rag mode (10 scored questions)

- **accuracy**: 4.50 (min=3, max=5)
- **completeness**: 3.90 (min=1, max=5)
- **citation_correctness**: 3.90 (min=1, max=5)
- **citation_recall**: 0.750
- **avg input_tokens**: 12154
- **avg output_tokens**: 282
- **avg wall_time_s**: 6.0

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 3 | 5.00 | 5.00 | 5.00 | 1.000 |
| list | 2 | 5.00 | 3.50 | 3.50 | 0.750 |
| synthesis | 3 | 3.67 | 2.67 | 2.33 | 0.333 |
| definition | 2 | 4.50 | 4.50 | 5.00 | 1.000 |

## Hybrid mode (10 scored questions)

- **accuracy**: 4.00 (min=2, max=5)
- **completeness**: 3.30 (min=1, max=5)
- **citation_correctness**: 4.10 (min=1, max=5)
- **citation_recall**: 0.838
- **avg input_tokens**: 3429
- **avg output_tokens**: 258
- **avg wall_time_s**: 5.6

### Per-category breakdown

| category | n | accuracy | completeness | cite_correct | recall |
|----------|---|----------|--------------|--------------|--------|
| lookup | 3 | 4.00 | 3.67 | 5.00 | 1.000 |
| list | 2 | 4.00 | 3.00 | 3.50 | 0.688 |
| synthesis | 3 | 3.67 | 2.33 | 3.00 | 0.667 |
| definition | 2 | 4.50 | 4.50 | 5.00 | 1.000 |

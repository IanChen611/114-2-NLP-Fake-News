# Model Performance

## Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Random Forest | 98.375% | 97.975% | 99.090% | 98.529% |
| DistilBERT | **99.875%** | **99.886%** | **99.886%** | **99.886%** |

## DistilBERT Training Details

| Parameter | Value |
|-----------|-------|
| Epochs | 2 |
| Max Steps | 400 |
| Batch Size | 32 |
| Initial Learning Rate | ~4.5e-5 |
| Final Learning Rate | ~1.25e-7 |

### Training Loss History

| Step | Epoch | Loss | Grad Norm |
|------|-------|------|-----------|
| 50 | 0.25 | 0.1206 | 0.04396 |
| 100 | 0.50 | 0.0123 | 0.02003 |
| 150 | 0.75 | 0.0199 | 0.28776 |
| 200 | 1.00 | 0.0093 | 0.02032 |
| 250 | 1.25 | 0.0011 | 0.01361 |
| 300 | 1.50 | 0.0032 | 0.01082 |
| 350 | 1.75 | 0.0063 | 0.01748 |
| 400 | 2.00 | 0.0082 | 0.01538 |

Total FLOPs: 847,791,351,398,400

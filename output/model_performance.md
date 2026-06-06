# Model Performance

## Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| Random Forest (TF-IDF) | 97.10% | 95.82% | 99.03% | 97.40% |
| DistilBERT (best epoch) | **99.754%** | **99.764%** | **99.788%** | **99.776%** |

> 訓練資料：38,639 筆（全部資料，Reuters 標頭已移除）；測試集：7,728 筆（20%）。

---

## DistilBERT Training Details

| Parameter | Value |
|-----------|-------|
| Base Model | `distilbert-base-uncased` |
| Epochs | 3（最佳模型於 Epoch 2） |
| Total Steps | 2,898 |
| Train Batch Size | 32（GPU）|
| Eval Batch Size | 64（GPU）|
| Max Sequence Length | 256 tokens |
| FP16 Mixed Precision | ✅ 啟用 |
| Device | NVIDIA GeForce RTX 4050 Laptop（6 GB VRAM）|
| Training Time | ~12 分 20 秒 |

### Per-Epoch Evaluation

| Epoch | Training Loss | Val Loss | Accuracy | Precision | Recall | F1 |
|-------|--------------|----------|----------|-----------|--------|----|
| 1 | 0.0149 | 0.0182 | 99.547% | 99.435% | 99.740% | 99.588% |
| **2** ✅ | **0.0038** | **0.0135** | **99.754%** | **99.764%** | **99.788%** | **99.776%** |
| 3 | 0.0008 | 0.0140 | 99.715% | 99.577% | 99.906% | 99.741% |

> Epoch 2 的 F1 最高，`load_best_model_at_end=True` 自動保留此 checkpoint。

---

## Random Forest Details

| Parameter | Value |
|-----------|-------|
| Vectorizer | TF-IDF（max_features=20,000，stop_words='english'）|
| n_estimators | 200 |
| Per-class Report | |

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| Fake (0) | 99% | 95% | 97% | 3,490 |
| Real (1) | 96% | 99% | 97% | 4,238 |

---

## Step 8 實際新聞測試結果

| 文章 | 真實標籤 | RF 預測 | RF P(fake) | BERT 預測 | BERT Score |
|------|---------|---------|------------|----------|------------|
| BBC — Putin/Zelensky 停火談判 | ✅ Real | ✅ Real | 0.2050 | ✅ **REAL** | 99.96% |
| CNN — Trump DOJ anti-weaponization | ✅ Real | ✅ Real | 0.1250 | ✅ **REAL** | 90.68% |
| 假新聞 — Putin 地下城陰謀論 | ❌ Fake | ❌ Real | 0.4800 | ✅ **FAKE** | 99.97% |
| 假新聞 — Trump 秘密島嶼 Deep State | ❌ Fake | ❌ Real | 0.4250 | ✅ **FAKE** | 99.96% |

> **BERT 四篇全部正確**；RF 對兩篇假新聞的信心接近邊界（TF-IDF 無法捕捉語意層面的陰謀論風格）。

---

## 修正歷程：Reuters 偏差問題

| 版本 | 訓練資料 | Epochs | BBC/CNN 真新聞 | 假新聞 |
|------|---------|--------|--------------|--------|
| 舊版（未修正）| 8,000 筆 | 2 | ❌ FAKE 99.5% | ✅ FAKE |
| **新版（修正後）** | **38,639 筆** | **3** | **✅ REAL 99.9%** | **✅ FAKE 99.97%** |

根本原因：Reuters 城市標頭讓 BERT 學到「有 Reuters 格式 = 真新聞」的捷徑；移除標頭並使用全部資料重新訓練後，模型改為從語意與敘事風格判斷真假。

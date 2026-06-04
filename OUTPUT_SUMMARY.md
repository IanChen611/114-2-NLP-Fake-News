# Fake News Detection — Output Summary

所有詳細數據存放於 [`output/`](output/) 資料夾，以下為各檔案內容概覽。

---

## 1. 資料集統計 → [output/dataset_statistics.md](output/dataset_statistics.md)

| | 原始資料 | 清理後 |
|--|---------|--------|
| Fake | 23,481 | 17,449 (45.2%) |
| Real | 21,417 | 21,190 (54.8%) |
| **Total** | **44,898** | **38,639** |

---

## 2. 模型效能 → [output/model_performance.md](output/model_performance.md)

| Model | Accuracy | F1 Score |
|-------|----------|----------|
| Random Forest | 98.375% | 98.529% |
| **DistilBERT** | **99.875%** | **99.886%** |

DistilBERT 訓練：2 epochs、400 steps、batch size 32，loss 從 0.1206 降至 0.0082。

---

## 3. LDA 主題建模 → [output/lda_topics.md](output/lda_topics.md)

- Fake / Real 各 5 個主題
- Fake news 主題關鍵字集中於 obama、clinton、conspiracy 相關詞彙
- Real news 主題多含 "reuters"，顯示來源可信度差異

---

## 4. 視覺化圖表

| 圖表 | 路徑 |
|------|------|
| 文字長度分布 | `dataset/plots/step3_text_distribution.png` |
| Boxplot | `dataset/plots/step3_boxplot.png` |
| 標籤分布 | `dataset/plots/step3_label_distribution.png` |
| TF-IDF 關鍵字 | `dataset/plots/step4_tfidf_keywords.png` |
| WordCloud (Fake) | `dataset/plots/step4_wordcloud_fake.png` |
| WordCloud (Real) | `dataset/plots/step4_wordcloud_real.png` |
| LDA Heatmap (Fake) | `dataset/plots/step4_lda_heatmap_fake.png` |
| LDA Heatmap (Real) | `dataset/plots/step4_lda_heatmap_real.png` |
| RF Confusion Matrix | `dataset/plots/rf_confusion_matrix_*.png` |
| LIME Explanation | `dataset/plots/lime_predict_explain_*.png` |

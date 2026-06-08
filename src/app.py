"""
Fake News 偵測 Demo App
輸入一段新聞文字，按下「開始預測」即可看到模型判斷為 True / Fake 的機率。
模型來源：src/main.ipynb Step 5 訓練並儲存於 dataset/bert_out 的 DistilBERT checkpoint。

執行方式：
    streamlit run src/app.py
"""
import os
import json

import streamlit as st
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

DATA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "dataset"))
BERT_ROOT = os.path.join(DATA_ROOT, "bert_out")


def find_bert_dir(root):
    if not os.path.isdir(root):
        return None
    best_dir, best_step = None, -1
    for sub in os.listdir(root):
        p = os.path.join(root, sub)
        cfg = os.path.join(p, "config.json")
        if os.path.isdir(p) and os.path.exists(cfg):
            try:
                step = int(sub.split("-")[-1])
            except ValueError:
                step = 0
            if step > best_step:
                best_dir, best_step = p, step
    return best_dir


@st.cache_resource(show_spinner="載入模型中...")
def load_model():
    bert_dir = find_bert_dir(BERT_ROOT)
    if bert_dir is None:
        raise FileNotFoundError(f"在 {BERT_ROOT} 找不到可用的 BERT checkpoint")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
    model = DistilBertForSequenceClassification.from_pretrained(bert_dir).to(device)
    model.eval()

    with open(os.path.join(bert_dir, "config.json"), encoding="utf-8") as f:
        id2label = json.load(f)["id2label"]

    return tokenizer, model, device, id2label, bert_dir


def predict(text, tokenizer, model, device, id2label):
    inputs = tokenizer(text, truncation=True, max_length=256, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)[0].tolist()

    prob_by_label = {id2label[str(i)]: p for i, p in enumerate(probs)}
    return prob_by_label.get("REAL", 0.0), prob_by_label.get("FAKE", 0.0)


st.set_page_config(page_title="Fake News 偵測 Demo", page_icon="📰")
st.title("📰 Fake News 偵測 Demo")
st.caption("使用 src/main.ipynb 訓練的 DistilBERT 模型（dataset/bert_out）")

text = st.text_area("請輸入想預測的新聞內容：", height=250, placeholder="在此貼上新聞文字...")

if st.button("開始預測", type="primary"):
    if not text.strip():
        st.warning("請先輸入新聞內容。")
    else:
        try:
            tokenizer, model, device, id2label, bert_dir = load_model()
        except FileNotFoundError as e:
            st.error(str(e))
        else:
            real_prob, fake_prob = predict(text, tokenizer, model, device, id2label)
            st.subheader("預測結果")
            col1, col2 = st.columns(2)
            col1.metric("判斷為 True（真新聞）", f"{real_prob * 100:.2f} %")
            col2.metric("判斷為 Fake（假新聞）", f"{fake_prob * 100:.2f} %")
            st.progress(real_prob, text=f"True {real_prob * 100:.1f}% / Fake {fake_prob * 100:.1f}%")
            st.caption(f"模型路徑：{bert_dir}（裝置：{device}）")

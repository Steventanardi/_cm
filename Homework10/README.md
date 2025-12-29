# Homework 11 - Scikit-Learn Examples

本作業展示了使用 `scikit-learn` 進行機器學習的三種範例：分類 (Classification)、分群 (Clustering) 與回歸 (Regression)。

## 範例說明

### 1. 分類 (Classification) - `classification.py`
使用 **Breast Cancer (乳腺癌)** 資料集，透過 **Support Vector Machine (SVM)** 分類器進行預測。
- **目標**：將腫瘤分類為良性或惡性。
- **執行方式**：`python classification.py`

### 2. 分群 (Clustering) - `clustering.py`
使用隨機生成的二維資料集 (make_blobs)，透過 **K-Means** 演算法進行分群。
- **目標**：自動將資料點劃分為 4 個不同的群集。
- **執行方式**：`python clustering.py`

### 3. 回歸 (Regression) - `regression.py`
使用 **Diabetes (糖尿病)** 資料集，透過 **Ridge (脊迴歸)** 模型進行預測。
- **目標**：預測一年後疾病進展的量化指標。
- **執行方式**：`python regression.py`

## 環境需求
請確保已安裝必要的 Python 庫：
```bash
pip install scikit-learn matplotlib numpy
```

## 注意事項
- 本作業完全避開了 `iris` 資料集，符合要求。
- 每個腳本執行後均會顯示視覺化圖形或評估報告。

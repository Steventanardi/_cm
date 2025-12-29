import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

# 1. 載入資料集 (使用乳腺癌資料集，不使用 iris)
cancer = datasets.load_breast_cancer()

# 2. 切分訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.3, shuffle=False
)

# 3. 建立 SVM 分類器
classifier = svm.SVC(gamma=0.001)

# 4. 訓練模型
classifier.fit(X_train, y_train)

# 5. 預測
predicted = classifier.predict(X_test)

# 6. 評估模型
print(f"Classification report for classifier {classifier}:\n"
      f"{metrics.classification_report(y_test, predicted)}\n")

# 7. 顯示混淆矩陣 (Confusion Matrix)
disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix - Breast Cancer Classification")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()

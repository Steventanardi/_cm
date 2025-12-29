import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# 1. 載入資料集 (使用糖尿病資料集，不使用 iris)
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# 2. 只使用一個特徵以便於繪圖
diabetes_X = diabetes_X[:, np.newaxis, 2]

# 3. 切分訓練集與測試集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# 4. 建立線性回歸模型 (使用 Ridge 脊迴歸作為範例)
regr = linear_model.Ridge(alpha=.5)

# 5. 訓練模型
regr.fit(diabetes_X_train, diabetes_y_train)

# 6. 預測
diabetes_y_pred = regr.predict(diabetes_X_test)

# 7. 評估模型
print("Coefficients: \n", regr.coef_)
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("Coefficient of determination (R2): %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# 8. 繪製結果
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.title("Ridge Regression Example - Diabetes Dataset")
plt.xlabel("Feature (Scaled Third Column)")
plt.ylabel("Target (Disease Progression)")
plt.show()

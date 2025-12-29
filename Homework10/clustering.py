import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# 1. 產生用於分群的模擬資料 (不使用 iris)
n_samples = 300
X, y = make_blobs(n_samples=n_samples, centers=4, cluster_std=0.60, random_state=0)

# 2. 建立 K-Means 模型，設定標籤數量為 4
kmeans = KMeans(n_clusters=4, n_init='auto')

# 3. 進行分群
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# 4. 繪製結果
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

# 繪製分群中心
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)

plt.title("K-Means Clustering Example")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

print("K-Means clustering completed. Plot displayed.")

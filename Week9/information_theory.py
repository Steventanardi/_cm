import math
import numpy as np

# 1. Probability of a fair coin flipping heads 10000 times in a row
def coin_flip_probability(n=10000, p=0.5):
    return p ** n

# 2. Log-probability calculation: log(p^n) = n * log(p)
def coin_flip_log_probability(n=10000, p=0.5):
    # Using base 2 for bits
    return n * math.log2(p)

# 3. Information Theory Metrics
def entropy(p):
    p = np.array(p)
    return -np.sum(p * np.log2(p + 1e-12))

def cross_entropy(p, q):
    p, q = np.array(p), np.array(q)
    return -np.sum(p * np.log2(q + 1e-12))

def kl_divergence(p, q):
    p, q = np.array(p), np.array(q)
    return np.sum(p * np.log2((p + 1e-12) / (q + 1e-12)))

def mutual_information(p_xy):
    p_xy = np.array(p_xy)
    p_x = np.sum(p_xy, axis=1)
    p_y = np.sum(p_xy, axis=0)
    
    mi = 0
    for i in range(len(p_x)):
        for j in range(len(p_y)):
            if p_xy[i, j] > 0:
                mi += p_xy[i, j] * math.log2(p_xy[i, j] / (p_x[i] * p_y[j]))
    return mi

if __name__ == "__main__":
    n = 10000
    p = 0.5
    
    print(f"--- Information Theory Calculations (n={n}, p={p}) ---\n")
    
    # Probabilities
    prob = coin_flip_probability(n, p)
    log_prob = coin_flip_log_probability(n, p)
    print(f"1. Probability of {n} consecutive heads: {prob}")
    print(f"2. Log2 probability of {n} consecutive heads: {log_prob} bits")
    
    # 4. Verifying Gibbs' Inequality: H(P, P) <= H(P, Q) or KL(P || Q) >= 0
    # Let P be [0.5, 0.5] and Q be [0.8, 0.2]
    P = [0.5, 0.5]
    Q = [0.8, 0.2]
    
    ce_pp = cross_entropy(P, P)
    ce_pq = cross_entropy(P, Q)
    kl_pq = kl_divergence(P, Q)
    
    print(f"\n3. Metrics with P={P}, Q={Q}:")
    print(f"   Entropy H(P): {ce_pp:.4f} bits")
    print(f"   Cross-Entropy H(P, Q): {ce_pq:.4f} bits")
    print(f"   KL Divergence KL(P||Q): {kl_pq:.4f} bits")
    
    print("\n4. Verifying Gibbs' Inequality (H(P,P) < H(P,Q) when P != Q):")
    if ce_pp < ce_pq:
        print(f"   Success: {ce_pp:.4f} < {ce_pq:.4f}")
    
    # MI Example
    # Joint distribution for two fair coins that are perfectly correlated
    p_xy = [[0.5, 0.0], [0.0, 0.5]]
    mi = mutual_information(p_xy)
    print(f"\n5. Mutual Information (Perfectly correlated coins): {mi:.2f} bits")

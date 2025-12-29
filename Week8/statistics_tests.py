import math

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_variance(data, is_sample=True):
    mean = calculate_mean(data)
    n = len(data)
    return sum((x - mean) ** 2 for x in data) / (n - 1 if is_sample else n)

def calculate_std(data, is_sample=True):
    return math.sqrt(calculate_variance(data, is_sample))

# 1. One-Sample Z-Test (Population Standard Deviation known)
def z_test_one_sample(sample_data, pop_mean, pop_std):
    sample_mean = calculate_mean(sample_data)
    n = len(sample_data)
    z_score = (sample_mean - pop_mean) / (pop_std / math.sqrt(n))
    return z_score

# 2. One-Sample T-Test (Population Standard Deviation unknown)
def t_test_one_sample(sample_data, pop_mean):
    sample_mean = calculate_mean(sample_data)
    sample_std = calculate_std(sample_data, is_sample=True)
    n = len(sample_data)
    t_score = (sample_mean - pop_mean) / (sample_std / math.sqrt(n))
    return t_score

# 3. Independent Two-Sample T-Test
def t_test_independent(group1, group2):
    mean1, mean2 = calculate_mean(group1), calculate_mean(group2)
    var1, var2 = calculate_variance(group1), calculate_variance(group2)
    n1, n2 = len(group1), len(group2)
    
    # Pooled variance (assuming equal variance)
    pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
    t_score = (mean1 - mean2) / math.sqrt(pooled_var * (1/n1 + 1/n2))
    return t_score

# 4. Paired Sample T-Test
def t_test_paired(before, after):
    differences = [a - b for a, b in zip(after, before)]
    return t_test_one_sample(differences, 0)

if __name__ == "__main__":
    print("--- Statistics Tests Demonstration ---\n")
    
    # Example for Z-test
    pop_mean = 100
    pop_std = 15
    sample = [110, 105, 115, 120, 110]
    z = z_test_one_sample(sample, pop_mean, pop_std)
    print(f"One-Sample Z-Test: z = {z:.4f}")
    
    # Example for One-Sample T-test
    t1 = t_test_one_sample(sample, pop_mean)
    print(f"One-Sample T-Test: t = {t1:.4f}")
    
    # Example for Independent T-test
    g1 = [85, 90, 88, 92, 89]
    g2 = [75, 80, 78, 82, 79]
    t2 = t_test_independent(g1, g2)
    print(f"Independent T-Test: t = {t2:.4f}")
    
    # Example for Paired T-test
    before = [80, 85, 78, 92, 88]
    after = [82, 88, 80, 95, 90]
    t3 = t_test_paired(before, after)
    print(f"Paired T-Test: t = {t3:.4f}")

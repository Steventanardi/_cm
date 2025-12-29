# Mathematical Principles of Hypothesis Testing

This document explains the derivation and logic behind the Z-test and T-test.

## 1. The Central Limit Theorem (CLT)
The foundation of these tests is the CLT, which states that the distribution of sample means approaches a normal distribution as the sample size increases, regardless of the population distribution.

## 2. One-Sample Z-Test
Used when the population variance $\sigma^2$ is **known**.
- **Formula**: $$ z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} $$
- **Derivation**: We standardize the sample mean $\bar{x}$ by subtracting the population mean $\mu$ and dividing by the standard error $\sigma / \sqrt{n}$.

## 3. One-Sample T-Test
Used when the population variance is **unknown**. We estimate it using the sample standard deviation $s$.
- **Formula**: $$ t = \frac{\bar{x} - \mu}{s / \sqrt{n}} $$
- **Key Difference**: The T-statistic follows a Student's t-distribution with $n-1$ degrees of freedom. This distribution has "heavier tails" to account for the uncertainty in estimating the variance.

## 4. Independent Two-Sample T-Test
Used to compare the means of two independent groups.
- **Pooled Variance**: $$ s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2} $$
- **Formula**: $$ t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2 (\frac{1}{n_1} + \frac{1}{n_2})}} $$

## 5. Paired Sample T-Test
Used when comparing the same subjects over time (e.g., before and after).
- **Logic**: It is mathematically identical to a one-sample T-test performed on the *differences* ($D = x_{after} - x_{before}$) between the pairs, testing against a null hypothesis of $\mu_D = 0$.
- **Formula**: $$ t = \frac{\bar{D} - 0}{s_D / \sqrt{n}} $$

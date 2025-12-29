import numpy as np
from collections import Counter

def solve_ode_general(coefficients):
    # Find roots of characteristic equation
    roots = np.roots(coefficients)
    
    # Numerical cleaning and grouping
    # High-order repeated roots are numerically unstable in np.roots
    # We will use a tolerance to group roots that are nearly identical
    tolerance = 1e-4
    
    unique_real = [] # List of [value, count]
    unique_complex = [] # List of [(alpha, beta), count] (beta positive)

    processed_indices = set()
    
    for i in range(len(roots)):
        if i in processed_indices: continue
        
        r1 = roots[i]
        alpha1 = np.real(r1)
        beta1 = np.imag(r1)
        
        # Group identical/near-identical roots
        group = [i]
        for j in range(i + 1, len(roots)):
            if j in processed_indices: continue
            if np.isclose(r1, roots[j], atol=tolerance):
                group.append(j)
        
        processed_indices.update(group)
        mult = len(group)
        
        if abs(beta1) < tolerance:
            # Real root
            unique_real.append([alpha1, mult])
        else:
            # Complex root
            # Find if its conjugate was already added or subtract half if we treat them in pairs
            # Actually, np.roots returns both alpha+ib and alpha-ib.
            # We want to group (alpha, |beta|) and count how many pairs we have.
            # Since we iterate through ALL roots, we'll find both +i*beta and -i*beta.
            # Let's count them all and divide by 2 for pairs.
            beta_abs = abs(beta1)
            
            found_pair = False
            for k in range(len(unique_complex)):
                c_alpha, c_beta = unique_complex[k][0]
                if np.isclose(alpha1, c_alpha, atol=tolerance) and np.isclose(beta_abs, c_beta, atol=tolerance):
                    unique_complex[k][1] += mult
                    found_pair = True
                    break
            
            if not found_pair:
                unique_complex.append([(alpha1, beta_abs), mult])

    # Construct terms
    terms = []
    c_idx = 1
    
    # 1. Real Roots
    for r, mult in sorted(unique_real, key=lambda x: x[0], reverse=True):
        for m in range(mult):
            x_term = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
            exp_val = f"{round(r, 4)}"
            terms.append(f"C_{c_idx}{x_term}e^({exp_val}x)")
            c_idx += 1
            
    # 2. Complex Roots
    for (alpha, beta), total_mult in sorted(unique_complex, key=lambda x: x[0][0], reverse=True):
        # total_mult is sum of counts of +i*beta and -i*beta roots.
        # For a standard pair with multiplicity m, total_mult should be 2m.
        pair_mult = int(round(total_mult / 2))
        for m in range(pair_mult):
            x_term = f"x^{m}" if m > 1 else ("x" if m == 1 else "")
            prefix = ""
            if abs(alpha) > 1e-4:
                prefix = f"e^({round(alpha, 4)}x)"
            
            b_str = f"{round(beta, 4)}"
            terms.append(f"C_{c_idx}{x_term}{prefix}cos({b_str}x)")
            c_idx += 1
            terms.append(f"C_{c_idx}{x_term}{prefix}sin({b_str}x)")
            c_idx += 1
            
    return "y(x) = " + " + ".join(terms)


if __name__ == "__main__":
    # Example 1: Real single roots
    print("--- Real Single Roots Example ---")
    coeffs1 = [1, -3, 2] # y'' - 3y' + 2y = 0 -> (r-2)(r-1)=0
    print(f"Equations coefficients: {coeffs1}")
    print(solve_ode_general(coeffs1))

    # Example 2: Real repeated roots
    print("\n--- Real Repeated Roots Example ---")
    coeffs2 = [1, -4, 4] # y'' - 4y' + 4y = 0 -> (r-2)^2 = 0
    print(f"Equations coefficients: {coeffs2}")
    print(solve_ode_general(coeffs2))

    # Example 3: Complex conjugate roots
    print("\n--- Complex Conjugate Roots Example ---")
    coeffs3 = [1, 0, 4] # y'' + 4y = 0 -> r^2 + 4 = 0 -> r = +/- 2i
    print(f"Equations coefficients: {coeffs3}")
    print(solve_ode_general(coeffs3))

    # Example 4: Complex repeated roots
    print("\n--- Complex Repeated Roots Example ---")
    coeffs4 = [1, 0, 2, 0, 1] # (D^2 + 1)^2 y = 0 -> (r^2+1)^2 = 0 -> r = +/- i (mult 2)
    print(f"Equations coefficients: {coeffs4}")
    print(solve_ode_general(coeffs4))

    # Example 5: High-order real repeated roots
    print("\n--- High-order Repeated Roots Example ---")
    coeffs5 = [1, -6, 12, -8] # (r-2)^3 = 0
    print(f"Equations coefficients: {coeffs5}")
    print(solve_ode_general(coeffs5))

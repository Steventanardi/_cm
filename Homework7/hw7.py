# A simple simulation of what the gradient descent code would do
# Function: f = x^2 + y^2 + z^2 - 2x - 4y - 6z + 8

# 1. Initialize variables (starting guess)
x = 0.0
y = 0.0
z = 0.0

# 2. Set learning rate (step size) and iterations
learning_rate = 0.1
iterations = 100

print(f"Start: x={x}, y={y}, z={z}")

# 3. Gradient Descent Loop
for i in range(iterations):
    # Calculate gradients (derivatives)
    grad_x = 2*x - 2
    grad_y = 2*y - 4
    grad_z = 2*z - 6
    
    # Update variables (move opposite to the gradient)
    x -= learning_rate * grad_x
    y -= learning_rate * grad_y
    z -= learning_rate * grad_z

print(f"Final Result after {iterations} steps:")
print(f"x = {x:.4f} (Expected: 1.0)")
print(f"y = {y:.4f} (Expected: 2.0)")
print(f"z = {z:.4f} (Expected: 3.0)")

# Calculate final value
f_val = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8
print(f"Minimum Value = {f_val:.4f} (Expected: -6.0)")
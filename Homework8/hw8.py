import torch


x = torch.tensor([0.0], requires_grad=True)
y = torch.tensor([0.0], requires_grad=True)
z = torch.tensor([0.0], requires_grad=True)

optimizer = torch.optim.SGD([x, y, z], lr=0.1)

print(f"Start: x={x.item():.2f}, y={y.item():.2f}, z={z.item():.2f}")

for i in range(100):
  
    optimizer.zero_grad()

    f = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8
    
    f.backward()
    
    optimizer.step()
    
    if i % 10 == 0:
        print(f"Step {i}: f={f.item():.4f} | x={x.item():.3f}, y={y.item():.3f}, z={z.item():.3f}")

print("-" * 30)
print("Final Result:")
print(f"x = {x.item():.4f} (Target: 1.0)")
print(f"y = {y.item():.4f} (Target: 2.0)")
print(f"z = {z.item():.4f} (Target: 3.0)")
print(f"Min Value = {f.item():.4f} (Target: -6.0)")
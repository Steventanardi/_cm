import torch


x = torch.tensor([0.0], requires_grad=True)
y = torch.tensor([0.0], requires_grad=True)
z = torch.tensor([0.0], requires_grad=True)


optimizer = torch.optim.SGD([x, y, z], lr=0.1)

print(f"Start: x={x.item()}, y={y.item()}, z={z.item()}")

for i in range(100):
    optimizer.zero_grad()  
    
    f = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8
    
    f.backward()    
    optimizer.step() 


print("-" * 20)
print(f"Found Minimum at: x={x.item():.2f}, y={y.item():.2f}, z={z.item():.2f}")
print(f"Minimum Value: {f.item():.2f}")

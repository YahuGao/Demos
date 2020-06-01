import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x + 2
print(y)
print(y.grad_fn)

z = y * y * 3
out = z.mean()

'''
All Tensors that have requires_grad which is False will be leaf
Tensors by convention.

For Tensors that have requires_grad which is True, they will be leaf
Tensors if they were created by the user. This means that they are not
the result of an operation and so grad_fn is None.

Only leaf Tensors will have their grad populated during a call to
backward(). To get grad populated for non-leaf Tensors, you can use
retain_grad().
'''

y.retain_grad()
z.retain_grad()
out.retain_grad()
out.backward()
print(x.grad)
print(y.grad)
print(z.grad)
print(out.grad)
print(x)
print(y)
print(z)
print(out)

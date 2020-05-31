#!/usr/bin/env python
import torch

TEST = True

def test_print(x):
    if TEST:
        print(x)


x = torch.empty(5,3)
test_print(x)

x = torch.rand(5, 3)
test_print(x)

x = torch.zeros(5, 3, dtype=torch.long)
test_print(x)

# construct a tensor with data
x = torch.tensor([5.5, 3])
test_print(x)

x = x.new_ones(5, 3, dtype=torch.double)
test_print(x)

print(x.size())

y = torch.rand(5, 3, dtype=torch.float)
print(y)

print(torch.add(x, y))

result = torch.empty(5, 3)
torch.add(x,y, out=result)
print(result)

print(result[:, 1])

print(result.size())
print(result.view(-1, 1).size())
print(result.view(15))

print(torch.randn(1))
print(torch.randn(1).size())
print(result.data)
print(result)
print(type(result))
print(type(result.data))

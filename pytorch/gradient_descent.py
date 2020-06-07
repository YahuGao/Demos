import numpy as np
import torch

# N: batch size, D_in: dim of input
# H: hidden dim, D_out: dim of output

N, D_in, H, D_out = 64, 1000, 100, 10

# Create input and output data
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

dtype = torch.float
device = torch.device("cpu")

x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.rand(N, D_out, device=device, dtype=dtype)

# Initial weight
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

w1 = torch.randn(D_in, H, device=device, dtype=dtype)
w2 = torch.randn(H, D_out, device=device, dtype=dtype)

learning_rate = 0.001
for t in range(500):
    # forward: compute predicte y
    # h = x.dot(w1)
    # h_relu = np.maximum(h, 0)
    # y_pred = h_relu.dot(w2)
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)
    # compute loss
    # loss = np.square(y_pred - y).sum()
    loss = (y_pred - y).pow(2).sum().item()
    print(t, loss)

    # backward: compute gradient
    grad_y_pred = 2.0 * (y_pred - y)
    # grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    # grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h_relu = grad_y_pred.mm(w2.t())
    # grad_h = grad_h_relu.copy()
    grad_h = grad_h_relu.clone()
    grad_h[h< 0] = 0
    # grad_w1 = x.T.dot(grad_h)
    grad_w1 = x.t().mm(grad_h)

    # update weight
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2

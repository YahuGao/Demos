import torch

class MyReLu(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        ctx.save_for_backward(x)
        return x.clamp(min=0)

    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        grad_x = grad_output.clone()
        grad_x[x < 0] = 0
        return grad_x

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

N, D_in, H, D_out = 64, 1000, 100, 10

x = torch.randn(N, D_in, device=device, requires_grad=True)
y = torch.randn(N, D_out, device=device, requires_grad=True)

w1 = torch.randn(D_in, H, device=device, requires_grad=True)
w2 = torch.randn(H, D_out, device=device, requires_grad=True)

lr = 0.001

for t in range(500):
    y_pred = MyReLu.apply(x.mm(w1)).mm(w2)

    loss = (y_pred - y).pow(2).sum()
    print(t, loss.item())

    loss.backward()

    with torch.no_grad():
        w1 -= lr * w1.grad
        w2 -= lr * w2.grad

        w1.grad.zero_()
        w2.grad.zero_()

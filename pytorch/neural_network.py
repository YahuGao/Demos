'''
A classical process of training neural network is:
 1.定义一个包含可训练参数的神经网络
 2.迭代整个输入
 3.通过神经网络处理输入
 4.计算损失(loss)
 5.反向传播梯度到神经网络的参数
 6.更新网络的参数,一个简单典型的更新方法:
   weight = weight - learning_rate *gradient
'''
import torch
import torch.nn as nn
import torch.nn.functional as F

# Define a neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 5x5 square
        # convolution kernel
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2,2))
        # if the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:] # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *=s
        return num_features

net = Net()
print(net)

# Get trainable parameters of a NET
paras = net.parameters()
print(type(paras)) # a generator

paras = list(paras)
print(type(paras))
print(paras[0].size())

# Process input data
input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)

# clean gradients of parameters
net.zero_grad()
# Do backward with a random gradient
out.backward(torch.randn(1,10))


output = net(input)
target = torch.randn(1,10) # a dummy target, for example
# make it the same shape with output
target = target.view(1, -1)

criterion = torch.nn.MSELoss()

loss = criterion(target, output)
print(loss.grad_fn)
print(loss.grad_fn.next_functions[0][0].next_functions[0][0])

net.zero_grad()
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)
loss.backward()
print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

learning_rate = 0.1
for f in net.parameters():
    f.data.sub_(f.grad.data * learning_rate)

# update parameters with torch.optim
import torch.optim as optim

optimizer = optim.SGD(net.parameters(), lr=0.01)
optimizer.zero_grad()
output = net(input)
loss = criterion(target, output)
loss.backward()
optimizer.step()   # Does the update


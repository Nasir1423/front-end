import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 构造样本数据
# 生成包含200个数据点的等间距数组，范围从-pi到2*pi
x = torch.unsqueeze(torch.linspace(-np.pi, np.pi * 2, 200), dim=1)

# 生成目标输出数据 y，通过对 x 的余弦值加上一些随机噪声得到
y = torch.cos(x) + 0.3 * torch.rand(x.size())


# 构建网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 定义神经网络的结构
        self.predict = nn.Sequential(
            nn.Linear(1, 20),  # 输入层到隐含层的线性变换，输入维度为1，输出维度为20
            nn.ReLU(),  # 使用ReLU激活函数
            nn.Linear(20, 1)  # 隐含层到输出层的线性变换，输入维度为20，输出维度为1
        )

    def forward(self, x):
        # 定义前向传播过程
        out = self.predict(x)
        return out


# 训练网络
net = Net()
optimizer = torch.optim.SGD(net.parameters(), lr=0.05)  # 使用随机梯度下降算法进行优化
loss_func = nn.MSELoss()  # 定义均方误差损失函数

plt.ion()  # 打开交互模式，以便动态显示训练过程
for epoch in range(6000):
    out = net(x)  # 前向传播
    loss = loss_func(out, y)  # 计算损失
    optimizer.zero_grad()  # 梯度清零
    loss.backward()  # 反向传播
    optimizer.step()  # 更新参数

    # 每隔一段时间就绘制当前的拟合结果
    if epoch % 200 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())  # 绘制原始数据散点图
        plt.plot(x.data.numpy(), out.data.numpy(), 'r-', lw=3)  # 绘制拟合曲线
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})  # 显示当前损失值
        plt.pause(0.1)

plt.ioff()  # 关闭交互模式
plt.show()

# 测试网络
# 生成新的测试数据
x_test = torch.unsqueeze(torch.linspace(-np.pi, np.pi * 2, 100), dim=1)
# 在测试数据上进行预测
y_pred = net(x_test)

# 绘制测试结果
plt.scatter(x_test.data.numpy(), y_pred.data.numpy(), color='r', label='Predictions')  # 绘制预测结果散点图
plt.plot(x.data.numpy(), y.data.numpy(), 'b--', label='Original Data')  # 绘制原始数据曲线
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regression Test')
plt.show()

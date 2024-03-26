import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 构造样本集
# 第一类数据均值为2，方差为1
x0 = torch.normal(mean=2, std=1, size=(100, 2))
# 第二类数据均值为-2，方差为1
x1 = torch.normal(mean=-2, std=1, size=(100, 2))
# 合并样本集
x = torch.cat((x0, x1), 0).type(torch.FloatTensor)

# 标签生成
y0 = torch.zeros(100)  # 第一类标签
y1 = torch.ones(100)  # 第二类标签
y = torch.cat((y0, y1)).type(torch.LongTensor)


# 构建网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.classify = nn.Sequential(
            nn.Linear(2, 15),  # 输入层到隐含层
            nn.ReLU(),  # ReLU激活函数
            nn.Linear(15, 2),  # 隐含层到输出层
            nn.Softmax(dim=1)  # Softmax函数输出结果
        )

    def forward(self, x):
        classification = self.classify(x)
        return classification


# 训练网络
net = Net()
optimizer = torch.optim.SGD(net.parameters(), lr=0.03)
loss_func = nn.CrossEntropyLoss()

for epoch in range(100):
    out = net(x)
    loss = loss_func(out, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# 可视化
# 获取每个点的分类结果
classification = torch.max(out, 1)[1].data.numpy()

# 绘制散点图
plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=classification, s=100, cmap='RdYlGn')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Classification Result')

# 计算准确率
accuracy = sum(classification == y.data.numpy()) / 200
# 显示准确率
plt.text(1.5, -4, f'Accuracy={accuracy}', fontdict={'size': 20, 'color': 'red'})

plt.show()

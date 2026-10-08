###分为几步
#数据集√    数据集扩展√     写net（在net.py）   训练    测试
###
import torchvision
import torch
import numpy as np
import torchvision.transforms as transforms
import torch.utils.data
import cv2
import matplotlib.pyplot as plt
# %matplotlib inline
import os
from PIL import Image
import torch.nn.functional as f
import torchvision.datasets
from torchvision.datasets import ImageFolder
import torch.optim as optim
import torch.nn as nn
from sklearn.model_selection import KFold
# 超参数         一会会用验证集再训练
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
EPOCH = 30
BATCH_SIZE = 256
class AlexNet(nn.Module):
    def __init__(self, num_classes=2, init_weights=False):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 48, kernel_size=11),  # input[3, 65,65]  output[48, 55, 55]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[48, 27, 27]
            nn.BatchNorm2d(48),
            nn.Conv2d(48, 128, kernel_size=5, padding=2),           # output[128, 27, 27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 13, 13]
            nn.BatchNorm2d(128),
            nn.Conv2d(128, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 128, kernel_size=3, padding=1),          # output[128, 13, 13]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 6, 6],
        )
        self.classifier = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(128 * 6 * 6, 2048),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, num_classes),
        )
        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, start_dim=1)
        x = self.classifier(x)
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)


# 数据处理
# # 数据预处理
aim_dir0 = r'C:\Users\mjr\PycharmProjects\Nets\EN\0'
aim_dir1 = r'C:\Users\mjr\PycharmProjects\Nets\EN\1'
source_path0 = r'C:\Users\mjr\PycharmProjects\Nets\kaggle\train\0'
source_path1 = r'C:\Users\mjr\PycharmProjects\Nets\kaggle\train\1'
def dataEnhance(sourth_path,aim_dir,size):
    h = 0
    #得到目标文件的文件和文件名
    file_list = os.listdir(sourth_path)
    #创建目标文件夹
    if not os.path.exists(aim_dir):
        os.mkdir(aim_dir)
    #对目标文件夹内的文件进行遍历
    for i in file_list:
        img = Image.open('%s\%s'%(sourth_path, i))
        print(img.size)
        h = h + 1
        transform1 = transforms.Compose([
            transforms.ToTensor(),
            transforms.ToPILImage(),
            transforms.Resize(size),
        ])
        img1 = transform1(img)
        img1.save('%s/%s.png'%(aim_dir,h))
        h = h + 1
        transform2 = transforms.Compose([
            transforms.ToTensor(),
            transforms.ToPILImage(),
            transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5),  #颜色变换
            transforms.Resize(size),  # 缩放成227*227
        ])
        img2 = transform2(img)
        img2.save('%s/%s.png'%(aim_dir,h))
        h = h + 1
        transform3 = transforms.Compose([
            transforms.ToTensor(),
            transforms.ToPILImage(),
            transforms.RandomCrop(227,pad_if_needed=True),  #随机剪裁
            transforms.Resize(size),
        ])
        img3 = transform3(img)
        img3.save('%s/%s.png'%(aim_dir,h))
        h = h + 1
        transform4 = transforms.Compose([
            transforms.ToTensor(),
            transforms.ToPILImage(),
            transforms.RandomRotation(60),   #随机旋转20度
            transforms.Resize(size),  # 缩放成227*227
        ])
        img4 = transform4(img)
        img4.save('%s/%s.png'%(aim_dir,h))



normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
# 数据增强图片的生成和保存（由于已经运行故标注，如第一次运行要取消标注运行）
# dataEnhance(source_path0,aim_dir0,(65,65))
# dataEnhance(source_path1,aim_dir1,(65,65))

path = r"C:\Users\mjr\PycharmProjects\Nets\EN"
trans = transforms.Compose([
        transforms.ToTensor(),
        normalize,
        ])
dataset = ImageFolder(root = path,transform=trans)
train_loader = torch.utils.data.DataLoader(dataset,
                                           batch_size=BATCH_SIZE, shuffle=True,
                                           num_workers=0)

path1 = r"C:\Users\mjr\PycharmProjects\Nets\kaggle\test"
transf = transforms.Compose([
        transforms.Resize((65,65)),
        transforms.ToTensor(),
        normalize,
        ])
datasettest = ImageFolder(root = path1,transform=transf)
test_loader = torch.utils.data.DataLoader(datasettest,
                                           batch_size=BATCH_SIZE, shuffle=True,
                                           num_workers=0)
path2 = r"C:\Users\mjr\PycharmProjects\Nets\kaggle\valid"
transf = transforms.Compose([
        transforms.Resize((65,65)),
        transforms.ToTensor(),
        normalize,
        ])
datasetvalid = ImageFolder(root = path2,transform=transf)
valid_loader = torch.utils.data.DataLoader(datasetvalid,
                                           batch_size=BATCH_SIZE, shuffle=True,
                                           num_workers=0)

model = AlexNet().to(DEVICE)
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9,weight_decay=0.0005)    #随机梯度下降


# # 训练（传入模型，cpu/gpu,训练数据，优化器，历元（次数））
def train_model(model, device, train_loader, optimizer, epoch):
    # 模型训练-----调取方法
    train_loss = 0
    model.train()
    for batch_index, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = f.cross_entropy(output, target)
        loss.backward()
        optimizer.step()
        if batch_index % 300 == 0:
            train_loss = loss.item()
            print("Train Epoch : {} \t train Loss : {:.6f} ".format(epoch, loss.item()))
    return train_loss



# 定义测试方法
def test_model(model, device, test_loader):
    # 模型验证-----否则的话，有输入数据，即使不训练，它也会改变权值---为了固定BN（批量归一化）层
    model.eval()
    correct = 0.0
    test_loss = 0.0
    with torch.no_grad():
        for data, target in test_loader:
            # 部署到device上
            data, target = data.to(device), target.to(device)
            # 测试数据
            output = model(data)
            # 计算测试损失------测试损失加和 += 交叉熵损失（输出预测值，标签）的数值
            test_loss += f.cross_entropy(output, target).item()
            pred = output.argmax(dim=1)
            print(target)
            print(pred)
            correct += pred.eq(target.view_as(pred)).sum().item()
        test_loss /= len(test_loader.dataset)
        print("Test_average_loss : {:.4f} , Accuracy : {:.3f}%\n".format(test_loss,
                                                                         100 * correct / len(test_loader.dataset)))
        acc = 100 * correct / len(test_loader.dataset)
        return test_loss,acc


#
# 调用方法
list = []
Train_Loss_list = []
Valid_Loss_list = []
Valid_Accuracy_list = []
for epoch in range(1, EPOCH + 1):
    train_loss = train_model(model, DEVICE, train_loader, optimizer, epoch)
    Train_Loss_list.append(train_loss)
    torch.save(model, r'C:\Users\mjr\PycharmProjects\Nets\CatvsDog\save_model\model%s.pth'%epoch)
    test_loss,acc = test_model(model, DEVICE, valid_loader)
    Valid_Loss_list.append(test_loss)
    Valid_Accuracy_list.append(acc)
    list.append(test_loss)
min_num = list[0]
min_index = 0
for iii in range(len(list)):
    if list[iii] < min_num:
        min_num = list[iii]
        min_index = iii
minloss = min_num
print('model%s'%min_index)
print('验证集最高准确率：')
print('{}%'.format(Valid_Accuracy_list[min_index]))
model = torch.load(r'C:\Users\mjr\PycharmProjects\Nets\CatvsDog\save_model\model%s.pth'%min_index)
model.eval()
accuracy = test_model(model, DEVICE, test_loader)
print('测试集合准确率')
print('{}%'.format(accuracy[1]))

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
x1 = range(0, 30)
y1 = Train_Loss_list
y3 = Valid_Accuracy_list
y2 = Valid_Loss_list
plt.subplot(221)
plt.plot(x1, y1, "-o")
plt.ylabel('训练集损失')
plt.xlabel('轮数')
plt.subplot(222)
plt.plot(x1, y2, "-o")
plt.ylabel('验证集损失')
plt.xlabel('轮数')
plt.subplot(212)
plt.plot(x1, y3, "-o")
plt.ylabel('验证集准确率')
plt.xlabel('轮数')
# plt.plot(x1, y1, "-o") #实线
# plt.plot(x1, y2, "--o") #虚线
# plt.plot(x1, y3, "-.o") #虚点线
# plt.plot(x, y4, ":o") # 点线
plt.show()
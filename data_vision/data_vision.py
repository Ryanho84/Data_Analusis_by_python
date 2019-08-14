#coding = utf -8

'''
数据可视化
'''


import seaborn as sns
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#数据准备
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)

'''
#使用matplotlib画散点图
plt.scatter(x, y, marker = 'x')
plt.show()
'''
'''
#使用Seaborn画散点图
df = pd.DataFrame({'x':x, 'y':y})
sns.jointplot(x = "x", y = "y", data=df, kind='scatter')
plt.show()
'''

#数据准备
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y =[5, 3, 6, 20, 17, 19, 70, 35, 25, 15]
'''
#使用Matplotlib画折线图
plt.plot(x, y)
plt.show()

#使用seaborn画折线图
print(sns.__version__)
df = pd.DataFrame({'x' : x, 'y': y})
sns.lineplot(x = "x", y ="y", data = df)
plt.show()
'''
'''
#数据准备
a = np.random.randn(100)
s = pd.Series(a)

#用Matplotlib画直方图
plt.hist(s)
plt.show()
#用seaborn画直方图
sns.distplot(s, kde = False)
plt.show()
sns.distplot(s, kde =True)
plt.show()
'''
'''
#数据准备
x = ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6']
y = [5, 4, 7, 12 ,6 ,3]
#Matplotlib画条形图
plt.bar(x, y)
plt.show()
#seaborn画条形图
sns.barplot(x, y)
plt.show()
'''
'''
#数据准备
data = np.random.normal(size = (10,4))
lables = ['A', 'B', 'C', 'D']
#Matplotlib画箱线图
plt.boxplot(data, labels = lables)
plt.show()

#seaborn画箱线图
df = pd.DataFrame(data, columns= lables)
sns.boxplot(data = df)
plt.show()
'''
'''
#数据准备
nums = [25, 37, 33, 37, 6]
labels = ['high-school', 'Bachelor', 'Master', 'Ph.d', 'Others']
#Matplotlib画饼图
plt.pie(x = nums, labels = labels)
plt.show()
'''

'''
#数据准备
flights = sns.load_dataset("flights")
data = flights.pivot('year', 'month', 'passengers')
#用seaborn画热力图
sns.heatmap(data)
plt.show()
'''
'''
#数据准备
labels = np.array([u"推进" , "KDA", u"生存", u"团战", u"发育", u"输出"])
stats = [83, 61, 95, 67, 76, 88]
#画图数据准备
angles = np.linspace(0, 2*np.pi, len(labels), endpoint = False)
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))
#用Matpplotlib画蜘蛛图
fig = plt.figure()
ax = fig.add_subplot(111, polar = True)
ax.plot(angles, stats, 'o-', linewidth = 2)
ax.fill(angles, stats, alpha = 0.25)
#设置中文字体
font = FontProperties(fname = r"C:\Windows\Fonts\simfang.ttf", size = 14)
ax.set_thetagrids(angles * 180/np.pi, labels, FontProperties = font)
plt.show()
'''

'''
#数据准备
tips= sns.load_dataset("tips")
print(tips.head(10))
#用seaborn画二元变量分布图
sns.jointplot(x = "total_bill", y = "tip", data = tips, kind = 'scatter')
sns.jointplot(x = "total_bill", y = "tip", data = tips, kind = 'kde')
sns.jointplot(x = "total_bill", y = "tip", data = tips, kind = 'hex')
plt.show()
'''
''''
#数据准备
iris = sns.load_dataset('iris')
#用seaborn画成对关系
sns.pairplot(iris)
plt.show()
'''

'''
练习
'''
#数据准备
data = sns.load_dataset('car_crashes')
print(data.head(10))
#用seaborn画成对关系
sns.pairplot(data)
plt.show()

#用seaborn画二元变量分布图
sns.jointplot(x = "total", y = "speeding", data = data, kind = 'scatter')
sns.jointplot(x = "total", y = "speeding", data = data, kind = 'kde')
sns.jointplot(x = "total", y = "speeding", data = data, kind = 'hex')
plt.show()
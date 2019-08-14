#coding - utf-8

'''
数据变换的目的:在数据挖掘建模前的准备环节，将不同渠道、不同量级的数据转化位统一的形式，方便后续的分析处理。

数据变换的具体方法包括：
1. 数据平滑：去除数据中的噪声，将连续的数据离散化
2. 数据聚集：对数据进行汇总，
3. 数据概化：将数据有较低的抽象概念抽象为较高的概念，减少数据的复杂度。
4. 数据规范化：使数据按照比例缩放
5. 属性构造： 构造出新的属性并添加到属性集中去。
'''


#1. Min-Max规范化： 将原始数据映射到[0,1]空间中，即 new_data = (original_data - Min)/(Max - Min)
#2. Z-Score规范化： 对于非统一标准下的数据，可以通过规范化，让数据具有可比性。   new_data = (original_data - mean_data) / SD
#3. 小数定标规范化： 通过移动小数点的位置来进行规范化。小数点的移动多少位取决于数据A的取值中的最大绝对值。

'''
使用Python的SciKit-Learn库
'''
from sklearn import preprocessing
import numpy as np 

#Min-Max规范化
x = np.array([[0., -3., 1.],
              [3., 1., 2. ],
              [0., 1., -1.]])

min_max_scaler = preprocessing.MinMaxScaler()
print(min_max_scaler)
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)

#Z-Score规范化
scaled_x = preprocessing.scale(x)
print(scaled_x)

#小数点定标规范化
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)

#练习，income的最大值和最小值分别是5000和58000，通过Min-Max映射到[0,1], 求16000映射后的值
def MinMaxfunc(x, min, max):
    trans_x = (x - min)/(max - min)
    return trans_x
y = 16000
minmax_y = MinMaxfunc(16000, 5000, 58000)
print(minmax_y)

y = np.array([[5000.],[16000.],[58000.]])
min_max_scaler = preprocessing.MinMaxScaler()
minmax_y = min_max_scaler.fit_transform(y)
print(minmax_y)
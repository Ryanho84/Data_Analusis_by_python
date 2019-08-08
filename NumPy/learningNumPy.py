"""
Numpy是python语言的一个扩展程序库，支持大量的维度数组
和矩阵运算，此外也针对数组运算提供大量的数学函数库。
* 一个强大的N维数组对象ndarray
* 广播功能函数
* 整合C/C++/Fortran代码的工具
* 线性代数、傅里叶变换、随机数生成等
"""
"""
numpy.array:
	numpy.array(object, dtype = None, copy = True, 
		order = None, subok = False, ndmin = 0)

	object:数组或嵌套的数列
	dtype:数组元素的数据类型，可选
	copy:对象是否需要复制，可选
	order:创建数组的样式，C为行方向，F为列方向，A为任意方向（default）
	subok:默认返回一个与基类类型一致的数组
	ndmin:指定生成数组的最小维度

dtype :
	数据类型对象用来描述与数组对应的内存区域如何使用，依赖于下面几个方面：
	* 数据的类型：整数/浮点数/...
	* 数据的大小：不同类型的数据对应的内存字节数
	* 数据的字节顺序：小端法/大端法
	* 在结构化类型情况下：字段的名称、每个字段的数据类型和每个字段所取得内存块得部分
	* 如果数据类型是子数组，它得形状和数据类型

	numpy.dtype(object, align, copy)

	object : 要转换为的数据类型对象
	align : 如果为true，填充字段使其类似C得结构体
	copy : 复制dtype对象，如果为false，则是对内置数据类型对象得引用

numpy.asarray:
	numpy.asarray(a, dtype = None, order = None)

	a : 任意形式的输入参数，可以是列表、元组、元组的元组、多维数组等
	dtype : 数据类型
	order : C/F

"""
#coding=utf-8
import numpy as np 
from numpy import *

print("========dnarray object==========")
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
#对b中的[1,1]元素复制为10.下标从0开始
b[1,1] = 10
"""
 Error:index is out of bounds for axis 0 with size 3
 b[3,4] = 100
"""
"""
 Error : index is out of bounds for axis 1 with size 3
 b[2,4] = 100
"""
c = np.array([1,2,3,4,5], ndmin = 2)
d = np.array([1,2,3], dtype = complex)
e = np.array([[1,2,3],[4,5,6],[9,6,4]],dtype = float)
print(a.shape)          #输出(3,) 前一个表示一个线性数组中元素的个数   后一个表示维数，即有多少个axis
print(b.shape)
print(a.dtype)
print(b)
print(c)				#注意输出的是[[1,2,3,4,5]] 这是一个二维数组
print(d)
print(e)

print("=========dtype object==========")
#使用标量类型
dt1 = np.dtype(np.complex)
f = np.array([1,2,3], dtype = dt1)
print(f)
print(dt1)
"""
int8,int16,int32,int64四种数据类型可以使用字符串'i1' 'i2' 'i4' 'i8'代替
同理：
uint8/16/32/64可以用'u1/2/4/8'代替
float16/32/64可以用'f2/4/8'代替
complex64/128可以用'c8/16'代替

每一个内建类型都有一个唯一定义它得字符代码：
b   bool
i   int
u   uint
f   float
c   complex
m   timedelta
M   datetime
O   python Object
S,a array
U   Unicode
V   void
"""
dt2 = np.dtype('i8')
print(dt2)
"""
 >/<字节顺序标注 
 >表示采用大端法存储（高位组放最前面）
 <表示采用小端法存储（低位组放最前面）
 """
dt3 = np.dtype('>i4')
print(dt3)
g = np.array([1,2,3], dtype = dt3)
print(g)

"""
结构化数类型，即结构体
"""
dt4 = np.dtype([('age', np.int8)])
print(dt4)
h = np.array([(10,),(20,),(30,)],dtype = dt4)
print(h)
#类型字段名可以同于存取实际得age列
print(h['age'])
student = np.dtype([('name','S20'),('age', 'i1'),('marks','f4')])
print(student)
i = np.array([('abc',21,50),('xyz',18,75),('opq',22,80)],dtype = student)
print(i)
print('==========ndarray attribute=========')
"""
Numpy数组的维数成为秩rank，一维数组秩为1，二维数组秩为2
每一个线性的数组成为一个轴axis，也就是维度。 轴的数量就是秩
对于一个二维数组，有两个维度，就是有两个轴，可以声明axis
axis = 0,表示沿着第0轴进行操作，即对每一列进行操作
axis = 1,表示沿着第1轴进行操作，即对每一行进行操作

ndarray.ndim  秩，维度的数量
ndarray.shape 数组的维度，对于二维数组（矩阵），显示n行m列
ndarray.size  数组元素的总个数，相当于n*m
ndarray.dtype 对象数组类型
ndarray.itemsize 对象中每个元素的大小，以字节为单位
ndarray.flags 对象的内存信息
ndarray.real  元素的实部
ndarray.imag  元素的虚部
ndarray.data  一般不用
"""
#ndarray.ndim  秩，即轴的数量或维度的数量
j = np.arange(24)
print(j.ndim)
print(j)
j1 = j.reshape(2,4,3)   #2*4*3 = 24
print(j1.ndim)
print(j1)
#ndarray.shape 数组的维度，返回一个元组，这个元组的长度就是维度的数目，即ndim
k = np.array([[1,2,3],[4,5,6]])
print(k)
print(k.shape)
#reshape 调整数组的维度和大小
l = np.array([[1,2,3],[4,5,6]])
l1 = l.reshape(3,2)
print(l)
print(l1)
#ndarray.itemsize  以字节形式返回数组中每个元素的大小
m = np.array([1,2,3,4,5], dtype = np.int8)
print(m.itemsize)
m1 = np.array([1,2,3,4,5], dtype = np.float64)
print(m1.itemsize)
"""
student = np.dtype([('name','S20'),('age', 'i1'),('marks','f4')])
i = np.array([('abc',21,50),('xyz',18,75),('opq',22,80)],dtype = student)
"""
print(i.itemsize)
"""
ndarray.flags:
	C_CONTIGUOUS(C) 数据是在一个单一的C风格的连续段中
	F_CONTIGUOUS(F) 数据是在一个单一的Fortran风格的连续段中
	OWNDATA(O)      数据拥有它所使用的内存或从另一个对象中借用他
	WRITEABLE(W)    数据区域可以被写入，将该值设置为flase。则数据为只读
	ALIGNED(A)      数据和所有元素都适当地对齐到硬件上
	UPDATEIFCOPY(U) 这个数组是其他数组的一个副本，当这个数组被释放时，原数组地内容将被更新
"""
n = np.array([1,2,3,4,5])
print(n.flags)
print("==========create array===========")
"""
numpy.empty(shape, dtype, order = 'C')
shape : 数组维度
dtype : 数据类型
order : C/F, C代表行优先, F代表列优先, 这些指在计算机内存中的存储元素的顺序
"""
#数组元素结果为随机数，未初始化
o = np.empty((3,2), dtype = int)
print(o)
"""
numpy.zeros(shape, dtype, order = 'C')
"""
#创建shape大小的数组，数组元素用0填充
#默认为浮点数
p = np.zeros(5)
print(p)

p1 = np.zeros((5,), dtype = np.int)
print(p1)

p2 = np.zeros((2,2),dtype = [('x', 'i4'), ('y','i4')])
print(p2)
"""
numpy.ones(shape, dtype, order = 'C')
"""
#创建shape大小的数组，数组元素用1填充
q = np.ones(5)
print(q)

q1 = np.ones((2,2), dtype = int)
print(q1)
"""
random.randn(size) 创建服从X-N(0,1)的正态分布随机数组
size可以是1维的 m
         2维的 m,n
         3维的 m,n,o
         ...
"""
r = random.randn(2,3,4)
print(r)
"""
randint([low,high], size)
创建[low, high]范围之间的size大小的数组
"""
s = random.randint(100,200,(3,3))
print(s)
print("============create array using exist array============")
t = [1,2,3]
#将列表转换为ndarray
t1 = np.asarray(t)
print(t1)
#将元组转换为ndarray
t2 = (1,2,3)
t3 = np.asarray(t2)
print(t3)
#将元组列表转化为ndarray
t4 = [(1,2,3),(4,5,6),(5,6,9)]
t5 = np.asarray(t4)
print(t5)
"""
Error:setting an array element with a sequence, 矩阵的列没有对齐，需要将没对齐的数据补齐
t6 = [[1,2,3],[4,5,],[7,8,9]]
t7 = np.asarray(t6, dtype = float)
"""
#并指定类型
t6 = np.asarray(t4, dtype = float)
print(t6)
print("====the difference between array and asarray====")
"""
	1. 参数个数不同, array最多5个参数, asarray最多三个参数
	2. array和asarray都可以将结构数据转化为ndarray，但是主要区别就是当数据源是ndarray时，
	   array仍然会copy出一个副本，占用新的内存，但asarray不会。
"""
#example 1:
print("example 1 :")
data1=[[1,1,1],[1,1,1],[1,1,1]]
arr2=np.array(data1)
arr3=np.asarray(data1)
data1[1][1]=2
print('data1:\n',data1)
print('arr2:\n',arr2)
print('arr3:\n',arr3)
#example 2:
print("example 2 :")
arr1=np.ones((3,3))
arr2=np.array(arr1)
arr3=np.asarray(arr1)
arr1[1]=2
print('arr1:\n',arr1)
print('arr2:\n',arr2)
print('arr3:\n',arr3)
print("===========create array from range===========")
"""
numpy.arange(start, stop, step, dtype):
	创建数值范围并返回ndarray对象
	start : 起始值，默认为0
	stop  : 终止值
	step  : 步长，默认为1
	dtype : 数据类型
	似乎只能创建一维向量
"""
#[0, 5)
u = np.arange(5)
print(u)
u1 = np.arange(5, dtype = float)
print(u1)
u2 = np.arange(10, 20, 2, dtype = complex)
print(u2)
"""
numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None)
	用于创建一个一维数组，数组是由一个等差数列构成的
	start : 序列的起始值
	stop : 序列的终止指，如果endpoint为true,则该值包含在数列中，即决定是半开半闭还是全闭区间
	num : 要生成的等步长的样本数量，默认为50
	endpoint : 该值为true时，数列中包含stop,否则不包含，默认为true
	retstep : 如果为true，生成的数组会显示间距，否则不显示
	dtype : 数据类型
"""
v = np.linspace(1, 10, 10)
print(v)
v1 = np.linspace(1, 1, 10)
print(v1)
v2 = np.linspace(10, 20, 6, endpoint = False)
print(v2)
v3 = np.linspace(1, 10, 10, retstep = True)
print(v3)
v4 = np.linspace(1, 10, 10).reshape((10, 1))
print(v4)
"""
numpy.logspace(start, stop, num = 50, endpoint = True, base = 10.0, dtype = None)
	创建一个等比数列，并返回一个ndarray对象
	start : 序列的初始值为base^start
	stop : 序列的终止值为base^stop
	num : 要生成的等步长的样本数量，默认为50
	endpoint : 同linspace()
	base : 对数log的底数
	dtype : 数据类型
"""
w = np.logspace(1.0, 2.0, num = 20)
print(w)
#区间[2^0, 2^9]，num = 10的等比数列
w1 = np.logspace(0, 9, 10, base = 2)
print(w1)
print("===============slice and index=============")
"""
ndarray可以通过索引或切片来访问和修改，操作与python中的list一样
ndarray可以基于0 - n的下标进行索引，切片可以通过slice函数，并设置start
	, stop, step参数进行
"""
x = np.arange(10, dtype = 'i1')
#slice(start, stop, step)
xs = slice(2, 7, 2)
print(x[xs])
#或者直接使用[start:stop:step]进行操作
xs1 = x[2:7:2]
print(xs1)
"""
[n], 返回该索引对应的单个元素
[n:], 返回从n起始的所有元素
[n:m], 返回从n到m的所有元素
[n:m:s], 返回从n到m, 间隔为s的所有元素
"""
x2 = np.arange(100) #[0,1,2,3,...,99]
x2_6 = x2[6]        #返回下标为6的元素
print(x2_6)
x2_2_ = x2[2:]      #返回从2开始的所有元素
print(x2_2_)
x2_2_5 = x2[2:5]    #返回2到4的值，默认step = 1
print(x2_2_5)
"""
多为数组也可以切割
"""
x3 = np.array([[1,2,3], [3,4,5], [4,5,6]])
print(x3)
#print("从数组索引a[1:]初开始切割 :")
print(x3[1:])                 #从数组的数组来理解
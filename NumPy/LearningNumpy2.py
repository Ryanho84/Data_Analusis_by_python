import numpy as np 

#维数称为秩，一维数组秩为1，二维数组秩为2...  每一个维度我们都称为轴，秩实际就是轴的数量
#可以这样理解：一维坐标系，里面有一个轴就是X轴；二维坐标系，里面有两个轴（X，Y）轴；三维坐标系，里面有（X，Y，Z）三个轴
a = np.array([1,2,3])
b = np.array([[1,3,4],[4,5,6],[7,8,9]])
b[1,1] = 10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)
print(a)

persontype = np.dtype({
	'names' : ['name', 'age','chinese', 'math' , 'english'],
	'formats': ['S32','i','i','i','f']
	})
peoples = np.array([("zhengfei",17,90,89,66),("wanghuizi",19,30,89,90),("guyihan",89,47,60,59.9),
	("hexingran",35,100,100,100)],dtype = persontype)

name = peoples[:]['name']
score1 = peoples[:]['chinese']
score2 = peoples[:]['math']
score3 = peoples[:]['english']

def show(name, course):
	print(name,"|",np.mean(course),"|",np.min(course),"|",np.max(course),"|",np.var(course),"|",np.std(course))
#print(name)
print("科目|平均成绩|最小成绩|最大成绩|方差|标准差")
show("语文",score1)
show("数学",score2)
show("英语",score3)
#初始，结尾（不包括结尾），步长
x1 = np.arange(1,11,2)
#初始，结尾，个数的等差数列
x2 = np.linspace(1,9,5)

print(x1)
print(x2)

def show2(array1, array2):
	print(np.add(array1,array2))
	print(np.subtract(array1,array2))
	print(np.multiply(array1,array2))
	print(np.divide(array1,array2))
	print(np.power(array1,array2))
	print(np.remainder(array1,array2))

show2(x1,x2)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
def show3(x):
	print(np.amin(x))
	#axis = 0 x轴； axis = 1 y轴
	print(np.amin(x,0))
	print(np.amin(x,1))
	print(np.amax(x))
	print(np.amax(x,0))
	print(np.amax(x,1))

show3(a)

def show4(x):
	print(np.ptp(x))
	print(np.ptp(x,0))
	print(np.ptp(x,1))

show4(a)

def show5(x):
	#分位数是指p%位置的值，比如数组元素个数为n, (1+n)X50%就是中位数的位置，对应的值就是中位数
	print(np.percentile(a, 50))
	print(np.percentile(a, 50, axis = 0))
	print(np.percentile(a, 50, axis = 1))

show5(a)


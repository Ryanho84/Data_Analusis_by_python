#coding=utf-8
'''
数据清洗，就是对数据进行整理裁剪，做到数据完整性、合法性、全面性、唯一性
下面的例子是对一个账户信息表进行数据清洗，我们可以观察到：
1. 数据表格每一列代表什么含义没有说明，让人看不懂；
2. 某些列的单位不一样，应该一致，才能更好的进行挖掘
3. 有些值是空的
4. 有很多多余的列，影响分析
5. 有重复的数据
'''


import pandas
import pandas as pd 
from pandas import Series, DataFrame

df = DataFrame(pd.read_excel(r'F:\Work\open_courses\Data_Analysis_by_python\clean_data\accountMessage.xlsx'))


print(df)
print('-------------------------------------------------------------------')
'''
初步对数据进行清洗，删除空行，填充空数据，保证数据的完整性
'''
#删除标记为0的列数据,以及标记为'\t'的列数据，注意，前面的序号是数据表格自带的编号
df.drop(columns=[0,'\t'], inplace = True)
#从标记的第1列开始，1-9列分别进行重命名
df.rename(columns = {1:'name', 2:'age', 3:'weights', 4:'m0006', 5:'m0612', 6:'m1218', 7:'f0006', 8:'f0612', 9:'f1218'}, inplace= True)
#对'age'列进行操作，对所有NAN空值进行填充，填充为age列的平均值
df['age'].fillna(df['age'].mean(),inplace=True)
#print(df['weights'].value_counts())
#value_counts()函数是统计相同数值的个数，并进行降序排列。一下代码的含义是，对weights列相同数值进行统计，然后将相同数值对多的数值填充到NAN中，如第2行和第8行的数值，填充为189lbs
df['weights'].fillna(df['weights'].value_counts().index[0], inplace = True)
#删除全为NAN值得行
df.dropna(how = 'all', inplace = True)
#对weights列中，选出字符串中包含lbs的行，并对NAN行不填充
lbs_row = df['weights'].str.contains('lbs').fillna(False)
print(lbs_row)
print('-------------------------------------------------------------------')
print(df[lbs_row])
print('-------------------------------------------------------------------')
#删除第八行
df.drop(index = [8],inplace=True)
print(df)
print('-------------------------------------------------------------------')
'''
再做进一步的清洗，统一单位，去除非ASCII码值，对多元列进行切片，用平均值进行填充等
'''
print(df[lbs_row])
print('-------------------------------------------------------------------')
#针对df[lbs_row]进行操作，将单位统一为kg
for i, row in df[lbs_row].iterrows():
    weight = int(float(row['weights'][:-3])/2.2)
    df.at[i,'weights'] = '{}kgs'.format(weight)
#删除所有非ASCII码
df.replace({r'[^\x00-\x7F]+':''},regex=True)
#去除多余小数点
for i, row in df.iterrows():
    age = int(float(row['age']))
    df.at[i,'age'] = '{}'.format(age)
print(df)
print('--------------------------------------------------------------------')
#split(str,num) 以str为分隔符，进行num次的切片分割，默认的分隔符为空格、换行等，默认的次数为-1，无数次
df[['first_name', 'last_name']] = df['name'].str.split(expand = True)
df.drop('name',axis = 1,inplace=True)
df.drop_duplicates(['first_name', 'last_name'], inplace = True)
print(df)
print('--------------------------------------------------------------------')
#换位置
columns = list(df)
#print(columns)
columns.insert(0, columns.pop(columns.index('last_name')))
columns.insert(0,columns.pop(columns.index('first_name')))
df = df.ix[:,columns]
df['first_name'].replace({r'[^\x00-\x7F]+':''},regex=True)
df['last_name'].replace({r'[^\x00-\x7F]+':''},regex=True)
print(df)
print('---------------------------------------------------------------------')
#对f0612列筛选出含有数字或字母的行，去除-的行
f0612_rows = df['f0612'].str.isalnum().fillna(True)
#print(f0612_rows)
#print(df[f0612_rows])
f0612_mean = df[f0612_rows]['f0612'].mean()
df['f0612'].fillna(f0612_mean, inplace = True)
print(df)
print('---------------------------------------------------------------------')
df.replace('-', '', inplace = True)
df = df.reindex(range(df.shape[0]),method = 'bfill')
print(df)

#输出成为csv
#df.to_csv(r'F:\Work\open_courses\Data_Analysis_by_python\clean_data\accountMessage_new.csv')
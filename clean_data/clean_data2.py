#coding = utf-8

'''
下面是对肉类数据进行清洗的练习

我们看到数据，有以下需要关注的：
1. 食物名称中首字母有大写有小写
2. 有很多重复数据，需要合并
'''

import pandas
import pandas as pd 
from pandas import Series, DataFrame

df = DataFrame(pd.read_excel(r'F:\Work\open_courses\Data_Analysis_by_python\clean_data\foodInformation.xlsx'))

print(df)
print('---------------------------------------------')


'''
首先将食物名称调整成统一的大小写
'''
df['food'] = df['food'].str.capitalize()
print(df)
print('---------------------------------------------')
'''
找到相同的项，对数据进行合并
1. 首先针对food对df进行分组，并进行数据合并
2. 对分组后的数据进行重新DataFrame转换，形成新的DataFrame
3. 对原来的dataframe进行处理，去重+去除没有意义的列
4. 两个dataframe合并
'''
#对数据进行分组
groupbyObj = df.groupby(df['food']).sum()
print(groupbyObj)
print('---------------------------------------------')
#对分组后的数据进行DataFrame化
new_df = groupbyObj.reset_index()
print(new_df)
print('---------------------------------------------')
#将原有的数据表进行去重,并删除ounces列
df.drop_duplicates(['food'], inplace=True)
df = df.reindex(range(df.shape[0]), method = 'bfill')
df.drop(columns = ['ounces'], inplace = True)
print(df)
print('---------------------------------------------')
#两个DataFrame合并
result = pd.merge(df, new_df, on = 'food')
print(result)

#打印
#result.to_csv(r'F:\Work\open_courses\Data_Analysis_by_python\clean_data\foodInformation_new.csv')
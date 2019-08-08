#coding=utf-8

import pandas
import pandas as pd 
import os
from pandas import Series, DataFrame
print(os.getcwd())


df = DataFrame(pd.read_excel('accountMessage.xlsx'))


print(df)
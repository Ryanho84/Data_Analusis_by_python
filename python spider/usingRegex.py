"""
using Regular Expression

RegEx pattern:
	RegEx jpg

re module:
	function compile(pattern, flag = 0):
	编译正则表达式pattern，然后返回一个正则表达式对象

	在使用预编译的代码对象比直接使用字符串快，因为解释器在执行字符串形式的代码前都必须把字符串编译成代码对象。
	正则表达式同样，在模式发生匹配前，正则表达式模式必须编译成正则表达式对象。由于正则表达式在执行过程中将进行
	多次比较操作，因此强烈建议使用预编译。

	function match(pattern, string, flag = 0)：
	字符串匹配函数，只从字符串的最开始与pattern进行匹配，匹配成功返回匹配对象（只有一个结果），否则返回None。
	简而言之，就是看被匹配的字符串是否完全符合正则表达式。
	

	function search(pattern, string, flag = 0):
	字符串搜索函数：与match()工作方式一样，但它不是从最开始匹配的，二是从任意位置查找第一次匹配的内容。如果所有
	字符串都没有匹配成功，返回None。简而言之，就是看被搜索字符串是否包含可以与正则表达式匹配的子串(最长的)。

	function findall(pattern, string, [,flags]):
	字符串查找函数，查找字符串中所有（非重复）出现的正则表达式模式(最长的)，并返回一个列表。



"""
import re
s1 = '我12345abcde'
s2 = '.12345abcde'
s3 = '+?!@12345abcde'
s4 = '+?!@123456abcdef@786ty'
#pattern字符串前加'r'表示原生字符串. 
pattern = r'\w.+'                         #表示开头为字母或数字的任意长的字符串
pattern2 = r'\d+'                         #表示任意长度数字字符串
#编译pattern
pattern_complie = re.compile(pattern)
#对s1和s2进行匹配
result1 = re.match(pattern,s1)
result2 = re.match(pattern,s2)

result3 = re.search(pattern,s2)
result4 = re.search(pattern,s3)

result5 = re.findall(pattern2,s4)

result6 = re.finditer(pattern2,s4)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
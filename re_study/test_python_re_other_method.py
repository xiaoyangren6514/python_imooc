"""
match 从头开始查找
search 匹配查找指定的子串
"""
import re

str = 'imooc video num = 1000 and users = 1200'

info = re.search(r'\d+', str)
print(info.group())

infolist = re.findall(r'\d+', str)
print(infolist)
print(sum([int(x) for x in infolist]))


def add_one(match):
    val = match.group()
    result = int(val)+1
    return str(result)


# 替换字符串
r = re.sub(r'\d+', '1200', str)
print(r)

# r = re.sub(r'\d+',add_one,str)
# print(r)

str = 'wang:java,c,php'
list = re.split(r',|:',str)
print(list)
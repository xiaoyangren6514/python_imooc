import re

ma = re.match(r'^[\w]{4,10}@126.com$', 'abdc@126.com')
"""
\A 必须以该字符串开头
\Z 必须以该字符串结尾
|  或
"""
ma = re.match(r'\Ahello[\w]*', 'hello world')
ma = re.match(r'[1-9]?\d$|100','100')
ma = re.match(r'[\w]{4,6}@(126|163).com','wang@126.com')
ma = re.match(r'<([\w]+>)[\w]+</\1','<book>wa</book>')
ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>wa</book>')
if ma is not None:
    print(ma.group())
else:
    print('ma is none ')

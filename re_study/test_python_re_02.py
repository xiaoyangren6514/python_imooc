import re

ma = re.match(r'[A-Z][a-z]*[0-9]', 'Ass4')
ma = re.match(r'[_a-zA-Z]+[\w]*','asda2231')
ma = re.match(r'[\w]{6}','ada12easd')
ma = re.match(r'[0-9a-z]+?','131asdaasd')
if ma is not None:
    print(ma.group())
else:
    print('ma is none ')

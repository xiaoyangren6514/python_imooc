import re

ma = re.match(r'{.}', '{a}')
ma = re.match(r'[[\w]]','[he]')
if ma is not None:
    print(ma.group())
else:
    print('ma is none ')

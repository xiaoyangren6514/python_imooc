import re

str1 = 'hello python hell'
print(str1.find('ss'))

p1 = re.compile(r'hell')
print(type(p1))
m1 = p1.match(str1)
print(m1.group())
print(m1.span())
print(m1.string)
print(m1.re)


# p2 = re.compile(r'o')
# m2 = p2.match('hello')
# print(m2.string)

pa = re.compile(r'hello',re.I)
ma = pa.match('Hello python')
print(ma.group())


ma2 = re.match(r'python','python')
print(ma2.group())
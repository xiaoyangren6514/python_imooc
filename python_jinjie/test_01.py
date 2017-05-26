class Person(object):
    def __init__(self, name, score):
        self.__score = score
        self.__name = name

    def get_grade(self):
        if self.__socre >= 80:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print(p1.get_grade())
print(p2.get_grade())
print(p3.get_grade())


class Animal(object):
     hobby = 'eat huo tui'

     def __init__(self,name,weight):
         self.name = name
         self.weight = weight

     @classmethod
     def get_hobby(cls):
         return cls.hobby

     @property
     def get_weight(self):
         return self.weight

class Dog(Animal):
    def __init__(self,name,weight,color):
        super(Dog, self).__init__(name,weight)
        self.color = color

if __name__ == '__main__':
    dog = Dog('wangcai',12,'blue')
    print(type(dog))
    print(dir(dog))
    print(dog.__dict__)
    print(dog.get_hobby())
    print(dog.get_weight)
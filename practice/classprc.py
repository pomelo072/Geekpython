class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


pomelo = Student("lzx",98)

print(pomelo.name)
print(pomelo.score)
print(pomelo.get_grade())

class Animal(object):

    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
class people():

    def run(self):
        print("people do not extends Animal")

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Cat())
run_twice(Animal())
run_twice(people())

print(type(Cat()))

h = Cat()
print(isinstance(h, Animal))
print(dir(Animal))

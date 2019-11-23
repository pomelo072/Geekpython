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
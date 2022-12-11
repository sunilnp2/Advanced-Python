class Student():

  def __init__(self):
    pass

  def Info(self, name, age):
    self.name = name
    self.age = age
    print(f'Name is :{self.name}, Age is {self.age}')


obj = Student()
obj.Info("sunil", 20)

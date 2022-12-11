class Student():

  def __init__(self):
    self.name = "Sunil"  #This is intance variable define in class

  def show(self):
    print(f'My Name is :{self.name}')


# create object

sunil = Student()
sunil.show()

#Create instance variable by object
sunil.age = 20
print(sunil.age)

# hamile instance variable chai class bata nai banauna perx

# Use you class method for accesing class variable in oop


class Student():
  address = "Kathmandu"

  @classmethod
  def show_address(cls, name):
    cls.name = name
    print(f'Name is {cls.name} and address is {cls.address}')


obj = Student()
obj.show_address("Sunil Nepali")

# when some processing related to class but don't need to use class or it's instance, like self, and cls in @classmethod
# we can access data without giving self and cls parameter
class Student():
  address = "KTM"

  @staticmethod
  def show_info(name, age):
    name = name
    age = age
    print(
      f'My Name is {name} i am {age} yearls old and i am from {Student.address}.'
    )


obj = Student()
obj.show_info("sunil Nepali", 20)

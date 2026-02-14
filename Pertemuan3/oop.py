class MyClass: # class
  x = 5

p1 = MyClass() # objek

print(p1.x)


# __init__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Antonov", 36)

print(p1.name)
print(p1.age)

# parameter
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Privet, name is " + self.name)

p1 = Person("Antonov", 25)
p1.greet()

# parameter (ft. self) pt.2
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

"""🟢 Q1 — Basic Inheritance
class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog=Dog()
dog.eat()"""

"""🟢 Q2 — Parent + Child Method

class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def drive(self,):
        print("car is driving")
car=Car()
car.start()
car.drive()"""

"""🟢 Q3 — Inheritance with Constructor
class Employee:
    def __init__(self,name):
        self.name=name
    def display_name(self):
        print(self.name)
class Tester(Employee):
    pass
tester=Tester("satyajit")
tester.display_name()"""

"""🟡 Q4 — Parent + Child Data
class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
class Tester(Employee):
    def testing(self):
        print("Tester is testing")
tester=Tester("satyajit","Automation Tester")
print(tester.name)
print(tester.role)
tester.testing()"""

"""🟡 Q5 — Employee → Developer
class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def code(self):
        print("Developer is coding")
dev=Developer("satyajit")
dev.work()
dev.code()"""

"""🟢 Question 1 — super().__init__()
class Employee:
    def __init__(self,name):
        self.name=name
class Tester(Employee):
    def __init__(self,name,tool):
        super().__init__(name)
        self.tool=tool
tester=Tester("satyajit","Selenium")
print(tester.name)
print(tester.tool)"""

"""🟢 Question 2 — Parent method with super()
class Vehicle:
    def start(self):
        print("vehicle is starting")
class Car(Vehicle):
    def drive(self):
        super().start()
        print("car is driving")
car=Car()
car.drive()"""

"""🟡 Question 3 — Constructor + Parent Method
class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def work(self):
        print("Employee is working")
class Tester(Employee):
    def __init__(self,name,role,tool):
        super().__init__(name,role)
        self.tool=tool
    def testing(self):
        super().work()
        print("tester is testing with selenium")
tester=Tester("satyajit","tester","Selenium")
tester.testing()"""

"""🟢 Question 4 — Parent Constructor
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self,brand,model,color):
        super().__init__(brand,model)
        self.color=color
    def display(self):
        print("brand",self.brand,"model",self.model,"color",self.color)
car=Car("Toyota","Fortuner","Black")
car.display()"""

"""🟢 Question 5 — Parent Method
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("dog barks")
dog=Dog()
dog.sound()"""

"""🟡 Question 6 — Constructor + Method
class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def work(self):
        print("employee is working")
class Developer(Employee):
    def __init__(self,name,role,language):
        super().__init__(name,role)
        self.language=language
    def coding(self):
        super().work()
        print("developer is coding in python")
dev=Developer("satyajit","Developer","Python")
dev.coding()"""

"""🟡 Question 7 — Two Child Classes
class Employee:
    def __init__(self,name):
        self.name=name
    def work(self):
        print("employee is working")
class Tester(Employee):
    def testing(self):
        super().work()
        print("tester is testing")
class Developer(Employee):
    def coding(self):
        super().work()
        print("developer is coding")
tester=Tester("satyajit")
dev=Developer("ishani")
tester.testing()
dev.coding()"""


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,name,age,role):
        super().__init__(name,age)
        self.role=role
class Tester(Employee):
    def __init__(self,name,age,role,tool):
        super().__init__(name,age,role)
        self.tool=tool
    def testing(self):
        super().display_person()
        print(self.role)
        print(self.tool)
tester=Tester("satyajit",26,"Tester","Selenium")
tester.testing()
























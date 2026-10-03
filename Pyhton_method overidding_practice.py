"""Question 1 — Method Overriding

class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
dog=Dog()
dog.sound()"""

"""class Employee:
    def work(self):
        print("employee is working")
class Tester(Employee):
    def work(self):
        super().work()
        print("tester is testing")
tester=Tester()
tester.work()"""

"""class Vehicle:
    def start(self):
        print("vehicle is starting")
class Car(Vehicle):
    def start(self):
        super().start()
        print("car is starting")
car=Car()
car.start()"""

"""class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def show_balance(self):
        print(self.__balance)
account=BankAccount(40000)
account.deposit(50000)
account.show_balance()"""

"""class Employee:
   def __init__(self,name,salary):
       self.__name=name
       self.__salary=salary
   def display_details(self):
       print(self.__name)
       print(self.__salary)
   def increase_salary(self,amount):
       self.__salary+=amount
emp=Employee("satyajit",40000)
emp.display_details()
emp.increase_salary(5000)
emp.display_details()"""


"""Q1. “Create a BankAccount class where the account balance should not be directly modified from outside the class. The class should allow the user to deposit money and withdraw money. The withdrawal should only happen if sufficient balance is available. Also provide a method to display the current balance.”

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance>=amount:
           self.__balance-=amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print(self.__balance)
account=BankAccount(10000)
account.deposit(30000)
account.withdraw(45000)
account.show_balance()"""

"""class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def display_details(self):
        print(self.__name)
        print(self.__marks)
    def update_marks(self,new_marks):
        if new_marks>100:
            print("invalid marks")
        else:
            self.__marks=new_marks
    def show_marks(self):
        print(self.__marks)
student=Student("satyajit",60)
student.display_details()
student.update_marks(90)
student.display_details()
student.update_marks(200)
student.display_details()"""



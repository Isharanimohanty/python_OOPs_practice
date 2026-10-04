class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def show_balance(self):
        print(self.__balance)

bank=BankAccount(5000)
bank.deposit(2000)
bank.show_balance()

class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
    def increase_salary(self,amount):
        self.__salary += amount
    def display_details(self):
        print(self.__name)
        print(self.__salary)
emp=Employee("satyajit",40000)
emp.increase_salary(20000)
emp.display_details()

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance
    def deposit(self,amount):
        self.__balance +=amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount
        else:
            print("Insuffiecient balance")
    def show_balance(self):
        print(self.__balance)

bank=BankAccount("satyajit",40000)
bank.deposit(10000)
bank.withdraw(60000)
bank.show_balance()

class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.__salary=salary
        self.role=role
    def increase_salary(self,amount):
        self.__salary +=amount
    def decrease_salary(self,amount):
        if amount <=self.__salary:
            self.__salary -=amount
        else:
            print("salary cannot become negative")
    def display_details(self):
        print(self.name)
        print(self.role)
        print(self.__salary)
emp=Employee("satyajit","developer",40000)
emp.increase_salary(20000)
emp.decrease_salary(70000)
emp.display_details()

class GamePlayer:
    def __init__(self,player_name,score):
        self.player_name=player_name
        self.__score=score
    def add_score(self,points):
        self.__score +=points
    def minus_score(self,points):
        if points <=self.__score:
            self.__score -=points
        else:
            print("player cannot be allowed to add negative points")
    def display_score(self):
        print(self.player_name)
        print(self.__score)
game=GamePlayer("satyajit",230)
game.add_score(30)
game.minus_score(40)
game.display_score()


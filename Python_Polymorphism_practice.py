class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("cat meows")
dog=Dog()
cat=Cat()
dog.sound()
cat.sound()

class CreditCard:
    def pay(self):
        print("payment made using credit card")
class UPI:
    def pay(self):
        print("payment made using UPI")

credit=CreditCard()
upi=UPI()
credit.pay()
upi.pay()

"""class Browser:
    def open(self):
        print("opening browser")
class Chrome(Browser):
    def open(self):
        print("opening chrome browser")
class Firefox(Chrome):
    def open(self):
        print("opening firefox browser")

chrome=Chrome()
firefox=Firefox()
chrome.open()
firefox.open()"""
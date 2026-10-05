from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        print("payment done")
class CreditCard(Payment):
    def pay(self):
        print("payment made using credit card")
class UPI(Payment):
    def pay(self):
        print("payment made using UPI")
credit=CreditCard()
upi=UPI()
credit.pay()
upi.pay()
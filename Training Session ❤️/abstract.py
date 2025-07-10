from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    #@abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"paid:{amount:,} via UPI")

upi = UPI()
upi.pay(900000)

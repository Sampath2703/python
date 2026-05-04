from abc import ABC, abstractmethod

class UPIPayment(ABC):

    def __init__(self, balance):
        self._balance = balance   # protected variable

    
    def pay(self, amount):
        pass

    def check_balance(self):
        print(f"Remaining Balance: ₹{self._balance}")



class PhonePe(UPIPayment):

    def pay(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Paid ₹{amount} using PhonePe")
        else:
            print("Insufficient Balance in PhonePe")



class GooglePay(UPIPayment):

    def pay(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Paid ₹{amount} using Google Pay")
        else:
            print("Insufficient Balance in Google Pay")



class Paytm(UPIPayment):

    def pay(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Paid ₹{amount} using Paytm")
        else:
            print("Insufficient Balance in Paytm")



phonepe = PhonePe(5000)
gpay = GooglePay(3000)
paytm = Paytm(4000)


phonepe.pay(1000)
phonepe.check_balance()

gpay.pay(500)
gpay.check_balance()

paytm.pay(2000)
paytm.check_balance()
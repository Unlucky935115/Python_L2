from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingAccount(BankAccount):
    def __init__(self, balance):
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        print("Deposit Amount: {}.\n New Balance: {}".format(amount, self.balance))

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn Amount: {}.\n New Balance: {}".format(amount, self.balance))
        else:
            print("insufficient Balance")

acnt= SavingAccount(1000)
acnt.deposit(3000)
acnt.withdraw(500)
acnt.deposit(1700)
acnt.withdraw(200)
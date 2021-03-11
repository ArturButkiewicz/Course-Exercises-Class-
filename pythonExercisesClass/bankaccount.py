
from result import Result, Error, Ok

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """that function check, is money real"""
        self.balance += amount

    def try_withdraw(self, amount):

        if (self.balance > amount):
            self.balance -= amount
            return Ok("Withdrawn money", amount)

        return Error("Withdrawn failure", amount)

    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance


    def try_withdraw(self, amount):
        if (self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            return Error("Withdrawn failure, attempt to exceed a threshold", amount)

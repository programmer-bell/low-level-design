## Encapsulation

'''

Encapsulation is about protecting the internal data of a class. You control what the outside world 
can see and what it cannot. This prevent accidental modification of import data. 

- Data and methods that operate on that data are bundled together inside a class
- Sensitive data is marked private so it can not be accessed directly from the outside
- Access is given through controlled methods called getter and setters
- Makes code more secure and predictiable

Real life example: ATM machine you can check balance and withdraw but you can not access the
bank's internal system directly.

'''

class Bank:
    def __init__(self, name: str, balance: int):
        self.name: str = name

        # pivate attribute
        self.__balance: int = balance

    def deposite(self, amount: int):
        if amount > 0:
            self.__balance += amount
            print(f"Amount deposite, current balance = {self.__balance}")
        else:
            print("Invalid amount")


    def get_balance(self):
        print(f"The current balance was {self.__balance}")

    def withdraw(self, amount: int): 
        if amount > self.__balance:
            print("Not enough money in bank")
        else:
            self.__balance -= amount
            print(f"Amount withdraw, current balance = {self.__balance}")

acc = Bank("Anirudh", 1000)
acc.deposite(1000)
acc.withdraw(500)

acc.get_balance()
acc.__balance = 1000000000
# acc._Bank__balance = 9999900000 -> can be changed
acc.get_balance()

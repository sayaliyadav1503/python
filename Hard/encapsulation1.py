class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # public variable
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)
acc = BankAccount("Sayali", 5000)

acc.deposit(1000)
acc.withdraw(2000)
acc.show_balance()

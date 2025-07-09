class BankAccount:
    def __init__(self, balance: int | float, name: str, account_number: int):
        self.balance = balance
        if balance < 0:
            balance = 0
        self.name = name
        self.account_number = account_number

    def isNumber(self, var):
        isInt = isinstance(var, int)
        isFloat = isinstance(var, float)

        return isInt or isFloat

    def withdraw(self, amount: int | float):
        if (not self.isNumber(amount)) or (amount > self.balance or amount < 0):
            print("Invalid amount!")
            return -1

        self.balance -= amount
        return self.balance

    def deposit(self, amount: int | float):
        print(self.isNumber(amount))
        if (not self.isNumber(amount)) or (amount < 0):
            print("Invalid amount!")
            return -1

        self.balance += amount
        return self.balance

    def print_balance(self):
        print("Name: " + self.name)
        print("Balance: " + "$" + self.balance + " dollars")
        print("Account ID: " + self.account_number)

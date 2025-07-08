class BankAccount:
    def __init__(self, balance, name, account_number):
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def withdraw(self, amount):
        if (not amount.isinstance(int) or not amount.isinstance(float)) or (
            amount > self.balance or amount < 0
        ):
            print("Invalid amount!")

        self.balance -= amount

    def deposit(self, amount):
        if (not amount.isinstance(int) or not amount.isinstance(float)) or (amount < 0):
            print("Invalid amount!")

        self.balance += amount

    def print_balance(self):
        print("Name: " + self.name)
        print("Balance: " + self.balance)
        print("Account ID: " + self.account_number)

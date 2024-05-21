
class BankAccount:
    def __init__(self, name, account_number, initial_balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"After depositing {amount}, new balance is {self.balance} ")
        else:
            print("Depositing amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient amount so withdrawal denied.")
        elif amount <= 0:
            print("Withdrawing amount must be positive.")
        else:
            self.balance -= amount
            print(f"After withdrawing {amount}, new balance is {self.balance}")

    def check_balance(self):
        print(f"Balance in the account is {self.balance}")


name = input("Enter name of the person: ")
account_number = int(input("Enter account number of the person: "))
initial_balance = int(input("Enter balance present at the person: "))
account1 = BankAccount(name,account_number,initial_balance)

account1.check_balance()
deposit_amount = int(input("Enter amount to deposit: "))
account1.deposit(deposit_amount)
withdraw_amount = int(input("Enter amount to withdraw: "))
account1.withdraw(withdraw_amount)
account1.check_balance()

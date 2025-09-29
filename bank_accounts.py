class BankAccount:
    account_counter = 1000

    def __init__(self,owner,balance=0,account_number=None):
        self.owner=owner
        self.balance=balance
        if account_number is None:
            BankAccount.account_counter+=1
            self.account_number = BankAccount.account_counter
        else:
            self.account_number = account_number

    def to_dict(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "account_number": self.account_number
        }

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance}, account_number={self.account_number})"

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited amount = Rs.{amount}")
        print(f"New balance = Rs.{self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient bank balance")
        else:
            self.balance-=amount
            print(f"Withdrawn amount = Rs.{amount}")
            print(f"New balance = Rs.{self.balance}")

    def check(self):
        print(f"Account owner: {self.owner}")
        print(f"Bank balance: Rs.{self.balance}")
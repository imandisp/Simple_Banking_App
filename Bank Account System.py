class BankAccount:
    account_counter = 1000

    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        BankAccount.account_counter+=1
        self.account_number = BankAccount.account_counter
        

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited amount = {amount}")
        print(f"New balance = {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient bank balance")
        else:
            self.balance-=amount
            print(f"Withdrawn amount = {amount}")
            print(f"New balance = {self.balance}")

    def check(self):
        print(f"Account owner: {self.owner}")
        print(f"Bank balance: {self.balance}")

        
def main(): ##seperate creating a new account from the process.

    name=input("Enter owner's name: ")
    opening_balance=int(input("Enter initial balance: Rs."))
    acc=BankAccount(name,opening_balance)

    print(f"New account created successfully! Your account number is {acc.account_number}")

    choice=0

    try :
        while choice!=4:
            print("---Banking Menu---")
            print("1.Check the Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")

            choice=int(input("Enter Choice Number: "))

            if choice==1:
                acc.check()
            elif choice==2:
                deposit_amount=int(input("Enter deposit amount: Rs."))
                acc.deposit(deposit_amount)
            elif choice==3:
                withdraw_amount=int(input("Enter withdraw amount: Rs."))
                acc.withdraw(withdraw_amount)
        else:
            #save account
            print("Acoount saved successfully! GoodBye!")


    except ValueError:
        print("Invalid Choice!")

main()
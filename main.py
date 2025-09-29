from bank_accounts import BankAccount
from json_storing import save_account, load_accounts

def main(): 

    accounts=load_accounts()

    if accounts:
        BankAccount.account_counter=max(acc.account_number for acc in accounts)
    

    name=input("Enter owner's name: ")

    for account in accounts:
        if account.owner == name:
            acc=account
            break
    else:
        opening_balance=int(input("Enter initial balance: Rs."))
        acc=BankAccount(name,opening_balance)
        print(f"New account created successfully! Your account number is {acc.account_number}")

    choice=0


    while choice!=4:
        print("---Banking Menu---")
        print("1.Check the Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        try:
            choice=int(input("Enter Choice Number: "))

            if choice==1:
                acc.check()
            elif choice==2:
                deposit_amount=int(input("Enter deposit amount: Rs."))
                acc.deposit(deposit_amount)
            elif choice==3:
                withdraw_amount=int(input("Enter withdraw amount: Rs."))
                acc.withdraw(withdraw_amount)
            elif choice==4:
                save_account(acc)
                print("Acoount saved successfully! GoodBye!")
            else:
                print("Invalid choice! Please select 1-4.")


        except ValueError:
            print("Invalid Choice!")

if __name__=="__main__":
    main()
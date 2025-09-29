from bank_accounts import BankAccount
import json

file_name="accounts.json"

def save_account(account:BankAccount):
    """Save an account to json file"""
    try:
        with open(file_name,"r") as file:
            accounts=json.load(file)
    except (FileNotFoundError,json.JSONDecodeError): #if file notfound or empty/corrupted
        accounts=[]

    accounts.append(account.to_dict())

    with open(file_name,"w") as file:
        json.dump(accounts,file,indent=4)


def load_accounts():
    """Load all accounts from json file"""
    try:
        with open(file_name,"r") as file:
            accounts=json.load(file)
        return [BankAccount(**acc) for acc in accounts] #for each acc in accounts,it creates a new BankAccount object.
    except (FileNotFoundError,json.JSONDecodeError):
        return []


if __name__=="__main__":
    acc=BankAccount("TestUser",100)
    save_account(acc)
    print(load_accounts())
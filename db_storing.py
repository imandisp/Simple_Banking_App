import sqlite3
from bank_accounts import BankAccount

db_file = "accounts.db"

def init_db():
    with sqlite3.connect(db_file) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                owner TEXT NOT NULL,
                balance REAL NOT NULL
            )
        """)

def save_account(account: BankAccount):
    """Save or update an account in the database"""
    init_db()
    with sqlite3.connect(db_file) as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT OR REPLACE INTO accounts (account_number,owner,balance)
            VALUES (?,?,?)
        """, (account.account_number,account.owner,account.balance))
        conn.commit()
    print("Account saved successfully!")

def load_accounts():
    """Load all accounts from the database and return as BankAccount objects"""
    init_db()
    accounts=[]
    with sqlite3.connect(db_file) as conn:
        cur = conn.cursor()
        cur.execute("SELECT account_number, owner, balance FROM accounts")
        rows = cur.fetchall()

    for row in rows:
        acc = BankAccount(owner=row[1], balance=row[2], account_number=row[0])
        accounts.append(acc)

    if accounts:
        BankAccount.account_counter = max(acc.account_number for acc in accounts)

    return accounts
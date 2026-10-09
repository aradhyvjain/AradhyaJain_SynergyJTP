def get_account_number():
    while True:
        try:
            account_number=int(input("Your account number"))
            if account_number<0:
                print("Please enter a valid account number")
                continue
            return account_number
        except ValueError:
            print("Please enter a valid account number")
            continue
def get_balance():
    while True:
        try:
            balance=float(input("Your account balance"))
            if balance<0:
                print("Please enter a valid balance")
                continue
            return balance
        except ValueError:
            print("Please enter a valid balance")
            continue
class account:
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number
    def debit(self,amount):
        if amount>self.balance:
            return "Insufficient balance"
        else:
            self.balance-=amount
            return "Transaction complete and your new balance is",self.balance
    def credit(self,amount):
        self.balance+=amount
        return "Transaction complete and your new balance is",self.balance
account1=account(get_balance(),get_account_number())
account1.debit(100)
print(account1.balance)
account1.credit(200)
print(account1.balance)

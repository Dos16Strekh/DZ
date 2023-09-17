class BankAccount:
    
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            result_deposit = self.balance + amount
            return print(f"Successful deposit of {result_deposit} on account {self.account_number}")
        else:
            return print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            result_withdraw = self.balance - amount
            return print(f"Successful withdraw of {result_withdraw} from account {self.account_number}")
        else:
            return  print(f"Withdraw failed: not enough balance {self.balance} on account {self.account_number}")
    
account1 = BankAccount(123456789, "Babayka", 100)

print(f'Your account number: {account1.account_number}, \nYour name: {account1.name}, \nYour balance: {account1.balance}')

account1.deposit(55)
account1.withdraw(43)
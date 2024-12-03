
class Saving_Account:
    def __init__(self,holder_name,initial_balance):
        self.holder_name=holder_name
        self.balance=initial_balance
        print(f"Saving Account Created is {self.holder_name} with balance {self.balance:.2f}")

    def get_balance(self):
        return print(f"Current balance of {self.holder_name} is {self.balance:.2f}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposited {amount:.2f} into {self.holder_name} account balance is {self.balance:.2f}")
    
    def check_balance(self,amount):
        if self.balance>=amount:
            return print(f"You have enough balance to withdraw {amount:.2f}")
        else:
            return print(f"You do not have enough balance to withdraw {amount:.2f}")
        
        
    
    def withdraw(self,amount):
        try:
            self.check_balance(amount)
            self.balance=self.balance-amount
            print(f"Withdrawn {amount:.2f} from {self.holder_name} account balance is {self.balance:.2f}")
        except  ValueError as error :
            print("Insufficient Balance")
            return error
    
    def transfer(self,amount,receiver_name):
        try:
            self.check_balance(amount)
            self.balance=self.balance-amount
            print(f"Transferred {amount:.2f} from {self.holder_name} to {receiver_name} account balance is {self.balance:.2f}")
        except :
            print("Insufficient Balance")
            
   
       
        
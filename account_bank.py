class BlanceException(Exception):
    pass



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
            return 
        else:
            raise BlanceException(f"You do not have enough balance {self.balance:.2f}")
        
        
    def withdraw(self,amount):
        try:
            self.check_balance(amount)
            self.balance=self.balance-amount
            print(f"Withdrawn {amount:.2f} from {self.holder_name} account balance is {self.balance:.2f}")
        except  BlanceException as error :
            return print(f"Insufficient Balance {error}")
    
    def transfer(self,amount,receiver_name):
        try:
            self.check_balance(amount)
            self.withdraw(amount)
            receiver_name.deposit(amount)
            print(f"Transferred {amount:.2f} from {self.holder_name} to {receiver_name} account balance is {self.balance:.2f}")
        except  BlanceException as error :
            return print(f"Insufficient Balance {error}")
        
class Normal_Account(Saving_Account):   # Inheritance
    def get_balance(self):
        return print(f"Current balance of {self.holder_name} is {self.balance + self.balance*0.05:.2f}")
    

         



            
   
       
        
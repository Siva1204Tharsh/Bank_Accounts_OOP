
class Account:
    def __init__(self, name, initial_amount):
       self.name = name
       self.balance = initial_amount
    

    def get_Balance(self):
       return self.balance

    def deposit(self, amount):
       self.balance += amount
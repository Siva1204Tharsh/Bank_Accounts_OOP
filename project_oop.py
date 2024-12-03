from account_bank import *
Siva=Saving_Account("Siva",1000)
# print(Siva)
# Siva.get_balance()

danu=Saving_Account("Danu",1000)

Siva.transfer(500,danu)
# danu.get_balance()
# Siva.get_balance()
danu.get_balance()


suji=Normal_Account("Suji",1000)
suji.get_balance()

print("----------------------------------------------------------------------------------------")

suji.transfer(500,Siva)
Siva.get_balance()
suji.get_balance()


suji.withdraw(500)
suji.withdraw(500)
class Balance: 
     def __init__(self, balance = 0): 
          self._balance = balance
       
     def get_balance(self): 
         return self._balance 
       
     def set_balance(self, balance): 
         self._balance = balance 
  

class Deposit: 
    def __init__(self, deposit = 0): 
         self._deposit = deposit 
      
    def getDeposit(self): 
        return self._deposit 
      
    def set_deposit(self, deposit): 
        self._deposit = deposit 
  
class Withdraw: 
    def __init__(self, withdraw = 0): 
         self._withdraw = withdraw 
      
    def getWithdraw(self): 
        return self._withdraw 
      
    def set_withdraw(self, withdraw): 
        self._withdraw = withdraw 
  


mark = Balance() 
raj = Deposit() 
bum = Withdraw()

print("Balance", mark.get_balance())
deposit = 100
raj.set_deposit(deposit)
print("Deposit", raj.getDeposit())


balance = raj.getDeposit()+mark.get_balance()
mark.set_balance(balance)

print("Balance", mark.get_balance())
deposit = 50
raj.set_deposit(deposit)
print("Deposit", raj.getDeposit())

balance = raj.getDeposit()+mark.get_balance()
mark.set_balance(balance)

print("Balance", mark.get_balance())
withdraw = 80
bum.set_withdraw(withdraw)
print("Withdraw", bum.getWithdraw())

balance = mark.get_balance()-bum.getWithdraw()
mark.set_balance(balance)

print("Balance", mark.get_balance())
withdraw = 20
bum.set_withdraw(withdraw)
print("Withdraw", bum.getWithdraw())

balance = mark.get_balance()-bum.getWithdraw()
mark.set_balance(balance)

print("Balance", mark.get_balance())

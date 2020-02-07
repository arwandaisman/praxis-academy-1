class Balance:
    def __init__(self, balance):
        self.set_a(balance)
   
    def get_a(self):
        return self.__balance
    
    def set_a(self, balance):
         self.__balance = balance

class Deposit:
    def __init__(self, deposit):
        self.set_a(deposit)
   
    def get_a(self):
        return self.__deposit
    
    def set_a(self, deposit):
         self.__deposit = deposit

a = Balance(100)
print(a.get_a())


b = Deposit(100)
print(b.get_a())


print(a.get_a())
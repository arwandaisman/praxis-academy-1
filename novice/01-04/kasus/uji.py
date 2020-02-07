class Deposit:
   def setDeposit(self,deposit):
      self.deposit=deposit
      print("Deposit anda: {}".format(self.deposit))

   def getDeposit(self):
      deposit=10

class Index:
   def depositMoney():
      deposit=int(input("Masukan Jumlah Uang"))
      Deposit().setDeposit(deposit)
   
   def manggil(self):
      depositMoney()


a = Index()
a.manggil()
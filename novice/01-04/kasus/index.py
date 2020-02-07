class Deposit:
    def setDeposit(self,deposit):
        self.deposit=deposit
        print("Deposit anda \t{}".format(self.deposit))

    def getDeposit():
        pass

class Withdraw:
    def setWithdraw():
        pass
    def getWithdraw():
        pass

class BalanceInquiry:
    def setBalanceInquiry():
        pass
    def getBalanceInquiry():
        pass

class Exit:
    def exitMachine(self):
        print("Thank for using Simple ATM")
        

class Index:
    def depositMoney():
        print()
        deposit=int(input("Masukan Jumlah Uang\t"))
        Deposit().setDeposit(deposit)
        otherSelection()

    def otherSelection():
        print("Other selection")

    print("Welcome to simple ATM")
    loop = 1
    while loop == 1:
        print("\nPlease Select ATM Transactions")
        print("Press [1] Deposit")
        print("Press [2] Withdraw")
        print("Press [3] Balance Inquiry")
        print("Press [4] Exit")
        select=int(input("What would you like to do?\t"))
        if select == 1:
            loop = 0
            print("Select 1")
            depositMoney()

        elif select == 2:
            print("select 2")
            def withdrawMoney(Withdraw):
                pass
        elif select == 3:
            print("select 3")
            def checkBalance(BalanceInquiry):
                pass
        elif select == 4:
            Exit().exitMachine()
            loop = 0
        else:
            print("Try Another Selection?")
            select=int(input("Press [1] Yes \t Press [2] No\t"))
            if select == 2:
                loop = 0
                Exit().exitMachine()
            elif select == 1:
                loop == 1


    def __init__():
        pass



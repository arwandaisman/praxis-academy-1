class Deposit:
    def setDeposit(self,deposit):
        self.deposit=deposit

    def getDeposit():
        return deposit

class Withdraw:
    def setWithdraw(self,withdraw):
        self.withdraw=withdraw
    def getWithdraw():
        return withdraw

class BalanceInquiry:
    def setBalanceInquiry(self,balance):
        self.balance=balance
    def getBalanceInquiry(balance):
        return balance

class Exit:
    def exitMachine(self):
        print("Thank for using Simple ATM")
        exit()
        
print(BalanceInquiry().setBalanceInquiry(10))
print(BalanceInquiry().getBalanceInquiry())

class Index(BalanceInquiry, Deposit):
    def otherSelection():
        print("Try Another Transaction?")
        select=int(input("Press [1] Yes \t Press [2] No\t"))
        if select == 2:
            Exit().exitMachine()
        elif select == 1:
            print()

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
            print("Select 1")
            deposit = int(input("Input Balance of Money\t"))
            print("Your Balance is {}".format(BalanceInquiry().getBalanceInquiry()))
            print()
            otherSelection()

        elif select == 2:
            print("Select 2")
            def withdrawMoney(Withdraw):
                pass
        elif select == 3:
            print("Select 3")
            print(BalanceInquiry().getBalanceInquiry())
            print("Your Balance is {}".format(BalanceInquiry().getBalanceInquiry()))
            otherSelection()
        elif select == 4:
            Exit().exitMachine()
            loop = 0
        else:
            print("Try Another Selection?")
            select=int(input("Press [1] Yes \t Press [2] No\t"))
            if select == 2:
                Exit().exitMachine()
                loop = 0
            elif select == 1:
                loop == 1

print("Halo")
print(BalanceInquiry().getBalanceInquiry(10))

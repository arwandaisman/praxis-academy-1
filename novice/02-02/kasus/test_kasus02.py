import unittest
from kasus02 import Deposit,Balance,Withdraw

class TestATM(unittest.TestCase):
    dep = Deposit()
    bal = Balance()
    wit = Withdraw()

    def test_deposit(self):
        result = self.dep.setDeposit(50)
        self.assertEqual(self.dep.getDeposit(), 90)
    
    def test_balance(self):
        result = self.bal.setBalance(90)
        self.assertEqual(self.bal.getBalance(), 80)

    def test_withdraw(self):
        result = self.wit.setWithdraw(90)
        self.assertEqual(self.wit.getWithdraw(), 90)

if __name__ == '__main__':
    unittest.main()

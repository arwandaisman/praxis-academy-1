import unittest
import kasus02

class TestSum(unittest.TestCase):
    def test_list_int(self):
        self.assertEqual(Deposit().setDeposit(6), Deposit().getDeposit(6))

if __name__ == '__main__':
    unittest.main()

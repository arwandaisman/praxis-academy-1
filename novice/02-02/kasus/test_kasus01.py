import unittest

class Case(unittest.TestCase):

    def __init__(self, deposit = 6): 
         self._deposit = deposit 
      
    def getDeposit(self): 
        return self._deposit 
      
    def setDeposit(self, deposit): 
        self._deposit = deposit 

    def test_sum_tuple(self):
        self.assertEqual(setDeposit(6), getDeposit(), "Should be 6")

if __name__ == '__main__':
    unittest.main()
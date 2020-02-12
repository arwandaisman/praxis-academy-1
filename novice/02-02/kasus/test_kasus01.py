import unittest
from kasus01 import Bootcamp
from kasus02 import Deposit,Balance,Withdraw
from kasus03 import bubble_sort
from kasus04 import Animal, Sheep
from kasus05 import fib,fib2


class Test(unittest.TestCase):
    def test_nama(self):
        result = Bootcamp("Cahya", "Mentor")
        self.assertEqual(result.nama, "Cahya")

    def test_createAssesment(self):
        result = Bootcamp("A","B").createAssesment()
        self.assertEqual(Bootcamp.assesment, 1)
    
    def test_createTask(self):
        result = Bootcamp("A","B").createTask()
        self.assertEqual(Bootcamp.assesment, 0)


if __name__ == '__main__':
    unittest.main()

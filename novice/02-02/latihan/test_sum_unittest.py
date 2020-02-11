import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

# Output testing by unittest
#
# .F
# ======================================================================
# FAIL: test_sum_tuple (__main__.TestSum)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_sum_unittest.py", line 9, in test_sum_tuple
#    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
# AssertionError: 5 != 6 : Should be 6
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# FAILED (failures=1)

# testing by nose2
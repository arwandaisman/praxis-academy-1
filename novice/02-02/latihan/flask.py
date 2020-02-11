import my_app
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        my_app.app.testing = True
        self.app = my_app.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        # Make your assertions

# $ python -m unittest test_flask.py
# E
# ======================================================================
# ERROR: test_flask (unittest.loader._FailedTest)
# ----------------------------------------------------------------------
# ImportError: Failed to import test module: test_flask
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/unittest/loader.py", line 153, in loadTestsFromName
#     module = __import__(module_name)
#   File "/home/dxc/Documents/Github/praxis-academy/novice/02-02/latihan/test_flask.py", line 1, in <module>
#     import my_app
# ModuleNotFoundError: No module named 'my_app'
# 
# 
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# 
# FAILED (errors=1)
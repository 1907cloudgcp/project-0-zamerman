# Import standard python modules
import unittest
import os
import sys

# Get path to main program files
test_path = os.path.abspath(__file__).split('/')
main_path = test_path[:-6]
main_path.append('main/python/com/revature')
main_path = '/'.join(main_path)

# Append this path to sys interpreter
sys.path.insert(0, main_path)

# Import custom modules
from IO.Client import Client

class TestClientDefault(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_username_default(self):
        self.assertEqual(self.client._Client__username, '')

    def test_password_default(self):
        self.assertEqual(self.client._Client__password, '')

    def test_balance_default(self):
        self.assertEqual(self.client._Client__balance, 0)

    def test_transactions_default(self):
        self.assertEqual(self.client._Client__transactions, [])

if __name__ == '__main__':
    unittest.main()

# Import standard python modules
import unittest
import os
import sys
import logging
import logging.config
import yaml

# Get path to main program files
test_path = os.path.abspath(__file__).split('/')
main_path = test_path[:-6]
main_path.append('main/python/com/revature')
main_path = '/'.join(main_path)

# Append this path to sys interpreter
sys.path.insert(0, main_path)

# Import custom modules
from IO.Client import Client
from error.Error import (InvalidCharacterError, SecureStringError,
IntegerRequiredError, NegativeIntegerError)
from logger.Logger import Logger

class TestClientMethods(unittest.TestCase):

    def setUp(self):
        self.client = Client(username="username",
                             password="password",
                             balance=1000,
                             transactions=['transaction'])

    def test_get_username(self):
        self.assertEqual(self.client.get_username(), 'username')

    def test_get_password(self):
        self.assertEqual(self.client.get_password(), "password")

    def test_get_balance(self):
        self.assertEqual(self.client.get_balance(), 1000)

    def test_get_transactions(self):
        self.assertEqual(self.client.get_transactions(), ['transaction'])

    def test_set_username(self):
        self.client.set_username("emanresu")
        self.assertEqual(self.client._Client__username, 'emanresu')

    def test_set_username_space(self):
        with self.assertRaises(InvalidCharacterError):
            self.client.set_username('user name')

    def test_set_username_length(self):
        with self.assertRaises(SecureStringError):
            self.client.set_username('user')

    def test_set_password(self):
        self.client.set_password("drowssap")
        self.assertEqual(self.client._Client__password, "drowssap")

    def test_set_password_space(self):
        with self.assertRaises(InvalidCharacterError):
            self.client.set_password('pass word')

    def test_set_password_length(self):
        with self.assertRaises(SecureStringError):
            self.client.set_password('pass')

    def test_set_balance(self):
        self.client.set_balance(2000)
        self.assertEqual(self.client._Client__balance, 2000)

    def test_set_balance_not_int(self):
        with self.assertRaises(IntegerRequiredError):
            self.client.set_balance('1000')

    def test_set_balance_negative(self):
        with self.assertRaises(NegativeIntegerError):
            self.client.set_balance(-1000)

    def test_set_transactions(self):
        self.client.set_transactions(['transaction', 'noitcasnart'])
        self.assertEqual(self.client._Client__transactions, ['transaction', 'noitcasnart'])

    def test_equality(self):
        client1 = Client('username')
        client2 = Client('username', 'password')
        self.assertEqual(client1, client2)

    def test_inequality(self):
        client1 = Client('username')
        client2 = Client('zamerman')
        self.assertNotEqual(client1, client2)


def main():
    # Configure Logger

	# Find logging.yaml config file relative to this file
	file_path = os.path.abspath(__file__)
	config_path = file_path.split('/')[:-5]
	config_path.append('resources/logging.yaml')
	config_path = '/'.join(config_path)

	# Securely read and load yaml config file
	if os.path.exists(config_path):
	    with open(config_path, 'r') as f:
	        config = yaml.safe_load(f.read())

	    # Enable our loaded configuration
	    logging.config.dictConfig(config)
	else:
	    raise ValueError('Logging configuration not found')

	# Start logger
	log = Logger(__name__)
	log.log_info("start logger")

	# Start tests
	log.log_info("start testing")

if __name__ == '__main__':
    main()
    unittest.main()

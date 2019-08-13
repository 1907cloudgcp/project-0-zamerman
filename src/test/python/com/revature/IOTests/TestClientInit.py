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

class TestClientInit(unittest.TestCase):

    def setUp(self):
        self.client = Client(username="username",
                             password="password",
                             balance=1000,
                             transactions=['transaction'])

    def test_username_init(self):
        self.assertEqual(self.client._Client__username, 'username')

    def test_username_init_space(self):
        with self.assertRaises(InvalidCharacterError):
            client = Client(username="user name")

    def test_username_init_length(self):
        with self.assertRaises(SecureStringError):
            client = Client(username="user")

    def test_password_init(self):
        self.assertEqual(self.client._Client__password, "password")

    def test_password_init_space(self):
        with self.assertRaises(InvalidCharacterError):
            client = Client(password="pass word")

    def test_password_init_length(self):
        with self.assertRaises(SecureStringError):
            client = Client(password="pass")

    def test_balance_init(self):
        self.assertEqual(self.client._Client__balance, 1000)

    def test_balance_init_not_int(self):
        with self.assertRaises(IntegerRequiredError):
            client = Client(balance="1000")

    def test_balance_init_negative(self):
        with self.assertRaises(NegativeIntegerError):
            client = Client(balance=-1000)

    def test_transactions_init(self):
        self.assertEqual(self.client._Client__transactions, ['transaction'])


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

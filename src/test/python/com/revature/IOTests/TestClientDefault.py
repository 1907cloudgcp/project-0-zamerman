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
from logger.Logger import Logger

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

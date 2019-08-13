# Import standard python modules
import os
import sys
import unittest
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
from IO.ClientDAOJSON import ClientDAOJSON
from service.BankSession import BankSession
from error.Error import ClientSetupError, LoginError
from logger.Logger import Logger

class TestBankSession(unittest.TestCase):
    def setUp(self):
        # Code to assemble and put together path to vault file relative to file
        file_path = os.path.abspath(__file__)
        vault_path = file_path.split('/')[:-7]
        vault_path.append('data/vault.json')
        vault_path = '/'.join(vault_path)

        # Instantiate a ClientDAO
        self.client_dao = ClientDAOJSON(vault_path)

        # Instantiate a BankSession
        self.bank_session = BankSession(self.client_dao)

    def tearDown(self):
        # Clear vault
        self.client_dao.clear_clients()

    def test_init(self):
        self.assertEqual(self.bank_session.client, Client())
        self.assertEqual(self.bank_session.client_dao, self.client_dao)

    def test_current_session(self):
        self.assertEqual(self.bank_session.current_session(), '')

    def test_register(self):
        self.bank_session.register(Client())
        self.assertEqual(self.bank_session.client, Client())
        self.assertEqual(self.client_dao.get_clients(), [Client()])

    def test_register_fail(self):
        self.bank_session.register(Client())
        with self.assertRaises(ClientSetupError):
            self.bank_session.register(Client())

    def test_login(self):
        self.client_dao.add_client(Client('username', 'password'))
        self.bank_session.login(Client('username', 'password'))
        self.assertEqual(self.bank_session.current_session(), 'username')

    def test_login_fail(self):
        self.client_dao.add_client(Client('username', 'password'))
        with self.assertRaises(LoginError):
            self.bank_session.login(Client('username1', 'password1'))

    def test_logout(self):
        self.bank_session.register(Client('username', 'password'))
        self.bank_session.logout_session()
        self.assertEqual(self.bank_session.current_session(), '')

    def test_view_balance(self):
        self.bank_session.register(Client('username', 'password', 10000))
        self.assertEqual(self.bank_session.view_balance(), 10000)


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

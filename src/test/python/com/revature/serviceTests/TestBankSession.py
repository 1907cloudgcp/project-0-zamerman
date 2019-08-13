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
from IO.ClientDAOJSON import ClientDAOJSON
from service.BankSession import BankSession
from error.Error import ClientRequiredError, ClientSetupError

class TestBankSession(unittest.TestCase):
    def setUp(self):
        # Code to assemble and put together path to vault file relative to file
    	file_path = os.path.abspath(__file__)
    	vault_path = file_path.split('/')[:-7]
    	vault_path.append('data/vault.json')
    	vault_path = '/'.join(vault_path)
    	self.client_dao = ClientDAOJSON(vault_path)
        self.bank_session = BankSession(self.client_dao)

        
    def tearDown(self):
        # Clear vault
        self.client_dao.clear_clients()

    def test_init(self):
        self.assertEqual(self.bank_session.client, Client())
        self.assertEqual(self.bank_session.client_dao, self.client_dao)

    def test_current_session(self):
        self.assertEqual(self.bank_session.current_session(), Client())

    def test_register(self):
        self.bank_session.register(Client())
        self.assertEqual(self.bank_session.client, Client())
        self.assertEqual(self.client_dao.get_clients(), [Client()])


if __name__ == '__main__':
    unittest.main()

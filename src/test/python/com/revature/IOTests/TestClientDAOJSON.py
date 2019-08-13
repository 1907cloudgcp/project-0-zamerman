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
from error.Error import ClientRequiredError, ClientSetupError

class TestClientDAOJSON(unittest.TestCase):

    def setUp(self):
        # Code to assemble and put together path to vault file relative to file
    	file_path = os.path.abspath(__file__)
    	vault_path = file_path.split('/')[:-7]
    	vault_path.append('data/vault.json')
    	self.vault_path = '/'.join(vault_path)

    	# Instantiate a ClientDAO for json files
    	self.client_dao = ClientDAOJSON(self.vault_path)

    def tearDown(self):
        # Clear vault
        self.client_dao.clear_clients()

    def test_init(self):
        self.assertEqual(self.client_dao.vault_file, self.vault_path)

    def test_get_clients(self):
        self.assertEqual(self.client_dao.get_clients(), [])

    def test_add_client(self):
        self.client_dao.add_client(Client())
        self.assertEqual(self.client_dao.get_clients(), [Client()])

    def test_add_client_not_client(self):
        with self.assertRaises(ClientRequiredError):
            self.client_dao.add_client("client")

    def test_add_client_client_setup(self):
        with self.assertRaises(ClientSetupError):
            self.client_dao.add_client(Client("zamerman", "password"))
            self.client_dao.add_client(Client("zamerman", "password"))

    def test_update_client(self):
        self.client_dao.add_client(Client('username', 'password'))
        self.assertEqual(self.client_dao.get_clients()[0].get_username(), 'username')
        self.assertEqual(self.client_dao.get_clients()[0].get_password(), 'password')
        self.client_dao.update_client(Client('username', 'PASSWORD'))
        self.assertEqual(self.client_dao.get_clients()[0].get_username(), 'username')
        self.assertEqual(self.client_dao.get_clients()[0].get_password(), 'PASSWORD')

    def test_update_client_not_client(self):
        with self.assertRaises(ClientRequiredError):
            self.client_dao.update_client('client')

    def test_delete_client(self):
        self.client_dao.add_client(Client('username', 'password'))
        self.assertEqual(self.client_dao.get_clients()[0].get_username(), 'username')
        self.assertEqual(self.client_dao.get_clients()[0].get_password(), 'password')
        self.client_dao.delete_client(Client('username'))
        self.assertEqual(self.client_dao.get_clients(), [])

    def test_delete_client_not_client(self):
        with self.assertRaises(ClientRequiredError):
            self.client_dao.delete_client('client')

    def test_clear_clients(self):
        self.client_dao.add_client(Client('username', 'password'))
        self.client_dao.add_client(Client('username1', 'password'))
        self.client_dao.clear_clients()
        self.assertEqual(self.client_dao.get_clients(), [])

if __name__ == '__main__':
    unittest.main()

from IO.Client import Client
from IO.ClientDAOJSON import ClientDAOJSON
from error.TwinClientError import TwinClientError

class Bank():
    def __init__(self, vault_path):
        self.vault_access = ClientDAOJSON(vault_path)

    def register(self, client):
        try:
            self.vault_access.add_client(client)
        except TwinClientError as e:
            print("TwinClientError: " + e.strerror)

    def login(self, client):
        print(client in self.vault_access.get_clients())

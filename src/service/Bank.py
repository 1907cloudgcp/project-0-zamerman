from IO.Client import Client
from IO.ClientDAOJSON import ClientDAOJSON
from error.Error import LoginError, SessionError

class Bank():
    def __init__(self, vault_path):
        self.vault_access = ClientDAOJSON(vault_path)
        self.client = Client()

    def current_session(self):
        return self.client.get_username()

    def logout_session(self):
        self.client = Client()

    def register(self, client):
        self.vault_access.add_client(client)
        self.client = client

    def login(self, client):
        clients = self.vault_access.get_clients()
        if client in clients:
            pulled_client = clients[clients.index(client)]
            if client.get_password() == pulled_client.get_password():
                self.client = pulled_client
            else:
                raise LoginError("Wrong username or password")
        else:
            raise LoginError("Wrong username or password")

    def view_balance(self):
        if self.client in self.vault_access.get_clients():
            return self.client.get_balance()
        else:
            raise SessionError('Not logged in or registered with bank')

    def deposit(self, cash):
        if self.client in self.vault_access.get_clients():
            self.client.set_balance(self.client.get_balance() + cash)
            record = "date: deposited: $" + str(cash)
            self.client.get_transactions().append(record)
            self.vault_access.update_client(self.client)
        else:
            raise SessionError('Not logged in or registered with bank')

    def withdraw(self, cash):
        if self.client in self.vault_access.get_clients():
            self.client.set_balance(self.client.get_balance() - cash)
            record = "date: withdrawn: $" + str(cash)
            self.client.get_transactions().append(record)
            self.vault_access.update_client(self.client)
        else:
            raise SessionError('Not logged in or registered with bank')

    def view_transactions(self):
        if self.client in self.vault_access.get_clients():
            for transaction in self.client.get_transactions():
                print(transaction)
        else:
            raise SessionError('Not logged in or registered with bank')

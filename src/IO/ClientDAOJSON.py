import sys
import os
import json

sys.path.insert(0, '/'.join(os.getcwd().split('/')[:-1]))

from IO.ClientDAO import ClientDAO
from IO.Client import Client

class ClientDAOJSON(ClientDAO):
    def __init__(self, json_file):
        self.__json_file = json_file

    def get_clients(self):
        with open(self.__json_file, 'r') as f:
            client_dicts = json.load(f)
        try:
            clients = [Client(dict['username'], dict['password'], dict['balance'], dict['transactions']) for dict in client_dicts]
        except ValueError:
            clients = []
        return clients

    def add_client(self, new_client):
        clients = self.get_clients()
        clients.append(new_client)
        client_dicts = [client.__dict__ for client in clients]
        with open(self.__json_file, 'w') as f:
            json.dump(client_dicts, f)

    def update_client(self):
        pass

    def delete_client(self):
        pass

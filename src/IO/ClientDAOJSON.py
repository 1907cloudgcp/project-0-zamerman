from IO.ClientDAO import ClientDAO
from IO.Client import Client
from error.Error import ClientSetupError
import json
import sys
import os


class ClientDAOJSON(ClientDAO):
    """
    JSON access object
    """

    def __init__(self, vault_file):
        """
        vault_file : path to json vault file
        """
        self.vault_file = vault_file

    def get_clients(self):
        """
        returns a list of clients in the vault
        """
        with open(self.vault_file, 'r') as f:
            client_dicts = json.load(f)
        clients = []
        for dict in client_dicts:
            new_client = Client()
            new_client.__dict__ = dict
            clients.append(new_client)
        return clients

    def add_client(self, new_client):
        """
        adds a client to the vault unless that client is already in the vault

        clients are uniquely identified by username so even if two clients with
        the same username have different passwords they are still considered
        the same
        """

        # get a list of clients
        clients = self.get_clients()

        # check if the client is already in the vault before adding
        if new_client in clients:
            raise ClientSetupError('Client with same username already exists')
        else:
            clients.append(new_client)

        # write the updated vault list to the vault
        client_dicts = [client.__dict__ for client in clients]
        with open(self.vault_file, 'w') as f:
            json.dump(client_dicts, f, indent=4)

    def update_client(self, client):
        """
        changes a client in the vault unless a client with the same username as
        new_client already exists

        always deletes old client

        clients are uniquely identified by username so even if two clients with
        the same username have different passwords they are still considered
        the same
        """

        # get a list of clients
        clients = self.get_clients()

        # remove old client
        clients.remove(client)

        # check if the updated client is already in the vault before adding
        if client in clients:
            raise ClientSetupError('Client with same username already exists')
        else:
            clients.append(client)

        # write the updated vault list to the vault
        client_dicts = [client.__dict__ for client in clients]
        with open(self.vault_file, 'w') as f:
            json.dump(client_dicts, f, indent=4)


    def delete_client(self, client):
        """
        deletes client from vault

        clients are uniquely identified by username so even if two clients with
        the same username have different passwords they are still considered
        the same
        """

        # get a list of clients
        clients = self.get_clients()

        # remove client
        clients.remove(client)

        # write the updated vault list to the vault
        client_dicts = [client.__dict__ for client in clients]
        with open(self.vault_file, 'w') as f:
            json.dump(client_dicts, f, indent=4)

# import json library for json file loading and dumping
import json

# Import custom errors, IO logger, and client models
from .ClientDAO import ClientDAO
from .Client import Client, requires_client
from error.Error import ClientSetupError
from logger.Logger import Logger


log = Logger(__name__)

class ClientDAOJSON(ClientDAO):
    """
    JSON access object
    """

    def __init__(self, vault_file):
        """
        vault_file : path to json vault file
        """

        self.vault_file = vault_file

        log_prefix = "instantiated ClientDAO for json file at: "
        log.log_debug(log_prefix + vault_file)

    def get_clients(self):
        """
        returns a list of clients in the vault
        """

        # Securely load client dictionaries from json vault file
        with open(self.vault_file, 'r') as f:
            client_dicts = json.load(f)

        # Create list of clients from client dictionaries
        clients = []
        for dict in client_dicts:
            new_client = Client()
            new_client.__dict__ = dict
            clients.append(new_client)

        log.log_debug("pulled list of Clients: " + str(clients))
        return clients

    @requires_client
    def add_client(self, new_client):
        """
        adds a client to the vault unless that client is already in the vault

        clients are uniquely identified by username so even if two clients with
        the same username have different passwords they are still considered
        the same

        can raise a ClientSetupError if a client with the same username already
        exists
        """

        # get a list of clients
        clients = self.get_clients()

        # check if the client is already in the vault before adding
        if new_client in clients:
            log.log_error("ClientSetupError: Client with same username already exists")
            raise ClientSetupError('Client with same username already exists')
        else:
            clients.append(new_client)

        # write the updated vault list to the vault
        client_dicts = [client.__dict__ for client in clients]
        with open(self.vault_file, 'w') as f:
            json.dump(client_dicts, f, indent=4)

        log.log_debug("added {0} to {1}".format(str(new_client), str(clients)))

    @requires_client
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

        # append updated client
        clients.append(client)

        # write the updated vault list to the vault
        client_dicts = [client.__dict__ for client in clients]
        with open(self.vault_file, 'w') as f:
            json.dump(client_dicts, f, indent=4)

        log.log_debug("updated {0}".format(str(client)))

    @requires_client
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

        log.log_debug("deleted {0}".format(str(client)))

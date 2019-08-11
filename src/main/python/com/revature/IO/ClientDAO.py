from abc import ABC, abstractmethod


class ClientDAO(ABC):
    """
    Abstract class for Data Access Objects for Client with four methods.

    get_clients
    add_client
    update_client
    delete_client
    """

    @abstractmethod
    def get_clients(self):
        pass

    @abstractmethod
    def add_client(self, new_client):
        pass

    @abstractmethod
    def update_client(self, client, updated_client):
        pass

    @abstractmethod
    def delete_client(self, client):
        pass

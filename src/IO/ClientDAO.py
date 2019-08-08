from abc import ABC, abstractmethod

class ClientDAO(ABC):

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

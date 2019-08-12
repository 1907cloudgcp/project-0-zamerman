from .decorators import secure_string, requires_int, invalid_characters
from .logger.IOLogger import log_info


class Client():
    """
    Data class which contains fields and methods for Client's username,
    password, balance, and transactions.

    username : unique identifier for Client objects : what is compared
    """

    def __init__(self, username="", password="", balance=0, transactions=[]):
        """
        Sets client fields
        """

        # set Client fields
        self.set_username(username)
        self.set_password(password)
        self.set_balance(balance)
        self.set_transactions(transactions)

        # log Client Creation
        log_info("Client({0}, {1}, {2}, {3})".format(username,
                                                     password,
                                                     balance,
                                                     transactions))

    def get_username(self):
        """
        Get client's username
        """
        log_info("Client username pulled")
        return self.__username

    @invalid_characters
    @secure_string
    def set_username(self, username):
        """
        Set client's username
        """
        log_info("Client username set to: {0}".format(username))
        self.__username = username

    def get_password(self):
        """
        Get client's password
        """
        log_info("Client password pulled")
        return self.__password

    @invalid_characters
    @secure_string
    def set_password(self, password):
        """
        Set client's password
        """
        log_info("Client password set to: {0}".format(password))
        self.__password = password

    def get_balance(self):
        """
        Get client's balance
        """
        log_info("Client balance pulled")
        return self.__balance

    @requires_int
    def set_balance(self, balance):
        """
        Set client's balance
        """
        log_info("Client balance set to: {0}".format(balance))
        self.__balance = balance

    def get_transactions(self):
        """
        Get client's transactions
        """
        log_info("Client transactions pulled")
        return self.__transactions

    def set_transactions(self, transactions):
        """
        Set client's transactions
        """
        log_info("Client transactions set")
        self.__transactions = transactions

    def __eq__(self, other_client):
        """
        Compares client usernames
        """
        username_check = self.__username == other_client.get_username()
        log_info("Client comparison made")
        return username_check

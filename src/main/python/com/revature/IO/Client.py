from logger.Logger import Logger
from decorators.decorator import invalid_characters, secure_string, requires_int, requires_positive
from error.Error import ClientRequiredError


log = Logger(__name__)

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
        log_format = "instantiated Client({0}, {1}, {2}, {3})"
        log.log_debug(log_format.format(username, password, balance, transactions))

    def get_username(self):
        """
        Get client's username
        """

        log.log_debug("pulled Client username: " + self.__username)
        return self.__username

    @invalid_characters
    @secure_string
    def set_username(self, username):
        """
        Set client's username
        """

        log.log_debug("set Client username to: {0}".format(username))
        self.__username = username

    def get_password(self):
        """
        Get client's password
        """

        log.log_debug("pulled Client password: " + self.__password)
        return self.__password

    @invalid_characters
    @secure_string
    def set_password(self, password):
        """
        Set client's password
        """

        log.log_debug("set Client password to: {0}".format(password))
        self.__password = password

    def get_balance(self):
        """
        Get client's balance
        """

        log.log_debug("pulled Client balance: " + str(self.__balance))
        return self.__balance

    @requires_int
    @requires_positive
    def set_balance(self, balance):
        """
        Set client's balance
        """

        log.log_debug("set Client balance to: {0}".format(balance))
        self.__balance = balance

    def get_transactions(self):
        """
        Get client's transactions
        """

        log.log_debug("pulled Client transactions: " + str(self.__transactions))
        return self.__transactions

    def set_transactions(self, transactions):
        """
        Set client's transactions
        """

        log.log_debug("set Client transactions to: " + str(transactions))
        self.__transactions = transactions

    def __eq__(self, other_client):
        """
        Compares client usernames
        """

        username_check = self.__username == other_client.get_username()
        log.log_debug("made Client comparison")
        return username_check


def requires_client(func):
    def func_wrapper(self, client):
        if type(client) == Client:
            return func(self, client)
        else:
            log.log_error("ClientRequiredError: requires Client argument")
            raise ClientRequiredError("requires Client argument")
    return func_wrapper

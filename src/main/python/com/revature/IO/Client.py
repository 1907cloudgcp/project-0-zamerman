from error.Error import ShortUsernameError


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

    def get_username(self):
        """
        Get client's username
        """
        return self.__username

    def set_username(self, username):
        """
        Set client's username
        """
        if username == '':
            self.__username = username
        elif len(username) < 8:
            raise ShortUsernameError
        else:
            self.__username = username

    def get_password(self):
        """
        Get client's password
        """
        return self.__password

    def set_password(self, password):
        """
        Set client's password
        """
        self.__password = password

    def get_balance(self):
        """
        Get client's balance
        """
        return self.__balance

    def set_balance(self, balance):
        """
        Set client's balance
        """
        self.__balance = balance

    def get_transactions(self):
        """
        Get client's transactions
        """
        return self.__transactions

    def set_transactions(self, transactions):
        """
        Set client's transactions
        """
        self.__transactions = transactions

    def __eq__(self, other_client):
        """
        Compares client usernames
        """
        username_check = self.__username == other_client.get_username()
        return username_check

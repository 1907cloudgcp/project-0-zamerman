#!/usr/bin/env python3


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
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = transactions

    def get_username(self):
        """
        Get client's username
        """
        return self.username

    def set_username(self, username):
        """
        Set client's username
        """
        self.username = username

    def get_password(self):
        """
        Get client's password
        """
        return self.password

    def set_password(self, password):
        """
        Set client's password
        """
        self.password = password

    def get_balance(self):
        """
        Get client's balance
        """
        return self.balance

    def set_balance(self, balance):
        """
        Set client's balance
        """
        self.balance = balance

    def get_transactions(self):
        """
        Get client's transactions
        """
        return self.transactions

    def set_transactions(self, transactions):
        """
        Set client's transactions
        """
        self.transactions = transactions

    def __eq__(self, other_client):
        """
        Compares client usernames
        """
        username_check = self.username == other_client.get_username()
        return username_check

#!/usr/bin/env python3
import logging
import logging.config
import yaml

class Client():
    """
    Data class which contains fields and methods for Client's username,
    password, balance, and transactions.
    """

    def __init__(self, username, password, balance, transactions):
        self.__username = username
        self.__password = password
        self.__balance = balance
        self.__transactions = transactions

        config_path = '/vagrant/project-0-zamerman/src/main/resources/logging.yaml'
        config = ''
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

        self.__logger = logging.getLogger(__name__)
        self.__logger.info('Client created with name: ' + __name__)

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getTransactions(self):
        return self.__transactions

    def setTransactions(self, transactions):
        self.__transactions = transactions

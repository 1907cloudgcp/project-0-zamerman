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
        # Set Client fields
        self.__username = username
        self.__password = password
        self.__balance = balance
        self.__transactions = transactions

        # Load logging configuration yaml file
        config_path = '''/vagrant/project-0-zamerman/bankapp/resources/logging.yaml'''
        config = ''
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

        # Create Client logger
        self.__logger = logging.getLogger(__name__)

        # Send info log upon Client creation
        self.__logger.info('Client created; ' +
                           'username: ' + username +
                           '; password: ' + password)

    def get_username(self):
        """
        Get client's username
        """
        self.__logger.info('Client username requested')
        return self.__username

    def set_username(self, username):
        """
        Set client's username
        """
        self.__username = username
        self.__logger.info('Client username changed to ' + username)

    def get_password(self):
        """
        Get client's password
        """
        self.__logger.info('Client password requested')
        return self.__password

    def set_password(self, password):
        """
        Set client's password
        """
        self.__password = password
        self.__logger.info('Client password changed to ' + password)

    def get_balance(self):
        """
        Get client's balance
        """
        self.__logger.info('Client balance requested')
        return self.__balance

    def set_balance(self, balance):
        """
        Set client's balance
        """
        self.__balance = balance
        self.__logger.info('Client balance changed to ' + balance)

    def get_transactions(self):
        """
        Get client's transactions
        """
        self.__logger.info('Client transactions requested')
        return self.__transactions

    def set_transactions(self, transactions):
        """
        Set client's transactions
        """
        self.__transactions = transactions
        self.__logger.info('Client transactions changed')

#!/usr/bin/env python3
import logging
import logging.config
import yaml


class Client():
    """
    Data class which contains fields and methods for Client's username,
    password, balance, and transactions.
    """

    def __init__(self, username="", password="", balance=0, transactions=[]):
        # Set Client fields
        self.username = username
        self.password = password
        self.balance = balance
        self.transactions = transactions

    def get_username(self):
        """
        Get client's username
        """
        __get_logger().info('Client username requested')
        return self.username

    def set_username(self, username):
        """
        Set client's username
        """
        self.username = username
        __get_logger().info('Client username changed to ' + username)

    def get_password(self):
        """
        Get client's password
        """
        __get_logger().info('Client password requested')
        return self.password

    def set_password(self, password):
        """
        Set client's password
        """
        self.password = password
        __get_logger().info('Client password changed to ' + password)

    def get_balance(self):
        """
        Get client's balance
        """
        __get_logger().info('Client balance requested')
        return self.balance

    def set_balance(self, balance):
        """
        Set client's balance
        """
        self.balance = balance
        __get_logger().info('Client balance changed to ' + balance)

    def get_transactions(self):
        """
        Get client's transactions
        """
        __get_logger().info('Client transactions requested')
        return self.transactions

    def set_transactions(self, transactions):
        """
        Set client's transactions
        """
        self.transactions = transactions
        __get_logger().info('Client transactions changed')

    @staticmethod
    def __get_logger():
        # Load logging configuration yaml file
        config_path = '''/vagrant/project-0-zamerman/bankapp/resources/logging.yaml'''
        config = ''
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

        # Create Client logger
        return logging.getLogger(__name__)

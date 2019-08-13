from service.BankSession import BankSession
from IO.Client import Client
from error.Error import (SessionError, ClientSetupError, SecureStringError,
InvalidCharacterError, NegativeIntegerError)
from logger.Logger import Logger

help_text = '''
List of commands:
help            presents a list of commands
register        register and login as a new client
login           login as a client in the bank
logout          logout of the bank
balance         view session balance
deposit         deposit into account
withdraw        withdraw from account
transactions    view past transactions
quit/exit       exit the program'''

log = Logger(__name__)


class ConsoleView():
    """
    A program to construct an interactive console that interacts with clients
    using a BankSession instance
    """

    def __init__(self, session):

        # Intro text that only runs once at the beginning
        print('\nWelcome to {redacted} Bank!')
        print('For a list of commands input `help`')

        self.session = session

        log.log_info('instantiated ConsoleView instance')

    def run(self):
        """
        A instance method that prompts the user for input and passes it to
        a parse function to be directed to the appropriate event
        """

        log.log_debug('requesting response')

        # Read user selection response
        print('')
        response = input("$" + self.session.current_session() + ":")

        log.log_debug('sending response to be parsed: ' + response)
        self.parse_response(response)

    def parse_response(self, response):
        """
        instance method to parse user response and point to appropriate
        response
        """

        log.log_debug('received response: `{0}` and parsing'.format(response))
        if response == 'help':
            log.log_info('responding to help request')
            print(help_text)
            self.run()
        elif response == 'register':
            log.log_info('responding to registration request')
            self.registration_event()
        elif response == 'login':
            log.log_info('responding to login request')
            self.login_event()
        elif response == 'logout':
            log.log_info('responding to logout request')
            self.logout_event()
        elif response == 'balance':
            log.log_info('responding to balance request')
            self.view_balance_event()
        elif response == 'deposit':
            log.log_info('responding to deposit request')
            self.deposit_event()
        elif response == 'withdraw':
            log.log_info('responding to withdraw request')
            self.withdraw_event()
        elif response == 'transactions':
            log.log_info('responding to transactions request')
            self.view_transactions_event()
        elif response == 'quit' or response == 'exit':
            log.log_info('responding to quit request')
            self.quit_event()
        else:
            log.log_debug('invalid request')
            print('invalid command')
            self.run()

    def registration_event(self):
        """
        event method for registration requests
        """

        # Attempt to register
        try:
            # Prompt for necessary fields
            print('')
            username = input('username:')
            password = input('password:')
            starting_balance = int(input('starting balance (int):'))

            # Register using BankSession
            log.log_debug("register a Client object with the BankSession")
            self.session.register(Client(username, password, starting_balance))

        # Except different possible errors
        except ClientSetupError as e:
            log.log_error("ClientSetupError: " + e.strerror)
        except SecureStringError as e:
            log.log_error("SecureStringError: " + e.strerror)
        except InvalidCharacterError as e:
            log.log_error("InvalidCharacterError: " + e.strerror)
        except NegativeIntegerError as e:
            log.log_error("NegativeIntegerError: " + e.strerror)
        except ValueError as e:
            log.log_error("ValueError: Balance must be of type int")

        # Redirect back to run for further responses
        log.log_info("finished response to registration request")
        self.run()

    def login_event(self):
        """
        event method for login requests
        """

        # Try to login
        try:
            # Prompt for necessary fields
            print('')
            username = input('username:')
            password = input('password:')

            # Login using BankSession
            log.log_debug("login a Client object with the BankSession")
            self.session.login(Client(username, password))

        # Except different possible errors
        except SessionError as e:
            log.log_error("SessionError:" + e.strerror)
        except ClientSetupError as e:
            log.log_error("ClientSetupError: " + e.strerror)
        except SecureStringError as e:
            log.log_error("SecureStringError: " + e.strerror)

        # Redirect back to run for further responses
        log.log_info("finished response to login request")
        self.run()

    def logout_event(self):
        """
        event method for logout requests
        """

        # Logout using BankSession
        self.session.logout_session()

        # Redirect back to run for further responses
        log.log_info("finished response to logout request")
        self.run()

    def view_balance_event(self):
        """
        event method for balance requests
        """

        # Try to request the session balance
        try:
            # Request and print the session balance from BankSession instance
            print('\nbalance:' + str(self.session.view_balance()))

        # Except SessionErrors for when our session is not registered or
        # logged in
        except SessionError as e:
            log.log_error("SessionError:" + e.strerror)

        # Redirect back to run for futher responses
        log.log_info("finished response to balance request")
        self.run()

    def deposit_event(self):
        """
        event method for deposit requests
        """

        # Try to deposit
        try:
            # Get user deposit and deposit with BankSession instance
            print('')
            self.session.deposit(int(input('deposit (int):')))

        # Except for different errors
        except SessionError as e:
            log.log_error("SessionError:" + e.strerror)
        except NegativeIntegerError as e:
            log.log_error("NegativeIntegerError: " + e.strerror)
        except ValueError as e:
            log.log_error("ValueError: Balance must be of type int")

        # Redirect back to run for futher responses
        log.log_info("finished response to deposit request")
        self.run()

    def withdraw_event(self):
        """
        event method for withdraw requests
        """

        # Try to withdraw
        try:
            # Get user wihtdraw and withdraw with BankSession instance
            print('')
            self.session.withdraw(int(input('withdraw (int):')))

        # Except for different errors
        except SessionError as e:
            log.log_error("SessionError:" + e.strerror)
        except NegativeIntegerError as e:
            log.log_error("NegativeIntegerError: " + e.strerror)
        except ValueError as e:
            log.log_error("ValueError: Balance must be of type int")

        # Redirect back to run for futher responses
        log.log_info("finished response to withdraw request")
        self.run()

    def view_transactions_event(self):
        """
        event method for transaction requests
        """

        try:
            print('')
            transactions = self.session.view_transactions()
            for transaction in transactions:
                print(transaction)
        except SessionError as e:
            print("SessionError:" + e.strerror)

        # Redirect back to run for futher responses
        log.log_info("finished response to transactions request")
        self.run()

    def quit_event(self):
        """
        event method for quit requests
        """

        # End program
        log.log_info("quitting bank app")
        pass

from .IOModels.Client import Client
from .IOModels.ClientDAO import ClientDAO
from .errors.ServiceErrors import LoginError, SessionError, OverdrawError
from .logger.ServiceLogger import log_info, log_debug, log_error
from .decorators import requires_client, requires_int, requires_positive

class BankSession():
    """
    Our service layer program which implements all the functionality we need
    for a session at the bank.
    """

    def __init__(self, client_dao, client=Client()):
        # set ClientDAO for session
        self.client_dao = client_dao

        # set up BankSession with starting Client
        # default is blank session
        self.client = client

        log_info("instantiated BankSession object")

    def current_session(self):
        """
        Returns the username of the current session
        """

        log_debug("pulled current session username")

        return self.client.get_username()

    def logout_session(self):
        """
        Logout of current session to a blank client
        """

        log_debug("logged out from current session to default")

        self.client = Client()

    @requires_client
    def register(self, client):
        """
        Registers a new client and logs in as that client
        """

        # Instruct ClientDAO to add client
        self.client_dao.add_client(client)

        # Use login method to login as new client
        self.login(client)

        log_debug("registed new client and logged in")

    @requires_client
    def login(self, client):
        """
        Login as a client

        Can raise LoginError if username or password is wrong
        """

        # Get a list of clients from the ClientDAO
        clients = self.client_dao.get_clients()

        # Check if the client we are logging in as is in the list
        if client in clients:

            # Pull the client and check our password
            pulled_client = clients[clients.index(client)]
            if client.get_password() == pulled_client.get_password():
                self.client = pulled_client
                log_debug("logged in as: " + str(pulled_client))

            # if password is wrong raise LoginError
            else:
                log_error("LoginError: Wrong username or password")
                raise LoginError("Wrong username or password")

        # if client is not in ClientDAO raise LoginError
        else:
            log_error("LoginError: Wrong username or password")
            raise LoginError("Wrong username or password")

    def view_balance(self):
        """
        Check balance of current login session

        May raise SessionError if you are not logged in or registered with
        bank
        """

        # Check if we are logged in
        if self.client in self.client_dao.get_clients():
            log_debug("viewed client balance")
            return self.client.get_balance()

        # if client is not part of bank raise SessionError
        else:
            log_error("SessionError: Not logged in or registered with bank")
            raise SessionError('Not logged in or registered with bank')

    @requires_int
    @requires_positive
    def deposit(self, cash):
        """
        Deposit cash into balance

        May raise SessionError if you are not logged in or registered with
        bank
        """

        # Checks if we are logged into an account in the vault
        if self.client in self.client_dao.get_clients():

            # Sets the clients balance
            self.client.set_balance(self.client.get_balance() + cash)

            # Adds to the clients transactions
            record = "date: deposited: $" + str(cash)
            self.client.get_transactions().append(record)

            # Updates client in vault
            self.client_dao.update_client(self.client)

            log_debug("${0} deposited".format(str(cash)))

        # If we are not logged into a vault account raises a SessionError
        else:
            log_error("SessionError: Not logged in or registered with bank")
            raise SessionError('Not logged in or registered with bank')

    @requires_int
    @requires_positive
    def withdraw(self, cash):
        """
        Withdraw cash from balance

        May raise SessionError if you are not logged in or registered with
        bank

        May raise OverdrawError if attempt is made to withdraw more money than
        is in the account
        """

        # Checks if we are logged into an account in the vault
        if self.client in self.client_dao.get_clients():

            # Checks and raises a OverdrawError if client attempts to withdraw
            # more money than is in the account
            if cash > self.client.get_balance():
                log_error("OverdrawError: Attempted to draw more than user's balance")
                raise OverdrawError("Attempted to draw more than user's balance")

            # Performs withdraw
            else:

                # Withdraws from the client account and sets it
                self.client.set_balance(self.client.get_balance() - cash)

                # Adds to transaction history
                record = "date: withdrawn: $" + str(cash)
                self.client.get_transactions().append(record)

                # Updates the client
                self.client_dao.update_client(self.client)
                log_debug("${0} withdrawn".format(str(cash)))

        # If we are not logged into a vault account raises a SessionError
        else:
            log_error("SessionError: Not logged in or registered with bank")
            raise SessionError('Not logged in or registered with bank')

    def view_transactions(self):
        """
        Pulls up client transaction history

        May raise SessionError if we are not logged in
        """

        # Checks that we are logged in
        if self.client in self.client_dao.get_clients():
            log_debug("BankSession: Pulled client transactions")
            return self.client.get_transactions()

        # Raises error if we are not logged in
        else:
            log_error("SessionError: Not logged in or registered with bank")
            raise SessionError('Not logged in or registered with bank')

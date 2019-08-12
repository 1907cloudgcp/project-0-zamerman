from service.BankSession import BankSession
from IO.Client import Client
from error.Error import SessionError
from IO.errors.IOErrors import ClientSetupError

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
quit/exit       exit the program
'''


class ConsoleView():
    def __init__(self, bank):
        self.bank = bank
        self.ran = False

    def run(self):
        if not self.ran:
            print('\nWelcome to {redacted} Bank of {redacted}!')
            print('For a list of commands input `help`')
            self.ran = True
        response = input("$" + self.bank.current_session() + ":")
        return self.parse_response(response)

    def parse_response(self, response):
        if response == 'help':
            print(help_text)
            return self.run()
        elif response == 'register':
            self.registration_event()
        elif response == 'login':
            self.login_event()
        elif response == 'logout':
            self.logout_event()
        elif response == 'balance':
            self.view_balance_event()
        elif response == 'deposit':
            self.deposit_event()
        elif response == 'withdraw':
            self.withdraw_event()
        elif response == 'transactions':
            self.view_transactions_event()
        elif response == 'quit' or response == 'exit':
            self.quit_event()
        else:
            print('invalid command')
            return self.run()

    def registration_event(self):
        username = input('username:')
        password = input('password:')
        starting_balance = int(input('starting balance (int):'))
        try:
            self.bank.register(Client(username, password, starting_balance))
        except ClientSetupError as e:
            print("ClientSetupError:" + e.strerror)
        return self.run()

    def login_event(self):
        username = input('username:')
        password = input('password:')
        try:
            self.bank.login(Client(username, password))
        except SessionError as e:
            print("SessionError:" + e.strerror)
        return self.run()

    def logout_event(self):
        self.bank.logout_session()
        return self.run()

    def view_balance_event(self):
        try:
            print('balance:' + str(self.bank.view_balance()))
        except SessionError as e:
            print("SessionError:" + e.strerror)
        return self.run()

    def deposit_event(self):
        try:
            self.bank.deposit(int(input('deposit (int):')))
        except SessionError as e:
            print("SessionError:" + e.strerror)
        return self.run()

    def withdraw_event(self):
        try:
            self.bank.withdraw(int(input('withdraw (int):')))
        except SessionError as e:
            print("SessionError:" + e.strerror)
        return self.run()

    def view_transactions_event(self):
        try:
            transactions = self.bank.view_transactions()
            for transaction in transactions:
                print(transaction)
        except SessionError as e:
            print("SessionError:" + e.strerror)
        return self.run()

    def quit_event(self):
        return None

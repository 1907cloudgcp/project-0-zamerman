class Client():
    def __init__(self, username, password, balance, transactions):
        self.__username = username
        self.__password = password
        self.__balance = balance
        self.__transactions = transactions

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

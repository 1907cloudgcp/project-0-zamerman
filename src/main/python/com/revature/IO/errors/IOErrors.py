class IOError(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

class SecureStringError(IOError):
    def __init__(self):
        self.strerror = "Entered string must be 8 or more characters"

class IntegerRequiredError(IOError):
    def __init__(self):
        self.strerror = "Integer required"

class InvalidCharacterError(IOError):
    def __init__(self):
        self.strerror = "Spaces are not allowed in strings"

class ClientSetupError(IOError):
    pass

class IOError(Exception):
    """
    Class of errors for IO layer
    """

    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

class SecureStringError(IOError):
    """
    Error raised when a string that is meant to be secure is not secure
    """
    pass

class IntegerRequiredError(IOError):
    """
    Error raised when a value that should be integer is not integer
    """
    pass

class InvalidCharacterError(IOError):
    """
    Error raised when string has invalid characters
    """
    pass

class ClientSetupError(IOError):
    """
    Error raised when there are problems when adding or updating clients
    """
    pass

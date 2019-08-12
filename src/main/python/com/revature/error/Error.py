class Error(Exception):
    """
    Standard Error
    """

    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

class SecureStringError(Error):
    """
    Error raised when a string that is meant to be secure is not secure
    """
    pass

class IntegerRequiredError(Error):
    """
    Error raised when a value that should be integer is not integer
    """
    pass

class InvalidCharacterError(Error):
    """
    Error raised when string has invalid characters
    """
    pass

class ClientRequiredError(ServiceError):
    """
    Error raised when input is not client
    """
    pass

class NegativeIntegerError(ServiceError):
    """
    Error raised when integer input is negative
    """
    pass
    
class ClientSetupError(Error):
    """
    Error raised when there are problems when adding or updating clients
    """
    pass

class LoginError(Error):
    """
    Error raised during login if username or password are wrong
    """
    pass

class SessionError(ServiceError):
    """
    Error raised when not logged in or registered
    """
    pass

class OverdrawError(Error):
    """
    Error raised when user attempts to withdraw more than his balance
    """
    pass

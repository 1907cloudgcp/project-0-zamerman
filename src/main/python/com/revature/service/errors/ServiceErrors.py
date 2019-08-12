class ServiceError(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

class LoginError(ServiceError):
    """
    Error raised during login if username or password are wrong
    """
    pass

class SessionError(ServiceError):
    """
    Error raised when not logged in or registered
    """
    pass

class ClientRequiredError(ServiceError):
    """
    Error raised when input is not client
    """
    pass

class IntegerRequiredError(ServiceError):
    """
    Error raised when a value that should be integer is not integer
    """
    pass

class NegativeIntegerError(ServiceError):
    """
    Error raised when integer input is negative
    """
    pass

class OverdrawError(ServiceError):
    """
    Error raised when user attempts to withdraw more than his balance
    """
    pass

from .IOModels.Client import Client
from .errors.ServiceErrors import ClientRequiredError, IntegerRequiredError, NegativeIntegerError


def requires_client(func):
    """
    Decorator function to check that decorated function has string field with
    length 8 or greater. Also excepts empty strings.
    """

    def func_wrapper(self, client):
        if type(client) == Client:
            return func(self, client)
        else:
            log_error("ClientRequiredError: Argument must be client")
            raise ClientRequiredError("Argument must be client")
    return func_wrapper


def requires_int(func):
    """
    Decorator function to check that input is integer.
    """

    def func_wrapper(self, integer):
        if type(integer) == int:
            return func(self, integer)
        else:
            log_error("IntegerRequiredError: Integer input required")
            raise IntegerRequiredError("Integer input required")
    return func_wrapper

def requires_positive(func):
    """
    Decorator function that checks integer input to make sure it's positive
    """

    def func_wrapper(self, integer):
        if integer < 0:
            return func(self, integer)
        else:
            log_error("NegativeIntegerError: Positive integer required")
            raise NegativeIntegerError("Positive integer required")
    return func_wrapper

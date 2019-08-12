from logger.Logger import log_error
from IO.Client import Client
from error.Error import ClientRequiredError, IntegerRequiredError, NegativeIntegerError, InvalidCharacterError, SecureStringError


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
# Import custom errors and IOLogger
from error.Error import (SecureStringError, IntegerRequiredError, InvalidCharacterError)
from logger.Logger import log_error


def secure_string(func):
    """
    Decorator function to check that decorated function has string field with
    length 8 or greater. Also excepts empty strings.
    """

    def func_wrapper(self, string):
        if string == '':
            return func(self, string)
        elif len(string) < 8:
            log_error("SecureStringError: String must be length 8 or greater")
            raise SecureStringError("String must be length 8 or greater")
        else:
            return func(self, string)
    return func_wrapper


def invalid_characters(func):
    """
    Decorator function to check for invalid characters.
    """

    def func_wrapper(self, string):
        if " " in string:
            log_error("InvalidCharacterError: No spaces in secured strings")
            raise InvalidCharacterError("No spaces in strings")
        else:
            return func(self, string)
    return func_wrapper

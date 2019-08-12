from .errors.IOErrors import (SecureStringError, IntegerRequiredError,
InvalidCharacterError)
from .logger.IOLogger import log_error

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

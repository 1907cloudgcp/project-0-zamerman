from .IOErrors import (SecureStringError, IntegerRequiredError,
InvalidCharacterError)

def secure_string(func):
    def func_wrapper(self, string):
        if string == '':
            return func(self, string)
        elif len(string) < 8:
            raise SecureStringError
        else:
            return func(self, string)
    return func_wrapper


def requires_int(func):
    def func_wrapper(self, integer):
        if type(integer) == int:
            return func(self, integer)
        else:
            raise IntegerRequiredError
    return func_wrapper


def invalid_characters(func):
    def func_wrapper(self, string):
        if " " in string:
            raise InvalidCharacterError
        else:
            return func(self, string)
    return func_wrapper

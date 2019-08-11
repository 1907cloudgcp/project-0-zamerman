from .IOErrors import SecureStringError

def secure_string(func):
    def func_wrapper(self, string):
        if string == '':
            return func(self, string)
        elif len(string) < 8:
            raise SecureStringError
        else:
            return func(self, string)
    return func_wrapper

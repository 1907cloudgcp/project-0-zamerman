class Error(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}

class LoginError(Error):
    pass

class SessionError(Error):
    pass

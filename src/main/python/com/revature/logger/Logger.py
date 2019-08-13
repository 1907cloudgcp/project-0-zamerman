import logging

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log_debug(self, debug_string):
        self.logger.debug(debug_string)


    def log_info(self, info_string):
        self.logger.info(info_string)


    def log_warning(self, warning_string):
        self.logger.warning(warning_string)


    def log_error(self, error_string):
        self.logger.error(error_string)


    def log_critical(self, critical_string):
        self.logger.critical(critical_string)

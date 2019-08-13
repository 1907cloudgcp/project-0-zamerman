import os
import logging
import logging.config
import yaml

# Find logging.yaml config file relative to this file
file_path = os.path.abspath(__file__)
config_path = file_path.split('/')[:-5]
config_path.append('resources/logging.yaml')
config_path = '/'.join(config_path)

# Securely read and load yaml config file
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f.read())

    # Enable our loaded configuration
    logging.config.dictConfig(config)
else:
    raise ValueError('Logging configuration not found')

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

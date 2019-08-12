import os
import logging
import logging.config
import yaml

# Find logging.yaml config file relative to this file
file_path = os.path.abspath(__file__)
config_path = file_path.split('/')[:-6]
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

logger = logging.getLogger('ServiceLogger')


def log_debug(debug_string):
    logger.debug(debug_string)


def log_info(info_string):
    logger.info(info_string)


def log_warning(warning_string):
    logger.warning(warning_string)


def log_error(error_string):
    logger.error(error_string)


def log_critical(critical_string):
    logger.critical(critical_string)

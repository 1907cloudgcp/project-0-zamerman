#!/usr/bin/env python3
from controller.ConsoleView import ConsoleView
from service.BankSession import BankSession
from IO.ClientDAOJSON import ClientDAOJSON
from logger.Logger import Logger
import os
import logging
import logging.config
import yaml

'''
This is your main script, this should call several other scripts within your
packages.
'''

def main():
	# Configure Logger

	# Find logging.yaml config file relative to this file
	file_path = os.path.abspath(__file__)
	config_path = file_path.split('/')[:-4]
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

	# Start logger
	log = Logger(__name__)
	log.log_info("start logger")

	# Start app
	log.log_info("start bank app")

	# Code to assemble and put together path to vault file relative to file
	file_path = os.path.abspath(__file__)
	vault_path = file_path.split('/')[:-6]
	vault_path.append('data/vault.json')
	vault_path = '/'.join(vault_path)

	# instantiate a ClientDAO for json files
	log.log_info("instantiate ClientDAO for application")
	client_dao = ClientDAOJSON(vault_path)

	# instantiate a BankSession using ClientDAO
	log.log_info("instantiate BankSession for application")
	bank_session = BankSession(client_dao)

	# instantiate a ConsoleView for our BankSession
	log.log_info("instantiate ConsoleView for application")
	console = ConsoleView(bank_session)

	# start our loops
	log.log_info("begin searching responding to user")
	console.run()


if __name__ == '__main__':
	main()

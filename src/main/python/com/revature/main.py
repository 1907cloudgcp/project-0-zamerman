#!/usr/bin/env python3
from controller.ConsoleView import ConsoleView
from service.BankSession import BankSession
from IO.ClientDAOJSON import ClientDAOJSON
import os

'''
This is your main script, this should call several other scripts within your
packages.
'''


def main():
	# Code to assemble and put together path to vault file relative to file
	file_path = os.path.abspath(__file__)
	vault_path = file_path.split('/')[:-6]
	vault_path.append('data/vault.json')
	vault_path = '/'.join(vault_path)

	# instantiate a ClientDAO for json files
	client_dao = ClientDAOJSON(vault_path)

	# instantiate a BankSession using ClientDAO
	bank_session = BankSession(client_dao)
	console = ConsoleView(bank_session)
	console.run()


if __name__ == '__main__':
	main()

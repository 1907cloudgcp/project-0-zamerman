#!/usr/bin/env python3
from controller.ConsoleView import ConsoleView
from service.BankSession import BankSession

'''
This is your main script, this should call several other scripts within your
packages.
'''


def main():
	bank_session = BankSession('/vagrant/project-0-zamerman/data/vault.json')
	console = ConsoleView(bank_session)
	console.run()


if __name__ == '__main__':
	main()

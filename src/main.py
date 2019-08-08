#!/usr/bin/env python3
from controller.ConsoleView import ConsoleView
from service.Bank import Bank

'''
This is your main script, this should call several other scripts within your
packages.
'''


def main():
	bank = Bank('/vagrant/project-0-zamerman/data/vault.json')
	console = ConsoleView(bank)
	console.run()


if __name__ == '__main__':
	main()

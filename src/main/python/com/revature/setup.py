import os


def main():
    home = os.getenv('HOME')
    os.system('sudo mkdir /var/log/bank')
    os.system('sudo mkdir ' + home + '/bank')
    os.system('sudo touch /var/log/bank/all.log')
    os.system('sudo touch /var/log/bank/error.log')
    os.system('sudo touch ' + home + '/bank/vault.json')


if __name__ == '__main__':
    main()

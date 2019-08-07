import os


def main():
    home = os.getenv('HOME')
    os.system('sudo rm -r /var/log/bank')
    os.system('sudo rm -r ' + home + '/bank')


if __name__ == '__main__':
    main()

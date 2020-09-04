import operations as op
from getpass import getpass

# Variables
user = 'tito'
password = 'holabola'


def login():
    """
    A function used to login that compares inputted user and password with the original ones

    Returns:
        A boolean that is true if the user was authenticated
    """
    current_user = input('Enter your user: ')
    current_password = getpass('Enter your password: ')

    if (current_user == user) & (current_password == password):
        print(f'Welcome back {current_user}')
        return True
    else:
        return False


def analysis(option):
    """
    A function that emulates a switch-case to select the analysis to perform
    :param option: selected choice, inputed by user
    :return: the associated function to the option it was selected
    """
    switcher = {
        1: op.option_1,
        2: op.option_2,
        3: op.option_3,
        4: op.option_4
    }
    func = switcher.get(option, "Invalid option")
    return func()


logged = login()
finish = 'n'

while finish != ('y' or 'Y'):

    if not logged:
        print('Retry login')
        logged = login()
    else:
        print('''
        Available options:
            1.- Top selling products and lagging products.
            2.- Reviewed products in the service.
            3.- Total income and average monthly sales, annual total and months with the most sales per year.
            4.- Print the whole analysis into a text file.
        ''')

        analysis(int(input('Type the selected option: ')))
        finish = input('Exit? (y/n): ')

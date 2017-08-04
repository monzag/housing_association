def welcome_screen(community_name):
    print('\nHello in community ' + community_name + '\n')


def print_main_menu():
    options = ['Show all blocks', 'Choose block', 'Add new block']
    get_menu(options)


def get_menu(options):
    number = 1
    print('')
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1

    print_exit_option()


def print_exit_option():
    print('0. Exit\n')


def print_exit_message():
    print('\nHave a nice day!:) ')


def get_user_input():
    return input('\nYour choice: ')


def get_block_data():
    # TODO validation
    street = input('Type street: ')
    number = input('Type number: ')

    return street, number


def print_block_menu():
    options = ['Show all flats', 'Find flat by number', 'Show statistic']
    get_menu(options)


def print_flat_menu():
    options = ['Show owners', 'Add owner', 'remove owner']
    get_menu(options)


def get_new_owner():
    name = input('\nType name: ')
    surname = input('Type surname: ')
    phone = input('Type phone: ')

    return name, surname, phone


def print_error_message():
    print('Bad choice!')


def print_block_exist():
    print('This block already exist!')



from flat import Flat
from owner import Owner
import view


def flat_menu(flat):
    print(flat.get_info_about_flat())
    user_choice = ''
    while user_choice != '0':
        view.print_flat_menu()
        user_choice = view.get_user_input()

        if user_choice == '1':
            show_owners(flat)

        elif user_choice == '2':
            add_owner(flat)

        elif user_choice == '3':
            remove_owner(flat)


def add_owner(flat):
    name, surname, phone = view.get_new_owner()
    owner = Owner(name, surname, phone)
    flat.add_owner(owner)


def remove_owner(flat):
    show_owners()
    user_choice = view.get_user_input()
    if int(user_choice) in range(len(flat.list_of_owners)):
        owner = flat.owners[user_choice - 1]
        flat.remove_owner(owner)
    else:
        view.print_error_message()


def show_owners(flat):
    number = 1
    for owner in flat.owners:
        print('{}. {}'.format(number, owner.get_owner()))
        number += 1


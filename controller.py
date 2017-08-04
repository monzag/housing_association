from community import Community
from block import Block
import block_controller
import view


def main_menu():
    csv_path = 'community.csv'
    community = Community.create_from_csv(csv_path)
    view.welcome_screen(community.name)

    user_choice = ''
    while user_choice != '0':
        view.print_main_menu()
        user_choice = view.get_user_input()

        if user_choice == '1':
            Community.get_all_blocks()

        elif user_choice == '2':
            choose_block()

        elif user_choice == '3':
            add_new_block(community)

        elif user_choice == '4':
            # TODO find address by owner
            pass

    view.print_exit_message()


def choose_block():
    Community.get_all_blocks()
    street, number = view.get_block_data()
    block = Community.find_block(street, number)
    if block:
        block_controller.block_menu(block)
    else:
        view.print_error_message()


def add_new_block(community):
    street, number = view.get_block_data()
    if not is_block_exist(street, number):
        block = Block(street, number)
        Community.add_blocks(block)
        community.save_to_file()

    else:
        view.print_block_exist()


def is_block_exist(street, number):
    if Community.find_block(street, number):
        return True
    else:
        return False


from block import Block
import flat_controller
import view


def block_menu(block):
    print(block.get_address_of_block())
    user_choice = ''
    while user_choice != '0':
        view.print_block_menu()
        user_choice = view.get_user_input()

        if user_choice == '1':
            block.get_all_flats()

        elif user_choice == '2':
            find_flat_by_number(block)

        elif user_choice == '3':
            print('to do:P')


def find_flat_by_number(block):
    number = view.get_user_input()
    flat = block.find_flat(number)

    if flat:
        flat_controller.flat_menu(flat)

    else:
        view.print_error_message()


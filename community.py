from block import Block
from flat import Flat
from owner import Owner
import csv


class Community:

    list_of_blocks = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def add_blocks(cls, block):
        cls.list_of_blocks.append(block)

    @classmethod
    def remove_block(cls, block):
        if block in cls.list_of_blocks:
            cls.list_of_blocks.remove(block)

    @classmethod
    def get_all_blocks(cls):
        for block in cls.list_of_blocks:
            print(block.get_address_of_block())

    @classmethod
    def find_block(cls, street, number):
        for block in cls.list_of_blocks:
            if block.street.lower() == street.lower() and str(block.number) == number:
                return block

    @classmethod
    def create_from_csv(cls, csv_path):
        splitted_data = cls.get_data_from_file(csv_path)

        # first data in csv file is community name
        name = splitted_data[0][0]
        community = cls(name)

        for row in splitted_data[1:]:
            street, number, house_no, name, surname, phone = row[0], row[1], row[2], row[3], row[4], row[5]

            block = cls.create_block(street, number)
            cls.create_owner_and_flat(block, house_no, name, surname, phone)

        return community

    @classmethod
    def get_data_from_file(cls, csv_path):
        with open(csv_path, 'r') as csvfile:
            splitted_rows = [line.strip().split(',') for line in csvfile]

        return splitted_rows

    @classmethod
    def create_block(cls, street, number):
        block = cls.find_block(street, number)
        if not block:
            block = Block(street, number)
            Community.add_blocks(block)

        return block

    @classmethod
    def create_owner_and_flat(cls, block, house_no, name, surname, phone):
        flat = block.find_flat(house_no)
        if not flat:
            flat = Flat(house_no)

        owner = Owner(name, surname, phone)

        flat.add_owner(owner)
        block.add_flat(flat)

    def save_to_file(self):
        list_to_save = self.get_data_to_save()
        file_path = self.name + '.csv'

        with open(file_path, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            for line in list_to_save:
                writer.writerow(line)

    def get_data_to_save(self):
        list_to_save = []
        for block in Community.list_of_blocks:
            street, number = block.street, block.number

            for flat in block.list_of_flats:
                house_no = flat.house.no

                for owner in flat.list_of_owners:
                    name, surname, phone = owner.name, owner.surname, owner.phone

                    row = [street, number, house_no, name, surname, phone]
                    list_to_save.append(row)

        return list_to_save




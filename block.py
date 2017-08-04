class Block:

    def __init__(self, street, number):
        self.street = street
        self.number = number
        self.list_of_flats = []

    def add_flat(self, flat):
        self.list_of_flats.append(flat)

    def find_flat(self, number):
        for flat in self.list_of_flats:
            if number == flat.house_no:
                return flat

    def get_all_flats(self):
        for flat in self.list_of_flats:
            print('Flat ' + flat.house_no)

    def get_address_of_block(self):
        return '{} {}'.format(self.street, self.number)

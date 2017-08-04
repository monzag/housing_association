from owner import Owner


class Flat:

    def __init__(self, house_no):
        self.house_no = house_no
        self.owners = []

    def add_owner(self, owner):
        self.owners.append(owner)

    def remove_owner(self, owner):
        self.owners.remove(owner)

    def get_info_about_flat(self):
        return 'Number {}'.format(self.house_no)



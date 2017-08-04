class Owner:

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def get_owner(self):
        return '{} {}, {}'.format(self.name, self.surname, self.phone)

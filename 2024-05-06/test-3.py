class PhoneBook:
    def __init__(self, data = dict()):
        self.data = data
    
    def add_contact(self, name, number):
        self.data[name] = number

    def find_contact(self, name):
        name_field = 0
        return list(filter(
            lambda item : name in item[name_field],
            self.data.items()
        ))
    
    def find_by_nmber(self, number):
        number_field = 1
        return list(
            filter(
                lambda item : number in item[number],
                self.data.items()
            )
        )


class PhoneBookNew:
    def __init__(self, data = []):
        self.data = data
    
    def add_contact(self, name, number):
        self.data.append(name, number)

    def find_contact(self, name):
        name_field = 0
        return list(filter(
            lambda item : name in item[name_field],
            self.data.items()
        ))
    
    def find_by_nmber(self, number):
        number_field = 1
        return list(
            filter(
                lambda item : number in item[number],
                self.data.items()
            )
        )

pb = PhoneBook(
)

import pprint


pprint.pprint(pb.find_contact("I"))
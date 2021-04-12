'''
This program contains a class called Restaurant which is type
of Store
'''


from store import *


class Restaurant(Store):
    def __init__(self, total_people, max_occ, current_occ, prices):
        self.total_people = total_people
        self.max_occ = max_occ
        self.current_occ = current_occ
        self.prices = prices

    def get_prices(self):
        return self.prices

    def set_prices(self, prices):
        self.prices = prices

    def seat_patrons(self):
        self.current_occ = input('Enter number of people to be seated')

        if self.current_occ < self.max_occ:
            print('Welcome to Panda Express')
            return True
        else:
            print('We are at capacity, we appreciate your patience')
            return False

    def save_patrons(self):
        self.total_people = input('How many people?')
        return self.total_people

    def checkout_patrons(self):
        self.total_people = input('People leaving: ')
        return self.current_occ - self.total_people







'''
This program  creates classes that represent to a certain degree
different types of stores in real life and the information tracked
and services provided by these stores

Name: Cristian Pintor
'''
from abc import ABC, abstractmethod


class Store:
    def __init__(self, name, address, availability, taxes):
        self.name = name
        self.address = address
        self.availability = availability
        self.taxes = taxes

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_availability(self):
        return self.availability

    def get_taxes(self):
        return self.taxes

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_availability(self, availability):
        self.availability = availability

    def set_taxes(self, taxes):
        self.taxes = taxes

    def calculate_total_sales_tax(self):
        pass

    def calculate_total_sales(self):
        pass

    def is_store_open(self, availability):
        if availability == 'open':
            return 'true'
        else:
            return 'false'

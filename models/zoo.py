import sys
sys.path.append('../helpers')

from validator import Validator


class Zoo(object):
    def __init__(self, name, capacity, budget):
        self.__validator = Validator()

        self.name = name
        self.capacity = capacity
        self.budget = budget

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__validator.validate_name(2, 'zoos', name)
        self.__name = name

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__validator.validate_number(1, capacity, 'capacity')
        self.__capacity = capacity

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        self.__validator.validate_number(0, budget, 'budget')
        self.__budget = budget

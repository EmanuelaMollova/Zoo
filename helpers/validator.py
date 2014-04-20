import sys
sys.path.append('../../repository')

from repository import Repository


class Validator():
    def __init__(self, db_name='../../database/zoos.db'):
        self.__db_name = db_name

    def validate_name(self, min_length, model, parameter):
        if len(parameter) < min_length:
            message = "The name should be at least {} symbols"
            raise Exception(message.format(min_length))

        repository = Repository(self.__db_name)
        if repository.is_name_used(model, parameter):
            raise Exception("This name is already taken")

    def validate_number(self, min_value, parameter, parameter_name):
        if isinstance(parameter, str):
            parameter = float(parameter)

        if parameter < min_value:
            message = "The {} should be at least {}"
            raise Exception(message.format(parameter_name, min_value))

    def validate(self, condition, parameter, message):
        if not condition(parameter):
            raise Exception(message)

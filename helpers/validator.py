class Validator():
    def validate_name(self, min_length, parameter):
        if len(parameter) < min_length:
            message = "The name should be at least {} symbols"
            raise Exception(message.format(min_length))

    def validate_number(self, min_value, parameter):
        if isinstance(parameter, str):
            parameter = float(parameter)

        if parameter < min_value:
            message = "The {} should be at least {}"
            raise Exception(message.format(parameter.__name__, min_value))

    def validate(self, condition, parameter, message):
        if not condition(parameter):
            raise Exception(message)

import re
from datetime import datetime as dt

from app.constants import DATE_FORMAT


def process_currency(value):
    if value:
        separetaor = len(value) - 1
        currency_value = value[:separetaor]
        return currency_value


def get_month(date_string):
    if date_string:
        return dt.strptime(date_string, DATE_FORMAT).month


def get_year(date_string):
    if date_string:
        return dt.strptime(date_string, DATE_FORMAT).year


def get_day(date_string):
    if date_string:
        return dt.strptime(date_string, DATE_FORMAT).day


def get_integers(string_with_integers):
    if string_with_integers:
        first = 0
        reg_ex = r"-?\d+"
        integers = re.search(reg_ex, string_with_integers)[first]
        if integers:
            return int(integers)
    return float('NaN')


def get_float(string_to_search_float):
    if string_to_search_float:
        first = 0
        reg_ex_coma = r"-?\d+,\d+"
        reg_ex_dot = r"-?\d+.\d+"
        if string_to_search_float.index("."):
            float_number = re.search(reg_ex_dot, string_to_search_float)[first]
        elif string_to_search_float(","):
            float_number = re.search(reg_ex_coma, string_to_search_float)[first]
        else:
            float_number = 'NaN'
    return float(float_number)


ACTIONS = {
    'get_currency': process_currency,
    'get_day': get_day,
    'get_month': get_month,
    'get_year': get_year,
    'get_integer': get_integers,
    'get_float': get_float,
    None: lambda x: x
}

TYPES = {
    'decimal': lambda x: float(x),
    'int': lambda x: int(x),
    'str': lambda x: str(x),
    'bool': lambda x: bool(x),
    'list': lambda x: list(x)
}

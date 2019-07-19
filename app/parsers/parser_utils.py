import re
from datetime import datetime as dt


def process_currency(value):
    separetaor = len(value) - 1
    currency_value = value[:separetaor]
    return currency_value


def get_month(date_string):
    return dt.strptime(date_string, "%m/%d/Y").month


def get_year(date_string):
    return dt.strptime(date_string, "%m/%d/Y").year


def get_day(date_string):
    return dt.strptime(date_string, "%m/%d/Y").day


def get_integers(string_with_integers):
    first = 0
    reg_ex = r"-?\d+"
    integers = re.search(reg_ex, string_with_integers)[first]
    if integers:
        return int(integers)
    return float('NaN')


def get_float(string_to_search_float):
    first = 0
    reg_ex_coma = r"-?\d+,\d+"
    reg_ex_dot = r"-?\d+.\d+"
    float_number = re.search(reg_ex_coma, string_to_search_float)[first] or \
                   re.search(reg_ex_dot, string_to_search_float)[first]
    if float_number:
        return float(float_number)
    return float('NaN')


ACTIONS = {
    'get_currency': process_currency,
    'get_day': get_day,
    'get_month': get_month,
    'get_year': get_year,
    'get_integers': get_integers,
    'get_float': get_float,
    None: lambda x: x
}

TYPES = {
    'decimal': lambda x: float(x),
    'int': lambda x: int(x),
    'str': lambda x: str(x),
    'bool': lambda x: bool(x)
}

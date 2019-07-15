import json
import os

from app.parsers.parser_utils import DIR


class FileParser:
    def __init__(self, parser_name):
        self.parser_name = parser_name

    @property
    def parser(self):
        with open(os.path.normpath(os.path.join(DIR,
                  "parser_file/{parser_name}.json".format(
                      parser_name=self.parser_name))), 'r') as par:
            return json.load(par)

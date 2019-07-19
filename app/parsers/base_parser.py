import json
import os
from abc import ABC, abstractmethod
from contextlib import AbstractContextManager

import xmltodict as xd

from app.constants import DIR


class ParserFileContext(AbstractContextManager):
    parser_file = None

    def __init__(self, location_dir, parser_name, extension):
        self.parser_name = parser_name
        self.location = location_dir
        self.extension = extension
        super(AbstractContextManager, self).__init__()

    def __enter__(self):
        self.parser_file = open(os.path.normpath(os.path.join(self.location,
            "parser_file/{parser_name}.{extension}".format(
                parser_name=self.parser_name,
                extension=self.extension))), 'r')
        return self.parser_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.parser_file.close()
        return


class BaseParser(ABC):
    def __init__(self, parser_name):
        self.parser_name = parser_name
        super(ABC).__init__(self)

    @abstractmethod
    def parse(self):
        pass


class JsonFileParser(BaseParser):
    def __init__(self, parser_name):
        super(BaseParser, self).__init__(self, parser_name)

    def parse(self):
        with ParserFileContext(DIR, self.parser_name, 'json') as parser_file:
            return json.load(parser_file)


class XmlFileParser(BaseParser):

    def __init__(self, parser_name):
        super(BaseParser, self).__init__(self, parser_name)

    def parse(self):
        with ParserFileContext(DIR, self.parser_name, 'xml') as parser_file:
            parsed = xd.parse(parser_file)
            return parsed.get("root")

from csv import DictReader

from app.parsers.base_parser import JsonFileParser
from app.parsers.parser_utils import ACTIONS, TYPES
import logging


def create_chunk(upload_file, parser_name, chunk_size):
    with open(upload_file, 'r') as file:
        file_processor = FileProcessor(file, parser_name)
        offset_csv = file_processor.csv_file()
        chunk = []
        for line in offset_csv:
            chunk.append(file_processor.process_line(line))
            if len(chunk) == chunk_size:
                yield chunk
                chunk.clear()


class FileProcessor:
    def __init__(self, file_to_upload, parser_name):
        self.file_to_upload = file_to_upload
        self.csv = None
        self.parser = JsonFileParser(parser_name)

    def csv_file(self):
        parser_data = self.parser.parse()
        offset = parser_data.get("offset")
        return self.dict_reader_offset(self.file_to_upload, offset)

    def process_line(self, line):
        logging.info(f"{line}")
        result = dict()
        for column, value in self.parser.parse().get("columns").items():
            logging.info(f"{column}: {value}")
            type_ = TYPES.get(value.get('type'))
            action = ACTIONS.get(value.get("action"))
            column_line = value.get("col")
            column_value = line.get(column_line)
            logging.info(f"{type_} - {action} : {column_line} :{column_value}")
            if type_ and action:
                result[column] = type_(action(column_value))
        return result

    @staticmethod
    def dict_reader_offset(file, offset):
        csv = DictReader(file)
        if offset:
            for i in range(offset):
                next(csv)
        return csv

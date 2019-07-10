from csv import DictReader

from app.parsers.base_parser import FileParser, ACTIONS, TYPES


def create_chunk(upload_file, parser_name, chunk_size):
    with open(upload_file, 'r') as file:
        file_processor = FileProcessor(file, parser_name)
        offset_csv = file_processor.csv_file()
        chunk = []
        for line in offset_csv:
            chunk.append(line)
            if len(chunk) == chunk_size:
                yield chunk
                chunk.clear()


class FileProcessor:
    def __init__(self, file_to_upload, parser_name):
        self.file_to_upload = file_to_upload
        self.csv = None
        self.parser = FileParser(parser_name)

    def csv_file(self):
        offset = self.parser.parser.get("offset")
        return self.dict_reader_offset(self.file_to_upload, offset)

    def process_line(self, line):
        result = dict()
        for column, value in self.parser.parser.get("columns").items():
            result[column] = TYPES.get(value.get('type'))(ACTIONS[value[
                "action"]](line.get(value.get('col'))))
        return result

    @staticmethod
    def dict_reader_offset(file, offset):
        csv = DictReader(file)
        if offset:
            for i in range(offset):
                next(csv)
        return csv

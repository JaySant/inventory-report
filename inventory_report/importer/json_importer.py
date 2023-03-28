import json


class JsonImporter:
    @staticmethod
    def import_data(path):
        with open(path) as json_file:
            return json.load(json_file)

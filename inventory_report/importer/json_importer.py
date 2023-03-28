import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".json"):
            with open(path) as json_file:
                return json.load(json_file)
        else:
            raise ValueError('Arquivo inválido')

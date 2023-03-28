import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".csv"):
            with open(path) as csv_file:
                reader = csv.DictReader(csv_file)
                return list(reader)
        else:
            raise ValueError('Arquivo inválido')

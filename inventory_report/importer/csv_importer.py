import csv


class CsvImporter:
    @staticmethod
    def import_data(path):
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file)
            return list(reader)

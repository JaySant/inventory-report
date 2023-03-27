import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        if path.endswith(".csv"):
            with open(path) as csv_file:
                reader = csv.DictReader(csv_file)
                data = list(reader)
        elif path.endswith(".json"):
            with open(path) as json_file:
                data = json.load(json_file)
        else:
            raise ValueError("Arquivo invalido")

        if report_type == 'simples':
            return SimpleReport.generate(data)
        elif report_type == 'completo':
            return CompleteReport.generate(data)
        else:
            raise ValueError('Relatorio invalido')

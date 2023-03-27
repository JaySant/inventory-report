import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        if report_type == 'simples':
            return SimpleReport.generate(data)
        elif report_type == 'completo':
            return CompleteReport.generate(data)
        else:
            raise ValueError('Relatorio invalido')

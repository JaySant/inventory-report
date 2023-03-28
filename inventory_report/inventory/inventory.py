from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    
    @staticmethod
    def verificacao(path: str):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)
        else:
            raise ValueError("Arquivo invalido")

    @staticmethod
    def import_data(path: str, report_type: str):
        data = Inventory.verificacao(path)
        if report_type == 'simples':
            return SimpleReport.generate(data)
        elif report_type == 'completo':
            return CompleteReport.generate(data)
        else:
            raise ValueError('Relatorio invalido')

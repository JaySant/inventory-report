from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path: str, report_type: str) -> str:
        imported_data = self.importer.import_data(path)
        self.data.extend(imported_data)

        if report_type == "simples":
            return SimpleReport.generate(self.data)
        elif report_type == "completo":
            return CompleteReport.generate(self.data)
        else:
            raise ValueError("Tipo de relatório inválido")

import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if path.endswith(".xml"):
            with open(path) as xml_file:
                reader = xml_file.read()
                return xmltodict.parse(reader)["dataset"]["record"]
        else:
            raise ValueError('Arquivo inválido')

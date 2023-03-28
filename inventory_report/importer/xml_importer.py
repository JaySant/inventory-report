import xmltodict


class XmlImporter:
    @staticmethod
    def import_data(path):
        with open(path) as xml_file:
            reader = xml_file.read()
            return xmltodict.parse(reader)["dataset"]["record"]

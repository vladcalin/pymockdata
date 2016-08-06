import xml.etree.cElementTree as ET

from pymockdata.core.base import BaseExporter


class XmlExporter(BaseExporter):
    def __init__(self, filename="output.xml"):
        self._output_fn = filename
        self._data = []

    def export(self):
        root = ET.Element("data")
        for entry in self._data:
            entry_elem = ET.SubElement(root, "entry")
            for key in entry.keys():
                ET.SubElement(entry_elem, key).text = str(entry[key])
        tree = ET.ElementTree(root)
        tree.write(self._output_fn)

    def add_entry(self, entry):
        self._data.append(entry)

    def add_entries(self, entries):
        self._data.extend(entries)

import csv

from pymockdata.core.base import BaseExporter


class CsvExporter(BaseExporter):
    def __init__(self, filename="output.csv"):
        self._output_fn = filename
        self._data = []

    def export(self):
        with open(self._output_fn, "w", newline='') as output:
            writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_NONE)
            for entry in self._data:
                writer.writerow(list(entry.values()))

    def add_entry(self, entry):
        self._data.append(entry)

    def add_entries(self, entries):
        self._data.extend(entries)


if __name__ == '__main__':
    exp = CsvExporter()
    exp.add_entry({"name": "teasdasdasdasdadst", "age": 21131, "Asdasda": True})
    exp.add_entry({"name": "test", "age": 21, "Asdasda": True})
    exp.add_entry({"name": "test", "age": 21,  "Asdasda": True})
    exp.add_entry({"name": "tadasdasdest", "age": 21,  "Asdasda": True})
    exp.export()

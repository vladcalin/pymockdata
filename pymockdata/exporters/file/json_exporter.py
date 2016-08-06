import json

from pymockdata.core.base import BaseExporter


class JsonExporter(BaseExporter):
    def __init__(self, filename="output.json"):
        self._output_fn = filename
        self._data = []

    def export(self):
        parsed_data = self._parse_data(self._data)
        with open(self._output_fn, "w") as output:
            json.dump(parsed_data, output, indent=4)

    def _parse_data(self, data_to_parse):
        final = {"entries": []}
        for entry in data_to_parse:
            final["entries"].append(entry)
        return final

    def add_entry(self, entry):
        self._data.append(entry)

    def add_entries(self, entries):
        self._data.extend(entries)

if __name__ == '__main__':
    exp = JsonExporter()
    exp.add_entry({"name": "test", "age": 21})
    exp.add_entry({"name": "test", "age": 21})
    exp.add_entry({"name": "test", "age": 21})
    exp.add_entry({"name": "test", "age": 21})
    exp.export()
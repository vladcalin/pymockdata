import sys

from pymockdata.core.base import BaseExporter


class StreamExporter(BaseExporter):
    def __init__(self, stream=sys.stdout):
        self._stream = stream
        self._data = []

    def export(self):
        for entry in self._data:
            for key in entry:
                self._stream.write("{}: {}\n".format(key, entry[key]))
            self._stream.write("\n")

    def add_entry(self, entry):
        self._data.append(entry)

    def add_entries(self, entries):
        self._data.extend(entries)


if __name__ == '__main__':
    exp = StreamExporter()
    exp.add_entry({"name": "teasdasdasdasdadst", "age": 21131, "Asdasda": True})
    exp.add_entry({"name": "test", "age": 21, "Asdasda": True})
    exp.add_entry({"name": "test", "age": 21, "Asdasda": True})
    exp.add_entry({"name": "tadasdasdest", "age": 21, "Asdasda": True})
    exp.export()

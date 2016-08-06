from io import StringIO

from pymockdata.core.base import BaseExporter


class HtmlTableExporter(BaseExporter):
    def __init__(self, filename="output.html"):
        self._output_fn = filename
        self._data = []

    def export(self):
        stream = StringIO()
        fields = self._data[0].keys()
        stream.write("<table>")
        stream.write("<thead>")
        stream.write("<tr>")
        for field in fields:
            stream.write("<th>" + field + "</th>")
        stream.write("</tr></thead><tbody>")

        for entry in self._data:
            stream.write("<tr>")
            if entry.keys() != fields:
                raise ValueError("Incosistent data")

            for key in fields:
                stream.write("<td>")
                stream.write(str(entry[key]))
                stream.write("</td>")

            stream.write("</tr>")
        stream.write("</tbdody></table>")

        with open(self._output_fn, "w") as output:
            output.write(stream.getvalue())

    def add_entry(self, entry):
        self._data.append(entry)

    def add_entries(self, entries):
        self._data.extend(entries)


if __name__ == '__main__':
    exp = HtmlTableExporter()
    exp.add_entry({"name": "teasdasdasdasdadst", "age": 21131, "Asdasda": True})
    exp.add_entry({"name": "test", "age": 21, "Asdasda": True})
    exp.add_entry({"name": "test", "age": 21,  "Asdasda": True})
    exp.add_entry({"name": "tadasdasdest", "age": 21,  "Asdasda": True})
    exp.export()

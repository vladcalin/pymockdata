from sqlite3 import connect as sqlite_connect

from pymockdata.core.base import BaseExporter
from pymockdata.core.errors import ExporterInitializationError


class RawSqlInsertStatementsExporter(BaseExporter):
    def __init__(self, table_name, to_file=None):
        """
        Exports entries as raw sql insert statements

        Entry values must not contain the characters `'`, `\`, `"`, `(`, `)`  or `;`.

        Parameters

            table_name: the name of the table where to insert the values

            to_file: if supploed, the RawSqlInsertStatementsExporter.generate() function will write the results to that
                file instead of returning them.
        """
        self._table_name = table_name
        self._entries = []
        self._to_file = None

        if not self._is_value_valid(self._table_name):
            raise ExporterInitializationError("Invalid table name: {}".format(self._table_name))

    def _is_value_valid(self, value):
        bad_chars = "'\"();"
        for bad_char in bad_chars:
            if bad_char in value:
                return False
        return True

    def add_entries(self, entries):
        self._entries.extend(entries)

    def add_entry(self, entry):
        self._entries.append(entry)

    def export(self):

        queries = []
        field_order = list(self._entries[0].keys())
        # validating field names
        for field in field_order:
            if not self._is_value_valid(field):
                raise ValueError("Invalid field name: {}".format(field))

        for entry in self._entries:
            # validating field values
            for entry_value in entry.values():
                if not self._is_value_valid(entry_value):
                    raise ValueError("Invalid entry value : {}".format(entry_value))

            sql_str = "insert into {}({}) values ({})".format(
                self._table_name,
                ",".join(['"' + x + '"' for x in field_order]),
                ",".join(['"' + entry[x] + '"' for x in field_order])
            )
            queries.append(sql_str)
        return queries


if __name__ == '__main__':
    from pymockdata import DataModel, DataFactory

    exporter = RawSqlInsertStatementsExporter("mockdata")
    data_model = DataModel(
        field1=DataModel.full_name,
        field2=DataModel.ipv4_addr,
        field3=DataModel.mac_addr
    )
    print(DataFactory(data_model, exporter).generate(10))

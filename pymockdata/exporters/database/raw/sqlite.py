from sqlite3 import connect as sqlite_connect

from pymockdata.core.base import BaseExporter
from pymockdata.core.errors import ExporterInitializationError


class RawSqliteExporter(BaseExporter):
    def __init__(self, database_file, table_name):
        """
        Exports data directly to a SQLITE database. The supplied `table_name` table must exist
        and its column names must match the entries' keys and must be of type TEXT.

        For example, a correct usage would be:

        for a table `mocked_data` defined as

        ```sql
        CREATE TABLE `mocked_data` (
            `field1`	TEXT,
            `field2`	TEXT,
            `field3`	TEXT
        )
        ```

        The data generation of 100 entries would be:

        ```python
        exporter = RawSqliteExporter("test.db", "mockdata")
        data_model = DataModel(
            field1=DataModel.full_name,
            field2=DataModel.ipv4_addr,
            field3=DataModel.mac_addr
        )
        DataFactory(data_model, exporter).generate(100)
        ```

        """
        self._db = sqlite_connect(database_file)
        self._table_name = table_name
        self._entries = []

        query_result = self._db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
                                        (self._table_name,))
        if not query_result.fetchall():
            raise ExporterInitializationError("No table '{}' exists".format(self._table_name))

    def add_entries(self, entries):
        self._entries.extend(entries)

    def add_entry(self, entry):
        self._entries.append(entry)

    def export(self):
        cursor = self._db.cursor()
        for entry in self._entries:
            sql_str = "insert into {}({}) values ({})".format(
                self._table_name,
                ",".join(['"' + x + '"' for x in list(entry.keys())]),
                ",".join(['"' + x + '"' for x in list(entry.values())])
            )
            cursor.execute(sql_str)
        self._db.commit()

        cursor.close()


if __name__ == '__main__':
    from pymockdata import DataModel, DataFactory

    exporter = RawSqliteExporter("test.db", "mockdata")
    data_model = DataModel(
        field1=DataModel.full_name,
        field2=DataModel.ipv4_addr,
        field3=DataModel.mac_addr
    )
    DataFactory(data_model, exporter).generate(10000)

from psycopg2 import connect as pg_connect

from pymockdata.core.base import BaseExporter
from pymockdata.core.errors import ExporterInitializationError
from pymockdata.exporters.database.raw.sqlquery_gen import RawSqlInsertStatementsExporter


class RawPostgresqlExporter(BaseExporter):
    def __init__(self, username, password, host, port, database_name, table_name):
        """
        Exports data directly to a PostgreSQL database. The supplied `table_name` table must exist
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
        exporter = RawPostgresqlExporter("test.db", "mockdata")
        data_model = DataModel(
            field1=DataModel.full_name,
            field2=DataModel.ipv4_addr,
            field3=DataModel.mac_addr
        )
        DataFactory(data_model, exporter).generate(100)
        ```

        """
        self._db = pg_connect(host=host, port=port, database=database_name, user=username, password=password)
        self._table_name = table_name
        self._entries = []
        self._query_generator = RawSqlInsertStatementsExporter(self._table_name)

        query_result = self._db.execute("""SELECT EXISTS (
                                            SELECT 1
                                            FROM   pg_catalog.pg_class c
                                            JOIN   pg_catalog.pg_namespace n ON n.oid = c.relnamespace
                                            WHERE  n.nspname = 'public'
                                            AND    c.relname = '?'
                                        );""",
                                        (self._table_name,))
        if not query_result.fetchall():
            raise ExporterInitializationError("No table '{}' exists".format(self._table_name))

    def add_entries(self, entries):
        self._query_generator.add_entries(entries)

    def add_entry(self, entry):
        self._query_generator.add_entry(entry)

    def export(self):
        cursor = self._db.cursor()
        for query in self._query_generator.export():
            cursor.execute(query)
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

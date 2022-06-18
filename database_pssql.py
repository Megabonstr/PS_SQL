import psycopg2


class Database:
    def __init__(self):
        self._conn = psycopg2.connect(database='postgres',
                                      user='postgres',
                                      password='test',
                                      host='localhost',
                                      port='5432')
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        return self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, request, params=None):
        self.cursor.execute(request, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query_one(self, request, params=None):
        self.cursor.execute(request, params or ())
        return print(self.fetchone())

    def query_all(self, request, params=None):
        self.cursor.execute(request, params or ())
        return print(*[row for row in self.fetchall()], sep='\n')

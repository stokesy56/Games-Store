import pyodbc

class Connection_db:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER= ' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn_nwdb.cursor()


    def filter_query(self, query):
        return self.cursor.execute(query)


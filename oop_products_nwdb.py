import pyodbc

class ProductsMcServer():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.conn_nwdb.cursor()

    # CRUD
#    first_entry = conn_nwdb


    # Create 1 entry
    # use INSERT
    # The Cursor cannot make transactions (go to documentation)

    # Update 1 entry
    # the ID of the record to update
    # update specific record
    # update table
    # the cursor cannot make transaction (go to documentation)


    def __filter_query(self, query):  # Strong Params/filter
        # Doing some filtering for bad queries
        return self.cursor.execute(query)

    # Read one entry
    # fetch a specific record
    # get one value using ID

    def read_one_sql_entry(self, table, ID, number):
        query_entry = self.__filter_query(f"SELECT * FROM {table} WHERE {ID} = {number}")
        return query_entry.fetchone()

    # Read all entries
    # fetch all record and return as a list of Dictionaries

    def list_all_sql_entries(self, table):
        all_entries = self.__filter_query(f"SELECT * FROM {table}")
        while True:
            record = all_entries.fetchone()
            if record is None:
                break
            print(record)

    # Destroy/one entry
    # The ID of the specific record
    # Destroy the record
    def destroy_code(self, table, ID, number):
        dropping_query = self.__filter_query(f"DELETE FROM {table} WHERE {ID} = {number}").fetchone()
        return dropping_query










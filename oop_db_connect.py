import pyodbc

# Concept of 'Strong Params' -- never ever trust user input, avoid SQL injections and filter for SQL injections
# Encapsulate
class ConnectMsServer():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def __filter_query(self, query): #Strong Params/filter
        # Doing some filtering for bad queries
        return self.cursor.execute(query)

    def sql_query(self, query):
        return self.__filter_query(query).execute(query)

    def sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

    def print_all_records_from_table(self, table):
        query_rows = self.__filter_query('SELECT * FROM {table}')
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def print_average_price_products(self):
        avg_rows = self.__filter_query('SELECT avg(UnitPrice) FROM Products')
        while True:
            avg_of_products = avg_rows.fetchone()
            if avg_of_products is None:
                break
            return avg_of_products

    def return_avg_unite_price_products(self):
        # Query
        query = self.__filter_query('SELECT * FROM Products')
        # Sum of all unit price
        prices = []

        while True:
            # get individual prices and append to my list
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        # Divide by length of rows
        return (sum(prices)/len(prices))

# CRUD

# Create 1 entry
    # use INSERT
    # The Cursor cannot make transactions (go to documentation)

# Read all entries
    # fetch all record and return as a list of Dictionaries

# Read one entry
    # fetch a specific record
    # get one value using ID

# Update 1 entry
    # the ID of the record to update
    # update specific record
    # update table
        # the cursor cannot make transaction (go to documentation)

#Destroy/one entry
    # The ID of the specific record
    # Destroy the record
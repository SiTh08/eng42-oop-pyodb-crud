import pyodbc

# Concept of 'Strong Params'
    # Never ever trust user input
    # Avoid SQL injections
    # Filter for SQL injections

class ConnectMsS():

    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_nwdb.cursor()

    def __filter_query(self, query):
        # Doing some filtering for bad queries
        return self.cursor.execute(query)

    def __sql_query(self, query):
        return self.__filter_query(query)

    def sql_query_fetchone(self, query):
        return self.__filter_query(query).fetchone()

    def print_all_products_records(self):
        query_rows = self.__filter_query('SELECT * FROM Products')
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    def print_all_products_from_table(self, table):
        query_rows = self.__filter_query(f'SELECT * FROM {table}')
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(record)

    # def average_product_price(self): SQL way
    #     return self.__filter_query('SELECT AVG(UnitPrice) FROM Products').fetchone()

    def return_average_unit_price_products(self):
        # Query
        query = self.__filter_query('SELECT * FROM Products')
        prices = []
        while True:
            # get individual prices and append to list
            record = query.fetchone()
            if record is None:
                break
            prices.append(record.UnitPrice)
        # Sum of unit prices
        # Divide by the length of rows
        return (sum(prices)/len(prices))

    # CRUD - create, read, update, delete

    # Create 1 entry
        # use Insert
        # the Cursor cannot make transactions (go to documentations to check)

    # Read all entries
        # fetch all records and return as a list of Dictionaries.

    # Read one entry
        # fetch a specific record
        # Get one value using ID

    # Update one entry
        # The id of the record to update
        # Update the specific record
            # the Cursor cannot make transactions (go to documentations to check)

    # Destroy one entry
        # The ID of the specific record
        # Destroy the record.
            # the Cursor cannot make transactions (go to documentations to check)
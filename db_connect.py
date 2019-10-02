import pyodbc
# In this file, we will make our connection.

# Parameters/variables for connection:
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_nwdb)


# Create a cursor
# Allows us to execute read-only queries on the db.

cursor = conn_nwdb.cursor()

# using .execute on cursor
# cursor.execute("SELECT @@version;")
cursor.execute("SELECT * from Customers;")

# Fetch some data - fetchone()
row = cursor.fetchone()
print(row)

row = cursor.fetchone() # It maintains state
print(row.ContactName)

row = cursor.fetchone() # It maintains state
print(row.ContactName)

# .fetchall()
# This is bad.
# We don't use this.

rows = cursor.execute("SELECT * FROM Customers").fetchall()
# print(rows)
# print(len(rows))
print(type(rows)) # If this is a list, then:

rows = cursor.execute("SELECT * FROM Products").fetchall()
# We can iterate:
for records in rows:
    print(type(records))
    print(records.UnitPrice) # We can access the column of a specific record.

# This is bad.
# We don't use this.
# Because there is a limited amount of RAM.

# However, this is dangerous as we said.
# Because we can clog our machine with too much data.
    # We can use While loop to be more efficient

rows = cursor.execute('SELECT * FROM Products')

while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)





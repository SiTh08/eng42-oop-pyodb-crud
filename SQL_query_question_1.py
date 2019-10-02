import pyodbc

# Connected to Northwind database

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

print(conn_nwdb)

#Created a cursor
cursor = conn_nwdb.cursor()

cursor.execute("SELECT COUNT(*) from Orders").fetchone
row = cursor.fetchone()
print(row)
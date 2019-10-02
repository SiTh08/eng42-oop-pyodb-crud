from oop_db_connect import *

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

db_nw = ConnectMsS(server, database, username, password)
print(db_nw)
print(db_nw.conn_nwdb)

print(db_nw.cursor.execute('SELECT * FROM Products').fetchone())
print(type(db_nw.cursor.execute('SELECT * FROM Products').fetchone()))
print(db_nw.cursor.execute('SELECT * FROM Products').fetchone().UnitPrice)

# print(db_nw.sql_query('SELECT * FROM Products').fetchone())

# print(db_nw.average_product_price()) sql way
# print(type(db_nw.average_product_price()))

print(db_nw.return_average_unit_price_products())
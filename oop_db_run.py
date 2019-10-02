from oop_db_connect import *
from oop_products_nwdb import *

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
#
#db_nw = ConnectMsServer(server, database, username, password)
# print(db_nw)
# print(db_nw.conn_nwdb)
#
# print(db_nw.cursor.execute('SELECT * FROM Products').fetchone(UnitPrice))
#
# print(db_nw.cursor.execute('SELECT * FROM Products').fetchone())

#print(db_nw.print_average_price_products())

#print(db_nw.return_avg_unit_price_products())

db_nw = ProductsMcServer(server, database, username, password)
print(db_nw.read_one_sql_entry("Products", "ProductID", "1")) #READING ONE SQL QUERY

db_nw =ProductsMcServer(server, database, username, password)
print(db_nw.list_all_sql_entries("Products")) #LISTING ALL QUERIES FOR ON TABLE 

import pyodbc

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#print(conn_nwdb)

cursor = conn_nwdb.cursor()
q1 = cursor.execute("SELECT * FROM Orders").fetchall()
print(q1)
print(len(q1))

q2 = cursor.execute("SELECT * FROM Orders WHERE ShipCity= 'Rio de Janeiro'").fetchall()
print(len(q2))

q3 = cursor.execute("SELECT * FROM Orders WHERE ShipCity= 'Rio de Janeiro' OR ShipCity= 'Reims'").fetchall()
print(len(q3))

while True:
    record = q3.fetchone()
    if record is None:
        break
    print(record.UnitPrice)



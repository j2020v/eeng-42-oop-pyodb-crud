import pyodbc
# In this file we'll make our connection

# Parameters/variables for connection:
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Establish a connection
conn_nwdb = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#print(conn_nwdb)

# Create a cursor
# Allows us to execute read only queries on the db
cursor = conn_nwdb.cursor ()

# using .execute() on cursor
cursor.execute("SELECT * from Customers;")
print(cursor)

# Fetch some rows from cursor - .fetchone()
row = cursor.fetchone()
#print(row)

# .fetchall() --- this is bad, we don't use this
rows = cursor.execute("SELECT * FROM Customers").fetchall()
#print(rows)
#print(len(rows))

# Fetch some data using for loop


print(len(rows))
print(type(rows)) #If this is a list, then:

rows = cursor.execute("SELECT * FROM Products").fetchall()
for record in rows: #Iterating but bad because more power on the RAM // "no break"
    print(type(record))
    print(record.UnitPrice) #We can access the column of a specific record

# This is dangerous because we can clog our machine with too much data.
# We can use While loop to be more efficient .

rows = cursor.execute("SELECT * FROM Products")

while True: #Iterating but good because more power in the processing // "break"
    record = rows.fetchone() #Maintains state
    if record is None:
        break
    print(record.UnitPrice)

### Connecting SQL to Python 

This is an example of us connecting to our SQL server using python and pyodbc.

We will look into:
- Cursor
- Rows
- Querying the db
- Using While loops for obtaining data queries 
- Transactions 

# connection
Fill in the data in the code to connect the database with pycharm. It is a method from pyodbc.

# .cursor 
Allows us to execute readonly queries on the database

# cursor().execute()
Prepares and executes SQL statements 

# .fetchall() vs .fetchone()
.fetchall() is bad if you are querying big data whereas .fetchone() is good and will retrieve only the first data when querying
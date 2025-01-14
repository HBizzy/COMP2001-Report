import pyodbc

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=dist-6-505.uopnet.plymouth.ac.uk;DATABASE=COMP2001_HBuck;UID=HBuck;PWD=KzgN819+'  # Replace YourDatabaseName with the actual database name
try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
import pyodbc
server = 'localhost'
username = 'sa'
password = 'Valuetech@123'
db = 'DB_PYTHON'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';UID='+username+';PWD='+password+';TrustServerCertificate=yes;autocommit=True;'
try: 
    connection=pyodbc.connect(connection_string)
    print('Conexión exitosa')
except Exception as ex:
    print(f'Conexión no exitosa error {ex}')
connection.close()
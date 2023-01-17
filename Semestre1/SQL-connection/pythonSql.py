import pyodbc
import pandas as pd
from SqlStatements import killDb, createDb, createTableCiudad, createTableDatos , createTableRegion
from data import Varios_Datos,Varias_Ciudades,Regiones

'''
# para no tener advertencias de conexión a la db con pandas se puede utilizar SQL alchemy
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
#connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';UID='+username+';PWD='+password+';TrustServerCertificate=yes;autocommit=True'
#connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#engine = create_engine(connection_url)
'''
# deshabilitar la advertencia
import warnings
warnings.filterwarnings('ignore')

#Declaro mis variables para conectarme al servidor
server = 'localhost'
username = 'sa'
password = 'Valuetech@123'
db = 'DB_PYTHON'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';UID='+username+';PWD='+password+';TrustServerCertificate=yes;autocommit=True;'
try: 
    #connection=pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';UID='+username+';PWD='+password+';TrustServerCertificate=yes;autocommit=True')
    connection=pyodbc.connect(connection_string)
    print('Conexión exitosa')
except Exception as ex:
    print(f'Conexión no exitosa error {ex}')

cursor = connection.cursor()
connection.autocommit = True

try:
    #cursor.execute('exec sp_columns Region')
    #cursor.execute(createDb)
    #cursor.execute(createTableRegion)
    #cursor.executemany("INSERT INTO Region VALUES(?,?)", Regiones)
    #cursor.execute("CREATE TABLE Ciudad(Ciudad VARCHAR(255) NOT NULL, Pais VARCHAR(100) NOT NULL, PRIMARY KEY (Ciudad))")
    print('Consulta SQL hecha satisfactoriamente')
except Exception as ex:
    print(ex)
#info = pd.read_sql("exec sp_columns Region", connection)
#regiones = pd.read_sql("SELECT * FROM Region", connection)
#df_regiones = pd.DataFrame(regiones)

#connection.commit()
cursor.close()
connection.close()

#print(df_regiones.head())
#print(info)

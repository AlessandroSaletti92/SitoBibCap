import pandas as pd
import pymysql
from sqlalchemy import create_engine
from confidenziale import databaseaddress_capitolare

cnx = create_engine(databaseaddress_capitolare)
df = pd.read_sql('SELECT * FROM descrizione_esterna', cnx) #read the entire table

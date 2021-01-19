import pandas as pd
import pymysql
from sqlalchemy import create_engine

cnx = create_engine('mysql+pymysql://root:@localhost/capitolare')    
df = pd.read_sql('SELECT * FROM descrizione_esterna', cnx) #read the entire table

descrizione_esterna = pd.read_sql('Select * from descrizione_esterna where segnatura='$search';')
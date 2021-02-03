import pandas as pd
import pymysql
from sqlalchemy import create_engine
from confidenziale import databaseaddress_capitolare_mongo
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine(databaseaddress_capitolare_mongo)

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
#User = Base.classes.user
#Address = Base.classes.address

session = Session(engine)


# collection-based relationships are by default named
# "<classname>_collection"
print (u1.address_collection)


df = pd.read_sql('SELECT * FROM descrizione_esterna', engine) #read the entire table

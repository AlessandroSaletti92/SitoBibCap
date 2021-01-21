from flask import Flask, render_template, request, url_for
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from confidenziale import databaseaddress_capitolare

cnx = create_engine(databaseaddress_capitolare)
df = pd.read_sql('SELECT * FROM descrizione_esterna', cnx) #read the entire table

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index_page():
   # return 'Hello, World!'
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/ricerca')
def ricerca():
	return render_template("search.html")





@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		segnatura = request.form.get('search')
		print(segnatura)
		descrizione_esterna = pd.read_sql("Select * from descrizione_esterna where segnatura='%s';" %segnatura, cnx)
		
	return render_template("risultati2.html", descrizione=descrizione_esterna)

	





if __name__  == '__main__':
	app.run(debug=True)
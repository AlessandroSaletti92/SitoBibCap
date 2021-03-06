from flask import Flask, render_template, request, url_for,send_file,jsonify
from confidenziale import databaseaddress_capitolare_mongo
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
import pymongo
from static_objects import segnaturecodici

GlobalVar = []

class MyForm(FlaskForm):
 #   name = StringField('Materiale', validators=[DataRequired()])
 	materiale = SelectField(u'Materiale: ', choices=['qualsiasi','papiro', 'pergamena', 'carta'])
 	autore = StringField('Autore')
 	titolo = StringField('Titolo')
 	segnatura = StringField('Segnatura')
 	anno = StringField('Datazione')

def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if isinstance(value,dict):
            get_all_values(value)
        if isinstance(value,list):
            for i in value:
                get_all_values(i)
        else:
            if (value == "") or (value is None):
                nested_dictionary[key] = "Non disponibile"

client = pymongo.MongoClient(databaseaddress_capitolare_mongo)

app = Flask(__name__)
# questo è per lo sviluppo (ricarica i file statici non caching) commentarlo in production!!
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = "Alessandro"

@app.route('/')
def index_page():
   # return 'Hello, World!'
	return render_template("index2.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/esplora')
def esplora():
	return render_template("explore.html")





@app.route('/ricerca', methods=['GET', 'POST'])
def ricerca():
	form = MyForm()
	if form.validate_on_submit():

		#import pdb; pdb.set_trace()
		#data = request.form['slider-range']
		anno = request.form['anno']
		var = client.capitolare.codici.find_one({'segnatura_id': segnatura})
		cursor = client.capitolare.codici.find({"segnatura_id": "X", "qty": {"$lt": 30}})
		print("Funziona!")
		print(form.data)
		#print(form.materiale)

	return render_template("search.html", form=form)






@app.route('/comefunziona')
def comefunziona():
	return render_template("comefunziona.html")

@app.route('/progetti')
def progetti():
	return render_template("progetti.html")

@app.route('/lineeguida')
def lineeguida():
	return render_template("lineguida.html")

@app.route('/strumenti')
def strumenti():
	return render_template("strumenti.html")


@app.route('/opendata')
def opendata():
	return render_template("opendata.html")

@app.route('/credits')
def credits():
	return render_template("credits.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		segnatura = request.form.get('autocomplete')
		var = client.capitolare.codici.find_one({'segnatura_id': segnatura})
		get_all_values(var)
	return render_template("risultati2.html", codice=var)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	search = request.args.get('q').upper()
	print(search)
	results = [i for i in segnaturecodici if i.startswith(search)]
	#query = db_session.query(Movie.title).filter(Movie.title.like('%' + str(search) + '%'))
	#results = [mv[0] for mv in query.all()]
	#results = testx
	#results = testx
	return jsonify(matching_results=results)

@app.route('/testautoc', methods=['GET'])
def test():
	return render_template("testautoc.html")

@app.route('/xmltext')
def get_TEI():
	import xml.etree.ElementTree as ET
	from xml.etree.ElementTree import Element, SubElement, Comment, tostring

	root = ET.Element('TEItest')

	child = ET.SubElement(root, 'child')
	child.text = 'This child contains text.'

	child_with_tail = ET.SubElement(root, 'child_with_tail')
	child_with_tail.text = 'This child has regular text.'

	child_with_entity_ref = ET.SubElement(root, 'child_with_entity_ref')
	child_with_entity_ref.text = 'This  that'
	# add your data to the root node in the format you want
	return app.response_class(b"""<?xml version="1.0" encoding="UTF-8"?>"""+ET.tostring(root), mimetype='application/xml')


@app.route('/downxml')
def down_TEI():
	import io
	import xml.etree.ElementTree as ET
	from xml.etree.ElementTree import Element, SubElement, Comment, tostring

	root = ET.Element('TEItest')

	child = ET.SubElement(root, 'child')
	child.text = 'This child contains text.'

	child_with_tail = ET.SubElement(root, 'child_with_tail')
	child_with_tail.text = 'This child has regular text.'

	child_with_entity_ref = ET.SubElement(root, 'child_with_entity_ref')
	child_with_entity_ref.text = 'This  that'
	# add your data to the root node in the format you want
	return send_file(io.BytesIO(b"""<?xml version="1.0" encoding="UTF-8"?>"""+ET.tostring(root)),
						mimetype='application/xml',
            			attachment_filename= 'teitest.xml',
            			as_attachment = True)



if __name__  == '__main__':
	app.run(debug=True)
from flask import Flask, render_template, request, url_for,send_file
from confidenziale import databaseaddress_capitolare_mongo
import pymongo


client = pymongo.MongoClient(databaseaddress_capitolare_mongo)

app = Flask(__name__)
# questo è per lo sviluppo (ricarica i file statici non caching) commentarlo in production!!
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

@app.route('/ricerca')
def ricerca():
	return render_template("search.html")

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
		segnatura = request.form.get('search')
		var = client.capitolare.codici.find_one({'segnatura_id': segnatura})
	return render_template("risultati2.html", codice=var)


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
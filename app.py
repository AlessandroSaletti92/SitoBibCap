# coding=utf-8
from flask import Flask, render_template, request,send_file,jsonify,send_from_directory
from confidenziale import databaseaddress_capitolare_mongo,secret_key,zoteroapikey
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
import pymongo
from static_objects import segnaturecodici,segnaturecodici_dict
import re
from collections import defaultdict
import xml.etree.ElementTree as ET
from TEIexporter import TEImsdesc
import requests
import filigranestatic
# from flask_consent import Consent
# from flask_debugtoolbar import DebugToolbarExtension
GlobalVar = []

class FormFiligrane(FlaskForm):
	#   name = StringField('Materiale', validators=[DataRequired()])
	#materiale = SelectField(u'Materiale: ',
	# 			choices=['qualsiasi','papiro', 'pergamena', 'carta'],
	#			render_kw={'class':"form-control",})
	luogo = SelectField('Luogo',choices=filigranestatic.luoghi,render_kw={'class':"form-control",})
	motivo = SelectField('Motivo',choices=filigranestatic.classi,render_kw={'class':"form-control",})
	manoscritto = StringField('Manoscritto',render_kw={'class':"form-control",})
	IPHN = StringField('IPHN',render_kw={'class':"form-control",})
 	#anno = StringField('Datazione',render_kw={'class':"form-control",})


class MyForm(FlaskForm):
	#   name = StringField('Materiale', validators=[DataRequired()])
	#materiale = SelectField(u'Materiale: ',
	# 			choices=['qualsiasi','papiro', 'pergamena', 'carta'],
	#			render_kw={'class':"form-control",})
	autore = StringField('Autore',render_kw={'class':"form-control",})
	titolo = StringField('Titolo',render_kw={'class':"form-control",})
	fulltext = StringField('Ricerca su tutti i campi',render_kw={'class':"form-control",})
 	#anno = StringField('Datazione',render_kw={'class':"form-control",})

def get_all_values(nested_dictionary):
	"""Aggiunge non disponibile se non specificato.

	Args:
		nested_dictionary (_type_): _description_
	"""
	if isinstance(nested_dictionary,str):
		pass
	else:
		for key, value in nested_dictionary.items():
			if isinstance(value,dict):
				get_all_values(value)
			if isinstance(value,list):
				for i in value:
					get_all_values(i)
			else:
				if (value == "") or (value is None):
					nested_dictionary[key] = "Non disponibile"

def sort_dec_int(var):
	try:
		var['descrizione_interna'] = sorted(var['descrizione_interna'], key= lambda s: list(map(int, s['Descrizione_interna_id'].split('.'))))
	except ValueError:
		pass



client = pymongo.MongoClient(databaseaddress_capitolare_mongo)

app = Flask(__name__)
# questo è per lo sviluppo (ricarica i file statici non caching) commentarlo in production!!
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = secret_key
# the toolbar is only enabled in debug mode:
# app.debug = True
# app.config['DEBUG_TB_PROFILER_ENABLED'] = True
# toolbar = DebugToolbarExtension(app)

#app.config['CONSENT_FULL_TEMPLATE'] = 'consent.html'
#app.config['CONSENT_BANNER_TEMPLATE'] = 'consent_banner.html'
#consent = Consent(app)
#consent.add_standard_categories()

@app.context_processor
def inject_template_scope():
    injections = dict()

    def cookies_check():
        value = request.cookies.get('cookie_consent')
        return value == 'true'
    injections.update(cookies_check=cookies_check)

    return injections

def get_authors(codice,field):
    return list(set([i[field] for i in codice['descrizione_esterna']]))

app.jinja_env.globals.update(get_authors=get_authors)

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def toRoman(n):
    g = {
        1: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        2: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "LC"],
        3: ["", "C", "CC", "CCC", "CD", "DC", "DCC", "DCCC", "CM"],
        4: ["", "M", "MM", "MMM", "MMMM"],
    }
    return "".join(g[len(str(n)) - ind][int(s)] for ind, s in enumerate(str(n)))



app.jinja_env.filters['toRoman'] = toRoman 



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





@app.route('/ricerca_old', methods=['GET', 'POST'])
def ricerca():
	form = MyForm()
	if form.validate_on_submit():

		#import pdb; pdb.set_trace()
		#TODO: cambiare
		segnatura = 'XXB'
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

@app.route('/privacypolicy')
def privacypolicy():
	return render_template("privacypolicy.html")

@app.route('/nontrovato')
def nontrovato():
	return render_template("nontrovato.html")

@app.route('/strumenti')
def strumenti():
	return render_template("strumenti.html")

@app.route('/exploreapp')
def exploreapp():
	return render_template("exploreapp.html")

@app.route('/archivioapp')
def archivioapp():
	return render_template("archivioapp.html")

@app.route('/opendata')
def opendata():
	return render_template("opendata.html")

@app.route('/credits')
def credits():
	return render_template("credits.html")

@app.route('/media')
def media():
	return render_template("media.html")

@app.route('/altaformazione')
def altaformazione():
	return render_template("altaformazione.html")

@app.route('/prodottidellaricerca')
def prodottidellaricerca():
	return render_template("prodottidellaricerca.html")

@app.route('/bootstraptable')
#TODO:remove
def bootstraptable():
	table = [['1','b','d'],['3','r','d'],['2','a','f']]
	return render_template("bootstraptable.html",tableA = table)

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		segnatura = request.form.get('autocomplete')
		if segnatura not in segnaturecodici_dict.keys():
			return render_template("nontrovato.html",segnatura=segnatura)
		segnatura_id = segnaturecodici_dict[segnatura]
		var = client.capitolare.codici.find_one({'segnatura_idx': segnatura_id})
		if var is None:
			return render_template("noncreato.html",segnatura=segnatura)
		#get_all_values(var)
		#sort_dec_int(var)
	# 4,5,6, 3
	return render_template("risultati5.html", codice=var)

@app.route('/archivio/')
def archivio():
	return render_template("archivio.html")

@app.route('/segnatura/<segnatura_id>')
def segnatura(segnatura_id):
	var = client.capitolare.codici.find_one({'segnatura_idx': segnatura_id})
	if var is None:
		return render_template("noncreato.html",segnatura=segnatura_id)
	## WORKAROUND temporary
	if segnatura_id == 'm0256_0':
		sgn = var['segnatura']
		# 4 versione prima, 5,6,3
		# breakpoint()
		del var['_id']
		var['created'] = var['created'].strftime('%Y-%m-%d')
		var['last_modified'] = var['last_modified'].strftime('%Y-%m-%d')
		return render_template("risultati6dyn.html",
							codice=var,
							bibliografia ="none",
							sgn=sgn)
	# get_all_values(var)
	# breakpoint()
	#sort_dec_int(var)
	#import pdb; pdb.set_trace()
	sgn = var['descrizione_esterna'][0]['Segnatura']
	#sgn = "DCCCXLIX (DCCCLIII)"
	filigrane = None
	for i in var['descrizione_esterna']:
		if i['filigrana'] == "Ravvisabile":
			filigrane = client.test.filigranev5.find({"mssc":{"$elemMatch":{"id":segnatura_id}}})
			break

	url = f"https://api.zotero.org/groups/3759014/items?key={zoteroapikey}&tag={sgn}&format=bib&locale=it-IT"
	r = requests.get(url)
	# 4 versione prima, 5,6,3
	return render_template("risultati6.html", codice=var,bibliografia = r.text,sgn=sgn,filigrane=filigrane)

@app.route('/<locale>/zoteroapi/<segnatura>')
def zoteroapi(locale,segnatura):
	style = "https://raw.githubusercontent.com/giacomomarchioro/LaMeDanCSL/main/LaMeDan_author_date/LaMeDan_author_date.csl"
	url = f"https://api.zotero.org/groups/3759014/items?key={zoteroapikey}&tag={segnatura}&format=bib&locale=it-IT&style={style}"
	r = requests.get(url)
	return r.text


@app.route('/segnaturadyn/<segnatura_id>')
def segnaturadyn(segnatura_id):
	var = client.capitolare.codici.find_one({'segnatura_idx': segnatura_id})
	if var is None:
		return render_template("noncreato.html",segnatura=segnatura_id)
	sgn = var['segnatura']
	# 4 versione prima, 5,6,3
	# breakpoint()
	del var['_id']
	var['created'] = var['created'].strftime('%Y-%m-%d')
	var['last_modified'] = var['last_modified'].strftime('%Y-%m-%d')
	return render_template("risultati6dyn.html",
						   codice=var,
						   bibliografia ="none",
						   sgn=sgn)

@app.route('/printableversion/<segnatura_id>')
def printableversion(segnatura_id):
	var = client.capitolare.codici.find_one({'segnatura_idx': segnatura_id})
	if var is None:
		return render_template("nontrovato.html",segnatura=segnatura)
	#get_all_values(var)
	#sort_dec_int(var)
	return render_template("schedaprintableversion.html", codice=var)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	search = request.args.get('q').upper()
	print(search)
	results = [i for i in segnaturecodici_dict.keys() if i.startswith(search)]
	#query = db_session.query(Movie.title).filter(Movie.title.like('%' + str(search) + '%'))
	#results = [mv[0] for mv in query.all()]
	#results = testx
	#results = testx
	return jsonify(matching_results=results)

@app.route('/testautoc', methods=['GET'])
def test():
	return render_template("testautoc.html")

@app.route('/ricerca', methods=['GET', 'POST'])
def BT2():
	form = MyForm()
	cursor = client.capitolare.codici.find({"$and":[{"version" : { "$gte": 1 } },{"status": { "$in": ["Concluso","Presentabile"] } }]})
	#import pdb; pdb.set_trace()
	if form.validate_on_submit():
		#data = request.form['slider-range']
		#anno = request.form['anno']
		#query = defaultdict(list)
		query = {"$and":[{"version" : { "$gte": 1 } },{"status": { "$ne": "appena creato" } }]}
		if form.autore.data != "":
			query_autore_re2 = {"descrizione_interna" :
									{"$elemMatch":
									{"autore":re.compile(form.autore.data,
									re.IGNORECASE)}}}
			query["$and"].append(query_autore_re2)
		# if form.materiale.data != "qualsiasi":
		#	query_materiale_re = {"descrizione_esterna.tipo_di_supporto_e_qualita" : 
		#							re.compile(form.materiale.data, re.IGNORECASE)}
		#
		#	query["$and"].append(query_materiale_re)

		#client.capitolare.codici.find({
		#		
		#	})
		#
		#
		if form.titolo.data != "":
			query_titolo_re2 = {"descrizione_interna" :
									{"$elemMatch": 
									{"titolo":re.compile(form.titolo.data, re.IGNORECASE)}}}
			query["$and"].append(query_titolo_re2)
		if form.fulltext.data != "":
			query_text = {"$text": { "$search": form.fulltext.data }}
			query["$and"].append(query_text)


		cursor = client.capitolare.codici.find(query)
		print("Funziona!")
		print(form.data)
		#print(form.materiale)

	return render_template("bootstraptable2.html",tableA = cursor, form=form)



@app.route('/ricercafiligrane', methods=['GET', 'POST'])
def ricercafiligrane():
	form = FormFiligrane()
	cursor = client.test.filigranev5.find()
	#import pdb; pdb.set_trace()
	if form.validate_on_submit():
		#import pdb; pdb.set_trace()
		#data = request.form['slider-range']
		#anno = request.form['anno']
		# if request.form.get('match-with-bears'):
		query = defaultdict(list)
		if form.luogo.data != "Qualsiasi":
			query_luogo = {"ids":{"$elemMatch":{"place":form.luogo.data}}}
			query["$and"].append(query_luogo)
		if form.motivo.data != "Qualsiasi":
			query_motivo = {"motivo_id": {'$regex':"^%s" %(form.motivo.data)}}
			query["$and"].append(query_motivo)
		if form.IPHN.data != "":
			query_IPHN = {"IPHN":{'$regex':"^%s" %(form.IPHN.data)}}
			query["$and"].append(query_IPHN)
		if form.manoscritto.data != "":
			query_manoscritto = {"mss":{"$elemMatch":{'$regex':"^%s" %(form.manoscritto.data)}}}
			query["$and"].append(query_manoscritto)
		# if form.materiale.data != "qualsiasi":
		#	query_materiale_re = {"descrizione_esterna.tipo_di_supporto_e_qualita" : 
		#							re.compile(form.materiale.data, re.IGNORECASE)}
		#
		#	query["$and"].append(query_materiale_re)

		#client.capitolare.codici.find({
		#		
		#	})
		#
		#
		# if form.titolo.data != "":
		# 	query_titolo_re2 = {"descrizione_interna" :
		# 							{"$elemMatch": 
		# 							{"titolo":re.compile(form.titolo.data, re.IGNORECASE)}}}
		# 	query["$and"].append(query_titolo_re2)
		# if form.fulltext.data != "":
		# 	query_text = {"$text": { "$search": form.fulltext.data }}
		# 	query["$and"].append(query_text)


		cursor = client.test.filigranev5.find(query)
		#cursor = client.capitolare.filigrane.find()
		#breakpoint()
		print("Funziona!")
		print(form.data)
		#print(form.materiale)

	return render_template("ricercafiligrane.html",tableA = cursor, form=form)

@app.route("/visualizzafiligrana/<identificativo>")
def visualizzafiligrana(identificativo):
	watermarkpath = "watermarks/%s.svg" %identificativo
	cursor = client.test.filigranev5.find_one({"id":identificativo})
	return render_template("visualizzafiligrana.html",watermarkpath=watermarkpath, cursor=cursor)

available_formats = {
	"oai_dc" :{
		"name":"oai_dc",
		"type":"application/xml",
		"docs":"http://www.openarchives.org/OAI/2.0/oai_dc.xsd"
	},
	"rdf_bibliontology" : {
		"name":"rdf_bibliontology",
		"type":"application/xml",
		"docs":"https://raw.githubusercontent.com/structureddynamics/Bibliographic-Ontology-BIBO/master/bibo.owl"
	},
	"tei_manuscriptdescription" : {
		"name":"tei_manuscriptdescription",
		"type":"application/xml",
		"docs":"https://tei-c.org/release/xml/tei/custom/schema/xsd/tei_lite.xsd"
	}

}

def get_formats(formats):
	"""Return available formats in XML.

	Args:
		formats (list): A list containing the formats to be shown.

	Returns:
		str: A bytes litteral of the XML containing the list of the formats.
	"""
	root = ET.Element('formats')
	for i in formats:
		child = ET.SubElement(root,'format')
		child.set("name",available_formats[i]['name']) 
		child.set("type",available_formats[i]['type'])
		child.set("docs",available_formats[i]['docs'])
	return b"""<?xml version="1.0" encoding="UTF-8"?>"""+ET.tostring(root)

@app.route('/unapi')
def unapi():
	database = ['none']
	el_id = request.args.get('id',None)
	el_format = request.args.get('format',None)
	#import pdb; pdb.set_trace()

	if el_id is None and el_format is None:
		# UNAPI (no parameters)
		# Provide a list of object formats which should be supported for all 
		# objects available through the unAPI service. Content-type must be 
		# "application/xml". An example response for a site that supports "oai_dc",
		# and "rdf" formats might be: 
		return app.response_class(get_formats(available_formats), mimetype='application/xml')  

	elif el_id and el_format is None:
		# Provide a list of object formats available from the unAPI service for
		# the object identified by IDENTIFIER. Content-type must be 
		# "application/xml". It is similar to the UNAPI response, adding only 
		# an "id" attribute on the root "formats" element; this echoes the 
		# requested identifier. An example response for a Pubmed citation 
		# available in text, Pubmed XML, and ASN.1 formats might be:
		# obj = database[el_id]
		return app.response_class(get_formats(available_formats), mimetype='application/xml')
	
	elif el_id and el_format is not None:
		# Provide a list of object formats available from the unAPI service for
		# the object identified by IDENTIFIER. Content-type must be 
		# "application/xml". It is similar to the UNAPI response, adding only 
		# an "id" attribute on the root "formats" element; this echoes the 
		# requested identifier. An example response for a Pubmed citation 
		# available in text, Pubmed XML, and ASN.1 formats might be:
		var = client.capitolare.codici.find_one({'segnatura_idx': el_id})
		if var is None:
			return app.response_class('Id not found in the database.',status=400)
		#import pdb; pdb.set_trace()
		if el_format == 'tei_manuscriptdescription':
			obj = b"""<?xml version="1.0" encoding="UTF-8"?>"""+ET.tostring(TEImsdesc(var))
		if el_format == 'rdf_bibliontology':
			from RDFexporter import RDFexporter
			obj = b"""<?xml version="1.0" encoding="UTF-8"?>"""+ET.tostring(RDFexporter(var))
			

		return app.response_class(obj, mimetype='application/xml')
	
	elif el_id is None and el_format is not None:
		# This is not specified in the API.
		return app.response_class('Use id, or id and format, not only format',status=400)


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

@app.route('/pagelayout')
def pagelayour():
	import SVGpagelayout
	mas = request.args.get('mas',None)
	# http://localhost:5000/pagelayout/?mas=250x165=24[185]41x15[(6)124(6)]15
	obj = ET.tostring(SVGpagelayout.generateSVG(mas,'test'))
	return app.response_class(obj, mimetype='application/xml')

@app.route('/testbossaglia/')
def testbossaglia():
	return render_template('test_bootstrap.html')

if __name__  == '__main__':
	app.run(debug=True)
from flask import Flask, render_template, request, url_for
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from confidenziale import databaseaddress_capitolare

cnx = create_engine(databaseaddress_capitolare)
df = pd.read_sql('SELECT * FROM descrizione_esterna', cnx) #read the entire table

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

@app.route('/progetti')
def progetti():
	return render_template("progetti.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
	if request.method == 'POST':
		segnatura = request.form.get('search')
		descrizione_esterna = pd.read_sql("Select * from descrizione_esterna where segnatura='%s';" %segnatura, cnx)
		descrizione_interna = pd.read_sql("Select * from descrizione_interna where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx)
		copisti = pd.read_sql("Select * from mano_copista where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx)
		annotazioni_marginali= pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s' AND Id!='';" %segnatura, cnx)
		annotazioni_testo = pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s'AND Id='';" %segnatura, cnx)
		biblio_int_libri = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, dir.Descrizione_interna_id	FROM libro l, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)
		biblio_int_articolo_rivista = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, dir.Descrizione_interna_id FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = 'articolo' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)
		biblio_int_articolo_miscellanea = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, dir.Descrizione_interna_id FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, descrizione_interna_has_riferimento dir, articolo_miscellanea am, libro l WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = 'miscellanea' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id AND am.libro_riferimento_id = l.riferimento_id;" %segnatura, cnx)
		biblio_int_articolo_miscellanea_libro = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, dir.Descrizione_interna_id FROM libro l, riferimento r, libro_has_autore c, descrizione_interna_has_riferimento dir WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)
		biblio_est_libri = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM libro l, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx)
		biblio_est_articolo_rivista = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = 'articolo' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx)
		biblio_est_articolo_miscellanea = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, articolo_miscellanea am, libro l, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = 'miscellanea' AND am.libro_riferimento_id = l.riferimento_id AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;;" %segnatura, cnx)













		biblio_est_articolo_miscellanea_libro = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM libro l, riferimento r, libro_has_autore c, descrizione_esterna_has_riferimento der WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx)




	return render_template("risultati2.html", descrizione=descrizione_esterna,descrizione_int=descrizione_interna, copisti=copisti, annotazioni_marginali=annotazioni_marginali,
							annotazioni_testo=annotazioni_testo, biblio_int_libri=biblio_int_libri, biblio_int_articolo_rivista=biblio_int_articolo_rivista, 
							biblio_int_articolo_miscellanea=biblio_int_articolo_miscellanea, biblio_int_articolo_miscellanea_libro=biblio_int_articolo_miscellanea_libro,
							biblio_est_libri=biblio_est_libri, biblio_est_articolo_rivista=biblio_est_articolo_rivista,	biblio_est_articolo_miscellanea=biblio_est_articolo_miscellanea,
							biblio_est_articolo_miscellanea_libro=biblio_est_articolo_miscellanea_libro, segnatura=segnatura);



if __name__  == '__main__':
	app.run(debug=True)
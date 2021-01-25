from flask import Flask, render_template, request, url_for
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from confidenziale import databaseaddress_capitolare
segnatura = "XXVIII (26)"
cnx = create_engine(databaseaddress_capitolare)
df = pd.read_sql('SELECT * FROM descrizione_esterna', cnx)
descrizione_esterna = pd.read_sql("Select * from descrizione_esterna where segnatura='%s';" %segnatura, cnx)
descrizione_interna = pd.read_sql("Select * from descrizione_interna where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx)
copisti = pd.read_sql("Select * from mano_copista where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx)
annotazioni_marginali= pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s' AND Id!='';" %segnatura, cnx)
annotazioni_testo = pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s'AND Id='';" %segnatura, cnx)
biblio_int_libri = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, dir.Descrizione_interna_id	FROM libro l, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)
biblio_int_articolo_rivista = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, dir.Descrizione_interna_id FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = 'articolo' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)


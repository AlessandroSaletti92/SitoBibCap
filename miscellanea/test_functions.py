
def testcon():
    descrizione_esterna = pd.read_sql("Select * from descrizione_esterna where segnatura='%s';" %segnatura, cnx).replace("","Non disponibile")
    descrizione_interna = pd.read_sql("Select * from descrizione_interna where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx).replace("","Non disponibile")
    copisti = pd.read_sql("Select * from mano_copista where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx).replace("","Non disponibile")
    annotazioni_marginali= pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s' AND Id!='';" %segnatura, cnx).replace("","Non disponibile")
    annotazioni_testo = pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s'AND Id='';" %segnatura, cnx).replace("","Non disponibile")
    biblio_int_libri = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, dir.Descrizione_interna_id	FROM libro l, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx).replace("","Non disponibile")
    biblio_int_articolo_rivista = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, dir.Descrizione_interna_id FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = 'articolo rivista' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx).replace("","Non disponibile")
    biblio_int_articolo_miscellanea = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, dir.Descrizione_interna_id FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, descrizione_interna_has_riferimento dir, articolo_miscellanea am, libro l WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = 'articolo miscellanea' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id AND am.libro_riferimento_id = l.riferimento_id;" %segnatura, cnx).replace("","Non disponibile")
    biblio_int_articolo_miscellanea_libro = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, dir.Descrizione_interna_id FROM libro l, riferimento r, libro_has_autore c, descrizione_interna_has_riferimento dir WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx).replace("","Non disponibile")
    biblio_est_libri = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM libro l, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx).replace("","Non disponibile")
    biblio_est_articolo_rivista = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = 'articolo rivista' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx).replace("","Non disponibile")
    biblio_est_articolo_miscellanea = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, articolo_miscellanea am, libro l, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = 'articolo miscellanea' AND am.libro_riferimento_id = l.riferimento_id AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;;" %segnatura, cnx).replace("","Non disponibile")
    biblio_est_articolo_miscellanea_libro = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM libro l, riferimento r, libro_has_autore c, descrizione_esterna_has_riferimento der WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx).replace("","Non disponibile")
    return True


def testcon2():
    descrizione_esterna = pd.read_sql("Select * from descrizione_esterna where segnatura='%s';" %segnatura, cnx)
    descrizione_interna = pd.read_sql("Select * from descrizione_interna where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx)
    copisti = pd.read_sql("Select * from mano_copista where Descrizione_Esterna_Segnatura='%s';" %segnatura, cnx)
    annotazioni_marginali= pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s' AND Id!='';" %segnatura, cnx)
    annotazioni_testo = pd.read_sql("Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='%s'AND Id='';" %segnatura, cnx)
    biblio_int_libri = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, dir.Descrizione_interna_id	FROM libro l, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)
    biblio_int_articolo_rivista = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, dir.Descrizione_interna_id FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = 'articolo rivista' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)
    biblio_int_articolo_miscellanea = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, dir.Descrizione_interna_id FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, descrizione_interna_has_riferimento dir, articolo_miscellanea am, libro l WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = 'articolo miscellanea' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id AND am.libro_riferimento_id = l.riferimento_id;" %segnatura, cnx)
    biblio_int_articolo_miscellanea_libro = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, dir.Descrizione_interna_id FROM libro l, riferimento r, libro_has_autore c, descrizione_interna_has_riferimento dir WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '%s' AND dir.riferimento_id = r.id;" %segnatura, cnx)
    biblio_est_libri = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM libro l, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx)
    biblio_est_articolo_rivista = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = 'articolo rivista' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx)
    biblio_est_articolo_miscellanea = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, articolo_miscellanea am, libro l, descrizione_esterna_has_riferimento der WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = 'articolo miscellanea' AND am.libro_riferimento_id = l.riferimento_id AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;;" %segnatura, cnx)
    biblio_est_articolo_miscellanea_libro = pd.read_sql("Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, der.Descrizione_Esterna_Segnatura FROM libro l, riferimento r, libro_has_autore c, descrizione_esterna_has_riferimento der WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = 'libro' AND der.Descrizione_Esterna_Segnatura = '%s' AND der.riferimento_id = r.id;" %segnatura, cnx)
    return True 
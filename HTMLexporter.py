from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
from confidenziale import databaseaddress_capitolare_mongo,secret_key
client = MongoClient(databaseaddress_capitolare_mongo)
idx = "m0257_0"
var = client.capitolare.codici.find_one({'segnatura_idx': idx}) 
#https://www.tei-c.org/release/doc/tei-p5-doc/it/html/MS.html
import xml.etree.ElementTree as ET

currentyear = 2021

def HTMLexp(var):
    """Ritorna i dati di un istanza MongoDB del database capitolare in formato
    HTML.

    Args:
        var (dict): il record come dizionario

    Returns:
        [type]: [description]
    """

with open('%s.html' %idx,"w") as f:
    def w(text):
        f.write(text) 
    
    
    def wl(text):
        f.write(text+"\n") 

    current_level = 0 

    wl("<h1>Verona, Biblioteca Capitolare, manoscritto %s</h1>" %var['descrizione_esterna'][0]['Segnatura'])
    
    wl(f"<img src={var['immagine_banner']}>")
    wl(f"<p>{var['sommario_desc']}</p>")
    # Descrizione interna
    wl("<h2>Descrizione esterna.</h2>")
    de = var['descrizione_esterna'] 
    for d in de:
        w(f" <p>Il manoscritto {d['Segnatura']} ({d['dimensioni']}) è databile al {d['datazione']}. Ha un supporto {d['tipo_di_supporto_e_qualita']} di {d['consistenza']}, con {d['numerazione_carte']}. Le carte di guardia sono {d['carte_di_guardia']}; ha una {d['legatura']}.</p>") 
        w(f"Il manoscritto presenta il seguente prospetto di fascicolazione: {d['prospetto_fascicolazione']}.")
    wl("<h2>Descrizioni interne.</h2>")
    items = var['descrizione_interna']
    wl("<ol>")
    current_level = 1
    for i in items: 
        level = len(i['Descrizione_interna_id'].split('.'))
        if  level > current_level:
            wl("   "*current_level+"<ol>")
            current_level = level
        elif level < current_level:
            wl("   "*current_level+r"</ol>")
            current_level = level
        #print(current_level,level)
        wl(f"<li><i>{i['titolo']}</i> ({i['autore']}), {i['carte']}. <b>Incipit:</b> <i>{i['incipit']}</i> <b>Explicit:</b> <i>{i['explicit']}</i></li>")
    wl("</ol>")
    wl("<h2>Mani.</h2>")
    numero_mani = len(var['copisti'])
    if numero_mani == 1: 
        wl(f"<p>Il manoscritto è scritto da una sola mano.</p>")
    else:
        wl(f"</p>Sono state identificate {numero_mani} mani differenti.<p>")
        wl("<ul>")
        for mano in var['copisti']:
            wl("<li>")
            wl(f"La mano qui identificata come {mano['id_cop']} ({mano['intervallo_carte']}) usa una {mano['tipologia_scrittura']}")
            w(f", è databile al {mano['datazione']}")
            wl("</li>")
        wl("</ul>")
    
    if not set(var['annotazioni_marginali'][0].values()) == {''}:
        wl("<h2>Annotazioni marginali.</h2>")
        wl(f"<p>Sono state individuate le seguenti annotazioni marginali.</p>")
        wl("<ul>")
        for anno in var['annotazioni_marginali']:
            wl("<li>")
            wl(f"{anno['Contenuto']} ({anno['intervallo_carte']}) usa una {mano['tipologia_scrittura']}")
            w(f", è databile al {anno['Datazione']}")
            wl("</li>")
        wl("</ul>")
    if not set(var['storia_del_manoscritto'][0].values()) == {''}:
        wl("<h2>Storia del manoscritto.</h2>")
        wl(f"<p>Di seguito vengono riportati gli elementi riconducibili alla storia del manoscritto.</p>")
        wl("<ul>")
        for evento in var['storia_del_manoscritto']:
            wl("<li>")
            wl(f"{evento['Contenuto']} ({evento['intervallo_carte']}) usa una {mano['tipologia_scrittura']}")
            w(f", è databile al {evento['Datazione']}")
            wl("</li>")
        wl("</ul>")
    

   
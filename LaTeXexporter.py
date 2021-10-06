from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#from confidenziale import databaseaddress_capitolare_mongo,secret_key
#client = MongoClient(databaseaddress_capitolare_mongo)
#idx = "m0043_0"
#var = client.capitolare.codici.find_one({'segnatura_idx': idx}) 
#https://www.tei-c.org/release/doc/tei-p5-doc/it/html/MS.html
import xml.etree.ElementTree as ET

currentyear = 2021

def TEImsdesc(var):
    """Ritorna i dati di un istanza MongoDB del database capitolare in formato
    TEI.

    Args:
        var (dict): il record come dizionario

    Returns:
        [type]: [description]
    """
    p = ET.Element("TEI")
    p.set("xmlns","http://www.tei-c.org/ns/1.0") 
    p.set("xml:lang","it")
    teiHeader = ET.SubElement(p,'teiHeader')
    # specifiche non trovate chiedere a prof.Ferrarini
    fileDesc = ET.SubElement(teiHeader,'teiHeader')
    titleStmt = ET.SubElement(fileDesc,'titleStmt')
    title1 = ET.SubElement(titleStmt,'title')
    title1.text = "Scriptorium Veronensis ecclesiae"
    title1.set('type','main')
    title2 = ET.SubElement(titleStmt,'title')
    title2.text = "Verona, Biblioteca Capitolare,%s" %var['descrizione_esterna'][0]['Segnatura'] 
    title2.set('type','sub')

    resS1 = ET.SubElement(titleStmt,'respStmt')
    resp1 = ET.SubElement(titleStmt,'resp')
    resp1.text = "Direzione scientifica di:"
    name1 = ET.SubElement(titleStmt,'name')
    name1.text = "Paolo Pellegrini" 

    resS2 = ET.SubElement(titleStmt,'respStmt')
    resp2 = ET.SubElement(titleStmt,'resp')
    resp2.text = "Scheda a cura di:"
    name2 = ET.SubElement(titleStmt,'name')
    name2.text = var['descrizione_esterna'][0]['utenti_email']

    resS3 = ET.SubElement(titleStmt,'respStmt')
    resp3 = ET.SubElement(titleStmt,'resp')
    resp3.text = "Codifica elettronica a cura di:"
    name3 = ET.SubElement(titleStmt,'name')
    name3.text = var['descrizione_esterna'][0]['utenti_email'] 

    resS4 = ET.SubElement(titleStmt,'respStmt')
    resp4 = ET.SubElement(titleStmt,'resp')
    resp4.text = "Revisione della codifica a cura di:"
    name4 = ET.SubElement(titleStmt,'name')
    name4.text = "" # inserire revisore

    publicationStmt = ET.SubElement(fileDesc,'publicationStmt')
    availability = ET.SubElement(publicationStmt,'availability')
    ab = ET.SubElement(availability,'ab')
    ab.text = "Tutti i contenuti sono riproducibili a patto che se ne indichi la fonte."
                                
    sourceDesc = ET.SubElement(teiHeader,'sourceDesc')
    msDesc = ET.SubElement(sourceDesc, 'msDesc')
    # Mandatory
    msIdentifier = ET.SubElement(sourceDesc, 'msIdentifier')
    # The msIdentifier element is intended to provide an unambiguous means of uniquely 
    # identifying a particular manuscript. This may be done in a struct ured way, by providing 
    # information about the holding institution and the call number, shelfmark, or other 
    # identifier used to indicate its location within that institution. Alternatively, or in 
    # addition, a manuscript may be identified simply by a commonly used name.
    country = ET.SubElement(msIdentifier, 'country')
    country.text = "Italy"
    # contiene il nome di un'unità geopolitica, come una nazione, un paese, una colonia, 
    # o un'unione di stati, che sia più ampia o amministrativamente superiore rispetto a una
    # regione ma di dimensioni inferiori rispetto a un blocco
    region = ET.SubElement(msIdentifier, 'region')
    region.text = "Veneto"
    settlement = ET.SubElement(msIdentifier, 'settlement')
    settlement.text = "Verona"
    institution = ET.SubElement(msIdentifier, 'institution')
    institution.text ="Biblioteca Capitolare di Verona"
    institution.set("xml:lang","it")

    #repository = ET.SubElement(msIdentifier, 'repository')
    #repository.text = "Cavou della biblioteca"
    collection = ET.SubElement(msIdentifier, 'collection')
    collection.text = "Fondo manoscritti Biblioteca Capitolare"
    collection.set("xml:lang","it")
    # for i in names
    # un qualsiasi nome alternativo non strutturato utilizzato per un manoscritto,
    # per esempio ‘ocellus nominum’, o soprannome
    #msName = ET.SubElement(msIdentifier, 'msName')
    #msName.text = "VAR Titolo spangolo? VAR"
    #msName.set("xml:lang",'la') # settare la lingua
    idno = ET.SubElement(msIdentifier, 'idno')
    idno.text = var['descrizione_esterna'][0]['Segnatura'] 


    altIdentifier = ET.SubElement(msIdentifier, 'altIdentifier')
    altIdentifier.set('type','SC')
    # collocazione!
    # Not mandatory
    #head = ET.SubElement(sourceDesc, 'head')
    #head.text('Marsilius de Inghen, Abbreviata phisicorum Aristotelis; Italy,1463.')
    #MS CONTENTS
    msContents = ET.SubElement(sourceDesc, 'msContents ')
    summary = ET.SubElement(msContents, 'summary ')
    summary.text = var['sommario_desc']
    items = ['VAR_descrizione_intere_VAR']
    # Descrizione interna
    items = var['descrizione_interna']
    for ind,item in enumerate(items):
        msItem = ET.SubElement(msContents, 'msItem')
        msItem.set("n",str(ind+1))
        locus = ET.SubElement(msItem, 'locus')
        locus.text = item['carte']
        spc = item['carte'].split("-")
        if len(spc) > 1:
            locus.set("from",spc[0])
            locus.set("to",spc[1])
        elif item['carte'].endswith('rv'):
            locus.set("from",item['carte'][:-1])
            locus.set("to","".join((item['carte'][:-2],"v")))
        # When used within a manuscript description, the title element should be 
        # used to supply a regularized form of the item's title
        title = ET.SubElement(msItem, 'title')
        title.text = item['titolo']
        author = ET.SubElement(msItem, 'author')
        author.text = item['autore']
        author.set("xml:lang",'la')
        incipit = ET.SubElement(msItem, 'incipit')
        incipit.text = item['incipit']
        incipit.set("xml:lang",'la')
        explicit = ET.SubElement(msItem, 'explicit')
        explicit.set("xml:lang",'la')
        if "((" in item['explicit']:
            explicit.set("defective","true")
        explicit.text = item['explicit']
        
        rubric = ET.SubElement(msItem, 'rubric')
        rubric.text = item['rubrica']
        # si potrebbe aggiungere la bibliografia
        # bibl = ET.SubElement(msItem, 'bibl')

    # filiation?
    # Text classification?
    # text language?
    #textLang = ET.SubElement(msContents, 'textLang ')
    #textLang.text = var[?]
    #textLang.set('mainLang','la')
    physDesc = ET.SubElement(sourceDesc , 'physDesc')
    #p = ET.SubElement(physDesc , 'p')
    #p.text = "general descritpion"
    objectDesc = ET.SubElement(physDesc , 'objectDesc')
    objectDesc.set('form','codex') # sempre codex?
    # Support Desc seems a more descriptive version of support that follows
    #supportDesc = ET.SubElement(objectDesc , 'supportDesc')
    #p_supportDesc = ET.SubElement(supportDesc , 'p')
    #p_supportDesc.text = var['descrizione_esterna'][0]['tipo_di_supporto_e_qualita']

    support = ET.SubElement(objectDesc , 'support')
    p_support = ET.SubElement(support , 'p')
    filig = ''
    if var['descrizione_esterna'][0]['filigrana'] != '':
        filig = 'con filigrana: <watermark> %s</watermark>' %['descrizione_esterna'][0]['filigrana']
    material = var['descrizione_esterna'][0]['tipo_di_supporto_e_qualita']

    p_support.text = " ".join((material,filig))
    extent = ET.SubElement(objectDesc , 'extent')
    extent.text = var['descrizione_esterna'][0]['consistenza']
    dimensions = ET.SubElement(extent , 'dimensions')
    dimensions.set('unit','mm')
    dims = var['descrizione_esterna'][0]['dimensioni'].split('=')[0]
    height,width = dims.split('x')
    height_p = ET.SubElement(dimensions , 'height')
    height_p.text = height
    width_p = ET.SubElement(dimensions , 'width')
    width_p.text = width
    fasc = var['descrizione_esterna'][0]['prospetto_fascicolazione']
    fasc = fasc.replace('<sup>',':').replace('</sup>','')
    collation = ET.SubElement(objectDesc , 'collation')
    p_col = ET.SubElement(collation , 'p')
    formula = ET.SubElement(p_col , 'formula')
    formula.text = fasc
    # dovrebbero essere multiple nel caso....
    # for i in foliations
    foliation = ET.SubElement(objectDesc , 'foliation')
    foliation_p = ET.SubElement(foliation , 'p')
    fols = var['descrizione_esterna'][0]['numerazione_carte']
    foliation_p.text = fols
    #condition = ET.SubElement(objectDesc , 'condition')
    #condition_p = ET.SubElement(condition , 'p')
    #condition_p.text = "?"
    #layout = ET.SubElement(objectDesc , 'layout')
    #layout.set('ruledLines',"25 32")
    #layout.set('columns',"1")
    #layout_p = ET.SubElement(layout , 'p')
    #layout_p.text = "?"

    hands = len(var['copisti']) 
    handDesc = ET.SubElement(physDesc, 'handDesc')
    handDesc.set('hands',str(hands))

    ordi = ['prima','seconda','terza','quarta','quinta','sesta']
    for ind,c in enumerate(var['copisti']):
        handNote = ET.SubElement(handDesc, 'handNote')
        handNote.set('xml:id',c['id_cop'])
        handNote_p = ET.SubElement(handNote, 'p')
        locus = ET.SubElement(handNote_p, 'locus')
        locus.text = c['intervallo_carte']
        spc = c['intervallo_carte'].split("-")
        desc = "alla carta"
        if len(spc) > 1:
            locus.set("from",spc[0])
            locus.set("to",spc[1])
            desc = " all'intervallo di carte "
        elif c['intervallo_carte'].endswith('rv'):
            locus.set("from",c['intervallo_carte'][:-1])
            locus.set("to","".join((c['intervallo_carte'][:-2],"v")))
        handNote_p.text = "Una %s mano è identificabile %s" %(ordi[ind],desc)
        locus.tail = 'utilizza una scrittura'
        term = ET.SubElement(handNote_p,'term')
        term.text = c['tipologia_scrittura']
        term.tail = 'è databile al '
        origndate = ET.SubElement(handNote_p,'OriginDate')
        origndate.text = c['datazione']

    # scriptDesc per gli incunabula ed i libri?
    # scriptNote per gli incunabula ed i libri?
    # typeDesc per gli incunabula ed i libri?
    # typeNote per gli incunabula ed i libri?

    deco = var['descrizione_esterna'][0]['decorazioni']  
    if deco != '':
        decoDesc = ET.SubElement(physDesc, 'decoDesc')
        decoDesc_p = ET.SubElement(decoDesc, 'p')
        decoDesc_p.text = deco
        
    # sarebbe meglio usare tanti elementi decoNote
    # con il locus, item invece non è consigliabile secondo me
    if set(var['annotazioni_marginali'][0].values()) != {''}:
        additions = ET.SubElement(physDesc, 'additions')
        additions_p = ET.SubElement(additions, 'p')
        additions_p.text = 'Il manoscritto contiene le seguenti annotazioni:'
        additions_list = ET.SubElement(additions_p, 'list')
    # problema singloare plurale annotazioni multiple eg cc. 262v, 263v, 267r
    # si può ciclare su ognni posizione 
        for idx,ann in enumerate(var['annotazioni_marginali']):
            item = ET.SubElement(additions_list, 'item')
            item.text = ann['Contenuto']
            locus = ET.SubElement(item, 'locus')
            locus.set('facs',ann['link_ROI'])
            locus.text = ann['intervallo_carte']
            locus.tail = ", %s" %ann['Posizione']
            origndate = ET.SubElement(item,'OriginDate')
            origndate.text = ann['Datazione']
            term = ET.SubElement(item,'term')
            term.text = ann['Tipologia_scrittura']

    # ci sarebbe la possibilità di più legature usando <binding>
    if var['descrizione_esterna'][0]['legatura'] != '':
        bindingDesc = ET.SubElement(physDesc, 'bindingDesc')
        bindingDesc_p = ET.SubElement(bindingDesc, 'p')
        bindingDesc_p.text = var['descrizione_esterna'][0]['legatura']

    # sigilli usando sealDesc?

    # Accompanying materials??
    if set(var['storia_del_manoscritto'][0].values()) != {''}:
        history = ET.SubElement(physDesc, 'history')
        history_list = ET.SubElement(history, 'list')
    # problema singloare plurale annotazioni multiple eg cc. 262v, 263v, 267r
    # si può ciclare su ognni posizione 
        for idx,ann in enumerate(var['storia_del_manoscritto']):
            item = ET.SubElement(history_list, 'item')
            item.text = ann['Contenuto']
            locus = ET.SubElement(item, 'locus')
            locus.set('facs',ann['link_ROI'])
            locus.text = ann['intervallo_carte']
            locus.tail = ", %s" %ann['Posizione']
            origndate = ET.SubElement(item,'OriginDate')
            origndate.text = ann['Datazione']
            term = ET.SubElement(item,'term')
            term.text = ann['Tipologia_scrittura']

    # additionals ?
    additional = ET.SubElement(msDesc, 'additional')
    adminInfo = ET.SubElement(additional, 'adminInfo')
    recordHist = ET.SubElement(adminInfo, 'recordHist')
    source = ET.SubElement(recordHist, 'source')
    source_p = ET.SubElement(source, 'p')
    source_p.text = 'Catalogato direttamente dal testo e dai suoi surrogati digitali.'
    # change, dovrebbe essere implementato.
    # surrogates
    availability = ET.SubElement(adminInfo, 'availability')
    availability_p = ET.SubElement(availability, 'p')
    availability_p.text = "Consultabile su appuntamento."
    # custodialHist DA IMPLEMENTARE!
    # custodialHist = ET.SubElement(adminInfo, 'custodialHist')
    # TYPE: conservation, photography, transfer, (analysis?)
    # custEvent = ET.SubElement(custodialHist, 'custEvent')
    # surrogates = ET.SubElement(additional, 'surrogates')

    # per manoscritti separati e poi ricongiunti
    # msPart = ET.SubElement(sourceDesc, 'msPart')
    # per manoscritti separati in più pezzi, Palinsesto di Gaio?
    # msFrag = ET.SubElement(sourceDesc, 'msFrag')

    def indent(elem, level=0):
                i = "\n" + level*"  "
                j = "\n" + (level-1)*"  "
                if len(elem):
                    if not elem.text or not elem.text.strip():
                        elem.text = i + "  "
                    if not elem.tail or not elem.tail.strip():
                        elem.tail = i
                    for subelem in elem:
                        indent(subelem, level+1)
                    if not elem.tail or not elem.tail.strip():
                        elem.tail = j
                else:
                    if level and (not elem.tail or not elem.tail.strip()):
                        elem.tail = j
                return elem  

    indent(p)
    #tree = ET.ElementTree(p)
    #tree.write('segnatura_idx.xml')
    return p
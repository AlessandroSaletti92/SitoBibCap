
from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
# from confidenziale import databaseaddress_capitolare_mongo,secret_key
# client = MongoClient(databaseaddress_capitolare_mongo)
# idx = "m0043_0"
# var = client.capitolare.codici.find_one({'segnatura_idx': idx}) 
#https://www.tei-c.org/release/doc/tei-p5-doc/it/html/MS.html
import xml.etree.ElementTree as ET

currentyear = 2021

def RDFexporter(var):

    root = ET.Element('rdf:RDF')
    root.set("xmlns:rdf","http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    root.set("xmlns:res","http://purl.org/vocab/resourcelist/schema#")
    root.set("xmlns:z","http://www.zotero.org/namespaces/export#")
    root.set("xmlns:dcterms","http://purl.org/dc/terms/")
    root.set("xmlns:bibo","http://purl.org/ontology/bibo/")
    root.set("xmlns:address","http://schemas.talis.com/2005/address/schema#")
    root.set("xmlns:foaf","http://xmlns.com/foaf/0.1/")
    zuser = ET.SubElement(root,'z:UserItem')
    zuser.set('rdf:about','http://zotero.org/users/local/ptD7P9CK/items/C6WTTNN3')
    res = ET.SubElement(zuser,'res:resource')
    res.set("rdf:resource",'lezione.meneghetti.it') # cambia
    repository = ET.SubElement(zuser,'z:repository')
    repository.text = 'repository'
    dcterms = ET.SubElement(zuser,'dcterms:rights')
    dcterms.text = "CC BY 4.0"
    bibom = ET.SubElement(root,'bibo:Manuscript')
    bibom.set("rdf:resource",'lezione.meneghetti.it') # cambia

    title = ET.SubElement(bibom,'dcterms:title')
    title.text = var['descrizione_esterna'][0]['Segnatura']
    abstract = ET.SubElement(bibom,'dcterms:abstract')
    abstract.text = var['sommario_desc']
    date = ET.SubElement(bibom,'dcterms:date')
    date.text = var['descrizione_esterna'][0]['datazione'] 
    language = ET.SubElement(bibom,'dcterms:language')
    language.text = 'la' # TODO: infer language
    #repository= ET.SubElement(bibom,'z:repository')
    #repository.text
    #source= ET.SubElement(bibom,'dcterms:source')
    #source.text
    lccn = ET.SubElement(bibom,'bibo:lccn')
    lccn.text = var['descrizione_esterna'][0]['Segnatura']
    uri= ET.SubElement(bibom,'bibo:uri')
    uri.text = 'lezione.meneghetti.it'
    extra = ET.SubElement(bibom,'z:extra')
    publisher = ET.SubElement(bibom,'dcterms:publisher')
    organization = ET.SubElement(publisher,'foaf:Organization')
    place = ET.SubElement(organization,'address:localityName')
    place.text = "Verona, Biblioteca Capitolare"
    bitype = ET.SubElement(bibom,'dcterms:type')
    bitype.text = 'manuscript'
    authorlist = ET.SubElement(bibom,'bibo:authorList')
    seq = ET.SubElement(authorlist,'rdf:Seq')
    #for i in author
    autori = set([descint['autore'] for descint in var['descrizione_interna']])
    rdfli = ET.SubElement(seq,'rdf:li')
    rdfli.set('rdf:nodeID','n15')
    for autore in autori:
        #TODO: GIVEN NAME, firstnae
        foafp = ET.SubElement(bibom,'foaf:Person')
        foafp.set('rdf:nodeID','n15')
        splitted =  autore.split(' ')
        if len(splitted) == 1:
            name = ET.SubElement(foafp,'foaf:givenName')
            name.text = splitted[0]
        if len(splitted) == 2:
            rname,rsurname = splitted
            name = ET.SubElement(foafp,'foaf:givenName')
            name.text = rname
            surname = ET.SubElement(foafp,'foaf:surname')
            surname.text = rsurname

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

    indent(root)
    #tree = ET.ElementTree(root)
    #tree.write('segnatura_idx.xml')
    return root

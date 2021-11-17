import xml.etree.ElementTree as ET
from .parserclass import layout



def generateSVG(strlayout,name,savetodisk=False):
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

    def _save_tree(p,name):
        indent(p)
        tree = ET.ElementTree(p)
        if not name.endswith('.svg'):
            name+='.svg'
        tree.write(name)
        return True

    #name = 'page'
    #test2 = "250 x 165 = 24[185]41 x 15[(6)124(6)]15"
    #test2 = "288 x 209 =  21[224]43 x 9[(8)69(7)][(7)70(7)]32"
    #test2 = "214 x 147 = 7[171]36 x 15[(5)95(5)]32"
    #test2 = " 250 x 165=  24[198]28 x 20[(9)97(9)(8)]22 "
    mylayout = layout(strlayout)

    p = ET.Element('svg')
    p.set("version", "1.1")
    p.set("baseProfile", "full")
    p.set("width","%smm"%mylayout.width)
    p.set("height","%smm"%mylayout.height)
    p.set("viewBox","0 0 %s %s"%(mylayout.width,mylayout.height))
    p.set("xmlns","http://www.w3.org/2000/svg")
    main_title = ET.SubElement(p, 'title')
    main_title.text = name
    # https://www.w3.org/TR/SVG11/metadata.html
    metadata = ET.SubElement(p,'metadata')
    rdf = ET.SubElement(metadata,'rdf:RDF')
    rdf.set('xmlns:rdf',"http://www.w3.org/1999/02/22-rdf-syntax-ns#")
    rdf.set('xmlns:rdfs',"http://www.w3.org/2000/01/rdf-schema#")
    rdf.set('xmlns:dc',"http://purl.org/dc/elements/1.1/")
    desc = ET.SubElement(rdf,'rdf:Description')
    # if self.about is not None:
    #     desc.set('about',self.about)
    # if name is not None:
    #     desc.set('dc:title',name)
    # if self.description is not None:
    #     desc.set('dc:description',self.description)
    # if self.publisher is not None:
    #     desc.set('dc:publisher',self.publisher)
    # desc.set('dc:date',self.date)
    desc.set('dc:format',"image/svg+xml")
    desc.set('dc:language',"en")
    creator = ET.SubElement(desc,'dc:creator')
    bag = ET.SubElement(creator,'rdf:Bag')
    # for i in self.creators:
    #     c = ET.SubElement(bag,'rdf:li')
    #     c.text = i

    # Image
    img = ET.SubElement(p, 'image')
    img.set("id","backgroundimage")
    # Title
    xtit,ytit = 4,4
    title_e = ET.SubElement(p, 'text')
    title_e.set("x",str(xtit))
    title_e.set("y",str(ytit))
    title_e.set("font-family","Verdana")
    title_e.set("font-size",str(3))
    title_e.set("fill","blue")
    title_e.text = str(mylayout.sheet_ref)
    border_e = ET.SubElement(p,'rect')
    border_e.set("x","0")
    border_e.set("y","0")
    border_e.set("id","collection_border")
    border_e.set("width",str(mylayout.width))
    border_e.set("height",str(mylayout.height))
    border_e.set("stroke-width","0.25")
    border_e.set("fill-opacity","0")
    border_e.set("stroke","black")
    tx = ET.SubElement(border_e, 'title')

    # for i in range(h_lines_n):
    #     line_h = ET.SubElement(p,'rect')
    #     line_h.set("y","0")
    #     line_h.set("id","collection_border")
    #     line_h.set("width",str(x))
    #     line_h.set("height",str(y))
    #     line_h.set("stroke-width","0.25")
    #     line_h.set("fill-opacity","0")
    #     line_h.set("stroke","blue")


    #"""<line x1="0" y1="80" x2="100" y2="20" stroke="black" />"""
    riga = 10
    current_x_dist = float(mylayout.left_margin)
    for col in mylayout.columns:
        

        line_h = ET.SubElement(p,'line')
        line_h.set("stroke-width","0.25")
        line_h.set("x1",str(current_x_dist))
        line_h.set("id","collection_border")
        line_h.set("x2",str(current_x_dist))
        line_h.set("y1",str(mylayout.top_margin))
        line_h.set("y2",str(float(mylayout.height) - float(mylayout.bottom_margin)))
        line_h.set("stroke","black")
        for lm in col.left_margins:
            current_x_dist += float(lm)
            line_h = ET.SubElement(p,'line')
            line_h.set("x1",str(current_x_dist))
            line_h.set("id","collection_border")
            line_h.set("stroke-width","0.25")
            line_h.set("x2",str(current_x_dist))
            line_h.set("y1",str(mylayout.top_margin))
            line_h.set("y2",str(float(mylayout.height) - float(mylayout.bottom_margin)))
            line_h.set("stroke","black")

        # linee per scrittura
        for i in range(int(int(mylayout.rows[0].height)/riga)+1):
            line_h = ET.SubElement(p,'line')
            line_h.set("x1",str(current_x_dist))
            line_h.set("id","collection_border")
            line_h.set("x2",str(float(current_x_dist)+float(col.width)))
            line_h.set("y1",str(float(mylayout.top_margin) + float(riga)*i))
            line_h.set("y2",str(float(mylayout.top_margin) + float(riga)*i))
            line_h.set("stroke","black")
            line_h.set("stroke-width","0.25")


        # linea del margine    
        current_x_dist += float(col.width)
        line_h = ET.SubElement(p,'line')
        line_h.set("x1",str(current_x_dist))
        line_h.set("id","collection_border")
        line_h.set("x2",str(current_x_dist))
        line_h.set("y1",str(mylayout.top_margin))
        line_h.set("y2",str(float(mylayout.height) - float(mylayout.bottom_margin)))
        line_h.set("stroke","black")
        line_h.set("stroke-width","0.25")
        for rm in col.right_margins:
            current_x_dist += float(rm)
            line_h = ET.SubElement(p,'line')
            line_h.set("x1",str(current_x_dist))
            line_h.set("id","collection_border")
            line_h.set("x2",str(current_x_dist))
            line_h.set("y1",str(mylayout.top_margin))
            line_h.set("y2",str(float(mylayout.height) - float(mylayout.bottom_margin)))
            line_h.set("stroke","black")
            line_h.set("stroke-width","0.25")
    
    indent(p)
    if savetodisk:
        _save_tree(p,"%s.svg" %name)
    
    #tree = ET.ElementTree(p)
    #tree.write('segnatura_idx.xml')
    return p

    #_save_tree(p,'test.svg')
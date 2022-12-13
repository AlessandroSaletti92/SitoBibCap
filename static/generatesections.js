
t = {
    'datazione': 'Datazione',
    'consistenza': 'Consistenza',
    'trascrizione_datazione': 'Trascrizione datazione',
    'luogo': 'Luogo',
    'trascrizione_luogo': 'Trascrizione luogo',
    'tipo_di_supporto_e_qualita': 'Tipo di supporto e qualità',
    'carte_di_guardia': 'Carte di guardia',
    'numerazione_carte': 'Numerazione carte',
    'prospetto_fascicolazione': 'Prospetto fascicolazione',
    'arrangiamento_fogli_gregory': 'Arrangiamento fogli gregory',
    'dimensioni': 'Dimensioni',
    'rigatura': 'Rigatura',
    'foratura': 'Foratura',
    'legatura': 'Legatura',
    'intervallo_carte': 'Intervallo carte',
    'Posizione': 'Posizione',
    'trascrizione': 'Trascrizione',
    'Contenuto': 'Contenuto',
    'Datazione': 'Datazione',
    'Tipologia_scrittura': 'Tipologia scrittura',
    'identificazione': 'Identificazione',
    'Descrizione_Esterna_Segnatura': 'ID descrizione esterna'
}

g = document.querySelector("#JSONMetadata")
codice = JSON.parse(g.innerHTML)
function populateDescEst() {
    pDescEst = document.querySelector('#panel_descrizione_esterna')
    if (pDescEst.innerHTML == "") {
        fields = ['datazione', 'consistenza', 'trascrizione_datazione', 'luogo', 'trascrizione_luogo', 'tipo_di_supporto_e_qualita', 'carte_di_guardia', 'numerazione_carte', 'prospetto_fascicolazione', 'arrangiamento_fogli_gregory', 'dimensioni', 'rigatura', 'foratura', 'legatura']
        for (let index = 0; index < codice.descrizione_esterna.length; index++) {
            const field = codice.descrizione_esterna[index];
            if (field['Descrizione_Esterna_Segnatura'] != "0") {
                h6a = document.createElement("h6");
                h6a.innerHTML = field['Descrizione_Esterna_Segnatura']
                h6b = document.createElement("h6");
                h6b.innerHTML = "(" + field['tipologia'] + ")"
                pDescEst.append(h6a, h6b)
            }
            let table = document.createElement("table");
            for (let index = 0; index < fields.length; index++) {
                counter = 0
                if (field[fields[index]] != "") {
                    let row = table.insertRow(counter);
                    row.insertCell(0).innerHTML = t[fields[index]].bold();
                    row.insertCell(1).innerHTML = field[fields[index]];
                    counter++;
                }
            }
            pDescEst.append(table)
            // scriventi 
            pDescEst.insertAdjacentHTML("beforeend", "Scriventi principali:".bold());
            ol = document.createElement("ol");
            for (let index = 0; index < codice.copisti.length; index++) {
                scr = codice.copisti[index]
                if (scr.Descrizione_Esterna_Segnatura.includes(field['Descrizione_Esterna_Segnatura'])) {
                    li = document.createElement("li");
                    li.className = 'scriventelist'
                    let f = [('Scrivente ' + scr.id_cop).bold(), scr.intervallo_carte, scr.tipologia_scrittura, scr.datazione]
                    li.innerHTML = f.join(', ')
                    ol.appendChild(li)
                }
            }
            pDescEst.appendChild(ol)
            // Postille e annotazioni 
            pDescEst.insertAdjacentHTML("beforeend", "Postille e annotazioni:".bold());
            ol = document.createElement("ol");
            for (let index = 0; index < codice.annotazioni_marginali.length; index++) {
                anno = codice.annotazioni_marginali[index]
                if (scr.Descrizione_Esterna_Segnatura.includes(field['Descrizione_Esterna_Segnatura']) && anno.tipologia == 'Postilla o annotazione') {
                    li = document.createElement("li");
                    li.className = 'annotationlist'
                    let f = [(anno.Id_anno).bold(), anno.intervallo_carte, anno.Posizione, anno.Datazione, anno.Tipologia_scrittura, anno.Contenuto]
                    li.innerHTML = f.join(', ')
                    img = document.createElement("img");
                    img.src = anno.link_ROI
                    img.alt = anno.Contenuto
                    img.className = "rounded mx-auto d-block"
                    img.width = "400"
                    li.appendChild(img)
                    li.insertAdjacentHTML("beforeend", "Trascrizione:".bold());
                    li.insertAdjacentHTML("beforeend", anno.trascrizione);
                    ol.appendChild(li)
                }
            }
            pDescEst.appendChild(ol)
        }
    }
}

function populateScrittureAvventizie() {
    pScrAvv = document.querySelector('#panel_scritture_avventizie')
    if (pScrAvv.innerHTML == "") {
        fields = ['intervallo_carte', 'Posizione', 'trascrizione', 'Contenuto', 'Datazione', 'Tipologia_scrittura', 'identificazione', 'Descrizione_Esterna_Segnatura',]
        for (let index = 0; index < codice.annotazioni_marginali.length; index++) {
            const field = codice.annotazioni_marginali[index];
            if (field.tipologia == "Scrittura avventizia") {
                h6a = document.createElement("h6");
                h6a.innerHTML = field.Id_anno.bold()
                pScrAvv.append(h6a)
                let table = document.createElement("table");
                for (let index = 0; index < fields.length; index++) {
                    counter = 0
                    if (field[fields[index]] != "") {
                        let row = table.insertRow(counter);
                        row.insertCell(0).innerHTML = t[fields[index]].bold();
                        row.insertCell(1).innerHTML = field[fields[index]];
                        counter++;
                    }
                }
                pScrAvv.append(table)
                img = document.createElement("img");
                img.src = field.link_ROI
                img.alt = field.Contenuto
                img.width = "400"
                img.className = "rounded mx-auto d-block p-3"
                pScrAvv.appendChild(img)
            }
        }
    }
}

function populateDescInt() {
    pDescInt = document.querySelector('#panel_descInt')
    if (pDescInt.innerHTML == "") {
        let current_level = 1
        let level = 1
        let dict = {};
        ol = document.createElement("ol")
        ol.className = 'olnumbered'
        dict[level] = ol

        for (let i = 0; i < codice.descrizione_interna.length; i++) {
            di = codice.descrizione_interna[i]
            level = di.Descrizione_interna_id.split('.').length
            if (level > current_level) {
                current_level = level
                if (level > 1) {
                    br = document.createElement("br")
                    li.append(br)
                    btn = document.createElement("button")
                    btn.setAttribute("onClick", "javascript: mostraDI(this);")
                    btn.innerHTML = "Mostra contenuto"
                    li.append(btn)
                    ol = document.createElement("ol")
                    ol.className = 'olnumbered'
                    ol.hidden = true
                    li.appendChild(ol)
                    dict[level] = ol
                } else {
                    ol = document.createElement("ol")
                    ol.className = 'olnumbered'
                    li.appendChild(ol)
                    dict[level] = ol
                }
            } else if (level < current_level) {
                current_level = level
            }
            li = document.createElement("li")
            li.className = 'linumbered'
            li.innerHTML = di.titolo.bold() + " " + di.autore + "," + di.carte + "." + "<b>Incipit: </b>" + di.incipit.italics() + "<b> Explicit: </b> " + di.explicit.italics()
            if (di.incipit_url != "") {
                a = document.createElement("a")
                a.href = di.incipit_url
                a.target = "_blank"
                a.innerHTML = "  &#x1F4F7;"
                li.appendChild(a)
            }
            dict[level].appendChild(li)
        }
        pDescInt.appendChild(dict[1])
    }
}

document.getElementById("accordion_descrizione_esterna").addEventListener("click", populateDescEst);
document.getElementById("accordion_scritture_avventizie").addEventListener("click", populateScrittureAvventizie);
document.getElementById("accordion_descInt").addEventListener("click", populateDescInt);


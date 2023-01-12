
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


function toRoman(str) {
    const g = {
        1: ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        2: ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'LC'],
        3: ['', 'C', 'CC', 'CCC', 'CD', 'DC', 'DCC', 'DCCC', 'CM'],
        4: ['', 'M', 'MM', 'MMM','MMMM']
    }
    if(/^-?\d+$/.test(str)){
        return [...str].map((s, i) => g[str.length - i][s]).join("")
    }else{
        return str
    }
}

function getUC(descin){
    res  = ""
    if (descin['Descrizione_Esterna_Segnatura'] != "0") {
        r = toRoman(descin['Descrizione_Esterna_Segnatura'])
        res = '(Unità codicologica ' + r + ') '
    }
    return res
}



let acc = document.getElementsByClassName("accordion");
let i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

function mostraDI(elem) {
  elem.nextElementSibling.toggleAttribute('hidden')
}

g = document.querySelector("#JSONMetadata")
codice = JSON.parse(g.innerHTML)
function populateDescEst() {
    pDescEst = document.querySelector('#panel_descrizione_esterna')
    if (pDescEst.innerHTML == "") {
        fields = ['legatura', 'foratura', 'rigatura', 'dimensioni', 'arrangiamento_fogli_gregory', 'prospetto_fascicolazione', 'numerazione_carte', 'carte_di_guardia', 'tipo_di_supporto_e_qualita', 'trascrizione_luogo', 'luogo', 'trascrizione_datazione', 'datazione','consistenza']
        for (let index = 0; index < codice.descrizione_esterna.length; index++) {
            const field = codice.descrizione_esterna[index];
            if (field['Descrizione_Esterna_Segnatura'] != "0") {
                h6a = document.createElement("h6");
                h6a.innerHTML = toRoman(field['Descrizione_Esterna_Segnatura'])
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
                if (anno.Descrizione_Esterna_Segnatura == field['Descrizione_Esterna_Segnatura'] && anno.tipologia == 'Postilla o annotazione') {
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
                    if (anno.trascrizione != ''){
                        li.insertAdjacentHTML("beforeend", "Trascrizione: ".bold());
                        li.insertAdjacentHTML("beforeend", anno.trascrizione);
                    }
                    ol.appendChild(li)
                }
            }
            if (ol.innerHTML == '') {
                ol.innerHTML = "Nessuna."
            }
            pDescEst.appendChild(ol)
        }
    }
}

function populateScrittureAvventizie() {
    pScrAvv = document.querySelector('#panel_scritture_avventizie')
    if (pScrAvv.innerHTML == "") {
        pScrAvv.innerHTML = "<br>"
        fields = ['intervallo_carte', 'Posizione', 'trascrizione', 'Contenuto', 'Datazione', 'Tipologia_scrittura', 'identificazione']
        for (let index = 0; index < codice.annotazioni_marginali.length; index++) {
            const field = codice.annotazioni_marginali[index];
            if (field.tipologia == "Scrittura avventizia") {
                let table = document.createElement("table");
                table.id = "scritturaaventizia-"+field.Id_anno
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
                    btn.className = 'DI-button'
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
            li.innerHTML = getUC(di).bold() + di.autore + ", " + di.titolo.italics() + ", " + di.carte + ". " + "<b>Incipit: </b>" + di.incipit + "<b> Explicit: </b> " + di.explicit
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


function populatenotedipossesso() {
    pNotep = document.querySelector('#panel_notepossesso')
    if (pNotep.innerHTML == "") {
        pNotep.innerHTML = "<br>"
        fields = ['Tipologia_scrittura','Posizione', 'trascrizione','Contenuto', 'Datazione']
        for (let index = 0; index < codice.storia_del_manoscritto.length; index++) {
            const field = codice.storia_del_manoscritto[index]
            let table = document.createElement("table");
            table.id = "notedibibl-"+field.ID_At
            for (let j = 0; j < fields.length; j++) {
                counter = 0
                if (field[fields[j]] != "") {
                    let row = table.insertRow(counter);
                    row.insertCell(0).innerHTML = t[fields[j]].bold();
                    row.insertCell(1).innerHTML = field[fields[j]];
                    counter++;
                }
            }
            pNotep.append(table)
            img = document.createElement("img");
            img.src = field.link_ROI
            img.alt = field.Contenuto
            img.width = "400"
            img.className = "rounded mx-auto d-block p-3"
            pNotep.appendChild(img)
            }
        }
      }





function populateStoriaDesc() {
    pStoria = document.querySelector('#show_storia_desc')
    pStoria.innerHTML = codice.storia_desc

}

function getBiblio() {
    bib = document.getElementById('bibextshow')
    if (bib.innerHTML == "") {
        bib.innerHTML = '<div class="text-center">' +
                        '<span class="sr-only">Sto acquisendo i dati da ZoteroAPI...</span> <br>'+
                        '<div class="spinner-border" role="status">'+
                        '</div>'+
                        '</div>'
        // da sostituire con codice.segnatura
        fetch('/it/zoteroapi/DCCCXLIX%20(DCCCLIII)').then(function (response) {
            // The API call was successful!
            return response.text();
        }).then(function (html) {
            // This is the HTML from our response as a text string
            bib.innerHTML= html
        }).catch(function (err) {
            // There was an error
            console.warn('Something went wrong.', err);
        });
    }
}


descest = document.getElementById("accordion_descrizione_esterna")
descest.addEventListener("click", populateDescEst);
scrittureavv  = document.getElementById("accordion_scritture_avventizie")
scrittureavv.addEventListener("click", populateScrittureAvventizie);
descint = document.getElementById("accordion_descInt")
descint.addEventListener("click", populateDescInt);
notediposs = document.getElementById("btn_note_di_possesso")
notediposs.addEventListener("click", populatenotedipossesso);
storiadesc = document.getElementById("btn_storia_desc")
storiadesc.addEventListener("click", populateStoriaDesc);
bibext = document.getElementById("btn_bibext")
bibext.addEventListener("click", getBiblio)

function hideacc(e) {
  se = e.currentTarget.selectedElement
  if(!se.classList.contains('active')){
      se.click()
    }
  se.scrollIntoView({behavior: 'smooth', block: "start"});
  }

//TOC
tcDE = document.getElementById("toc_Descrizione_esterna")
tcDE.addEventListener("click", hideacc)
tcDE.selectedElement = descest
tcSA = document.getElementById("toc_Scritture_avventizie")
tcSA.addEventListener("click", hideacc)
tcSA.selectedElement = scrittureavv
tcDI = document.getElementById("toc_Descrizione_interna")
tcDI.addEventListener("click", hideacc)
tcDI.selectedElement = descint
tcNP = document.getElementById("toc_Note_di_possesso")
tcNP.addEventListener("click", hideacc)
tcNP.selectedElement = notediposs
tcSD = document.getElementById("toc_Storia_del_manoscritto")
tcSD.addEventListener("click", hideacc)
tcSD.selectedElement = storiadesc
tcBB = document.getElementById("toc_Bibliografia_esterna")
tcBB.addEventListener("click", hideacc)
tcBB.selectedElement = bibext

function closeall() {
    accordions = document.getElementsByClassName("accordion")
    for
        (let index = 0; index < accordions.length; index++) {
              if(accordions[index].classList.contains('active')){
              accordions[index].click()
            }
    }
}

document.getElementById("chiuditutto").addEventListener("click",closeall)
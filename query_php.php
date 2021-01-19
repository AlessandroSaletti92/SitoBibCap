<?php

include '../dbms/dbms.php';


if(isset($_POST['submit'])){

  // apro la connessione
  $con = open_connection();

  //salvo nella variabile $search il contenuto della barra di ricerca "search" 
  $search = mysqli_real_escape_string($con, $_POST['search']);

////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                //
//                    DESCRIZIONE ESTERNA                                                         //
//                                                                                                //
////////////////////////////////////////////////////////////////////////////////////////////////////

  

  // chiamo la funzione per effettuare la query
  $result = select_descrizione_esterna($search);

  // conto gli elementi ritornati dalla query
  $num = count($result);


  $i = 0;

  if($num != 0){
  
  

  if($num > 0){
    while ($i<$num) {


        $segnatura = $result[$i];
        $datazione = $result[$i+1];
        $tipo_di_supporto_e_qualita = $result[$i+2];
        $consistenza = $result[$i+3];
        $numerazione_carte = $result[$i+4];
        $carte_di_guardia = $result[$i+5];
        $prospetto_fascicolazione = $result[$i+6];
        $arrangiamento_fogli_gregory = $result[$i+7];
        $dimensioni = $result[$i+8];
        $rigatura = $result[$i+9];
        $foratura = $result[$i+10];
        $legatura = $result[$i+11];
        $utenti_email = $result[$i+12];
        $Descrizione_Esterna_Segnatura = $result[$i+13];

        if($Descrizione_Esterna_Segnatura == $segnatura){
          $Descrizione_Esterna_Segnatura = "No. E'presente un'unica descrizione esterna";
        }

      echo "<table>
            <h2>Manoscritto $segnatura</h2>
            <h3>Descrizione Esterna</h3><br>
           <tr>
            <tr><td><b>Segnatura: </b></td><td>$segnatura</td></tr>
            <tr><td><b>Datazione: </b></td><td>$datazione</td></tr>
            <tr><td><b>Tipologia di supporto e qualità: </b></td><td>$tipo_di_supporto_e_qualita</td></tr>
            <tr><td><b>Consistenza: </b></td><td>$consistenza</td></tr>
            <tr><td><b>Numerazione delle carte: </b></td><td>$numerazione_carte</td></tr>
            <tr><td><b>Carte di guardia: </b></td><td>$carte_di_guardia</td></tr>
            <tr><td><b>Prospetto fascicolazione: </b></td><td>$prospetto_fascicolazione</td></tr>
            <tr><td><b>Arrangiamento dei fogli (regola di Gregory): </b></td><td>$arrangiamento_fogli_gregory</td></tr>
            <tr><td><b>Dimensioni: </b></td><td>$dimensioni</td></tr>
            <tr><td><b>Rigatura: </b></td><td>$rigatura</td></tr>
            <tr><td><b>Foratura: </b></td><td>$foratura</td></tr>
            <tr><td><b>Legatura: </b></td><td>$legatura</td></tr>
            <tr><td><b>Utente: </b></td><td>$utenti_email</td></tr>
            <tr><td><b>Palinsesto: </b></td><td>$Descrizione_Esterna_Segnatura</td></tr>
        </table>";
   $i = $i+14;

  }

  }else{
      $output = "<br>Non è stato trovato nessun testo con segnatura: <b>$search</b> <br /></b><br />";
      echo "$output";
    }

////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                    //
//                    DESCRIZIONE INTERNA                                       //
//                                                  //
////////////////////////////////////////////////////////////////////////////////////////////////////

// chiamo la funzione per effettuare la query
  $result = select_descrizione_interna($search);

  // conto gli elementi ritornati dalla query
  $num = count($result);


  $i = 0;
  $j = 1;


  if($num > 0){
    echo "<br>";
    echo "<h2>Descrizioni interne</h2>";
    while ($i<$num) {


      $segnatura = $result[$i];
        
      $autore = $result[$i];
      $titolo = $result[$i+1];  
      $id = $result[$i+2];  
      $incipit = $result[$i+3]; 
      $explicit = $result[$i+4];
      $carte = $result[$i+5];
      $rubrica = $result[$i+6]; 
      $Descrizione_Esterna_Segnatura = $result[$i+7]; 
      $Descrizione_interna_id = $result[$i+8];

        if($Descrizione_interna_id == NULL){
          $Descrizione_interna_id = 'Nessuna descrizione interna di riferimento';
        }

      echo "<table>
            <h3>Descrizione Interna $j</h3>
           <tr>
            <tr><td><b>Autore: </b></td><td>$autore</td></tr>
            <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
            <tr><td><b>Id: </b></td><td>$id</td></tr>
            <tr><td><b>Incipit: </b></td><td>$incipit</td></tr>
            <tr><td><b>Explicit: </b></td><td>$explicit</td></tr>
            <tr><td><b>Carte: </b></td><td>$carte</td></tr>
            <tr><td><b>Rubrica: </b></td><td>$rubrica</td></tr>
            <tr><td><b>Testo di riferimento(segnatura): </b></td><td>$Descrizione_Esterna_Segnatura</td></tr>
            <tr><td><b>Descrizione interna di riferimento: </b></td><td>$Descrizione_interna_id</td></tr>
        </table><br>";
   $i = $i+9;
   $j = $j+1;
  }

  }

  /*else{
      $output = "<br>Non è stato trovato nessun testo con segnatura: <b>$search</b> <br /></b><br />";
      echo "$output";
    }
*/


////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                    //
//                  BIBLIOGRAFIA DESCRIZIONE INTERNA                                //
//                                                  //
////////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////////////////////////
// BIBLIOGRAFIA INTERNA - LIBRI
/////////////////////////////////////

  $result = biblio_int_libro($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);


  $i = 0;

  if($num > 0){
    echo "<br>";
    echo "<h2>Bibliografia interna</h2>";
    echo "<h3>Libri</h3>";

    while ($i<$num) {


      $id = $result[$i];
      $titolo = $result[$i+1];
      $anno = $result[$i+2];
      $numero_pagine = $result[$i+3];
      $citta = $result[$i+4];
      $casa_editrice = $result[$i+5]; 
      $collana  = $result[$i+6];  
      $n_collana = $result[$i+7];
      $autore_nome_cognome = $result[$i+8];
      $desc_int = $result[$i+9];

      if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }
        if($citta == null){
          $citta = "Non presente";
        }
        if($casa_editrice == null){
          $casa_editrice = "Non presente";
        }
        if($collana == null){
          $collana = "Non presente";
        }
        if($n_collana == null){
          $n_collana = "Non presente";
        }

        echo "<table>
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Città: </b></td><td>$citta</td></tr>
              <tr><td><b>Casa editrice scrittura: </b></td><td>$casa_editrice</td></tr>
              <tr><td><b>Collana: </b></td><td>$collana</td></tr>
              <tr><td><b>Numero collana: </b></td><td>$n_collana</td></tr>
              <tr><td><b>Autore: </b></td><td>$autore_nome_cognome</td></tr>
              <tr><td><b>Descrizione interna di riferimento: </b></td><td>$desc_int</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+10;
      }

  }else{
    echo "<h4>Non presenti</h4>";
    }


//////////////////////////////////////////////
// BIBLIOGRAFIA INTERNA - ARTICOLI DI RIVISTA
//////////////////////////////////////////////


$result = biblio_int_articolo_rivista($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);

  $i = 0;

  echo "<h3>Articoli in rivista</h3>";

  if($num > 0){

      while ($i<$num) {
        
        $id = $result[$i];
        $titolo = $result[$i+1];
        $anno = $result[$i+2];
        $numero_pagine = $result[$i+3];
        $numero_fascicolo = $result[$i+4];
        $nome_rivista = $result[$i+5];
        $autore_nome_cognome = $result[$i+6];
        $desc_int = $result[$i+7];

        if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }
        if($numero_fascicolo == null){
          $numero_fascicolo = "Non presente";
        }
        if($nome_rivista == null){
          $nome_rivista = "Non presente";
        }

        echo "<table>
            
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Numero fascicolo: </b></td><td>$numero_fascicolo</td></tr>
              <tr><td><b>Nome rivista: </b></td><td>$nome_rivista</td></tr>
              <tr><td><b>Autore: </b></td><td>$autore_nome_cognome</td></tr>
              <tr><td><b>Descrizione interna di riferimento: </b></td><td>$desc_int</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+8;
      }

  }else{
    echo "<h5>Non presenti</h5><br>";
     }


//////////////////////////////////////////////////
// BIBLIOGRAFIA INTERNA - ARTICOLI DI MISCELLANEA
//////////////////////////////////////////////////
  

$result = biblio_int_articolo_miscellanea($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);

  $i = 0;

  echo "<h3>Articoli in miscellanea</h3>";

  if($num > 0){

      while ($i<$num) {

        $id = $result[$i];
        $titolo = $result[$i+1];
        $anno = $result[$i+2];
        $numero_pagine = $result[$i+3];
        $curatore_nome_cognome = $result[$i+4];
        $autore_nome_cognome = $result[$i+5];
        $desc_int = $result[$i+6];

        if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }

        echo "<table>
            
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Curatore: </b></td><td>$curatore_nome_cognome</td></tr>
              <tr><td><b>Autore: </b></td><td>$autore_nome_cognome</td></tr>
              <tr><td><b>Descrizione interna di riferimento: </b></td><td>$desc_int</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+7;
      }

  }else{
    echo "<h5>Non presenti</h5><br>";
  }


///////////////////////////////////////////////
// BIBLIOGRAFIA INTERNA - LIBRI DI MISCELLANEA
///////////////////////////////////////////////

  $result = biblio_int_libro_miscellanea($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);

  echo "<h3>Libri Miscellanea</h3>";
  $i = 0;

  if($num > 0){

    while ($i<$num) {


      $id = $result[$i];
      $titolo = $result[$i+1];
      $anno = $result[$i+2];
      $numero_pagine = $result[$i+3];
      $citta = $result[$i+4];
      $casa_editrice = $result[$i+5]; 
      $collana  = $result[$i+6];  
      $n_collana = $result[$i+7];
      $curatore_nome_cognome = $result[$i+8];
      $desc_int = $result[$i+9];

      if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }
        if($citta == null){
          $citta = "Non presente";
        }
        if($casa_editrice == null){
          $casa_editrice = "Non presente";
        }
        if($collana == null){
          $collana = "Non presente";
        }
        if($n_collana == null){
          $n_collana = "Non presente";
        }


        echo "<table>
            <caption>
            </caption>
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Città: </b></td><td>$citta</td></tr>
              <tr><td><b>Casa editrice scrittura: </b></td><td>$casa_editrice</td></tr>
              <tr><td><b>Collana: </b></td><td>$collana</td></tr>
              <tr><td><b>Numero collana: </b></td><td>$n_collana</td></tr>
              <tr><td><b>Curatore: </b></td><td>$curatore_nome_cognome</td></tr>
              <tr><td><b>Descrizione interna di riferimento: </b></td><td>$desc_int</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+10;
      }

  }else{
    echo "<h5>Non presenti</h5>";
    }



////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                    //
//                         COPISTI                                            //
//                                                  //
////////////////////////////////////////////////////////////////////////////////////////////////////

  $result = select_copisti($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);


  $i = 0;
  $j = 1;

  
  if($num > 0){
  echo "<br>";
  echo "<br>";
  echo "<h2>Copisti</h2>";

    while ($i<$num) {


        
      $id = $result[$i];  
      $datazione = $result[$i+1]; 
      $tipologia_scrittura = $result[$i+2];
      $Descrizione_Esterna_Segnatura = $result[$i+3]; 

        if($Descrizione_interna_id == NULL){
          $Descrizione_interna_id = 'Nessuna descrizione interna di riferimento';
        }

      echo "<table>
            <h3>Copista $j</h3>
           <tr>
            <tr><td><b>Id: </b></td><td>$id</td></tr>
            <tr><td><b>Datazione: </b></td><td>$datazione</td></tr>
            <tr><td><b>Tipologia scrittura: </b></td><td>$tipologia_scrittura</td></tr>
            <tr><td><b>Testo di riferimento(segnatura): </b></td><td>$Descrizione_Esterna_Segnatura</td></tr>
        </table>";
        echo "<br>";
   $i = $i+4;
   $j = $j+1;
  }

  }


////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                    //
//                   STORIA DEL MANOSCRITTO                                       //
//                                                  //
////////////////////////////////////////////////////////////////////////////////////////////////////

  /////////////////////////////////////
  // ANNOTAZIONI MARGINALI
  /////////////////////////////////////

  $result = annotazioni_marginali($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);


  $i = 0;
  $j = 1;

  
  if($num > 0){
  echo "<br>";
  echo "<br>";
  echo "<h2>Storia del manoscritto</h2>";
    echo "<br>";

  echo "<h3>Annotazioni marginali</h3>";
    while ($i<$num) {


      $Id_auto_inc = $result[$i];
      $Id = $result[$i+1];
      $Datazione = $result[$i+2];
      $Contenuto = $result[$i+3];
      $Posizione = $result[$i+4]; 
      $Tipologia_scrittura  = $result[$i+5];  
      $Descrizione_Esterna_Segnatura = $result[$i+6];

      echo "<table>
            <h3>Annotazione $j</h3>
           <tr>
            <tr><td><b>Id: </b></td><td>$Id_auto_inc</td></tr>
            <tr><td><b>Mano: </b></td><td>$Id</td></tr>
            <tr><td><b>Datazione: </b></td><td>$datazione</td></tr>
            <tr><td><b>Contenuto: </b></td><td>$Contenuto</td></tr>
            <tr><td><b>Posizione: </b></td><td>$Posizione</td></tr>
            <tr><td><b>Tipologia scrittura: </b></td><td>$Tipologia_scrittura</td></tr>
            <tr><td><b>Testo di riferimento(segnatura): </b></td><td>$Descrizione_Esterna_Segnatura</td></tr>
        </table>
        ";
        echo "<br>";
   $i = $i+7;
   $j = $j+1;
  }

  }

  /////////////////////////////////////
  // ANNOTAZIONI SUL TESTO
  /////////////////////////////////////

  $result = annotazioni_testo($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);


  $i = 0;
  $j = 1;


  if($num > 0){
  echo "<br>";
  echo "<br>";
  echo "<h2>Annotazioni sul testo</h2>";

    while ($i<$num) {


      $Id_auto_inc = $result[$i];
      //$Id = $result[$i+1];
      $Datazione = $result[$i+2];
      $Contenuto = $result[$i+3];
      $Posizione = $result[$i+4]; 
      $Tipologia_scrittura  = $result[$i+5];  
      $Descrizione_Esterna_Segnatura = $result[$i+6];

      echo "<table>
            <h3>Annotazione $j</h3>
           <tr>
            <tr><td><b>Id: </b></td><td>$Id_auto_inc</td></tr>
            <tr><td><b>Datazione: </b></td><td>$datazione</td></tr>
            <tr><td><b>Contenuto: </b></td><td>$Contenuto</td></tr>
            <tr><td><b>Posizione: </b></td><td>$Posizione</td></tr>
            <tr><td><b>Tipologia scrittura: </b></td><td>$Tipologia_scrittura</td></tr>
            <tr><td><b>Testo di riferimento(segnatura): </b></td><td>$Descrizione_Esterna_Segnatura</td></tr>
        </table>
        ";
        echo "<br>";
   $i = $i+7;
   $j = $j+1;
  }

  }


////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                    //
//                  BIBLIOGRAFIA DESCRIZIONE ESTERNA                                //
//                                                  //
////////////////////////////////////////////////////////////////////////////////////////////////////



/////////////////////////////////////
// BIBLIOGRAFIA ESTERNA - LIBRI
/////////////////////////////////////

$result = biblio_est_libro($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);

  echo "<br>";
  echo "<br>";
  echo "<h2>Bibliografia Esterna</h2>";
  echo "<h3>Libri</h3>";

  $i = 0;

  if($num > 0){
    
      while ($i<$num) {

        $id = $result[$i];
        $titolo = $result[$i+1];
        $anno = $result[$i+2];
        $numero_pagine = $result[$i+3];
        $citta = $result[$i+4];
        $casa_editrice = $result[$i+5]; 
        $collana  = $result[$i+6];  
        $n_collana = $result[$i+7];
        $autore_nome_cognome = $result[$i+8];
        $desc_est = $result[$i+9];

        if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }
        if($citta == null){
          $citta = "Non presente";
        }
        if($casa_editrice == null){
          $casa_editrice = "Non presente";
        }
        if($collana == null){
          $collana = "Non presente";
        }
        if($n_collana == null){
          $n_collana = "Non presente";
        }

        echo "<table>
            <caption>
            </caption>
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Città: </b></td><td>$citta</td></tr>
              <tr><td><b>Casa editrice scrittura: </b></td><td>$casa_editrice</td></tr>
              <tr><td><b>Collana: </b></td><td>$collana</td></tr>
              <tr><td><b>Numero collana: </b></td><td>$n_collana</td></tr>
              <tr><td><b>Autore: </b></td><td>$autore_nome_cognome</td></tr>
              <tr><td><b>Manoscritto di riferimento: </b></td><td>$desc_est</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+10;
      }

  }else{
    echo "<h4>Non presenti</h4>";
    }
  


//////////////////////////////////////////////
// BIBLIOGRAFIA ESTERNA - ARTICOLI DI RIVISTA
//////////////////////////////////////////////


$result = biblio_est_articolo_rivista($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);

  $i = 0;

  echo "<h3>Articoli in rivista</h3>";

  if($num > 0){
    
      while ($i<$num) {
        
        $id = $result[$i];
        $titolo = $result[$i+1];
        $anno = $result[$i+2];
        $numero_pagine = $result[$i+3];
        $numero_fascicolo = $result[$i+4];
        $nome_rivista = $result[$i+5];
        $autore_nome_cognome = $result[$i+6];
        $desc_est = $result[$i+7];

        if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }
        if($numero_fascicolo == null){
          $numero_fascicolo = "Non presente";
        }
        if($nome_rivista == null){
          $nome_rivista = "Non presente";
        }

        echo "<table>
            
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Numero fascicolo: </b></td><td>$numero_fascicolo</td></tr>
              <tr><td><b>Nome rivista: </b></td><td>$nome_rivista</td></tr>
              <tr><td><b>Autore: </b></td><td>$autore_nome_cognome</td></tr>
              <tr><td><b>Manoscritto di riferimento: </b></td><td>$desc_est</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+8;
      }

  }else{
    echo "<h4>Non presenti</h4>";
     }




//////////////////////////////////////////////////
// BIBLIOGRAFIA INTERNA - ARTICOLI DI MISCELLANEA
//////////////////////////////////////////////////
  

$result = biblio_est_articolo_miscellanea($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);

  $i = 0;

  echo "<h3>Articoli in miscellanea</h3>";

  if($num > 0){
    
      while ($i<$num) {

        $id = $result[$i];
        $titolo = $result[$i+1];
        $anno = $result[$i+2];
        $numero_pagine = $result[$i+3];
        $curatore_nome_cognome = $result[$i+4];
        $autore_nome_cognome = $result[$i+5];
        $desc_est = $result[$i+6];

        if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }

        echo "<table>
            
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Curatore: </b></td><td>$curatore_nome_cognome</td></tr>
              <tr><td><b>Autore: </b></td><td>$autore_nome_cognome</td></tr>
              <tr><td><b>Manoscritto di riferimento: </b></td><td>$desc_est</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+7;
      }

  }else{
    echo "<h4>Non presenti</h4>";
  }

  

//////////////////////////////////////////////////
// BIBLIOGRAFIA ESTERNA - LIBRI DI MISCELLANEA
//////////////////////////////////////////////////

$result = biblio_est_libro_miscellanea($search, $con);

  // conto gli elementi ritornati dalla query
  $num = count($result);


  $i = 0;

  if($num > 0){

    echo "<h3>Libri miscellanea</h3>";
    
      while ($i<$num) {

        $id = $result[$i];
        $titolo = $result[$i+1];
        $anno = $result[$i+2];
        $numero_pagine = $result[$i+3];
        $citta = $result[$i+4];
        $casa_editrice = $result[$i+5]; 
        $collana  = $result[$i+6];  
        $n_collana = $result[$i+7];
        $curatore_nome_cognome = $result[$i+8];
        $desc_est = $result[$i+9];

        if($anno == null){
          $anno = "Non presente";
        }
        if($numero_pagine == null){
          $numero_pagine = "Non presente";
        }
        if($citta == null){
          $citta = "Non presente";
        }
        if($casa_editrice == null){
          $casa_editrice = "Non presente";
        }
        if($collana == null){
          $collana = "Non presente";
        }
        if($n_collana == null){
          $n_collana = "Non presente";
        }



        echo "<table>
            <caption>
            </caption>
             <tr>
              <tr><td><b>Id: </b></td><td>$id</td></tr>
              <tr><td><b>Titolo: </b></td><td>$titolo</td></tr>
              <tr><td><b>Anno: </b></td><td>$anno</td></tr>
              <tr><td><b>Numero pagine: </b></td><td>$numero_pagine</td></tr>
              <tr><td><b>Città: </b></td><td>$citta</td></tr>
              <tr><td><b>Casa editrice scrittura: </b></td><td>$casa_editrice</td></tr>
              <tr><td><b>Collana: </b></td><td>$collana</td></tr>
              <tr><td><b>Numero collana: </b></td><td>$n_collana</td></tr>
              <tr><td><b>Curatore: </b></td><td>$curatore_nome_cognome</td></tr>
              <tr><td><b>Manoscritto di riferimento: </b></td><td>$desc_est</td></tr>

          </table>
          ";

          echo "<br>";
        $i = $i+10;
      }

  }else{
    echo "<h4>Non presenti</h4>";
    }

close_connection($con);

}
else {
  echo "Nessun manoscritto trovato con segnatura: <b>$search</b><br><br>";
}
}


?>
</div>


</body>
</html>
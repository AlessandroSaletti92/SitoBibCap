<?php

//funzione per stabilire la connessione con il database

function open_connection(){
	$con = mysqli_connect("localhost","root","","capitolare");
	// Check connection

	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}

return $con;

}

////////////////////////////////////////////////////////////////////////////////////////////////////

//funzione per la chiusura della connessione con il database

function close_connection($connessione){

	mysqli_close($connessione);

}

////////////////////////////////////////////////////////////////////////////////////////////////////
//																							      //
//									QUERY PER L'INSERIMENTO DATI                                  //
//																								  //
////////////////////////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////////////////////

//FUNZIONE PER L'INSERIMENTO DELLA DESCRIZIONE ESTERNA

function insert_desc_est($segnatura, $datazione, $tipo_di_supporto_e_qualità, $consistenza, $numerazione_carte, $carte_di_guardia, $prospetto_fascicolazione, $arrangiamento_fogli_gregory, $dimensioni, $rigatura, $foratura, $legatura, $utenti_email, $con){

	$sql="INSERT INTO `descrizione_esterna` (`segnatura`, `datazione`, `tipo_di_supporto_e_qualita`, `consistenza`, `numerazione_carte`, `carte_di_guardia`, `prospetto_fascicolazione`, `arrangiamento_fogli_gregory`, `dimensioni`, `rigatura`, `foratura`, `legatura`, `Descrizione_Esterna_Segnatura`, `utenti_email` )
	VALUES
	('$segnatura','$datazione','$tipo_di_supporto_e_qualità', '$consistenza', '$numerazione_carte','$carte_di_guardia','$prospetto_fascicolazione','$arrangiamento_fogli_gregory','$dimensioni','$rigatura','$foratura','$legatura','$segnatura','$utenti_email')";


	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));

  	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////

//FUNZIONE PER L'INSERIMENTO DELLA DESCRIZIONE INTERNA

function insert_desc_int($autore, $titolo, $incipit, $explicit, $carte, $rubrica, $Descrizione_Esterna_Segnatura, $con){

	$sql="INSERT INTO `descrizione_interna` (`autore`, `titolo`, `incipit`, `explicit`, `carte`, `rubrica`, `Descrizione_Esterna_Segnatura`, Descrizione_interna_id)
	VALUES
	('$autore','$titolo', '$incipit', '$explicit', '$carte','$rubrica', '$Descrizione_Esterna_Segnatura' , NULL)";


	if (!mysqli_query($con,$sql))
  	{
  	die('Error: ' . mysqli_error($con));
  	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////

//FUNZIONE PER IL RECUPERO DELL'ID DELLA DESCRIZIONE INTERNA PER L'INSERIMENTO DELLA SOTTO DESCRIZIONE INTERNA

function id_from_desc_int($autore, $titolo, $incipit, $explicit, $carte, $rubrica, $segnatura, $con){

	//salvo il risultato della query --- cerca soltanto il nome, non tutti i campi della tabella
  	$result = mysqli_query($con,"Select id from descrizione_interna where autore='$autore' AND titolo='$titolo' AND incipit='$incipit' AND explicit='$explicit' AND carte='$carte' AND rubrica='$rubrica' AND Descrizione_Esterna_Segnatura='$segnatura' AND Descrizione_interna_id IS NULL ORDER BY id DESC LIMIT 1;");

  	$num_rows = mysqli_num_rows($result);

	if($num_rows > 0){

  		//creo l'associazione con gli elementi del record
    	while ($row2 = mysqli_fetch_assoc($result)){

    	$id_desc_int = $row2['id'];
    	
    	}
	}

	return $id_desc_int;

}



/////////////////////////////////////////////////////////////////////////////////////////////////////

//FUNZIONE PER L'INSERIMENTO DELLA DESCRIZIONE INTERNA

function insert_sub_desc_int($sub_autore, $sub_titolo, $sub_incipit, $sub_explicit, $sub_carte, $sub_rubrica, $segnatura, $id_desc_int, $con){

	$sql="INSERT INTO `descrizione_interna` (`autore`, `titolo`, `incipit`, `explicit`, `carte`, `rubrica`, `Descrizione_Esterna_Segnatura`, `Descrizione_interna_id`)
	VALUES
	('$sub_autore','$sub_titolo', '$sub_incipit', '$sub_explicit', '$sub_carte','$sub_rubrica', '$segnatura' , '$id_desc_int' )";


	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  }

}

/////////////////////////////////////////////////////////////////////////////////////////////////////

// FUNZIONE PER L'INSERIMENTO DEL RIFERIMENTO

function riferimento($tipo, $titolo, $anno, $numero_pagine, $con){

	$sql="INSERT INTO `riferimento` (`tipo`, `titolo`, `anno`, `numero_pagine`)
	VALUES
	('$tipo', '$titolo','$anno', '$numero_pagine')";


	if (!mysqli_query($con,$sql))
  	{
  	die('Error: ' . mysqli_error($con));
  	}

}


/////////////////////////////////////////////////////////////////////////////////////////////////////

// FUNZIONE PER IL RECUPERO DELL'ID DEL RIFERIMENTO

function id_from_riferimento($titolo, $anno, $numero_pagine, $con){

	$sql="Select id from riferimento where titolo='$titolo' AND anno='$anno' AND numero_pagine='$numero_pagine' ORDER BY id DESC LIMIT 1";
	$result = mysqli_query($con,$sql);

  	$num_rows = mysqli_num_rows($result);

  	if($num_rows > 0){

    	//creo l'associazione con gli elementi del record
    	while ($row2 = mysqli_fetch_assoc($result)){

      	$id_riferimento = $row2['id'];
 	 
 	 	}
	}
	return $id_riferimento;
}

////////////////////////////////////////////////////////////////////////////////////////////////////

// FUNZIONE PER L'INSERIMENTO DEL LOBRO

function insert_libro($citta, $casa_editrice, $collana, $n_collana, $riferimento_id, $con){

	$sql="INSERT INTO `libro` (`citta`, `casa_editrice`, `collana`, `n_collana`, `riferimento_id`)
	VALUES
	('$citta','$casa_editrice', '$collana', '$n_collana', '$riferimento_id' )";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////

// FUNZIONE PER L'INSERIMENTO DEI DATI NELLA TABELLA 'DESCRIZIONE INTERNA HAS RIFERIMENTO'

function descrizione_interna_has_riferimento($id_desc_int, $segnatura, $id_riferimento, $con){

	$sql="INSERT INTO `descrizione_interna_has_riferimento` (`Descrizione_interna_id`, `Descrizione_interna_Descrizione_Esterna_Segnatura`, `riferimento_id`)
	VALUES
	('$id_desc_int', '$segnatura', '$id_riferimento')";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////

// FUNZIONE PER L'INSERIMENTO DEI DATI NELLA TABELLA 'LIBRO_HAS_AUTORE'

function autore_has_riferimento($autore, $id_riferimento, $con){

	$sql="INSERT INTO `autore_has_riferimento` (`autore_nome_cognome`, `riferimento_id`)
	VALUES
	('$autore', '$id_riferimento')";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}

}


////////////////////////////////////////////////////////////////////////////////////////////////////

// FUNZIONE PER L'INSERIMENTO DELL'AUTORE

function insert_autore($autore, $con){

	$sql="INSERT INTO `autore` (`nome_cognome`)
	VALUES
	('$autore')";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////

// FUNZIONE PER L'INSERIMENTO DELLA RIVISTA

function insert_rivista($numero_fascicolo, $nome_rivista, $id_riferimento, $con){

	$sql="INSERT INTO `articolo_rivista` (`numero_fascicolo`, `nome_rivista`, `riferimento_id`)
	VALUES
	('$numero_fascicolo', '$nome_rivista', '$id_riferimento')";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}
}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER L'INSERIMENTO DEL CURATORE

function libro_has_autore($id_riferimento, $curatore_libro, $con){

	$sql="INSERT INTO `libro_has_autore` (`libro_riferimento_id`, `autore_nome_cognome`)
	VALUES
	('$id_riferimento', '$curatore_libro')";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}

}


////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER L'INSERIMENTO DELL'ID DELL'ARTICOLO DI MISCELLANEA E L'ID DEL LIBRO (TABELLA ARTICOLO_MISCELLANEA)

function insert_miscellanea($id_riferimento_miscellanea, $id_riferimento_libro, $con){

	$sql="INSERT INTO `articolo_miscellanea` (`riferimento_id`, `libro_riferimento_id`)
	VALUES
	('$id_riferimento_miscellanea', '$id_riferimento_libro')";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}

}


////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER L'INSERIMENTO DEI COPISTI
function insert_copista($id, $datazione, $tipo_scrittura, $segnatura, $con){

	$sql="INSERT INTO `mano_copista` (`id`, `datazione`, `tipologia_scrittura`, `Descrizione_Esterna_Segnatura`)
	VALUES
	('$id', '$datazione', '$tipo_scrittura', '$segnatura')";


	if (!mysqli_query($con,$sql) && !mysqli_query($con,$sql))
 	 {
  	die('Error: ' . mysqli_error($con));
  	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER L'INSERIMENTO DELLA STORIA DEL MANOSCRITTO (ANNOTAZIONI)

function insert_nota($id, $datazione, $contenuto, $posizione, $tipologia_scrittura, $segnatura, $con){

	$sql="INSERT INTO `storia_del_manoscritto` (`Id`, `Datazione`, `Contenuto`, `Posizione`, `Tipologia_scrittura`, `Descrizione_Esterna_Segnatura`)
	VALUES
	('$id', '$datazione', '$contenuto', '$posizione', '$tipologia_scrittura', '$segnatura')";


	if (!mysqli_query($con,$sql) && !mysqli_query($con,$sql))
  	{
  	die('Error: ' . mysqli_error($con));
  	}

}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER L'INSERIMENTO DEI DATI NELLA TABELLA "DESCRIZIONE ESTERNA HAS RIFERIMENTO"

function descrizione_esterna_has_riferimento($segnatura, $id_riferimento, $con){

	$sql="INSERT INTO `descrizione_esterna_has_riferimento` (`Descrizione_Esterna_Segnatura`, `riferimento_id`)
	VALUES
	('$segnatura', '$id_riferimento')";

	if (!mysqli_query($con,$sql)){

		die('Error: ' . mysqli_error($con));
  	}

}



function check_autore($autore, $con){

	
	$result = mysqli_query($con, "Select nome_cognome from autore where nome_cognome='$autore';");
	
	$num_rows = mysqli_num_rows($result);

	return $num_rows;

}


////////////////////////////////////////////////////////////////////////////////////////////////////
//																							      //
//										QUERY PER LA LETTURA DATI                                 //
//																								  //
////////////////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEI DATI DELLA DESCRIZIONE ESTERNA

function select_descrizione_esterna($search){

  $connessione = open_connection();

  $result = mysqli_query($connessione,"Select * from descrizione_esterna where segnatura='$search';");


   $num_rows = mysqli_num_rows($result);

   $data = array(); 
   
   if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$segnatura = $row['Segnatura'];
			$datazione = $row['datazione'];
			$tipo_di_supporto_e_qualita = $row['tipo_di_supporto_e_qualita'];
			$consistenza = $row['consistenza'];
			$numerazione_carte = $row['numerazione_carte'];
			$carte_di_guardia = $row['carte_di_guardia'];
			$prospetto_fascicolazione = $row['prospetto_fascicolazione'];
			$arrangiamento_fogli_gregory = $row['arrangiamento_fogli_gregory'];
			$dimensioni = $row['dimensioni'];
			$rigatura = $row['rigatura'];
			$foratura = $row['foratura'];
			$legatura = $row['legatura'];
			$utenti_email = $row['utenti_email'];
			$Descrizione_Esterna_Segnatura = $row['Descrizione_Esterna_Segnatura'];



			array_push( $data, $segnatura, $datazione, $tipo_di_supporto_e_qualita, $consistenza, $numerazione_carte, $carte_di_guardia, $prospetto_fascicolazione, $arrangiamento_fogli_gregory, $dimensioni, $rigatura, $foratura, $legatura, $utenti_email, $Descrizione_Esterna_Segnatura);
		
		}
	}



  mysqli_close($connessione);

return $data;


}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEI DATI DELLA DESCRIZIONE ESTERNA

function select_descrizione_interna($search){

	$connessione = open_connection();

    $result = mysqli_query($connessione,"Select * from descrizione_interna where Descrizione_Esterna_Segnatura='$search';");
 
    $num_rows = mysqli_num_rows($result);

    $data = array(); 


    if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$autore = $row['autore'];
			$titolo = $row['titolo'];	
			$id = $row['id'];	
			$incipit = $row['incipit'];	
			$explicit =	$row['explicit'];
			$carte = $row['carte'];
			$rubrica = $row['rubrica'];	
			$Descrizione_Esterna_Segnatura = $row['Descrizione_Esterna_Segnatura'];	
			$Descrizione_interna_id = $row['Descrizione_interna_id'];

			array_push($data, $autore, $titolo, $id, $incipit, $explicit, $carte, $rubrica, $Descrizione_Esterna_Segnatura, $Descrizione_interna_id);
		
		}
	}

  	mysqli_close($connessione);

return $data;


}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEI COPISTI

function select_copisti($search, $con){

   $result = mysqli_query($con,"Select * from mano_copista where Descrizione_Esterna_Segnatura='$search';");

   $num_rows = mysqli_num_rows($result);

   $data = array(); 

   if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$datazione = $row['datazione'];	
			$tipologia_scrittura  = $row['tipologia_scrittura'];	
			$Descrizione_Esterna_Segnatura = $row['Descrizione_Esterna_Segnatura'];	

			if($datazione == ""){
				$datazione = "Non presente";
			}
			if($tipologia_scrittura == ""){
				$tipologia_scrittura = "Non presente";
			}

			array_push($data, $id, $datazione, $tipologia_scrittura, $Descrizione_Esterna_Segnatura);
		
		}
	}

return $data;

}


////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DELLE ANNOTAZIONI MARGINALI

function annotazioni_marginali($search, $con){

   $result = mysqli_query($con,"Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='$search' AND Id!='';");

   $num_rows = mysqli_num_rows($result);

   $data = array(); 

   if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$Id_auto_inc = $row['Id_auto_inc'];
			$Id = $row['Id'];
			$Datazione = $row['Datazione'];
			$Contenuto = $row['Contenuto'];
			$Posizione = $row['Posizione'];	
			$Tipologia_scrittura  = $row['Tipologia_scrittura'];	
			$Descrizione_Esterna_Segnatura = $row['Descrizione_Esterna_Segnatura'];	

			if($Datazione == ""){
				$Datazione = "Non presente";
			}
			if($Tipologia_scrittura == ""){
				$Tipologia_scrittura = "Non presente";
			}
			if($Contenuto == ""){
				$Contenuto = "Non presente";
			}



			array_push($data, $Id_auto_inc, $Id, $Datazione, $Contenuto, $Posizione, $Tipologia_scrittura, $Descrizione_Esterna_Segnatura);
		
		}
	}

return $data;

}


////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DELLE ANNOTAZIONI SUL TESTO

function annotazioni_testo($search, $con){

   $result = mysqli_query($con,"Select * from storia_del_manoscritto where Descrizione_Esterna_Segnatura='$search' AND Id='';");

   $num_rows = mysqli_num_rows($result);

   $data = array(); 

   if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$Id_auto_inc = $row['Id_auto_inc'];
			$Id = $row['Id'];
			$Datazione = $row['Datazione'];
			$Contenuto = $row['Contenuto'];
			$Posizione = $row['Posizione'];	
			$Tipologia_scrittura  = $row['Tipologia_scrittura'];	
			$Descrizione_Esterna_Segnatura = $row['Descrizione_Esterna_Segnatura'];	

			if($Datazione == ""){
				$Datazione = "Non presente";
			}
			if($Tipologia_scrittura == ""){
				$Tipologia_scrittura = "Non presente";
			}
			if($Contenuto == ""){
				$Contenuto = "Non presente";
			}



			array_push($data, $Id_auto_inc, $Id, $Datazione, $Contenuto, $Posizione, $Tipologia_scrittura, $Descrizione_Esterna_Segnatura);
		
		}
	}

return $data;

}

////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                //
//                                      BIBLIOGRAFIA INTERNA                                      //
//                                                                                                //
////////////////////////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEI LIBRI DELLA BIBLIOGRAFIA INTERNA

function biblio_int_libro($search, $con){

	$libro = "libro";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, dir.Descrizione_interna_id
	FROM libro l, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir 
	WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = '$libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '$search' AND
	dir.riferimento_id = r.id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$citta = $row['citta'];	
			$casa_editrice  = $row['casa_editrice'];	
			$collana = $row['collana'];	
			$n_collana = $row['n_collana'];
			$autore_nome_cognome = $row['autore_nome_cognome'];
			$desc_int = $row['Descrizione_interna_id'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $citta, $casa_editrice, $collana, $n_collana, $autore_nome_cognome, $desc_int);
		
		}
	}

return $data;

}



////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEGLI ARTICOLI DI RIVISTA DELLA BIBLIOGRAFIA INTERNA

function biblio_int_articolo_rivista($search, $con){

	$articolo = "articolo rivista";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, dir.Descrizione_interna_id
	FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_interna_has_riferimento dir
	WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = '$articolo' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '$search' AND dir.riferimento_id = r.id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$numero_fascicolo = $row['numero_fascicolo'];
			$nome_rivista = $row['nome_rivista'];
			$autore_nome_cognome = $row['autore_nome_cognome'];
			$desc_int = $row['Descrizione_interna_id'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $numero_fascicolo ,$nome_rivista ,$autore_nome_cognome, $desc_int);
		
		}
	}

return $data;

}


////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEGLI ARTICOLI DI MISCELLANEA DELLA BIBLIOGRAFIA INTERNA


function biblio_int_articolo_miscellanea($search, $con){

	$miscellanea = "articolo miscellanea";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, dir.Descrizione_interna_id
	FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, descrizione_interna_has_riferimento dir, articolo_miscellanea am, libro l
	WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = '$miscellanea' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '$search' AND dir.riferimento_id = r.id AND am.libro_riferimento_id = l.riferimento_id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$curatore_nome_cognome = $row['curatore_nome_cognome'];
			$autore_nome_cognome = $row['autore_nome_cognome'];
			$desc_int = $row['Descrizione_interna_id'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $curatore_nome_cognome, $autore_nome_cognome, $desc_int);
		
		}
	}

return $data;

}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEI LIBRI DI MISCELLANEA DELLA BIBLIOGRAFIA INTERNA

function biblio_int_libro_miscellanea($search, $con){

	$libro = "libro";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, dir.Descrizione_interna_id
		FROM libro l, riferimento r, libro_has_autore c, descrizione_interna_has_riferimento dir
		WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = '$libro' AND dir.Descrizione_interna_Descrizione_Esterna_Segnatura = '$search' AND dir.riferimento_id = r.id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$citta = $row['citta'];	
			$casa_editrice  = $row['casa_editrice'];	
			$collana = $row['collana'];	
			$n_collana = $row['n_collana'];
			$curatore_nome_cognome = $row['curatore_nome_cognome'];
			$desc_int = $row['Descrizione_interna_id'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $citta, $casa_editrice, $collana, $n_collana, $curatore_nome_cognome, $desc_int);
		
		}
	}

return $data;

}

////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                //
//                                      BIBLIOGRAFIA ESTERNA                                      //
//                                                                                                //
////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEI LIBRI DELLA BIBLIOGRAFIA ESTERNA

function biblio_est_libro($search, $con){

	$libro = "libro";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura
		FROM libro l, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der
		WHERE a.riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = '$libro' AND der.Descrizione_Esterna_Segnatura = '$search' AND der.riferimento_id = r.id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$citta = $row['citta'];	
			$casa_editrice  = $row['casa_editrice'];	
			$collana = $row['collana'];	
			$n_collana = $row['n_collana'];
			$autore_nome_cognome = $row['autore_nome_cognome'];
			$desc_est = $row['Descrizione_Esterna_Segnatura'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $citta, $casa_editrice, $collana, $n_collana, $autore_nome_cognome, $desc_est);
		
		}
	}

return $data;

}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEGLI ARTICOLI DI RIVISTA DELLA BIBLIOGRAFIA ESTERNA

function biblio_est_articolo_rivista($search, $con){

	$articolo = "articolo rivista";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, ar.numero_fascicolo, ar.nome_rivista, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura
		FROM articolo_rivista ar, riferimento r, autore_has_riferimento a, descrizione_esterna_has_riferimento der
		WHERE a.riferimento_id = r.id AND r.id = ar.riferimento_id AND r.tipo = '$articolo' AND der.Descrizione_Esterna_Segnatura = '$search' AND der.riferimento_id = r.id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$numero_fascicolo = $row['numero_fascicolo'];
			$nome_rivista = $row['nome_rivista'];
			$autore_nome_cognome = $row['autore_nome_cognome'];
			$desc_est = $row['Descrizione_Esterna_Segnatura'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $numero_fascicolo ,$nome_rivista ,$autore_nome_cognome, $desc_est);
		
		}
	}

return $data;

}

////////////////////////////////////////////////////////////////////////////////////////////////////

// QUERY PER IL RECUPERO DEGLI ARTICOLI DI MISCELLANEA DELLA BIBLIOGRAFIA INTERNA


function biblio_est_articolo_miscellanea($search, $con){

	$miscellanea = "articolo miscellanea";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, c.curatore_nome_cognome, a.autore_nome_cognome, der.Descrizione_Esterna_Segnatura
	FROM  riferimento r, autore_has_riferimento a, libro_has_autore c, articolo_miscellanea am, libro l, descrizione_esterna_has_riferimento der
	WHERE a.riferimento_id = r.id AND am.riferimento_id = r.id AND r.tipo = '$miscellanea' AND am.libro_riferimento_id = l.riferimento_id AND der.Descrizione_Esterna_Segnatura = '$search' AND der.riferimento_id = r.id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$curatore_nome_cognome = $row['curatore_nome_cognome'];
			$autore_nome_cognome = $row['autore_nome_cognome'];
			$desc_est = $row['Descrizione_Esterna_Segnatura'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $curatore_nome_cognome, $autore_nome_cognome, $desc_est);
		
		}
	}

return $data;

}


// QUERY PER IL RECUPERO DEI LIBRI DI MISCELLANEA DELLA BIBLIOGRAFIA ESTERNA

function biblio_est_libro_miscellanea($search, $con){

	$libro = "libro";

	$result = mysqli_query($con, "Select r.id, r.titolo, r.anno, r.numero_pagine, l.citta, l.casa_editrice, l.collana, l.n_collana, c.curatore_nome_cognome, der.Descrizione_Esterna_Segnatura
		FROM libro l, riferimento r, libro_has_autore c, descrizione_esterna_has_riferimento der
		WHERE c.libro_riferimento_id = r.id AND r.id = l.riferimento_id AND r.tipo = '$libro' AND der.Descrizione_Esterna_Segnatura = '$search' AND der.riferimento_id = r.id;");

	$num_rows = mysqli_num_rows($result);

   	$data = array(); 

   	if($num_rows > 0){

		//creo l'associazione con gli elementi del record
		while ($row = mysqli_fetch_assoc($result)){

			$id = $row['id'];
			$titolo = $row['titolo'];
			$anno = $row['anno'];
			$numero_pagine = $row['numero_pagine'];
			$citta = $row['citta'];	
			$casa_editrice  = $row['casa_editrice'];	
			$collana = $row['collana'];	
			$n_collana = $row['n_collana'];
			$curatore_nome_cognome = $row['curatore_nome_cognome'];
			$desc_est = $row['Descrizione_Esterna_Segnatura'];

			array_push($data, $id, $titolo, $anno, $numero_pagine, $citta, $casa_editrice, $collana, $n_collana, $curatore_nome_cognome, $desc_est);
		
		}
	}

return $data;

}


?>
-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Creato il: Ott 21, 2020 alle 13:09
-- Versione del server: 5.7.26
-- Versione PHP: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `capitolare`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `articolo_miscellanea`
--

DROP TABLE IF EXISTS `articolo_miscellanea`;
CREATE TABLE IF NOT EXISTS `articolo_miscellanea` (
  `riferimento_id` int(11) NOT NULL,
  `libro_riferimento_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`riferimento_id`),
  KEY `libro_riferimento_id` (`libro_riferimento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `articolo_miscellanea`
--

INSERT INTO `articolo_miscellanea` (`riferimento_id`, `libro_riferimento_id`) VALUES
(31, 30);

-- --------------------------------------------------------

--
-- Struttura della tabella `articolo_rivista`
--

DROP TABLE IF EXISTS `articolo_rivista`;
CREATE TABLE IF NOT EXISTS `articolo_rivista` (
  `numero_fascicolo` varchar(100) NOT NULL,
  `nome_rivista` varchar(100) NOT NULL,
  `riferimento_id` int(11) NOT NULL,
  PRIMARY KEY (`riferimento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `articolo_rivista`
--

INSERT INTO `articolo_rivista` (`numero_fascicolo`, `nome_rivista`, `riferimento_id`) VALUES
('18', 'Antiquite Tardive', 32);

-- --------------------------------------------------------

--
-- Struttura della tabella `autore`
--

DROP TABLE IF EXISTS `autore`;
CREATE TABLE IF NOT EXISTS `autore` (
  `nome_cognome` varchar(100) NOT NULL,
  PRIMARY KEY (`nome_cognome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `autore`
--

INSERT INTO `autore` (`nome_cognome`) VALUES
('E. Colombi'),
('G. Cavallo'),
('M.B Parkes'),
('O. Pecere, F. Ronconi'),
('Sancti Aurelii Augustini');

-- --------------------------------------------------------

--
-- Struttura della tabella `autore_has_riferimento`
--

DROP TABLE IF EXISTS `autore_has_riferimento`;
CREATE TABLE IF NOT EXISTS `autore_has_riferimento` (
  `autore_nome_cognome` varchar(100) NOT NULL,
  `riferimento_id` int(11) NOT NULL,
  PRIMARY KEY (`autore_nome_cognome`,`riferimento_id`),
  KEY `fk_autore_has_riferimento_riferimento1_idx` (`riferimento_id`),
  KEY `fk_autore_has_riferimento_autore1_idx` (`autore_nome_cognome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `autore_has_riferimento`
--

INSERT INTO `autore_has_riferimento` (`autore_nome_cognome`, `riferimento_id`) VALUES
('Sancti Aurelii Augustini', 29),
('G. Cavallo', 31),
('O. Pecere, F. Ronconi', 32),
('M.B Parkes', 33);

-- --------------------------------------------------------

--
-- Struttura della tabella `descrizione_esterna`
--

DROP TABLE IF EXISTS `descrizione_esterna`;
CREATE TABLE IF NOT EXISTS `descrizione_esterna` (
  `Segnatura` varchar(100) NOT NULL,
  `datazione` varchar(100) NOT NULL,
  `tipo_di_supporto_e_qualita` varchar(100) NOT NULL,
  `consistenza` varchar(100) NOT NULL,
  `numerazione_carte` varchar(100) NOT NULL,
  `carte_di_guardia` varchar(100) NOT NULL,
  `prospetto_fascicolazione` varchar(100) NOT NULL,
  `arrangiamento_fogli_gregory` varchar(100) NOT NULL,
  `dimensioni` varchar(100) NOT NULL,
  `rigatura` varchar(100) NOT NULL,
  `foratura` varchar(100) DEFAULT NULL,
  `legatura` varchar(100) NOT NULL,
  `utenti_email` varchar(45) NOT NULL,
  `Descrizione_Esterna_Segnatura` varchar(100) NOT NULL,
  PRIMARY KEY (`Segnatura`),
  KEY `fk_Descrizione_Esterna_utenti1_idx` (`utenti_email`),
  KEY `fk_Descrizione_Esterna_Descrizione_Esterna1_idx` (`Descrizione_Esterna_Segnatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `descrizione_esterna`
--

INSERT INTO `descrizione_esterna` (`Segnatura`, `datazione`, `tipo_di_supporto_e_qualita`, `consistenza`, `numerazione_carte`, `carte_di_guardia`, `prospetto_fascicolazione`, `arrangiamento_fogli_gregory`, `dimensioni`, `rigatura`, `foratura`, `legatura`, `utenti_email`, `Descrizione_Esterna_Segnatura`) VALUES
('XXVIII (26)', 'Sec. V med.', 'membranaceo', 'cc. II, 254, I', 'numeri arabici, sec. XX, matita, porzione esterna margine sup. del recto di ciascuna carta', 'cartacee, inserite nel corso del rifacimento della legatura', 'no', 'inizio fascicoli lato carne; rispettata la regola', '286x185 (c. 87) = 35 [197] 54 x 15 [117] 53', 'Eseguita a secco con incisione su fascicolo aperto e composto', 'No', 'Di restauro in pergamena su asse in cartone', 'donatella.tronca@outlook.com', 'XXVIII (26)');

-- --------------------------------------------------------

--
-- Struttura della tabella `descrizione_esterna_has_riferimento`
--

DROP TABLE IF EXISTS `descrizione_esterna_has_riferimento`;
CREATE TABLE IF NOT EXISTS `descrizione_esterna_has_riferimento` (
  `Descrizione_Esterna_Segnatura` varchar(100) NOT NULL,
  `riferimento_id` int(11) NOT NULL,
  PRIMARY KEY (`Descrizione_Esterna_Segnatura`,`riferimento_id`),
  KEY `fk_Descrizione_Esterna_has_riferimento_riferimento1_idx` (`riferimento_id`),
  KEY `fk_Descrizione_Esterna_has_riferimento_Descrizione_Esterna1_idx` (`Descrizione_Esterna_Segnatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `descrizione_esterna_has_riferimento`
--

INSERT INTO `descrizione_esterna_has_riferimento` (`Descrizione_Esterna_Segnatura`, `riferimento_id`) VALUES
('XXVIII (26)', 30),
('XXVIII (26)', 31),
('XXVIII (26)', 32),
('XXVIII (26)', 33);

-- --------------------------------------------------------

--
-- Struttura della tabella `descrizione_interna`
--

DROP TABLE IF EXISTS `descrizione_interna`;
CREATE TABLE IF NOT EXISTS `descrizione_interna` (
  `autore` varchar(50) NOT NULL,
  `titolo` varchar(100) NOT NULL,
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `incipit` varchar(100) NOT NULL,
  `explicit` varchar(100) NOT NULL,
  `carte` varchar(100) NOT NULL,
  `rubrica` varchar(100) NOT NULL,
  `Descrizione_Esterna_Segnatura` varchar(100) NOT NULL,
  `Descrizione_interna_id` int(10) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`id`,`autore`,`titolo`,`Descrizione_Esterna_Segnatura`),
  KEY `fk_Descrizione_interna_Descrizione_Esterna1_idx` (`Descrizione_Esterna_Segnatura`),
  KEY `fk_Descrizione_interna_Descrizione_interna1_idx` (`Descrizione_interna_id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8 ROW_FORMAT=REDUNDANT;

--
-- Dump dei dati per la tabella `descrizione_interna`
--

INSERT INTO `descrizione_interna` (`autore`, `titolo`, `id`, `incipit`, `explicit`, `carte`, `rubrica`, `Descrizione_Esterna_Segnatura`, `Descrizione_interna_id`) VALUES
('Sancti Aurelii Augustini', 'De Civitate Dei', 102, 'incipit', 'explicit', '1r-251v', '1v Incipit capitulalibri xi de civitate dei', 'XXVIII (26)', NULL),
('Sancti Aurelii Augustini', 'De Civitate Dei', 103, 'incipit', 'explicit', '1v-2v', '1v Incipit capitulalibri xi de civitate dei', 'XXVIII (26)', 102);

-- --------------------------------------------------------

--
-- Struttura della tabella `descrizione_interna_has_riferimento`
--

DROP TABLE IF EXISTS `descrizione_interna_has_riferimento`;
CREATE TABLE IF NOT EXISTS `descrizione_interna_has_riferimento` (
  `Descrizione_interna_id` int(10) UNSIGNED NOT NULL,
  `Descrizione_interna_Descrizione_Esterna_Segnatura` varchar(100) NOT NULL,
  `riferimento_id` int(11) NOT NULL,
  PRIMARY KEY (`Descrizione_interna_id`,`Descrizione_interna_Descrizione_Esterna_Segnatura`,`riferimento_id`),
  KEY `fk_Descrizione_interna_has_riferimento_riferimento1_idx` (`riferimento_id`),
  KEY `fk_Descrizione_interna_has_riferimento_Descrizione_interna1_idx` (`Descrizione_interna_id`,`Descrizione_interna_Descrizione_Esterna_Segnatura`),
  KEY `Descrizione_interna_id` (`Descrizione_interna_id`,`Descrizione_interna_Descrizione_Esterna_Segnatura`,`riferimento_id`),
  KEY `Descrizione_interna_id_2` (`Descrizione_interna_id`,`Descrizione_interna_Descrizione_Esterna_Segnatura`,`riferimento_id`),
  KEY `Descrizione_interna_id_3` (`Descrizione_interna_id`,`Descrizione_interna_Descrizione_Esterna_Segnatura`,`riferimento_id`),
  KEY `descrizione_interna_has_riferimento_ibfk_2` (`Descrizione_interna_Descrizione_Esterna_Segnatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `descrizione_interna_has_riferimento`
--

INSERT INTO `descrizione_interna_has_riferimento` (`Descrizione_interna_id`, `Descrizione_interna_Descrizione_Esterna_Segnatura`, `riferimento_id`) VALUES
(102, 'XXVIII (26)', 29);

-- --------------------------------------------------------

--
-- Struttura della tabella `libro`
--

DROP TABLE IF EXISTS `libro`;
CREATE TABLE IF NOT EXISTS `libro` (
  `citta` varchar(100) NOT NULL,
  `casa_editrice` varchar(100) NOT NULL,
  `collana` varchar(100) NOT NULL,
  `n_collana` varchar(100) NOT NULL,
  `riferimento_id` int(11) NOT NULL,
  PRIMARY KEY (`riferimento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `libro`
--

INSERT INTO `libro` (`citta`, `casa_editrice`, `collana`, `n_collana`, `riferimento_id`) VALUES
('Turnhout', 'B. Dombart - A Kalb', 'CCSL', 'XLVII-XLVIII', 29),
('Turnhout', '', '', '', 30),
('Aldershot', '', '', '', 33);

-- --------------------------------------------------------

--
-- Struttura della tabella `libro_has_autore`
--

DROP TABLE IF EXISTS `libro_has_autore`;
CREATE TABLE IF NOT EXISTS `libro_has_autore` (
  `libro_riferimento_id` int(11) NOT NULL,
  `curatore_nome_cognome` varchar(100) NOT NULL,
  PRIMARY KEY (`libro_riferimento_id`,`curatore_nome_cognome`),
  KEY `fk_libro_has_autore_autore1_idx` (`curatore_nome_cognome`),
  KEY `fk_libro_has_autore_libro1_idx` (`libro_riferimento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `libro_has_autore`
--

INSERT INTO `libro_has_autore` (`libro_riferimento_id`, `curatore_nome_cognome`) VALUES
(30, 'E. Colombi');

-- --------------------------------------------------------

--
-- Struttura della tabella `mano_copista`
--

DROP TABLE IF EXISTS `mano_copista`;
CREATE TABLE IF NOT EXISTS `mano_copista` (
  `id` char(10) NOT NULL DEFAULT '',
  `intervallo_carte` varchar(200) DEFAULT NULL,
  `datazione` varchar(100) DEFAULT NULL,
  `tipologia_scrittura` varchar(500) DEFAULT NULL,
  `Descrizione_Esterna_Segnatura` varchar(100) NOT NULL,
  PRIMARY KEY (`id`,`Descrizione_Esterna_Segnatura`),
  KEY `fk_Mano_copista_Descrizione_Esterna_idx` (`Descrizione_Esterna_Segnatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `mano_copista`
--

INSERT INTO `mano_copista` (`id`, `intervallo_carte`, `datazione`, `tipologia_scrittura`, `Descrizione_Esterna_Segnatura`) VALUES
('A', '1v-6r,102r,248br', '', 'minuscola carolina secondo la tipizzazione veronese', 'XXVIII (26)'),
('B', '7r-101v,103r-251v', '', 'onciale old style', 'XXVIII (26)'),
('C', '252v', '', 'minuscola carolina della metà del secolo xi', 'XXVIII (26)');

-- --------------------------------------------------------

--
-- Struttura della tabella `riferimento`
--

DROP TABLE IF EXISTS `riferimento`;
CREATE TABLE IF NOT EXISTS `riferimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL,
  `titolo` varchar(1000) NOT NULL,
  `anno` varchar(100) DEFAULT NULL,
  `numero_pagine` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `riferimento`
--

INSERT INTO `riferimento` (`id`, `tipo`, `titolo`, `anno`, `numero_pagine`) VALUES
(29, 'libro', 'De Civitate Dei', '1955', ''),
(30, 'libro', 'La trasmissione dei testi patristici latini', '2012', ''),
(31, 'articolo miscellanea', 'I fondamenti materiali', '', '63'),
(32, 'articolo rivista', 'Le opere dei Padri della Chiesa tra produzione e ricezione', '2010', '83'),
(33, 'libro', 'Their hands before our eyes: a closer look at scribes', '2008', '129');

-- --------------------------------------------------------

--
-- Struttura della tabella `storia_del_manoscritto`
--

DROP TABLE IF EXISTS `storia_del_manoscritto`;
CREATE TABLE IF NOT EXISTS `storia_del_manoscritto` (
  `Id_auto_inc` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `Id` char(10) DEFAULT NULL,
  `intervallo_carte` varchar(1000) DEFAULT NULL,
  `Datazione` varchar(100) DEFAULT NULL,
  `Contenuto` varchar(500) DEFAULT NULL,
  `Posizione` varchar(1000) DEFAULT NULL,
  `Tipologia_scrittura` varchar(500) DEFAULT NULL,
  `Descrizione_Esterna_Segnatura` varchar(100) NOT NULL,
  PRIMARY KEY (`Id_auto_inc`,`Descrizione_Esterna_Segnatura`),
  KEY `fk_Storia_del_Manoscritto_Descrizione_Esterna1_idx` (`Descrizione_Esterna_Segnatura`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `storia_del_manoscritto`
--

INSERT INTO `storia_del_manoscritto` (`Id_auto_inc`, `Id`, `intervallo_carte`, `Datazione`, `Contenuto`, `Posizione`, `Tipologia_scrittura`, `Descrizione_Esterna_Segnatura`) VALUES
(1, 'a', '8v', '', '', 'c. 8v', '', 'XXVIII (26)'),
(2, 'b', '9rv, 12rv, 13r, 14r, 16rv, 17r, 22v, 23rv, 24rv, 28r, 29v, 30v, 31rv, 32rv, 33r, 37v, 39v, 40rv, 41rv, 42rv, 43v,45v, 52r, 54r, 60r, 61rv, 63v, 77rv, 79rv, 80rv, 81rv, 82r, 83rv, 84rv, 85r, 86v, 87rv, 88r, 89v, 100v, 101r, 105rv, 106rv, 107v, 113rv, 114rv, 115v, 116r, 117rv, 118rv, 119rv, 120v, 123v, 124r, 125r, 127rv, 128rv, 129rv, 130rv, 131rv, 132rv, 133rv, 134r, 135v, 136rv, 137rv, 138r, 139r, 140v, 141rv, 142rv, 147v, 148r, 149rv, 151v, 153v, 154rv, 155rv, 156rv, 157r, 161r, 164v, 165r, 167r, 169v, 170rv, 174r, 177r, 178v, 179r, 181r, 183v, 184rv, 185v, 186r, 187rv, 188v, 189r, 190r, 191rv, 192rv, 193r, 194r, 195rv, 198rv, 199rv, 200rv, 201rv, 202v, 206v, 207v, 208r, 229r, 230v, 231r, 232rv, 233rv, 234r, 238r', '', '', 'cc. 9rv, 12rv, 13r, ecc', 'minusicola carolina con ancora alcuni elementi corsivi del secolo ix', 'XXVIII (26)'),
(3, 'c', NULL, '', '', 'cc. 29r, 78v', '', 'XXVIII (26)'),
(4, 'd', NULL, '', '', 'c. 30v', '', 'XXVIII (26)'),
(5, 'e', NULL, '', '', 'cc. 37v, 38rv, 39rv', '', 'XXVIII (26)'),
(6, 'f', NULL, '', '', 'cc. 143, 186v', '', 'XXVIII (26)'),
(7, 'g', NULL, '', '', 'cc. 161v, 207r', 'minuscola cancelleresca del secolo xiv', 'XXVIII (26)'),
(8, 'h', NULL, '', '', 'c. 186v', '', 'XXVIII (26)'),
(9, 'i', NULL, '', '', 'c. 230r', '', 'XXVIII (26)'),
(10, '', NULL, 'secolo xiv', 'Beati augustini de civitate dei libri vi. videlicet xj, xjj, xiij, xiiij, xv, xvj', 'c. 1r', 'littera textualis', 'XXVIII (26)'),
(11, '', NULL, 'secolo viii', 'Deridam quod poterit ante pec/ catum asque libidinis causa/filios proceare <sic>', 'c. 143v', 'corsiva nuova', 'XXVIII (26)'),
(12, '', NULL, 'secolo xi', 'Pietate tua nostrum quae sumus. domine', 'c. 252v', 'minuscola carolina ', 'XXVIII (26)');

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

DROP TABLE IF EXISTS `utenti`;
CREATE TABLE IF NOT EXISTS `utenti` (
  `email` varchar(45) NOT NULL,
  `psw` varchar(45) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `cognome` varchar(45) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`email`, `psw`, `nome`, `cognome`) VALUES
('alessandro.saletti@outlook.com', '123456', 'Alessandro', 'Saletti'),
('donatella.tronca@outlook.com', '987654', 'Donatella', 'Tronca'),
('massimiliano.bassetti@univr.it', 'max', 'Massimiliano', 'Bassetti'),
('paolo.pellegrini@univr.it', 'pelle', 'Paolo', 'Pellegrini');

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `articolo_miscellanea`
--
ALTER TABLE `articolo_miscellanea`
  ADD CONSTRAINT `articolo_miscellanea_ibfk_1` FOREIGN KEY (`libro_riferimento_id`) REFERENCES `libro` (`riferimento_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_articolo_miscellanea_riferimento1` FOREIGN KEY (`riferimento_id`) REFERENCES `riferimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `articolo_rivista`
--
ALTER TABLE `articolo_rivista`
  ADD CONSTRAINT `fk_articolo_rivista_riferimento1` FOREIGN KEY (`riferimento_id`) REFERENCES `riferimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `autore_has_riferimento`
--
ALTER TABLE `autore_has_riferimento`
  ADD CONSTRAINT `fk_autore_has_riferimento_autore1` FOREIGN KEY (`autore_nome_cognome`) REFERENCES `autore` (`nome_cognome`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_autore_has_riferimento_riferimento1` FOREIGN KEY (`riferimento_id`) REFERENCES `riferimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `descrizione_esterna`
--
ALTER TABLE `descrizione_esterna`
  ADD CONSTRAINT `fk_Descrizione_Esterna_Descrizione_Esterna1` FOREIGN KEY (`Descrizione_Esterna_Segnatura`) REFERENCES `descrizione_esterna` (`Segnatura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Descrizione_Esterna_utenti1` FOREIGN KEY (`utenti_email`) REFERENCES `utenti` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `descrizione_esterna_has_riferimento`
--
ALTER TABLE `descrizione_esterna_has_riferimento`
  ADD CONSTRAINT `fk_Descrizione_Esterna_has_riferimento_Descrizione_Esterna1` FOREIGN KEY (`Descrizione_Esterna_Segnatura`) REFERENCES `descrizione_esterna` (`Segnatura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Descrizione_Esterna_has_riferimento_riferimento1` FOREIGN KEY (`riferimento_id`) REFERENCES `riferimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `descrizione_interna`
--
ALTER TABLE `descrizione_interna`
  ADD CONSTRAINT `fk_Descrizione_interna_Descrizione_Esterna1` FOREIGN KEY (`Descrizione_Esterna_Segnatura`) REFERENCES `descrizione_esterna` (`Segnatura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Descrizione_interna_Descrizione_interna1` FOREIGN KEY (`Descrizione_interna_id`) REFERENCES `descrizione_interna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `descrizione_interna_has_riferimento`
--
ALTER TABLE `descrizione_interna_has_riferimento`
  ADD CONSTRAINT `descrizione_interna_has_riferimento_ibfk_1` FOREIGN KEY (`Descrizione_interna_id`) REFERENCES `descrizione_interna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `descrizione_interna_has_riferimento_ibfk_2` FOREIGN KEY (`Descrizione_interna_Descrizione_Esterna_Segnatura`) REFERENCES `descrizione_interna` (`Descrizione_Esterna_Segnatura`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Descrizione_interna_has_riferimento_riferimento1` FOREIGN KEY (`riferimento_id`) REFERENCES `riferimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `libro`
--
ALTER TABLE `libro`
  ADD CONSTRAINT `fk_libro_riferimento1` FOREIGN KEY (`riferimento_id`) REFERENCES `riferimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `libro_has_autore`
--
ALTER TABLE `libro_has_autore`
  ADD CONSTRAINT `fk_libro_has_autore_autore1` FOREIGN KEY (`curatore_nome_cognome`) REFERENCES `autore` (`nome_cognome`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_libro_has_autore_libro1` FOREIGN KEY (`libro_riferimento_id`) REFERENCES `libro` (`riferimento_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limiti per la tabella `mano_copista`
--
ALTER TABLE `mano_copista`
  ADD CONSTRAINT `fk_Mano_copista_Descrizione_Esterna` FOREIGN KEY (`Descrizione_Esterna_Segnatura`) REFERENCES `descrizione_esterna` (`Segnatura`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limiti per la tabella `storia_del_manoscritto`
--
ALTER TABLE `storia_del_manoscritto`
  ADD CONSTRAINT `fk_Storia_del_Manoscritto_Descrizione_Esterna1` FOREIGN KEY (`Descrizione_Esterna_Segnatura`) REFERENCES `descrizione_esterna` (`Segnatura`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

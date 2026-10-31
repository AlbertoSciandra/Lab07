# Lab 07

#### Argomenti

- Utilizzo pacchetto `Flet` di Python (suggerita v1.0.4)
- Utilizzo Pattern MVC
- Utilizzo dei Package
- Utilizzo di mysql-connector-python (suggerita v8.4.0)
- Utilizzo del Pattern DAO

---
> **❗ ATTENZIONE:**
>  Ricordare di effettuare il **fork** del repository principale, quindi clonare su PyCharm il **repository personale**
> (https://github.com/my-github-username/Lab07) e non quello principale.
>
> In caso di dubbi consultare la guida caricata nel lab02:
> https://github.com/Programmazione-Avanzata-2026-27/Lab02/blob/main/Guida.pdf
>
> Per il setup del database (XAMPP, DBeaver e creazione del database tramite il file `biblioteche_torino.sql`) fare riferimento alla spiegazione del Lab06.
>

---

##  Gestione Biblioteche
Implementare un'applicazione per la gestione di un sistema bibliotecario. L'applicazione deve consentire di:
- Visualizzare i libri presenti in tutte le biblioteche
- Visualizzare i libri presenti in una specifica biblioteca
- Visualizzare i libri di uno specifico genere
- Visualizzare i libri di uno specifico genere in una specifica biblioteca

Fare uso del pattern MVC, utilizzando i pacchetti `flet` e `mysql-connector-python`. Interagire con il database tramite
l'uso pattern DAO, come spiegato a lezione.

### Implementazione
Realizzare un'interfaccia grafica con `flet` organizzata come segue, dall'alto verso il basso:
![layout.png](img/layout.png)

La proposta di interfaccia include:
- Titolo pagina ("Lab07") – già fatto ✅
- Pulsante per cambiare tema (default dark mode) utilizzando `Switch` – già fatto ✅
- **Sezione 1**: Intestazione Gestione Biblioteche - già fatto ✅
  - Un controllo `Text` con testo "Biblioteche di Torino".
- **Sezione 2**: Filtraggio - TODO 📝
  - Un controllo `Dropdown` per selezionare una biblioteca tra tutte quelle presenti nel database.
  - Un controllo `Dropdown` per selezionare un genere tra tutti quelli a cui appartengono i libri presenti nel
  database.
- **Sezione 3**: Lista Libri Filtrata - TODO 📝
  - Un controllo `Button` "Mostra Libri" per mostrare tutti i libri che soddisfano i criteri di
  filtraggio specificati sopra.
  - Un contenitore `ListView` da popolare con i libri che vengono letti dal database (in base al tipo di
  filtraggio indicato). Se nessun libro soddisfa i criteri di filtraggio indicati, il sistema risponderà con
  un alert.

### NOTA BENE
- Per popolare il menu a tendina tramite DropDown, occorre aggiungere alla sua lista `options` oggetti di
tipo `ft.dropdown.Option`.
Ad esempio:
    ```code
    self._view.elemento_dropdown.options.append(ft.dropdown.Option("Scelta 1"))
    ```
- Per reagire alla scelta dell'utente in un `Dropdown` si usa il parametro `on_select` (in Flet 1.0 non esiste più
`on_change` per questo controllo).
- Per risolvere l'esercizio è necessario filtrare i libri in base alle scelte effettuate dall'utente.
- Ogni menu a tendina deve includere anche l'opzione "Nessun filtro", che indica che il relativo filtro
(ad esempio per nome della biblioteca o per genere) non è attivo. Ciò si può gestire in due modi:
  1. Direttamente con una query SQL che tiene conto dei filtri opzionali.
  2. In Python, filtrando i dati dopo averli letti dal database.

  **Nel primo caso (i)**, è possibile utilizzare la funzione `SQL COALESCE()`, che restituisce il primo valore non nullo tra
  quelli passati come argomento. In questo modo, la query risulta valida sia quando l'utente seleziona un filtro,
  sia quando sceglie "Nessun filtro".

  Ad esempio:

     ```code
     WHERE genere = COALESCE(%s, genere)
     ```
  Se l'utente sceglie una opzione del dropdown, l'opzione viene usata per filtrare la lista di libri; se invece
  l'utente seleziona in uno specifico dropdown "nessun filtro", il campo viene confrontato con se stesso e la condizione
  risulta sempre vera.

  **Nel secondo caso (ii)** si possono leggere da SQL tutti i libri, e poi applicare i filtri in Python.
- Viene lasciata la libertà di utilizzare o meno l'**ORM** (Object Relational Mapping) spiegato a lezione, mediante,
ad esempio, una identity map, oppure considerando che gli oggetti del DTO tengano traccia delle relazioni.

---

## Materiale Fornito
Il repository del lab07 è organizzato con la struttura ad albero mostrata di seguito e contiene tutto il necessario per
svolgere il laboratorio:

```code
Lab07/
├── database/
│   ├── __init__.py
│   ├── biblioteca_DAO.py (DA MODIFICARE)
│   ├── connector.cnf
│   ├── DB_connect.py
│   └── libro_DAO.py (DA MODIFICARE)
│
├── model/
│   ├── __init__.py
│   ├── biblioteca_DTO.py
│   ├── libro_DTO.py
│   └── model.py (DA MODIFICARE)
│
├── UI/
│   ├── __init__.py
│   ├── alert.py
│   ├── controller.py (DA MODIFICARE)
│   └── view.py (DA MODIFICARE)
│
├── biblioteche_torino.sql (DA IMPORTARE CON DBeaver)
├── main.py (DA ESEGUIRE)
└── requirements.txt
 ```

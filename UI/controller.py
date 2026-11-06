import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self._biblioteca_selezionata = None
        self._genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))
        biblioteche = self._model.get_biblioteche()
        if biblioteche:
            for b in biblioteche:
                self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b), text=str(b)))

        self._view.dd_genere.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))
        generi = self._model.get_generi()
        if generi:
            for g in generi:
                self._view.dd_genere.options.append(ft.dropdown.Option(key=str(g), text=str(g)))

        self._view.update()

    # CALLBACKS DROPDOWN
    def handle_selezione_biblioteca(self, e):
        self._biblioteca_selezionata = e.control.value

    def handle_selezione_genere(self, e):
        self._genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        self._view.lv_libri.controls.clear()

        # Se l'utente seleziona "Nessun filtro", passiamo None alla query
        biblio = self._biblioteca_selezionata if self._biblioteca_selezionata and self._biblioteca_selezionata != "Nessun filtro" else None
        genere = self._genere_selezionato if self._genere_selezionato and self._genere_selezionato != "Nessun filtro" else None

        libri = self._model.get_libri_filtrati(biblio, genere)

        if not libri:
            self._view.show_alert("Nessun libro trovato con i criteri di filtraggio selezionati.")
            self._view.update()
            return

        for libro in libri:
            self._view.lv_libri.controls.append(ft.Text(str(libro)))

        self._view.update()

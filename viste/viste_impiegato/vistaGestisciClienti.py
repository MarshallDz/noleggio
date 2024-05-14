from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Attivita.prenotazione import Prenotazione
from Attivita.cliente import Cliente
import darkdetect


class VistaGestioneClienti(QMainWindow):
    def __init__(self, user, psw):
        super().__init__()

        self.user = user
        self.psw = psw

        self.setWindowTitle("CarGreen")
        self.setGeometry(0, 0, QApplication.desktop().width(), QApplication.desktop().height())
        if darkdetect.isDark():
            self.setStyleSheet("background-color: #121212;")
        self.showMaximized()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.central_layout = QVBoxLayout()

        title_layout = QVBoxLayout()
        title_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        self.central_widget.setLayout(self.central_layout)

        self.title_label = QLabel("Gestisci clienti")
        self.title_font = self.title_label.font()
        self.title_font.setPointSize(42)
        self.title_font.setBold(True)
        self.title_label.setFont(self.title_font)
        self.title_label.adjustSize()

        title_layout.addWidget(self.title_label)
        self.central_layout.addLayout(title_layout)
        # Aggiungi la barra di ricerca in alto a destra
        self.search_layout = QHBoxLayout()
        self.search_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)

        self.search_label = QLabel("Cerca per nome cliente:")
        self.search_layout.addWidget(self.search_label)

        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Inserisci il nome del cliente")
        self.search_layout.addWidget(self.search_edit)

        self.search_edit.textChanged.connect(self.search_cliente)

        self.central_layout.addLayout(self.search_layout)
        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("QScrollBar:vertical {"
                                  "    border: none;"
                                  "    border-radius: 5px;"
                                  "    background: #272626;"
                                  "    width: 10px;"  # Imposta la larghezza della barra di scorrimento
                                  "}"
                                  "QScrollBar::handle:vertical {"
                                  "    background: white;"  # Imposta il colore del cursore
                                  "    border-radius: 5px;"
                                  "    min-height: 20px;"  # Imposta l'altezza minima del cursore
                                  "}"
                                  "QScrollBar::add-line:vertical {"
                                  "    background: none;"
                                  "}"
                                  "QScrollBar::sub-line:vertical {"
                                  "    background: none;"
                                  "}")

        scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget(scroll_area)
        scroll_area.setWidget(self.scroll_content)
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        self.central_layout.addWidget(scroll_area)

        self.aggiungi_box_info()
        """#aggiungiPrenotazione_button = QPushButton("Aggiungi prenotazione")
        aggiungiPrenotazione_button.setStyleSheet("width: 150px; max-width: 150px; background-color: #6AFE67; border-radius: 15px; "
                                  "color: black; padding: 10px; margin-bottom: 20px")
        aggiungiPrenotazione_button.clicked.connect(self.go_aggiungiPrenotazione)
        self.central_layout.addWidget(aggiungiPrenotazione_button, alignment=Qt.AlignHCenter | Qt.AlignBottom)"""
        back_button = QPushButton("Indietro")
        back_button.clicked.connect(self.go_back)
        back_button.setStyleSheet("width: 150px; max-width: 150px; background-color: #F85959; border-radius: 15px; "
                                  "color: black; padding: 10px; margin-bottom: 20px")
        self.central_layout.addWidget(back_button, alignment=Qt.AlignHCenter | Qt.AlignBottom)

    def aggiungi_box_info(self):
        cliente = Cliente()
        clienti_info = cliente.get_dati()
        for client in clienti_info:
            info_box = QGroupBox(f"Informazioni sul cliente")
            info_box.setStyleSheet("QGroupBox{max-height: 200px;}")
            info_layout = QGridLayout(info_box)

            cF_label = QLabel("Codice Fiscale:")

            cF_label.setStyleSheet("font-size: 24px; ")
            info_layout.addWidget(cF_label, 1, 0)

            self.cf_edit = QLineEdit(client["codiceFiscale"])
            self.cf_edit.setEnabled(False)
            info_layout.addWidget(self.cf_edit, 1, 1)

            nome_label = QLabel("Nome cliente:")
            nome_label.setStyleSheet("font-size: 24px; ")
            info_layout.addWidget(nome_label, 2, 0)

            self.nome_edit = QLineEdit(client["nome"])
            self.nome_edit.setEnabled(False)
            info_layout.addWidget(self.nome_edit, 2, 1)

            cognome_label = QLabel("Cognome cliente:")
            cognome_label.setStyleSheet("font-size: 24px; ")
            info_layout.addWidget(cognome_label, 3, 0)

            self.cognome_edit = QLineEdit(client["cognome"])
            self.cognome_edit.setEnabled(False)
            info_layout.addWidget(self.cognome_edit, 3, 1)

            dataNascita_label = QLabel("Data di nascita cliente:")
            dataNascita_label.setStyleSheet("font-size: 24px; ")
            info_layout.addWidget(dataNascita_label, 1, 2)

            self.dataNascita_edit = QLineEdit(client["dataNascita"])
            self.dataNascita_edit.setEnabled(False)
            info_layout.addWidget(self.dataNascita_edit, 1, 3)

            email_label = QLabel("Email cliente:")
            email_label.setStyleSheet("font-size: 24px; ")
            info_layout.addWidget(email_label, 2, 2)

            self.email_edit = QLineEdit(client["email"])
            self.email_edit.setEnabled(False)
            info_layout.addWidget(self.email_edit, 2, 3)

            cellulare_label = QLabel("Cellulare cliente:")
            cellulare_label.setStyleSheet("font-size: 24px; ")
            info_layout.addWidget(cellulare_label, 3, 2)

            self.cellulare_edit = QLineEdit(client["cellulare"])
            self.cellulare_edit.setEnabled(False)
            info_layout.addWidget(self.cellulare_edit, 3, 3)

            buttons_layout = QHBoxLayout()
            info_layout.addLayout(buttons_layout, 4, 2, alignment=Qt.AlignRight)
            modify_button = QPushButton("Modifica")
            modify_button.setStyleSheet("width: 150px; max-width: 150px; background-color: #D9D9D9; border-radius: 15px; color: black; "
                           "padding: 10px;")
            modify_button.clicked.connect(
                lambda _, a=self.cf_edit, b=self.nome_edit, c=self.cognome_edit, d=self.dataNascita_edit,
                       e=self.email_edit, f=self.cellulare_edit, g=modify_button: self.modifica_valori_lineedit(a, b, c, d, e, f, g))

            buttons_layout.addWidget(modify_button)
            disdici = QPushButton("Elimina")
            #disdici.clicked.connect(lambda _, p=x: self.disdici(p))
            disdici.setStyleSheet("width: 150px; max-width: 150px; background-color: #F85959; border-radius: 15px; color: black; "
                                  "padding: 10px;")
            buttons_layout.addWidget(disdici)

            self.scroll_layout.addWidget(info_box)

    def go_back(self):
        self.close()
        from viste.viste_impiegato.pannelloControllo import VistaPannelloControllo
        self.vista = VistaPannelloControllo(self.user, self.psw)
        self.vista.show()

    def disdici(self, p):
        reply = QMessageBox.warning(self, 'Conferma Disdetta', 'Sei sicuro di voler disdire questa prenotazione?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            Prenotazione().eliminaPrenotazione(p)
        if reply == QMessageBox.Yes:
            QMessageBox.information(self, 'Disdetta Confermata', 'La prenotazione è stata disdetta con successo.', QMessageBox.Ok)
            self.go_back()

    def modifica_valori_lineedit(self, cF, nome, cognome, dataN, email, cellulare, modify_button):
        #bisogna aggiungere anche la modifica nel file prenotazioni.json
        if modify_button.text() == "Modifica":
            modify_button.setText("Salva")
            cF.setEnabled(True)
            nome.setEnabled(True)
            cognome.setEnabled(True)
            dataN.setEnabled(True)
            email.setEnabled(True)
            cellulare.setEnabled(True)
            # Salva i riferimenti ai campi QLineEdit
            self.cf = cF
            self.nome = nome
            self.cognome = cognome
            self.datan = dataN
            self.email = email
            self.cel = cellulare
        else:
            modify_button.setText("Modifica")
            cF.setEnabled(False)
            nome.setEnabled(False)
            cognome.setEnabled(False)
            dataN.setEnabled(False)
            email.setEnabled(False)
            cellulare.setEnabled(False)
            #self.salva_valori()"""


    """def go_aggiungiCliente(self):
        from viste.viste_impiegato.vistaEffettuaPrenotazioneImpiegato import VistaEffettuaPrenotazioneImpiegato
        self.vista = VistaEffettuaPrenotazioneImpiegato(self.user, self.psw)
        self.vista.show()
        self.close()"""

    def search_cliente(self, text):
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if isinstance(item, QLayoutItem):
                widget = item.widget()
                if isinstance(widget, QGroupBox):
                    cliente_labels = widget.findChildren(QLineEdit)
                    for label in cliente_labels:
                        client_name = label.text()
                        if text.lower() in client_name.lower():
                            widget.show()
                            break
                    else:
                        widget.hide()

    """def salva_valori(self):
        # Estrai i valori dai campi QLineEdit e memorizzali nelle variabili di istanza
        self.valore_data = self.modifica_data.date().toString(Qt.ISODate)
        self.valore_mezzo = self.modifica_mezzo.text()
        self.valore_tariffa = self.modifica_tariffa.currentText()
        self.valore_data_inizio = self.modifica_data_inizio.text()
        self.valore_data_fine = self.modifica_data_fine.text()
        self.valore_polizza = self.modifica_polizza.currentText()
        prenotazione = Prenotazione()
        prenotazione.aggiornaValori(self.nome_cliente, self.valore_data, self.valore_polizza, self.valore_data_inizio,
                                    self.valore_data_fine, self.valore_mezzo, self.valore_tariffa)"""


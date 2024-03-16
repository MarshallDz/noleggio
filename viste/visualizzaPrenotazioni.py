from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Attivita.prenotazione import *
from Attivita.cliente import Cliente
import darkdetect
import datetime

class PrenotazioniView(QMainWindow):
    def __init__(self, user, psw):
        super().__init__()

        self.user = user
        self.psw = psw

        self.setWindowTitle("Pagina prenotazioni cliente")
        self.setGeometry(0, 0, QApplication.desktop().width(), QApplication.desktop().height())
        if(darkdetect.isDark()):
            self.setStyleSheet("background-color: #121212;")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.central_layout = QVBoxLayout()

        title_layout = QVBoxLayout()
        title_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        self.central_widget.setLayout(self.central_layout)

        self.title_label = QLabel("Visualizza lista delle prenotazioni: ")
        self.title_font = self.title_label.font()
        self.title_font.setPointSize(42)
        self.title_font.setBold(True)
        self.title_label.setFont(self.title_font)
        self.title_label.adjustSize()

        title_layout.addWidget(self.title_label)
        self.central_layout.addLayout(title_layout)

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

        back_button = QPushButton("Indietro")
        back_button.clicked.connect(self.go_back)
        back_button.setStyleSheet("width: 150px; max-width: 150px; background-color: #F85959; border-radius: 15px; color: black; "
                                  "padding: 10px; margin-bottom: 20px")
        self.central_layout.addWidget(back_button, alignment=Qt.AlignHCenter | Qt.AlignBottom)

    def aggiungi_box_info(self):
        cliente = Cliente().get_cliente(self.user, self.psw)
        prenotazioniCliente = Cliente().get_prenotazione(cliente['codiceFiscale'])
        if len(prenotazioniCliente) == 0:
            label = QLabel("Non hai effettuato nessuna prenotazione")
            label.setStyleSheet("color: #F85959; border: 1px solid red; padding: 0px; max-height: 44px")
            label_font = label.font()
            label_font.setPointSize(42)
            label_font.setBold(True)
            label.setFont(label_font)
            self.scroll_layout.addWidget(label, alignment=Qt.AlignHCenter)
        else:
            for x in prenotazioniCliente:
                info_box = QGroupBox(f"Informazioni sulla prenotazione codice {x['id']}")
                info_box.setStyleSheet("QGroupBox{max-height: 200px;}")
                info_layout = QGridLayout(info_box)

                data_label = QLabel(f"data prenotazione: {x['data_prenotazione']} ")
                data_label.setStyleSheet("font-size: 24px; ")
                info_layout.addWidget(data_label, 1, 0)

                mezzo_label = QLabel(f"mezzo prenotato: {x['mezzo']['produttore']} {x['mezzo']['modello']}")
                mezzo_label.setStyleSheet("font-size: 24px; ")
                info_layout.addWidget(mezzo_label)

                tariffa_label = QLabel(f"tariffa selezionata: {x['tariffa']}")
                tariffa_label.setStyleSheet("font-size: 24px; ")
                info_layout.addWidget(tariffa_label)

                dataInizio_label = QLabel(f"data inizio prenotazione: {x['data_inizio']}")
                dataInizio_label.setStyleSheet("font-size: 24px; ")
                info_layout.addWidget(dataInizio_label, 1, 2)

                dataFine_label = QLabel(f"data fine prenotazione: {x['data_fine']}")
                dataFine_label.setStyleSheet("font-size: 24px; ")
                info_layout.addWidget(dataFine_label, 2, 2)

                polizza_label = QLabel(f"polizza selezionata: {x['polizza']}")
                polizza_label.setStyleSheet("font-size: 24px; ")
                info_layout.addWidget(polizza_label, 3, 2)

                disdici = QPushButton("Disdici")
                disdici.clicked.connect(lambda _, p=x: self.disdici(p))
                disdici.setStyleSheet("width: 150px; max-width: 150px; background-color: #F85959; border-radius: 15px; color: black; "
                                          "padding: 10px;")
                info_layout.addWidget(disdici, 4, 2, alignment= Qt.AlignRight)

                self.scroll_layout.addWidget(info_box)

    def go_back(self):
        self.close()

    def disdici(self, p):
        oggi = datetime.date.today()
        data_inizio = datetime.datetime.strptime(p["data_inizio"].split(" ")[0], "%Y-%m-%d").date()
        #posso disdire la prenotazione fino ad un giorno prima dell'inizio della prenotazione
        if data_inizio > oggi:
            reply = QMessageBox.warning(self, 'Conferma Disdetta', 'Sei sicuro di voler disdire questa prenotazione?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.prenotazione.eliminaPrenotazione(p)
            if reply == QMessageBox.Yes:
                QMessageBox.information(self, 'Disdetta Confermata', 'La prenotazione è stata disdetta con successo.', QMessageBox.Ok)
                self.close()
        else: QMessageBox.warning(self, 'Attenzione', 'Non puoi disdire questa prenotazione')
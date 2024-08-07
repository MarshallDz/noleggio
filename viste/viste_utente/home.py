from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from viste.viste_utente.areacliente import VistaCliente
from viste.viste_utente.vistaPrenotazione import VistaPrenotazione
from viste.viste_utente.visualizzaPrenotazioni import PrenotazioniView
from viste.viste_utente.vistaPagamenti import VistaPagamenti
from Attivita.cliente import Cliente
import darkdetect


class VistaHome(QMainWindow):
    def __init__(self, cliente):
        super().__init__()

        self.cliente = cliente

        self.setWindowTitle("CarGreen")
        self.setGeometry(0, 0, QApplication.desktop().width(), QApplication.desktop().height())
        if darkdetect.isDark():
            self.setStyleSheet("background-color: #121212;")
        self.showMaximized()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        form_layout = QHBoxLayout()
        self.central_widget.setLayout(form_layout)

        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        cliente_button = QPushButton("Area utente")
        cliente_button.setStyleSheet("max-width: 200px; border: none")
        cliente_button.setIcon(QIcon("viste/Icone/varie/boy.png"))
        cliente_button.setIconSize(QSize(50, 50))
        cliente_button.clicked.connect(self.area_clienti)
        left_layout.addWidget(cliente_button)
        form_layout.addLayout(left_layout)

        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignTop)

        self.title_label = QLabel(f"Benvenuto {self.cliente['nome']} {self.cliente['cognome']}")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_font = QFont("Arial", 42, QFont.Bold)
        self.title_label.setFont(self.title_font)
        self.title_label.adjustSize()
        center_layout.addWidget(self.title_label)

        options_layout = QVBoxLayout()
        button1 = QPushButton("Nuova prenotazione")
        button1.setStyleSheet(
            "width: 500px; height: 100px; color: black; background-color: #D9D9D9; border-radius: 25px; padding: 10px; "
            "margin-top: 100px; font-size: 20px;")
        button1.clicked.connect(self.go_prenotazione)

        button2 = QPushButton("Visualizza prenotazioni")
        button2.setStyleSheet(
            "width: 500px; height: 100px; background-color: #D9D9D9; border-radius: 25px; color: black; padding: "
            "10px; font-size: 20px")
        button2.clicked.connect(self.go_visualizza_prenotazioni)

        button3 = QPushButton("Visualizza pagamenti")
        button3.setStyleSheet(
            "width: 500px; height: 100px; background-color: #D9D9D9; border-radius: 25px; color: black; padding: "
            "10px; font-size: 20px")
        button3.clicked.connect(self.go_pagamenti)

        options_layout.addWidget(button1)
        options_layout.addWidget(button2)
        options_layout.addWidget(button3)
        options_layout.setSpacing(50)
        center_layout.addLayout(options_layout)
        form_layout.addLayout(center_layout)

        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        back_button = QPushButton("Esci")
        back_button.setStyleSheet("max-width: 200px; border: none")
        back_button.setIcon(QIcon("viste/Icone/varie/logout.png"))
        back_button.setIconSize(QSize(50, 50))
        back_button.clicked.connect(self.go_back)
        right_layout.addWidget(back_button)
        form_layout.addLayout(right_layout)

    def area_clienti(self):
        self.area = VistaCliente(self.cliente)
        self.area.show()
        self.close()

    def go_prenotazione(self):
        self.area = VistaPrenotazione(self.cliente)
        self.area.show()
        self.close()

    def go_visualizza_prenotazioni(self):
        self.vista = PrenotazioniView(self.cliente)
        self.vista.show()
        self.close()

    def go_pagamenti(self):
        self.vista = VistaPagamenti(self.cliente)
        self.vista.show()
        self.close()

    def go_back(self):
        from viste.login import VistaLogin
        self.vista = VistaLogin()
        self.vista.show()
        self.close()

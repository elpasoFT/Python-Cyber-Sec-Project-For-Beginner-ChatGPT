import socket
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("IP Address Bulucu")
        self.setGeometry(100, 100, 300, 200)

        self.centralwidget = QtWidgets.QWidget(self)

        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setGeometry(30, 30, 100, 20)
        self.ip_label.setText(" IP Adresin:")

        self.ip_text = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_text.setGeometry(130, 30, 150, 20)

        self.get_ip_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_ip_button.setGeometry(100, 70, 75, 23)
        self.get_ip_button.setText("BUL")
        self.get_ip_button.clicked.connect(self.get_ip)

        self.setCentralWidget(self.centralwidget)

    def get_ip(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        self.ip_text.setText(ip_address)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

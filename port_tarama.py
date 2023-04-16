import socket
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Port Tarama")
        self.setGeometry(100, 100, 300, 200)

        self.centralwidget = QtWidgets.QWidget(self)

        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setGeometry(30, 30, 60, 20)
        self.ip_label.setText("IP Address:")

        self.ip_text = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_text.setGeometry(100, 30, 150, 20)

        self.ip_text.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ip_text.customContextMenuRequested.connect(self.show_context_menu)

        self.scan_button = QtWidgets.QPushButton(self.centralwidget)
        self.scan_button.setGeometry(100, 70, 75, 23)
        self.scan_button.setText("Tara")
        self.scan_button.clicked.connect(self.port_scan)

        self.output_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output_text.setGeometry(30, 110, 240, 80)

        self.setCentralWidget(self.centralwidget)

    def port_scan(self):
        ip_address = self.ip_text.text()
        ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]
        output = ""

        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    output += "[+] Port " + str(port) + " is open\n"
                else:
                    output += "[-] Port " + str(port) + " is closed\n"
                sock.close()
            except:
                output += "[-] Error connecting to Port " + str(port) + "\n"

        self.output_text.setPlainText(output)

    def show_context_menu(self, position):
        menu = QtWidgets.QMenu()
        copy_action = menu.addAction("Copy")
        action = menu.exec_(self.ip_text.mapToGlobal(position))
        if action == copy_action:
            self.ip_text.copy()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

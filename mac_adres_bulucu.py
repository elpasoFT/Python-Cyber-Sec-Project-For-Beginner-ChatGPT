import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt
import psutil

class MacAddressFinder(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ağ Arayüzlerinin MAC Adresleri")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.add_mac_addresses()

    def add_mac_addresses(self):
        self.layout.addWidget(QLabel("Tüm ağ arayüzlerinin MAC adresleri:"))
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == psutil.AF_LINK:
                    label = QLabel(f"{interface}: {addr.address}")
                    label.setTextInteractionFlags(label.textInteractionFlags() | Qt.TextSelectableByMouse)
                    label.setCursor(Qt.IBeamCursor)
                    self.layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MacAddressFinder()
    window.show()
    sys.exit(app.exec_())

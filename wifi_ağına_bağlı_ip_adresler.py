import os
import platform
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from scapy.all import ARP, Ether, srp

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # arayüz bileşenlerini oluştur
        self.button = QPushButton('Ağı Tara', self)
        self.button.clicked.connect(self.find_devices)
        self.text_box = QTextEdit(self)

        # arayüz bileşenlerini konumlandır
        self.button.move(50, 50)
        self.text_box.move(50, 100)
        self.text_box.resize(400, 300)

        # pencere özelliklerini ayarla
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Ağdaki Cihazları Bul')

    def find_devices(self):
        # hedef IP adresi için ARP isteği oluştur
        arp = ARP(pdst="192.168.1.1/24")
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp

        # paketleri gönder ve yanıtları yakala
        result = srp(packet, timeout=3, verbose=0)[0]

        # yanıtların listesini yazdır
        clients = []
        for sent, received in result:
            clients.append({'ip': received.psrc, 'mac': received.hwsrc})

        # cihazları arayüzde göster
        self.text_box.clear()
        self.text_box.insertPlainText("Ağdaki cihazlar:\n")
        self.text_box.insertPlainText("IP Adresi\t\tMAC Adresi\n")
        for client in clients:
            self.text_box.insertPlainText(f"{client['ip']}\t\t{client['mac']}\n")

if __name__ == '__main__':
    # Scapy modüllerini yükle
    if platform.system() == "Windows":
        os.system("pip install --pre scapy[basic]")
    else:
        os.system("sudo apt-get install -y scapy")

    # uygulamayı başlat
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

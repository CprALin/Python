from PyQt5.QtWidgets import *

app = QApplication([])

app.setStyle('Fusion')

app.setStyleSheet("QPushButton {margin: 10ex; }")
button = QPushButton('Hello')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

button.clicked.connect(on_button_clicked)

button.show()

app.exec()
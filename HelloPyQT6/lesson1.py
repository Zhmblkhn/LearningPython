import sys
from tkinter import Button 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle("HI PyQt6")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        # COUNTER MODEL
        self.counter = 0
        label = QLabel("Counter: ", self)
        label.move(250, 100)
        self.label_counter = QLabel(str(self.counter), self)
        self.label_counter.move(300, 100)
        self.label_counter.setFixedWidth(30)
        button = QPushButton('Increase', self)
        button.move(250, 120)
        button.clicked.connect(self.intCounter)

        #INPUT MODEL
        self.counter_input = QLineEdit(self)
        self.counter_input.move(450, 100)
        save_button = QPushButton('Save', self)
        save_button.move(450, 125)
        save_button.clicked.connect(self.saveInput)

        # IMAGE MODEL
        text = QLabel('SALEM ALEM!', self)
        text.move(350, 60)
        image_source = 'HelloPyQT6\Cat.jpg'
        with open(image_source):
            image_label = QLabel(self)
            image_label.move(33, 150)
            image_pixmap = QPixmap(image_source)
            image_label.setPixmap(image_pixmap)

    def intCounter(self):
        self.counter += 1
        self.label_counter.setText(str(self.counter)) # Меняет содержимое в интерфейсе
    
    def saveInput(self):
        new_value = self.counter_input.text()
        self.label_counter.setText(new_value)
        self.counter = int(new_value)

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
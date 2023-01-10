'''
Created on Jan 4, 2023

@author: dsnyder
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("My GUI")
    
    layout = QVBoxLayout();
    
    label = QLabel("Press the Button Below")
    button = QPushButton("Press me!")
    
    button.clicked.connect(on_clicked)
    
    label = QLabel(window)
    label.setText("Hello World")
    label.setFont(QFont("Arial", 16))
    label.move(50, 100)
    
    window.show()
    app.exec_()
    
    def on_clicked
    
if __name__ == '__main__':
    main()
    
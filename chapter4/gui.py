"""Basic GUI example with PyQt."""
from PyQt4 import QtGui

class HelloWorld(QtGui.QWidget):
    def __init__(self):
        super(HelloWorld, self).__init__()
        # create the button
        self.button = QtGui.QPushButton('Click me', self)
        self.button.clicked.connect(self.clicked)
        # create the layout
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.button)
        self.setLayout(vbox)
        # show the window
        self.show()
        
    def clicked(self):
        msg = QtGui.QMessageBox(self)
        msg.setText("Hello World !")
        msg.show()
        
window = HelloWorld()

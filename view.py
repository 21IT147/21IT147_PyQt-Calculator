from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor

class GUI(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 400)

        # Set light blue color theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(230, 244, 255))  # Light blue background
        palette.setColor(QPalette.WindowText, Qt.black)  # Text color
        self.setPalette(palette)

        self.generalLayout = QVBoxLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplayLED()
        self._createButtons()

    def _createDisplayLED(self):
        """Create the display."""
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("QLineEdit { font-size: 24px; }")  
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        """Create the buttons."""
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            'C': (0, 4), '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '*': (1, 3), '(': (1, 4), '1': (2, 0), '2': (2, 1),
            '3': (2, 2), '-': (2, 3), ')': (2, 4), '0': (3, 0),
            '00': (3, 1), '.': (3, 2), '+': (3, 3), '=': (3, 4),
        }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(60, 60)
            self.buttons[btnText].setStyleSheet("QPushButton { font-size: 16px; }") 
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Set display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def getDisplayText(self):
        """Get display's text."""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display."""
        self.setDisplayText('')

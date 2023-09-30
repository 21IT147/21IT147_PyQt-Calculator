import sys


from PyQt5.QtWidgets import QApplication
from view import GUI
from Controller import Controller
from  model import evaluateExpression


def main():
    """Main function."""

    pycalc = QApplication(sys.argv)

    view = GUI()
    view.show()


    model = evaluateExpression
    Controller(model=model, view=view)


    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()
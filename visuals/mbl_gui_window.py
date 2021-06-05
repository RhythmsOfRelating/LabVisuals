from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication

from visuals.gui import Ui_MainWindow


class MBL_GuiWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        print("No signals implemented yet")# implement action connections






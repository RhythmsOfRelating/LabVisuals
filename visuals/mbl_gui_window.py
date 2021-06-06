from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from visuals.gui import Ui_MainWindow
from threading import Thread


class MBL_GuiWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        print("No signals implemented yet") # implement action connections

    def show_gui_threaded(self):
        self.thread = Thread(target=self.show())

    def stop_gui_thread(self):
        self.thread.join()


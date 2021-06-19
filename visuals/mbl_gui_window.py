from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QLabel
from visuals.gui import Ui_MainWindow
from threading import Thread


class MBL_GuiWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals_slots()

        # creating label
        self.head_label_a = QLabel(self)
        self.head_label_b = QLabel(self)

        # loading images
        self.pixmap_a = QPixmap('res\\headA_resized.png')
        self.pixmap_b = QPixmap('res\\headB_resized.png')

        # adding images to labels
        self.head_label_a.setPixmap(self.pixmap_a)
        self.head_label_b.setPixmap(self.pixmap_b)

        # Optional, resize label to image size
        self.head_label_a.resize(self.pixmap_a.width(), self.pixmap_a.height())
        self.head_label_b.resize(self.pixmap_b.width(), self.pixmap_b.height())

        #self.ui.CentralArea.addWidget(self.head_label_a)
        #self.ui.CentralArea.addWidget(self.head_label_b)

        self.head_label_a.move(300, 200)
        self.head_label_b.move(800, 200)

    def connect_signals_slots(self):
        print("No signals implemented yet")  # implement action connections

    def show_gui_threaded(self):
        self.thread = Thread(target=self.show())

    def stop_gui_thread(self):
        self.thread.join()


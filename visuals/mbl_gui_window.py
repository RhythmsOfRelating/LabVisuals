from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QLabel

from lsl.mbl_lsl_receiver import MBL_LSLReceiver
from visuals.gui import Ui_MainWindow
from threading import Thread


class MBL_GuiWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals_slots()
        self.receiver = MBL_LSLReceiver()
        self.receiver.start()

        # creating label
        self.head_label_a = QLabel(self)
        self.head_label_b = QLabel(self)

        # loading images
        self.pixmap_a = QPixmap('res\\headA_resized.png')
        self.pixmap_b = QPixmap('res\\headB_resized.png')

        # adding images to labels
        self.head_label_a.setPixmap(self.pixmap_a)
        self.head_label_b.setPixmap(self.pixmap_b)

        # Optional, resize label to image size and remove background
        self.head_label_a.resize(self.pixmap_a.width(), self.pixmap_a.height())
        self.head_label_b.resize(self.pixmap_b.width(), self.pixmap_b.height())
        self.head_label_a.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.head_label_b.setStyleSheet("background-color: rgba(255, 255, 255, 0)")


        #self.ui.CentralArea.addWidget(self.head_label_a)
        #self.ui.CentralArea.addWidget(self.head_label_b)

        self.head_label_a.move(300, 200)
        self.head_label_b.move(800, 200)

        # Update the interface every 0.5 seconds

        # make QTimer
        self.qTimer = QTimer()
        # set interval to 1 s
        self.qTimer.setInterval(500)  # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.update_head_position)
        # start timer
        self.qTimer.start()


    def connect_signals_slots(self):
        print("No signals implemented yet")  # implement action connections

    def show_gui_threaded(self):
        self.thread = Thread(target=self.show())

    def stop_gui_thread(self):
        self.thread.join()

    def update_head_position(self):
        if self.receiver.score > 0.9:
            self.head_label_a.move(500, 200)
            self.head_label_b.move(600, 200)
        elif self.receiver.score > 0.95:
            self.head_label_a.move(550, 200)
            self.head_label_b.move(550, 200)
        else:
            self.reset_head_position()

    def reset_head_position(self):
        self.head_label_a.move(300, 200)
        self.head_label_b.move(800, 200)

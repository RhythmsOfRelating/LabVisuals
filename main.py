import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QThread
from visuals.mbl_gui_window import MBL_GuiWindow
from lsl.mbl_lsl_receiver import MBL_LSLReceiver


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui_window = MBL_GuiWindow()

    receiver = MBL_LSLReceiver()
    receiver.start()
    gui_window.show()

    receiver.stop_listener()
    sys.exit(app.exec_())




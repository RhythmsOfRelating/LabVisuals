import sys

from PyQt5.QtWidgets import QApplication, QDialog
import time
# from mbl_osc_receiver import MBLOscReceiver

# osc_receiver = MBLOscReceiver("Rvalues")
# osc_receiver.initialize()
from gui import Ui_MainWindow
from lsl.mbl_lsl_receiver import MBLLSLReceiver


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    lsl_receiver = MBLLSLReceiver()
    lsl_receiver.resolve_streams()
    lsl_receiver.start_listener()
    time.sleep(10)
    # lsl_receiver.stop_listener()
    sys.exit(app.exec_())

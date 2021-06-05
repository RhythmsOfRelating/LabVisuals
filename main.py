import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QDialog
from visuals.mbl_gui_window import MBL_GuiWindow
from lsl.mbl_lsl_receiver import MBL_LSLReceiver


def receive_data_threaded(receiver):
    print("Thread started")
    receiver.resolve_streams()
    receiver.start_listener()
    time.sleep(10)
    receiver.stop_listener()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui_window = MBL_GuiWindow()
    lsl_receiver = MBL_LSLReceiver()
    gui_window.show()

    receiver_thread = threading.Thread(target=receive_data_threaded(lsl_receiver))
    receiver_thread.start()

    sys.exit(app.exec_())




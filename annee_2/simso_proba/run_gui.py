import simsogui
from PyQt5.QtWidgets import QApplication
import sys


simsogui.run_gui()
app = QApplication()
app.setOrganizationName("SimSo")
app.setApplicationName("SimSo")
sys.exit(app.exec_())
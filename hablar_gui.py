import sys
import cv2
from PyQt4 import QtGui, QtCore, Qt
from ui import Ui_MainWindow
from hablar import hablar_master, hablar_client

class Gui(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.start_button.clicked.connect(self.start_master)
		self.ui.connect_button.clicked.connect(self.start_client)
		self.ui.close_button.clicked.connect(self.close)
		self.CONNECTION_PORT = 1111
		self.update()

	def start_master(self):
		hablar_master(self.CONNECTION_PORT, self.ui.label)
		
	def start_client(self):
		ip = self.ui.ip.getText()
		hablar_client(ip, self.CONNECTION_PORT, self.ui.label)
		
	def close(self):
		sys.exit()
		
def main():
	app = QtGui.QApplication(sys.argv)
	ex = Gui()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
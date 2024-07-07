from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(
            open("resources/stylesheets/dark_theme.qss", "r").read())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tab widget setup
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 691, 461))
        self.tabWidget.setObjectName("tabWidget")

        # First tab setup
        self.tab1 = self.setup_tab1()
        self.tabWidget.addTab(self.tab1, "Vegetation Index - Altum")

        # Second tab setup
        self.tab2 = self.setup_tab2()
        self.tabWidget.addTab(self.tab2, "Raster Data Extraction")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

    def setup_tab1(self):
        tab = QtWidgets.QWidget()
        tab.setObjectName("tab1")

        self.label_2 = QtWidgets.QLabel(tab)
        self.label_2.setGeometry(QtCore.QRect(0, 140, 200, 16))
        self.label_2.setFont(QtGui.QFont("Arial", 10))
        self.label_2.setObjectName("label_2")

        self.btn_save = QtWidgets.QPushButton(tab)
        self.btn_save.setGeometry(QtCore.QRect(0, 165, 274, 31))
        self.btn_save.setFont(QtGui.QFont("Arial", 10))
        self.btn_save.setObjectName("btn_save")

        self.btn_select_location = QtWidgets.QPushButton(tab)
        self.btn_select_location.setGeometry(QtCore.QRect(0, 90, 274, 31))
        self.btn_select_location.setFont(QtGui.QFont("Arial", 10))
        self.btn_select_location.setObjectName("btn_select_location")

        self.label = QtWidgets.QLabel(tab)
        self.label.setGeometry(QtCore.QRect(0, 60, 230, 16))
        self.label.setFont(QtGui.QFont("Arial", 10))
        self.label.setObjectName("label")

        self.groupBox = QtWidgets.QGroupBox(tab)
        self.groupBox.setGeometry(QtCore.QRect(330, 50, 331, 361))
        self.groupBox.setFont(QtGui.QFont("Arial", 10))
        self.groupBox.setObjectName("groupBox")

        self.setup_group_buttons()

        self.label_3 = QtWidgets.QLabel(tab)
        self.label_3.setGeometry(QtCore.QRect(90, 0, 500, 20))
        self.label_3.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.label_3.setObjectName("label_3")

        self.btn_info = QtWidgets.QPushButton(tab)
        self.btn_info.setGeometry(QtCore.QRect(10, 310, 111, 61))
        self.btn_info.setFont(QtGui.QFont("Arial", 10))
        self.btn_info.setObjectName("btn_info")

        self.btn_exit = QtWidgets.QPushButton(tab)
        self.btn_exit.setGeometry(QtCore.QRect(150, 310, 111, 61))
        self.btn_exit.setFont(QtGui.QFont("Arial", 10))
        self.btn_exit.setObjectName("btn_exit")

        self.retranslate_tab1(tab)
        return tab

    def setup_group_buttons(self):
        self.btn_ndvi = QtWidgets.QPushButton(self.groupBox)
        self.btn_ndvi.setGeometry(QtCore.QRect(30, 40, 274, 31))
        self.btn_ndvi.setFont(QtGui.QFont("Arial", 10))
        self.btn_ndvi.setObjectName("btn_ndvi")

        self.btn_savi = QtWidgets.QPushButton(self.groupBox)
        self.btn_savi.setGeometry(QtCore.QRect(30, 90, 274, 31))
        self.btn_savi.setFont(QtGui.QFont("Arial", 10))
        self.btn_savi.setObjectName("btn_savi")

        self.btn_sr = QtWidgets.QPushButton(self.groupBox)
        self.btn_sr.setGeometry(QtCore.QRect(30, 140, 274, 31))
        self.btn_sr.setFont(QtGui.QFont("Arial", 10))
        self.btn_sr.setObjectName("btn_sr")

        self.btn_ndre = QtWidgets.QPushButton(self.groupBox)
        self.btn_ndre.setGeometry(QtCore.QRect(30, 190, 274, 31))
        self.btn_ndre.setFont(QtGui.QFont("Arial", 10))
        self.btn_ndre.setObjectName("btn_ndre")

        self.btn_gndvi = QtWidgets.QPushButton(self.groupBox)
        self.btn_gndvi.setGeometry(QtCore.QRect(30, 240, 274, 31))
        self.btn_gndvi.setFont(QtGui.QFont("Arial", 10))
        self.btn_gndvi.setObjectName("btn_gndvi")

        self.btn_evi = QtWidgets.QPushButton(self.groupBox)
        self.btn_evi.setGeometry(QtCore.QRect(30, 290, 274, 31))
        self.btn_evi.setFont(QtGui.QFont("Arial", 10))
        self.btn_evi.setObjectName("btn_evi")

    def setup_tab2(self):
        tab = QtWidgets.QWidget()
        tab.setObjectName("tab2")

        self.label_4 = QtWidgets.QLabel(tab)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 270, 16))
        self.label_4.setFont(QtGui.QFont("Arial", 10))
        self.label_4.setObjectName("label_4")

        self.btn_select_shp = QtWidgets.QPushButton(tab)
        self.btn_select_shp.setGeometry(QtCore.QRect(350, 10, 201, 41))
        self.btn_select_shp.setObjectName("btn_select_shp")

        self.label_5 = QtWidgets.QLabel(tab)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 300, 16))
        self.label_5.setFont(QtGui.QFont("Arial", 10))
        self.label_5.setObjectName("label_5")

        self.btn_select_folder = QtWidgets.QPushButton(tab)
        self.btn_select_folder.setGeometry(QtCore.QRect(350, 100, 201, 41))
        self.btn_select_folder.setObjectName("btn_select_folder")

        self.btn_start_process = QtWidgets.QPushButton(tab)
        self.btn_start_process.setGeometry(QtCore.QRect(100, 340, 201, 41))
        self.btn_start_process.setObjectName("btn_start_process")

        self.btn_exit_tab2 = QtWidgets.QPushButton(tab)
        self.btn_exit_tab2.setGeometry(QtCore.QRect(360, 340, 201, 41))
        self.btn_exit_tab2.setObjectName("btn_exit_tab2")

        self.retranslate_tab2(tab)
        return tab

    def retranslate_tab1(self, tab):
        _translate = QtCore.QCoreApplication.translate
        tab.setWindowTitle(_translate(
            "MainWindow", "Vegetation Index - Altum"))
        self.label_2.setText(_translate("MainWindow", "Select Save Location"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.btn_select_location.setText(
            _translate("MainWindow", "Select Location"))
        self.label.setText(_translate("MainWindow", "Select File Location"))
        self.groupBox.setTitle(_translate("MainWindow", "Vegetation Indices"))
        self.btn_ndvi.setText(_translate("MainWindow", "Calculate NDVI"))
        self.btn_savi.setText(_translate("MainWindow", "Calculate SAVI"))
        self.btn_sr.setText(_translate("MainWindow", "Calculate SR"))
        self.btn_ndre.setText(_translate("MainWindow", "Calculate NDRE"))
        self.btn_gndvi.setText(_translate("MainWindow", "Calculate GNDVI"))
        self.btn_evi.setText(_translate("MainWindow", "Calculate EVI"))
        self.label_3.setText(_translate(
            "MainWindow", "Micasense Altum Vegetation Index Calculator"))
        self.btn_info.setText(_translate("MainWindow", "Info"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))

    def retranslate_tab2(self, tab):
        _translate = QtCore.QCoreApplication.translate
        tab.setWindowTitle(_translate("MainWindow", "Raster Data Extraction"))
        self.label_4.setText(_translate(
            "MainWindow", "Select Shapefile Location"))
        self.btn_select_shp.setText(
            _translate("MainWindow", "Select Shapefile"))
        self.label_5.setText(_translate("MainWindow", "Select Image Folder"))
        self.btn_select_folder.setText(
            _translate("MainWindow", "Select Folder"))
        self.btn_start_process.setText(
            _translate("MainWindow", "Start Process"))
        self.btn_exit_tab2.setText(_translate("MainWindow", "Exit"))

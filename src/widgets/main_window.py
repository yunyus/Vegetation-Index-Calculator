from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui_mainwindow import Ui_MainWindow
from handlers.file_handler import FileHandler
from handlers.index_calculator import IndexCalculator
from handlers.zonal_statistics import ZonalStatistics
from utils.message_utils import show_info_message, show_error_message


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_handler = FileHandler()
        self.index_calculator = IndexCalculator()
        self.zonal_statistics = ZonalStatistics()

        self.setup_connections()

    def setup_connections(self):
        self.ui.btn_select_location.clicked.connect(
            self.file_handler.select_file_location)
        self.ui.btn_save.clicked.connect(self.file_handler.save_file)
        self.ui.btn_ndvi.clicked.connect(lambda: self.calculate_index("NDVI"))
        self.ui.btn_savi.clicked.connect(lambda: self.calculate_index("SAVI"))
        self.ui.btn_sr.clicked.connect(lambda: self.calculate_index("SR"))
        self.ui.btn_ndre.clicked.connect(lambda: self.calculate_index("NDRE"))
        self.ui.btn_gndvi.clicked.connect(
            lambda: self.calculate_index("GNDVI"))
        self.ui.btn_evi.clicked.connect(lambda: self.calculate_index("EVI"))
        self.ui.btn_info.clicked.connect(self.show_info)
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_select_shp.clicked.connect(
            self.file_handler.select_shapefile)
        self.ui.btn_select_folder.clicked.connect(
            self.file_handler.select_folder)
        self.ui.btn_start_process.clicked.connect(self.run_zonal_statistics)
        self.ui.btn_exit_tab2.clicked.connect(self.close)

    def calculate_index(self, index_type):
        try:
            path = self.file_handler.get_selected_file_path()
            save_location = self.file_handler.get_save_location()
            if not path or not save_location:
                raise ValueError("Path or Save location not set")
            self.index_calculator.calculate(index_type, path, save_location)
            show_info_message(
                "Success", f"{index_type} calculation completed!")
        except Exception as e:
            show_error_message("Error", str(e))

    def show_info(self):
        info_text = (
            "Program Usage Instructions:\n"
            "1. Click 'Select Location' to choose an image.\n"
            "2. Click 'Save' to choose the save directory.\n"
            "3. Calculate the desired vegetation index."
        )
        show_info_message("Program Usage", info_text)

    def run_zonal_statistics(self):
        try:
            shp_path = self.file_handler.get_selected_shapefile()
            img_folder = self.file_handler.get_selected_folder()
            if not shp_path or not img_folder:
                raise ValueError("Shapefile or Image folder not set")
            self.zonal_statistics.calculate(shp_path, img_folder)
            show_info_message(
                "Success", "Zonal statistics calculation completed!")
        except Exception as e:
            show_error_message("Error", str(e))

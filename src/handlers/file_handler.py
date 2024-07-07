from PyQt5.QtWidgets import QFileDialog


class FileHandler:
    def __init__(self):
        self.selected_file_path = None
        self.save_location = None
        self.selected_shapefile = None
        self.selected_folder = None

    def select_file_location(self):
        self.selected_file_path, _ = QFileDialog.getOpenFileName()
        return self.selected_file_path

    def save_file(self):
        self.save_location = QFileDialog.getExistingDirectory()
        return self.save_location

    def get_selected_file_path(self):
        return self.selected_file_path

    def get_save_location(self):
        return self.save_location

    def select_shapefile(self):
        self.selected_shapefile, _ = QFileDialog.getOpenFileName()
        return self.selected_shapefile

    def get_selected_shapefile(self):
        return self.selected_shapefile

    def select_folder(self):
        self.selected_folder = QFileDialog.getExistingDirectory()
        return self.selected_folder

    def get_selected_folder(self):
        return self.selected_folder

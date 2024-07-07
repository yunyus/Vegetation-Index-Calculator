import rasterio
import numpy as np
import os
from PyQt5.QtWidgets import QMessageBox


class IndexCalculator:
    def calculate(self, index_type, file_path, save_location):
        if index_type == "NDVI":
            self.calculate_ndvi(file_path, save_location)
        elif index_type == "SAVI":
            self.calculate_savi(file_path, save_location)
        elif index_type == "SR":
            self.calculate_sr(file_path, save_location)
        elif index_type == "NDRE":
            self.calculate_ndre(file_path, save_location)
        elif index_type == "GNDVI":
            self.calculate_gndvi(file_path, save_location)
        elif index_type == "EVI":
            self.calculate_evi(file_path, save_location)
        else:
            raise ValueError("Unknown index type")

    def calculate_ndvi(self, path, save_location):
        try:
            src = rasterio.open(path)
            b5 = src.read(5)
            b3 = src.read(3)
            ndvi = (b5 - b3) / (b5 + b3)
            ndvi = np.clip(ndvi, 0, 1)
            self.save_raster(ndvi, src, save_location, path, '_NDVI')
        except Exception as e:
            raise RuntimeError(f"Error calculating NDVI: {str(e)}")

    def calculate_savi(self, path, save_location):
        try:
            src = rasterio.open(path)
            b5 = src.read(5)
            b3 = src.read(3)
            savi = 1.1 * (b5 - b3) / (0.1 + b5 + b3)
            savi = np.clip(savi, 0, 1)
            self.save_raster(savi, src, save_location, path, '_SAVI')
        except Exception as e:
            raise RuntimeError(f"Error calculating SAVI: {str(e)}")

    def calculate_sr(self, path, save_location):
        try:
            src = rasterio.open(path)
            b5 = src.read(5)
            b3 = src.read(3)
            sr = b5 / b3
            sr = np.clip(sr, 0, None)
            self.save_raster(sr, src, save_location, path, '_SR')
        except Exception as e:
            raise RuntimeError(f"Error calculating SR: {str(e)}")

    def calculate_ndre(self, path, save_location):
        try:
            src = rasterio.open(path)
            b5 = src.read(5)
            b4 = src.read(4)
            ndre = (b5 - b4) / (b5 + b4)
            ndre = np.clip(ndre, 0, 1)
            self.save_raster(ndre, src, save_location, path, '_NDRE')
        except Exception as e:
            raise RuntimeError(f"Error calculating NDRE: {str(e)}")

    def calculate_gndvi(self, path, save_location):
        try:
            src = rasterio.open(path)
            b5 = src.read(5)
            b2 = src.read(2)
            gndvi = (b5 - b2) / (b5 + b2)
            gndvi = np.clip(gndvi, 0, 1)
            self.save_raster(gndvi, src, save_location, path, '_GNDVI')
        except Exception as e:
            raise RuntimeError(f"Error calculating GNDVI: {str(e)}")

    def calculate_evi(self, path, save_location):
        try:
            src = rasterio.open(path)
            b5 = src.read(5)
            b3 = src.read(3)
            b1 = src.read(1)
            evi = 2.5 * (b5 - b3) / (b5 + (6 * b3 - 7.5 * b1) + 1)
            evi = np.clip(evi, 0, 1)
            self.save_raster(evi, src, save_location, path, '_EVI')
        except Exception as e:
            raise RuntimeError(f"Error calculating EVI: {str(e)}")

    def save_raster(self, data, src, save_location, path, suffix):
        meta = src.meta
        meta.update(dtype=data.dtype, count=1)
        head, tail = os.path.split(path)
        save_path = os.path.join(save_location, f'{tail[:-4]}{suffix}.tif')
        with rasterio.open(save_path, 'w', **meta) as dst:
            dst.write(data, 1)

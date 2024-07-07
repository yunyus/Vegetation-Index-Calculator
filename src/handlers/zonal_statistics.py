import glob
import os
import pandas as pd
from rasterstats import zonal_stats


class ZonalStatistics:
    def calculate(self, shp_path, img_folder):
        try:
            image_files = glob.glob(os.path.join(img_folder, "*.tif"))
            for img_file in image_files:
                self.calculate_statistics(shp_path, img_file, img_folder)
            self.combine_statistics(img_folder)
        except Exception as e:
            raise RuntimeError(f"Error calculating zonal statistics: {str(e)}")

    def calculate_statistics(self, shp, img_file, folder):
        try:
            stats = zonal_stats(shp, img_file, stats="mean")
            df = pd.DataFrame(stats)
            head, tail = os.path.split(img_file)
            df.rename(columns={'mean': tail[:-4]}, inplace=True)
            df.to_csv(os.path.join(
                folder, f"{tail[:-4]}.txt"), sep="-", index=False)
        except Exception as e:
            raise RuntimeError(
                f"Error calculating statistics for {img_file}: {str(e)}")

    def combine_statistics(self, folder):
        try:
            txt_files = glob.glob(os.path.join(folder, "*.txt"))
            combined_csv = pd.concat([pd.read_csv(f, sep="-")
                                     for f in txt_files], axis=1)
            combined_csv.index += 1
            combined_csv.to_excel(os.path.join(
                folder, "combined_statistics.xlsx"), index=True, encoding="utf-8-sig")
            for txt_file in txt_files:
                os.remove(txt_file)
        except Exception as e:
            raise RuntimeError(f"Error combining statistics: {str(e)}")

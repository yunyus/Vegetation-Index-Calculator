# Vegetation Index Calculator

This is a PyQt5-based GUI application for calculating various vegetation indices from raster images and performing zonal statistics using shapefiles.

## Features

- Calculate various vegetation indices including NDVI, SAVI, SR, NDRE, GNDVI, and EVI.
- Perform zonal statistics on raster images using shapefiles.
- Save calculated indices and zonal statistics to specified locations.

## Installation

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Setup

1. Clone the repository:

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. Use the GUI to:
   - Select file locations and save directories.
   - Calculate vegetation indices.
   - Perform zonal statistics.

## File Structure

vegetation_index_calculator/
│
├── resources/
│ ├── icons/
│ │ ├── Altum.png
│ │ ├── Unlem.png
│ ├── stylesheets/
│ │ ├── dark_theme.qss
├── src/
│ ├── main.py
│ ├── ui_mainwindow.py
│ ├── handlers/
│ │ ├── file_handler.py
│ │ ├── index_calculator.py
│ │ ├── zonal_statistics.py
│ ├── utils/
│ │ ├── message_utils.py
│ ├── widgets/
│ │ ├── main_window.py
├── requirements.txt
└── README.md

## Dependencies

- PyQt5
- rasterio
- numpy
- pandas
- rasterstats
- shapely
- fake-useragent

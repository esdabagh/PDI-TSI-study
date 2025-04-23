# PDI-TSI Study Repository

This repository contains datasets and code for the study "A Simple Statistical Method for Assessing Trend Linearity and Separating Periodic Patterns in Time Series".

## Contents
- **Datasets**:
  - `noaa_temperature_2020_2021.csv`: Daily maximum temperatures in New York (Station USW00094728) from Jan 1, 2020 to Dec 31, 2021.
  - `usgs_seismic_2024.csv`: Hourly seismic amplitudes in Southern California (near Calexico, CA) from Jan 1 to Jan 31, 2024.
- **Code**:
  - `pdi_tsi.py`: Python implementation of the PDI and TSI indices for time series analysis.

## Usage
To use the code with the datasets:
1. Install Python and required libraries (`numpy`).
2. Load the datasets using a library like `pandas`.
3. Run the `calculate_pdi_tsi` function from `pdi_tsi.py` on your time series data.

Example:
```python
import pandas as pd
from pdi_tsi import calculate_pdi_tsi

# Load NOAA data
noaa_data = pd.read_csv("noaa_temperature_2020_2021.csv")
temperature = noaa_data["Temperature_C"].values
pdi, tsi, mpdi = calculate_pdi_tsi(temperature)
print("PDI:", pdi, "TSI:", tsi, "MPDI:", mpdi)

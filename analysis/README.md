## Analysis Overview

This project detects urban vegetation loss by comparing satellite imagery from two different time periods.

### Method Used
1. Satellite images (Sentinel-2) were collected for two time ranges:
   - 2020 (baseline)
   - 2024 (recent)

2. NDVI (Normalized Difference Vegetation Index) was computed for both periods.
   - NDVI measures vegetation health using light reflected by plants.

3. NDVI difference was calculated:
   - Decrease → vegetation loss
   - Increase → vegetation growth

4. Regions with significant vegetation loss were extracted as polygons.

5. Area of each polygon was computed (in square meters).

6. Final results were exported as a CSV file for transparency and further analysis.

### Tools Used
- Google Earth Engine
- Python
- Satellite imagery (Sentinel-2)

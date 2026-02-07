# Monitoring Urban Vegetation Loss Using AI and Satellite Imagery

This project focuses on detecting and analyzing urban vegetation loss using satellite imagery and AI-based geospatial analysis techniques.

## Project Overview
Rapid urbanization has led to a significant reduction in green cover in cities. Manual surveys are often slow, costly, and difficult to scale. This project uses satellite data and automated analysis to identify vegetation loss over time in urban areas.

Satellite images from Sentinel-2 were analyzed for two different time periods (2020 and 2024) using NDVI-based change detection. Areas showing a decline in vegetation health were identified and quantified.

## Methodology
- Sentinel-2 multispectral satellite imagery
- NDVI-based temporal change detection
- Comparison of vegetation health across years
- Conversion of detected regions into vector data
- Area calculation in square meters
- Export of results as a structured CSV dataset

## Results
- Detected **15,963 significant vegetation-loss regions** (>1000 m²)
- Quantified vegetation loss with geographic location
- Generated a dataset suitable for further statistical and spatial analysis

## Dataset
The complete dataset generated from this analysis is available in the repository:

- `Vegetation_Loss_2020_2024.csv`

## Technologies Used
- Google Earth Engine
- Python
- Remote Sensing
- NDVI (Normalized Difference Vegetation Index)
- Geospatial Data Analysis
- Blockchain (conceptual data integrity for tamper-proof reporting)

## Applications
- Urban planning and smart city development
- Environmental monitoring
- Sustainability analysis
- Land-use change detection

## Future Scope
- Multi-year vegetation trend analysis
- Integration with administrative boundaries
- Blockchain-based immutable audit trails for environmental data

## License
This project is intended for academic and educational use.


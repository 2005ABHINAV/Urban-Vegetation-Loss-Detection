"""
NDVI Change Analysis for Urban Vegetation Loss
---------------------------------------------

This script explains the logic used to detect vegetation loss
using satellite imagery and NDVI.
"""

# NDVI formula explanation:
# NDVI = (NIR - RED) / (NIR + RED)

def explain_ndvi():
    explanation = """
NDVI (Normalized Difference Vegetation Index) is a value between -1 and +1.

- High NDVI (close to +1): Healthy vegetation
- Low NDVI (close to 0 or negative): Built-up areas, water, or barren land

By comparing NDVI values from two different years,
we can detect where vegetation has decreased over time.
"""
    return explanation


def project_workflow():
    steps = [
        "Collect satellite images for two time periods (2020 and 2024)",
        "Compute NDVI for both periods",
        "Subtract NDVI_2020 from NDVI_2024",
        "Identify regions with negative NDVI change",
        "Convert loss regions into polygons",
        "Calculate area of vegetation loss",
        "Export results as CSV for transparency"
    ]
    return steps


if __name__ == "__main__":
    print(explain_ndvi())
    print("Project Workflow:")
    for step in project_workflow():
        print("-", step)

# Urban Vegetation Loss Detection using AI & Blockchain

## 📌 Project Overview
Urban areas are expanding rapidly, often at the cost of green cover.  
This project detects **urban vegetation loss** by analyzing satellite images from different years and identifying areas where greenery has decreased over time.

The system combines:
- **AI-based satellite image analysis**
- **NDVI vegetation index**
- **Blockchain-based transparency**

to provide a reliable and tamper-proof record of environmental change.

---

## 🌱 What Problem Does This Solve? (Simple Explanation)
Many environmental reports are:
- Manual
- Time-consuming
- Easy to manipulate or dispute

This project provides **automated, data-backed proof** of vegetation loss using satellites and stores the results in a transparent way.

Even a non-technical user can visually see:
- Where vegetation has reduced
- How much area is affected

---

## 🧠 How This Project Works (Non-Technical Explanation)

Think of satellites as **giant cameras in space**.

1. Satellites take photos of the Earth in 2020 and again in 2024.
2. Plants reflect light differently than buildings or roads.
3. Using this difference, we calculate a “green score” for every location.
4. If the green score goes down over time → vegetation is lost.
5. These loss regions are measured and recorded.
6. The final results are stored in a transparent and verifiable format.

---

## 🔬 Technical Workflow (For Technical Readers)
3. NDVI difference computed between 2020 and 2024
4. Regions with negative NDVI change extracted
5. Polygons created for vegetation loss areas
6. Area calculated in square meters
7. Results exported as CSV
8. Data integrity ensured using blockchain concepts

---

## 🔗 Role of Blockchain in This Project (Very Important)

Blockchain is **not used for heavy computation** here.

Instead, it is used for:
- Ensuring **data integrity**
- Preventing **tampering of results**
- Providing **trust and transparency**

In real-world deployment:
- Vegetation loss records can be hashed
- Stored on a blockchain
- Any change becomes detectable

This is useful for:
- Government audits
- Environmental compliance
- Legal disputes
- Public transparency

---

## 💻 What is NVIDIA & Why It Matters? (Simple)

**NVIDIA** builds powerful hardware (GPUs) that help computers process images fast.

In large-scale versions of this project:
- NVIDIA GPUs speed up satellite image processing
- AI models run faster
- Large city-level or country-level analysis becomes feasible

You do NOT need NVIDIA hardware to understand this project — but it enables scaling.

---

## 📊 Dataset
- Source: Sentinel-2 (Google Earth Engine)
- Format: CSV
- Contents:
- Polygon geometry
- Vegetation loss area (m²)

Dataset is available in the `data/` folder.

---

## 🛠 Technologies Used
- Python
- Google Earth Engine
- Satellite Remote Sensing
- NDVI
- Geospatial Analysis
- Blockchain (conceptual integration)

---

## 🌍 Applications
- Urban planning
- Environmental monitoring
- Smart cities
- Climate impact studies
- Government reporting
- ESG compliance

---

## 🚀 Future Scope
- Live yearly monitoring
- Smart contract integration
- Web dashboard
- Carbon footprint estimation
- AI-based prediction of future vegetation loss

---

## 📜 License
This project is open for academic and educational use.



1. Sentinel-2 satellite imagery collected via Google Earth Engine  
2. NDVI calculated using:

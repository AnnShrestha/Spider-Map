# Spider Map - Kathmandu Transit Explorer 🏔️🚌

An interactive web map showing the closest bus stations in Kathmandu to any location, with adjustable "spider legs" (1-8 stations) and real-time walking routes using actual street data.

This project is an enhanced version of the Spider Map concept, specifically optimized for **Kathmandu, Nepal**. It features a high-performance backend for instant pedestrian network analysis.

---

## ✨ Key Features

- **Kathmandu Focused**: Deep integration with Kathmandu's bus stop network (via OSM/Overpass).
- **Walking Network Mode**: Switch from straight-line (Euclidean) distances to realistic street-following paths.
- **Ultra-High Performance**: Backend powered by **[NetworKit](https://github.com/networkit/networkit)** for sub-millisecond route calculations.
- **Smart Labels**: Station names and distances (in KM) are displayed directly above each station marker.
- **Basemap Switcher**: Toggle between Dark, Light, OpenStreetMap, and Satellite imagery.
- **"No-Build" Frontend**: Fast-loading Leaflet.js interface with zero compilation steps.

---

## 🚀 Getting Started

To run the Spider Map locally, you need both the Python backend (for routes) and a simple web server for the frontend.

### Prerequisites

- **Python 3.10+**
- Dependencies: `flask`, `flask-cors`, `networkit`, `osmnx`, `scipy`, `numpy`

### Installation & Launch

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/AnnShrestha/Spider-Map.git
    cd Spider-Map
    ```

2.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Start the Backend Service** (Port 8080):

    ```bash
    python3 src/walking_service.py
    ```

4.  **Start the Frontend Server** (Port 8001):
    In a new terminal:

    ```bash
    python3 -m http.server 8001
    ```

5.  **View the Map**:
    Open [http://localhost:8001](http://localhost:8001) in your browser.

---

## 📂 Project Structure

- `index.html` - The core application interface (HTML/JS/CSS).
- `src/walking_service.py` - Flask backend using NetworKit for fast walking distance calculation.
- `src/download_data.py` - Script for downloading and processing Kathmandu OSM data (Network + Stations).
- `CityData/` - Pre-processed network graphs and station files.
  - `ktm_walking_graph.pkl` - Serialized NetworKit graph for Kathmandu.
  - `ktm_stations.json` - Processed bus station coordinates and names.

---

## 🤝 Acknowledgments

- Based on the original "Spoke" design by [Carlos Enrique Vázquez Juárez](https://carto.mx/webmap/spoke/).
- Data provided by [OpenStreetMap](https://www.openstreetmap.org/) contributors.
- Performance optimization using [NetworKit](https://networkit.github.io/).

---

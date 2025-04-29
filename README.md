# 🚗 Shortest Path Finder (Canada)

A **Streamlit** web app that calculates and visualizes the shortest driving route between two points in any Canadian city. Built using **OpenStreetMap** data, **NetworkX's A\*** algorithm, and **Folium** for interactive map rendering.

---

## 📌 Features

- 🏙️ Select any major **Canadian city**.
- 📍 Choose source and destination nodes (automatically labeled via reverse geocoding).
- ⚡ Calculate the **shortest path** using the A* algorithm.
- 🗺️ Display the path interactively on a **Leaflet-based Folium map**.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [OSMnx](https://osmnx.readthedocs.io/en/stable/)
- [NetworkX](https://networkx.org/)
- [Folium](https://python-visualization.github.io/folium/)
- [Nominatim API (OpenStreetMap)](https://nominatim.org/)

---

🧠 How It Works

- The app uses OSMnx to download the drivable road network of the selected city.
- It builds a graph and applies A* pathfinding to find the optimal route.
- Each node’s coordinates are reverse geocoded using the Nominatim API to generate human-readable labels (e.g., streets or landmarks).
- The computed path is drawn on an interactive map using Folium.

📄 License

- This project is open-source and available under the MIT License.

🙌 Acknowledgments

- Thanks to OpenStreetMap for free and open mapping data.
- Thanks to Streamlit for making data apps easy and fun.

## Contact
For questions or further information, please reach out to:

**Jay Dilip Varma**  
Email: jay01varma@gmail.com  
LinkedIn: [jay01varma](https://www.linkedin.com/in/connect-wtih-jay-varma/) 

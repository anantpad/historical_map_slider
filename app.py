import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 1. Set up a clean, full-width webpage layout
st.set_page_config(layout="wide")
st.title("Interactive Historical Atlas")

# 2. Your Historical Database (Add as many rows/years as you want)
data = {
    "Name": [
        "Rome (Republic)", 
        "Pataliputra (Sunga Capital)", 
        "Alexandria", 
        "Carthage",
        "Rome (Empire Hub)", 
        "Pompeii (Destroyed)", 
        "Herculaneum (Destroyed)",
        "Hopewell Core (Mound Builders)", 
        "Teotihuacán (Rising Metropolis)", 
        "Basketmaker II Culture", 
        "Old Bering Sea Marine Hunters"
    ],
    "Start_Year": [-509, -185, -331, -814, 27, 79, 79, -200, -100, -500, -500],
    "End_Year":   [27, -73, 641, -146, 476, 79, 79, 500,  750,  500,  700],
    "Latitude":   [41.8902, 25.6110, 31.2001, 36.8529, 41.8902, 40.7512, 40.8060, 39.3, 19.6, 36.5, 65.6],
    "Longitude":  [12.4922, 85.1414, 29.9187, 10.3217, 12.4922, 14.4870, 14.3490, -82.9, -98.8, -109.5, -168.0],
    "Info": [
        "Rising power in Italy", 
        "Imperial capital in Northern India", 
        "Center of science & culture", 
        "Phoenician trade superpower",
        "Capital of the vast Roman Empire", 
        "Buried completely by Mt. Vesuvius", 
        "Buried by pyroclastic flows",
        "Building massive geometric earthworks and continental trade routes", 
        "Rapidly expanding urban grid and early pyramid construction", 
        "Transitioning to sedentary maize farming and master basket weaving", 
        "Sophisticated walrus and whale hunters using carved ivory tools"
    ]
}

df = pd.DataFrame(data)

# 3. Create the Reactive Slider (No play/pause buttons!)
selected_year = st.slider(
    "Drag to change the historical year:", 
    min_value=-600, 
    max_value=500, 
    value=-73, 
    step=1
)

# This creates a slider from 600 BCE to 500 CE, defaulting to 73 BCE (Spartacus era)

# Display the currently selected year neatly to the user
if selected_year < 0:
    st.subheader(f"Current Map View: {abs(selected_year)} BCE")
else:
    st.subheader(f"Current Map View: {selected_year} AD")

# 4. Filter data in real-time based on the exact slider position
# A city/event is shown only if the selected year falls between its Start and End years
filtered_df = df[(df['Start_Year'] <= selected_year) & (df['End_Year'] >= selected_year)]

# 1. Create a dictionary of coordinates and zoom levels for different regions
regions = {
    "World View": {"center": [25.0, 10.0], "zoom": 2},
    "Mediterranean & Rome": {"center": [38.0, 20.0], "zoom": 5},
    "North America": {"center": [38.0, -97.0], "zoom": 4},
    "Ancient India": {"center": [22.0, 78.0], "zoom": 5},
    "Mesoamerica": {"center": [19.0, -96.0], "zoom": 6}
}

#  2. Add a dropdown selection menu to the Streamlit sidebar
selected_region = st.sidebar.selectbox("Choose Map Focus Region:", list(regions.keys()))

# 3. Pull the specific coordinates based on what the user clicked
map_center = regions[selected_region]["center"]
map_zoom = regions[selected_region]["zoom"]

# 5. Initialize the Map centered on the Mediterranean/Middle East
m = folium.Map(location=[35.0, 45.0], zoom_start=3, tiles="CartoDB Voyager")

# 6. Drop markers for only the active cities/events in that specific year
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['Name']}</b><br>{row['Info']}",
        tooltip=row['Name'],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 7. Render the map in the browser
st_folium(m, width="100%", height=600)
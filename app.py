import streamlit as st
from src.data_loader import load_data
from src.map_builder import build_historical_map, REGIONS

from src.ui import (
    configure_page,
    display_year_selector, 
    display_year_title, 
    display_region_selector, 
    display_map
)

# 1. Set up a clean, full-width webpage layout
configure_page()

# 2. Your Historical Database (Add as many rows/years as you want)
df = load_data()

# 3. Create the Reactive Slider (No play/pause buttons!)
selected_year = display_year_selector()
# This creates a slider from 600 BCE to 500 CE, defaulting to 73 BCE (Spartacus era)

# Display the currently selected year neatly to the user
display_year_title(selected_year)

# 4. Filter data in real-time based on the exact slider position
# A city/event is shown only if the selected year falls between its Start and End years
filtered_df = df[
    (df['Start_Year'] <= selected_year) & 
    (df['End_Year'] >= selected_year)
    ]

#  2. Add a dropdown selection menu to the Streamlit sidebar
selected_region = st.sidebar.selectbox("Choose Map Focus Region:", list(REGIONS.keys()))

# 7. Render the map in the browser
region = REGIONS[selected_region]
m = build_historical_map(
    filtered_df, 
    region
)

display_map(m)
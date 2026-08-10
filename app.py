import streamlit as st
from src.data_loader import load_data
from src.map_builder import build_historical_map, REGIONS
from src.data_processor import filter_data

from src.ui import (
    configure_page,
    display_year_selector, 
    display_year_title, 
    display_region_selector, 
    display_type_selector,
    display_category_selector,
    display_map,
    render_about,
    render_footer
)

# 1. Set up a clean, full-width webpage layout
configure_page()
render_about()
render_footer()

# 2. Your Historical Database (Add as many rows/years as you want)
df = load_data()

# 3. Create the Reactive Slider (No play/pause buttons!)
selected_year = display_year_selector()
# This creates a slider from 600 BCE to 500 CE, defaulting to 73 BCE (Spartacus era)

# Display the currently selected year neatly to the user
display_year_title(selected_year)

#  2. Add a dropdown selection menu to the Streamlit sidebar
selected_types = display_type_selector(df)
selected_categories = display_category_selector(
    df,
    selected_types
)

selected_region = display_region_selector(REGIONS)

filtered_df = filter_data(
    df=df, 
    selected_year=selected_year, 
    selected_types=selected_types, 
    selected_categories=selected_categories
)

# 7. Render the map in the browser
region = REGIONS[selected_region]
m = build_historical_map(
    filtered_df, 
    region
)

display_map(m)
import streamlit as st
from streamlit_folium import st_folium

def configure_page():
    # 1. Set up a clean, full-width webpage layout
    st.set_page_config(layout="wide")
    st.title("Interactive Historical Atlas")

def display_year_selector():
    """
    Display the historical year slider and return the selected year.
    """

    selected_year = st.slider(
        "Drag to change the historical year:",
        min_value=-600,
        max_value=500,
        value=-73,
        step=1
    )

    return selected_year

def display_year_title(selected_year):
    """
    Display the currently selected historical year.
    """

    if selected_year < 0:
        st.subheader(
            f"Current Map View: {abs(selected_year)} BCE"
        )
    else:
        st.subheader(
            f"Current Map View: {selected_year} AD"
        )

def display_region_selector(regions):
    """
    Display the region selector and return the selected region.
    """

    return st.sidebar.selectbox(
        "Choose Map Focus Region:",
        list(regions.keys())
    )

def display_map(m):
    """
    Render the Folium map in Streamlit.
    """
    st_folium(
        m,
        width="100%",
        height=600
    )
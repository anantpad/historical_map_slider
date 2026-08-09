import streamlit as st
from streamlit_folium import st_folium

def configure_page():
    # 1. Set up a clean, full-width webpage layout
    st.set_page_config(
        page_title="Historical Atlas", 
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        iframe {
            max-width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Interactive Historical Atlas")

def display_year_selector():
    """
    Display the historical year slider and return the selected year.
    """

    selected_year = st.slider(
        "Drag to change the historical year:",
        min_value=-10000,
        max_value=2026,
        value=-4000,
        step=1
    )

    selected_year = st.number_input(
    "Or enter an exact year:",
    min_value=-10000,
    max_value=2026,
    value=selected_year,
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

def display_type_selector(df):
    """Display the Type selector."""

    types = sorted(
        df["Type"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_types = st.sidebar.multiselect(
        "What do you want to see?",
        options=types,
        default=types
    )

    return selected_types
def display_category_selector(df, selected_types):
    """
    Display the Category selector.

    When a Type is selected, only categories belonging
    to that Type are shown.
    """

    if not selected_types:
        return []
    
    categories = sorted(
        df[df["Type"].isin(selected_types)]["Category"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_categories = st.sidebar.multiselect(
        "Filter by Category:",
        options=categories,
        default=categories
    )

    return selected_categories
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
import pandas as pd
import plotly.express as px

# Mock dataset
data = {
    "City/Event": [
        "Rome (Capital)", 
        "Pataliputra (Sunga Capital)", 
        "Alexandria", 
        "Cartilage",
        "Pompeii (Destroyed)", 
        "Rome (Empire Hub)", 
        "Herculaneum (Destroyed)"],
    "Year": [-300, -300, -300, -300, 79, 79, 79],
    "Latitude": [41.8902, 25.6110, 31.2001, 36.8529,
        40.7512, 41.8902, 40.8060],
    "Longitude": [12.4922, 85.1414, 29.9187, 10.3217,
        14.4870, 12.4922, 14.3490],
    "Description": [
        "Rising power in central Italy", 
        "Imperial capital in Northern India", 
        "Center of Hellenistic science & culture", 
        "Major Phoenician trade superpower",
        "Buried completely by Mt. Vesuvius", 
        "Capital of the vast Roman Empire", 
        "Buried by pyroclastic flows"],
    "Size_Marker":[10, 10, 10, 10, 12, 15, 12]
}

df = pd.DataFrame(data)

# Build interactive map with slider
fig = px.scatter_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    hover_name="City/Event",
    hover_data={"Year": True, "Description": True},
    size="Size_Marker",
    color="Year",
    animation_frame="Year", # THIS CREATES THE TIMELINE SLIDER
    zoom=1.5,
    height=600,
    title="Global Historical Atlas Prototype"
)

# Set the map style using Open source street map styles
fig.update_layout(
    mapbox_style = "open-street-map",
    margin={"r":0,"t":40,"l":0,"b":0})

# Save and launch
fig.write_html(
    "historical_map_slider.html", 
    auto_open=True
)

print("Successfully generated 'historical_map_slider.html'. Open this file in any browser to use your slider!")
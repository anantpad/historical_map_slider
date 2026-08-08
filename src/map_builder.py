import folium

REGIONS = {
    "World View": {
        "center": [25.0, 10.0],
        "zoom": 2
    },
    "Mediterranean & Rome": {
        "center": [38.0, 20.0],
        "zoom": 5
    },
    "North America": {
        "center": [38.0, -97.0],
        "zoom": 4
    },
    "Ancient India": {
        "center": [22.0, 78.0],
        "zoom": 5
    },
    "Mesoamerica": {
        "center": [19.0, -96.0],
        "zoom": 6
    }
}

def build_historical_map(filtered_df, region):
    # """Build a Folium map using the supplied historical locations."""
    # map construction here
    # use df["Latitude"], df["Longitude"], etc.
    
    # Pull the specific coordinates based on what the user clicked
    map_center = region["center"]
    map_zoom = region["zoom"]

    # Initialize the Map centered on the Mediterranean/Middle East
    m = folium.Map(
        location=map_center, 
        zoom_start=map_zoom, 
        tiles="CartoDB Voyager")

    # Drop markers for only the active cities/events in that specific year
    for _, row in filtered_df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"<b>{row['Name']}</b><br>{row['Info']}",
            tooltip=row['Name'],
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)

    return m
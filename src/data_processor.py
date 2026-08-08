

# 4. Filter data in real-time based on the exact slider position
# A city/event is shown only if the selected year falls between its Start and End years
def filter_data(df, selected_year, selected_topic):

    filtered_df = df[
        (df["Start_Year"] <= selected_year) &
        (df["End_Year"] >= selected_year)
    ]

    if selected_topic != "All Topics":
        filtered_df = filtered_df[
            filtered_df["Category"] == selected_topic
        ]

    return filtered_df

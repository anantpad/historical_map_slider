import pandas as pd

# 4. Filter data in real-time based on the exact slider position
# A city/event is shown only if the selected year falls between its Start and End years
def filter_data(
        df: pd.DataFrame, 
        selected_year: int, 
        selected_types: str = None, 
        selected_categories: str = None
    ) -> pd.DataFrame:

    filtered_df = df.copy()

    filtered_df = df[
        (df["Start_Year"] <= selected_year) &
        (df["End_Year"] >= selected_year)
    ]

    if selected_types:
        filtered_df = filtered_df[
            filtered_df["Type"].isin(selected_types)
        ]

    if selected_categories:
        filtered_df = filtered_df[
            filtered_df["Category"].isin(selected_categories)
        ]

    return filtered_df

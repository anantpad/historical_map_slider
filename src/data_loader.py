import pandas as pd
from pathlib import Path    

def load_data():
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_FILE = BASE_DIR/"data"/"Events.csv"
    
    df = pd.read_csv(
        DATA_FILE, 
        sep="|"
        )
    
    return df
import pandas as pd 
def load_data():
    df = pd.read_csv("data/vehicles_us.csv") 
    df = df.drop_duplicates()
    
    # Create manufaturer column from model column
    df["manufacturer"] = (
        df["model"]
        .str.split(" ")
        .str[0]
        .str.lower()
    )
    return df
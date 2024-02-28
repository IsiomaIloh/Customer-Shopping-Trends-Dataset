import pandas as pd
def load_data(file_path):
    # Load DataFrame from CSV file
    df = pd.read_csv(file_path)
    return df


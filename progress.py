import pandas as pd
import os

FILE = "progress.xlsx"

def save_progress(feature):
    if os.path.exists(FILE):
        df = pd.read_excel(FILE)
    else:
        df = pd.DataFrame(columns=["Feature"])

    df.loc[len(df)] = [feature]

    df.to_excel(FILE, index=False)
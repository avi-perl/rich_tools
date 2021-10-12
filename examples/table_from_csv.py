import pandas as pd
from rich import print
from rich_tools import df_to_table

if __name__ == "__main__":
    df = pd.read_csv("sample_input.csv")
    table = df_to_table(df)
    print(table)

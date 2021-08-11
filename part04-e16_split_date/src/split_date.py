#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(how="all", axis=0, inplace=True)
    df.dropna(how="all", axis=1, inplace=True)

    df1 = df['Päivämäärä'].copy()
    clean_df = df1.str.split(expand=True)
    clean_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    
    weekdays = {
        'ma': 'Mon',
        'ti': 'Tue',
        'ke': 'Wed',
        'to': 'Thu',
        'pe': 'Fri',
        'la': 'Sat',
        'su': 'Sun'
    }
    months = {
        'tammi': 1,
        'helmi': 2,
        'maalis': 3,
        'huhti': 4,
        'touko': 5,
        'kesä': 6,
        'heinä': 7,
        'elo': 8,
        'syys': 9,
        'loka': 10,
        'marras': 11,
        'joulu': 12
    }

    clean_df["Weekday"] = clean_df["Weekday"].map(weekdays)
    clean_df["Month"] = clean_df["Month"].map(months)
    clean_df["Hour"] = clean_df["Hour"].str[:2]
    clean_df = clean_df.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    return clean_df


def main():
    split_date()
       
if __name__ == "__main__":
    main()

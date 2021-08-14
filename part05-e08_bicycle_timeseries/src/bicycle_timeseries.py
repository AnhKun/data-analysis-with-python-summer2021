#!/usr/bin/env python3

import pandas as pd

def split_date(df):
    df.dropna(how="all", axis=0, inplace=True)
    df.dropna(how="all", axis=1, inplace=True)

    df1 = df['Päivämäärä'].copy()
    date_df = df1.str.split(expand=True)
    date_df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    
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

    date_df["Weekday"] = date_df["Weekday"].map(weekdays)
    date_df["Month"] = date_df["Month"].map(months)
    date_df["Hour"] = date_df["Hour"].str[:2]
    date_df = date_df.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    return date_df

def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(axis=0, how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)
    d = split_date(df)
    df['Date'] = pd.to_datetime(d[['Year', 'Month', 'Day', 'Hour']])
    df.drop(['Päivämäärä'], axis=1, inplace=True)
    df = df.set_index('Date')

    return df

def main():
    print(bicycle_timeseries())

if __name__ == "__main__":
    main()

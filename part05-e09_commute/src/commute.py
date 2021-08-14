#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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
    df = pd.concat([df, d], axis=1)
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day', 'Hour']])
    df.drop(['Päivämäärä', 'Year', 'Month', 'Day', 'Hour'], axis=1, inplace=True)
    df = df.set_index('Date')

    return df

def commute():
    df = bicycle_timeseries()
    df = df["2017-08-01":"2017-08-31"]
    
    days = dict(zip("Mon Tue Wed Thu Fri Sat Sun".split(), range(1,8)))
    df["Weekday"] = df["Weekday"].map(days)
    return df.groupby("Weekday").sum()
    
def main():
    df = commute()
    plt.plot(df)
    weekdays="x mon tue wed thu fri sat sun".title().split()
    plt.gca().set_xticklabels(weekdays)
    plt.show()


if __name__ == "__main__":
    main()

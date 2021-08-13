#!/usr/bin/env python3

import pandas as pd

def split_date(df):
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

def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    date_df = split_date(df)
    df.drop(['Päivämäärä'], axis=1, inplace=True)
    return pd.concat([date_df, df], axis=1)

def cycling_weather():
    df_cycling = split_date_continues()
    df_weather = pd.read_csv('src/kumpula-weather-2017.csv')
    df_weather = df_weather.rename(columns={'m': 'Month', 'd': 'Day'})
    df = pd.merge(df_cycling, df_weather, how='inner')
    df.drop(['Time', 'Time zone'], axis=1, inplace=True)
    return df

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()

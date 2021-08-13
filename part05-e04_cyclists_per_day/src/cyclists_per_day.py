#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
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

    df.drop(['Päivämäärä'], axis=1, inplace=True)
    return pd.concat([date_df, df], axis=1)

def cyclists_per_day():
    df = split_date()
    df2 = df.copy()
    df2.drop(['Weekday', 'Hour'], axis=1, inplace=True)
    return df2.groupby(['Year', 'Month', 'Day']).sum()
    
def main():
    df = cyclists_per_day()
    print(df)
    df = df.loc[(2017, 8), :]
    df.plot()
    plt.show()
    
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    df['President'] = df['President'].str.partition(',')[2] + ' ' + df['President'].str.partition(',')[0]
    df['President'] = df['President'].str.title()
    df['President'] = df['President'].str.strip()

    df["Vice-president"] = df["Vice-president"].str.partition(',')[2] + ' ' + df["Vice-president"].str.partition(',')[0]
    df["Vice-president"] = df["Vice-president"].str.title()
    df["Vice-president"] = df["Vice-president"].str.strip()
    
    df['Last'] = pd.to_numeric(df['Last'], errors='coerce')
    df['Start'] = df['Start'].str.split(' ', expand=True)[:][0]
    df['Seasons'] = df['Seasons'].str.replace('two', '2')
    df = df.astype({'President': object, 'Start': int, 'Last': float, 'Seasons': int, 'Vice-president': object})
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()

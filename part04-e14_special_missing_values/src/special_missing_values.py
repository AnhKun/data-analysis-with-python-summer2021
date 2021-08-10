#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df.replace({"New": None, "Re": None}, value=None, inplace=True)
    df.dropna(how='any', axis=0, inplace=True)
    df[['Pos', 'LW']] = df[['Pos', 'LW']].astype('float')
    mask = df['Pos'] > df['LW']
    return df[mask]

def main():
    special_missing_values()

if __name__ == "__main__":
    main()

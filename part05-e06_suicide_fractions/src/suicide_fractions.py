#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df2 = df.groupby('country')
    return df2.apply(lambda df2: (df2['suicides_no']/df2['population']).mean())
def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()

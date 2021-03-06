#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    df2 = df.groupby("Publisher").sum()
    best_company = df2["WoC"].idxmax()
    return df[df["Publisher"] == best_company]
    
def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()

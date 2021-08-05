#!/usr/bin/env python3
import pandas as pd
import numpy as np

def read_series():
    indx = []
    val = []
    while True:
        txt = input('Enter: ')
        if not txt: 
            break
        try:
            i, v = txt.split()
            indx.append(i)
            val.append(v)
        except ValueError:
            print('Value error')
            continue
    return pd.Series(val, index=indx, dtype='object')


def main():
    read_series()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    indx = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    val = {'Year of independence': [np.nan, 1917, 1776, 1523, np.nan, 1992], 
           'President': [None, 'Niinistö', 'Trump', None, 'Steinmeier', 'Putin']}

    return pd.DataFrame(val, index=indx)
               
def main():
    missing_value_types()

if __name__ == "__main__":
    main()

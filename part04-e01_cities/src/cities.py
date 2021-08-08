#!/usr/bin/env python3

import pandas as pd

def cities():
    indx = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']
    data = [[643272, 715.48],
            [279044, 528.03],
            [231853, 689.59],
            [223027, 240.35],
            [201810, 3817.52]]
    columns = ['Population', 'Total area']

    return pd.DataFrame(data, columns=columns, index=indx)
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()

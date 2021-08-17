#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = df.iloc[:,0:5]
    y = df.iloc[:,5]
    reg = LinearRegression()
    reg.fit(X,y)
    scores = []
    scores.append(reg.score(X,y))
    for i in X:
        reg.fit(df[i].values.reshape(-1,1), y)
        score = reg.score(df[i].values.reshape(-1,1), y)
        scores.append(score)
    return scores
    
def main():
    scores = coefficient_of_determination()
    for i, n in enumerate(scores):
        if i==0:
            print("R2-score with feature(s) X: {}".format_(n))
        else:
            print("R2-score with feature(s) X{}: {}".format(i+1, n))

if __name__ == "__main__":
    main()

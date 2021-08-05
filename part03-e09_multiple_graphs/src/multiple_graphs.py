#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    ax = [2,4,6,7]
    ay = [4,3,5,1]
    bx = [1,2,3,4]
    by = [4,2,3,1]

    plt.plot(ax, ay)
    plt.plot(bx, by)
    plt.title('title')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

if __name__ == "__main__":
    main()

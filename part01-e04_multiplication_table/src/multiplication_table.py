#!/usr/bin/env python3


def main():
    a = ''
    for i in range(1,11):
        for j in range(1, 11):
            a = a + str(i*j) + '\t'
        a += "\n"
    return print(a)

if __name__ == "__main__":
    main()

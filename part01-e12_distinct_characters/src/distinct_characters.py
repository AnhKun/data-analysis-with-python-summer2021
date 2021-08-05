#!/usr/bin/env python3

def distinct_characters(L):
    new_dict = {}
    for i in L:
        new_dict[i] = len(set(i))
    return new_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()

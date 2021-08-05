#!/usr/bin/env python3

def find_matching(L, pattern):
    lists = []
    for i, ele in enumerate(L):
        if pattern in ele:
            lists.append(i)
    return lists

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    find_matching([], "en")
if __name__ == "__main__":
    main()

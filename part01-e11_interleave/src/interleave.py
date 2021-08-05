#!/usr/bin/env python3

def interleave(*lists):
    new_list = []
    zipped_list = list(zip(*lists))
    for i in zipped_list:
        new_list.extend(i)
    return new_list
def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()

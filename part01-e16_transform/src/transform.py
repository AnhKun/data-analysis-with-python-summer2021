#!/usr/bin/env python3

def transform(s1, s2):
    new_s1 = s1.split()
    new_s2 = s2.split()

    zipped_list = zip(new_s1, new_s2)
    return list(map(lambda x: int(x[0])*int(x[1]), zipped_list))

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()

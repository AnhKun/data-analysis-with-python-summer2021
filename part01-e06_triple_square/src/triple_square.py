#!/usr/bin/env python3

def triple(a):
        return int(a*3)
def square(b):
        return int(b**2)
def main():
    for i in range(1,11):
        a = square(i)
        b = triple(i)
        if a <= b:
            print(f"triple({i})=={b} square({i})=={a}")
        else:
            break

        

if __name__ == "__main__":
    main()

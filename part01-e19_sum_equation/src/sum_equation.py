#!/usr/bin/env python3

def sum_equation(L):
    if L == []:
        return "0 = 0"
    else:
        s = "{}".format(L[0])
        for i in range(1,len(L)):
            s += " + {}".format(L[i])
    return s + " = " + str(sum(L))
def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()

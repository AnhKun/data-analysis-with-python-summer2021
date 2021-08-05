#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i =0
    j =0
    k =0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i+=1
        elif L1[i]==L2[j]:
            L.append(L1[i])
            i+=1
            L.append(L2[j])
            j+=1    
        else:
            L.append(L2[j])  
            j+=1      
    while i < len(L1):
        L.append(L1[i])
        i+=1

    while j < len(L2):
        L.append(L2[j])
        j+=1    
    if len(L1) +len(L2) == len(L):    
        return L       


def main():
    L1 = [1,5,9,12]
    L2 = [2,6,10]
    #L1 = [-100, -77, -41, -37, -37, -33, -28, -22, -17, -9, -7, -6, 20, 21, 38, 50, 60, 66, 75, 78]
    #L2 = [74, -67, -52, -43, -16, -11, -4, 43, 55, 67]
    #sorted(L1)
    #sorted(L2)
    print(merge(L1,L2))

if __name__ == "__main__":
    main()

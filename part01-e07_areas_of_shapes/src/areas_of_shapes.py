#!/usr/bin/env python3

import math

def triangle():
    b = int(input("Give base of the triangle: "))
    h = int(input("Give height of the triangle: "))
    print("The area is {}".format(b*h*0.5))

def rectangle():
    w = int(input("Give width of the rectangle: "))
    h = int(input("Give height of the rectangle: "))
    print("The area is {}".format(w*h)) 

def circle():
    r = int(input("Give radius of the circle: "))
    print("The area is {}".format(math.pi*r*r))  

def main():
    # enter you solution here
    status = True
    while status:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            triangle()
        elif shape == "rectangle":
            rectangle()
        elif shape == "circle":
            circle()
        elif shape == "":
            break
        else:
            print("Unknown shape!")
if __name__ == "__main__":
    main()

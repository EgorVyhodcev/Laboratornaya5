#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    x = float(input("Enter the x coordinate: "))
    y = float(input("Enter the y coordinate: "))
    if (x*x + y*y <= 1) and (x*x + y*y >= 0.25):
        print("It does belong")
    else:
        print("It doesn't belong")

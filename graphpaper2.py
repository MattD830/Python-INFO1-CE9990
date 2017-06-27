"""
I came up with this the first try.  So, that's why this is posted in duplicate.
"""

import sys

try:
    columns = int(input("How many columns? "))
    rows = int(input("How many rows? "))
    tall = int(input("How tall should the boxes be? "))
    wide = int(input("How wide should the boxes be? "))
except Exception as e:
    print(e)
    print("You have fail")
    print("Try type valid integer")
    sys.exit(1)

i = 0
j = 0
k = 0
m = 0

while j <= rows:
    print("+",end="")
    while k < columns:
        while i < wide:
            print("-",end="")
            i += 1
        print("+",end="")
        i = 0
        k += 1
    print('\r')
    k = 0
    if j < rows:
        while m < tall:
            print("|",end="")
            while k < columns:
                print(" "*wide,end="")
                print("|",end="")
                k += 1
            k = 0
            m += 1
            print("\r")
        m = 0
    j += 1
        
sys.exit(0)

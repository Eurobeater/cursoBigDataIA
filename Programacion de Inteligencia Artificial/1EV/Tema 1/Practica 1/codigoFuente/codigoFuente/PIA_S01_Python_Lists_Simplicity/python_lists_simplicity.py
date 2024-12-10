#!/usr/bin/python3

import random

MAX_VALUE = 100
N = 10


def main():
    l = []
    for i in range(N):
        l.append(random.randint(1, MAX_VALUE))

    # List comprehension en Python
    # newlist = [expression for item in iterable if condition == True]
    # l = [random.randint(1, MAX_VALUE) for value in range(N)]

    print(l[:])    # Print all elements in l
    print(l[:5])   # Print first 5 elements in l
    print(l[:-1])  # Print all but last element in l
    print(l[4:])   # Print last 5 elements in l
    print(l[-3:])  # Print 3 last elements in l
    print(l[3:6])  # Print sublist
    print(l[2:-1]) # Print sublist
    
    
if __name__ == "__main__":
    main()

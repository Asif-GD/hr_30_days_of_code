#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter the size of the array: ").strip())

    arr = list(map(int, input(f"Enter the elements of the array of size {n}: ").rstrip().split()))
    output = ""
    for item in arr[::-1]:
        output += "".join(str(item) + " ")

    print(output)
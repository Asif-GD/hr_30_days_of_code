#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input("Enter your number: ").strip())
    if N % 2 == 1:
        print("Weird")
    else:
        if 2 <= N <= 5 or N > 20:
            print("Not Weird")
        elif 6 <= N <= 20:
            print("Weird")

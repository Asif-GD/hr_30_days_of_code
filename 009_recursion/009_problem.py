#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(num: [int]) -> [int]:
    # Write your code here
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Enter the number: ").strip())

    result = factorial(n)
    # print(result)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    extra = meal_cost * (tip_percent + tax_percent) / 100
    answer = round(meal_cost + extra)
    print(answer)

if __name__ == '__main__':
    meal_cost = float(input("Cost of the meal? ").strip())

    tip_percent = int(input("What's the tip? ").strip())

    tax_percent = int(input("How much is the tax? ").strip())

    solve(meal_cost, tip_percent, tax_percent)

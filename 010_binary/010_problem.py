#!/bin/python3

import math
import os
import random
import re
import sys


def get_binary(num: [int]) -> [str]:
    if num == 1 or num == 0:
        return str(num)
    else:
        mod = num % 2
        num //= 2
        return str(get_binary(num)) + str(mod)


def get_max_consecutive_1(bin_num: [str]) -> [int]:
    current_max: [int] = 0
    count: [int] = 0
    for char in bin_num:
        if char == '0':
            current_max = max(current_max, count)
            count = 0
        else:
            count += 1

    return max(current_max, count)


if __name__ == '__main__':
    n = int(input("Enter the number: ").strip())
    binary_number = get_binary(num=n)
    print(binary_number)
    print(get_max_consecutive_1(bin_num=binary_number))

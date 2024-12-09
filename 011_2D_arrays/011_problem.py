#!/bin/python3

import math
import os
import random
import re
import sys

sample_arr_1 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

sample_arr_2 = [
    [-1, -1, 0, -9, -2, -2],
    [-2, -1, -6, -8, -2, -5],
    [-1, -1, -1, -2, -3, -4],
    [-1, -9, -2, -4, -4, -5],
    [-7, -3, -3, -2, -9, -9],
    [-1, -3, -1, -2, -4, -5],
]


def max_hourglass_sum(array: list[list[int]]) -> [int]:
    # we know the array is always of size 6x6
    # declaring this as a list() because declaring this as integer 0 will cause issues in case of negative sums.
    hourglass_sum_list: list[int] = []
    for index_1 in range(4):
        for index_2 in range(4):
            a = array[index_1 + 0][index_2 + 0]
            b = array[index_1 + 0][index_2 + 1]
            c = array[index_1 + 0][index_2 + 2]
            d = array[index_1 + 1][index_2 + 1]
            e = array[index_1 + 2][index_2 + 0]
            f = array[index_1 + 2][index_2 + 1]
            g = array[index_1 + 2][index_2 + 2]
            current_hourglass_sum = a + b + c + d + e + f + g

            # print(max_sum, hourglass_sum)

            hourglass_sum_list.append(current_hourglass_sum)

    return max(hourglass_sum_list)


if __name__ == '__main__':
    arr = sample_arr_2

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    print(max_hourglass_sum(array=arr))

'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing
exactly four of the five integers. Then print the respective minimum and maximum values as a single line
of two space-separated long integers.

For example,
Our minimum sum is and our maximum sum is . We would print [1,3,5,7,9] 16 or 24
'''


import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minArr = arr.copy()
    maxArr = arr.copy()
    minSum = 0
    maxSum = 0

    for x in range(4):
        minnum = min(minArr)
        minSum += minnum
        minArr.remove(minnum)

        maxnum = max(maxArr)
        maxSum += maxnum
        maxArr.remove(maxnum)

    print(minSum)
    print(maxSum)




arr = [1, 3, 5, 7, 9]
miniMaxSum(arr)
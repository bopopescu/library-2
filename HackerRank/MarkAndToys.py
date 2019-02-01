#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    print(k)
    print(prices)
    # sort
    '''
    for x in range(len(prices)):
        for y in range(x, len(prices)-1):
            current = prices[x]
            next = prices[y+1]
            if current > next:
                prices[x] = next
                prices[y+1] = current
    '''

    prices.sort()
    count = 0

    for price in prices:
        if price < k:
            k = k - price
            count += 1

    return count

if __name__ == '__main__':
    # 99383 806930886
    fptr = open('./resources/markandtoy_test6', 'r')
    r = fptr.read()

    nk = r.split()
    prices = list(map(int, nk))
    result = maximumToys(prices, 806930886)



'''
k = 50
prices = [1, 12, 5, 111, 200, 1000, 10]
maximumToys(prices, k)
'''
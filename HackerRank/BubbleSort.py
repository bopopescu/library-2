import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    srtlist = list()
    numSwaps = 0
    for x in range(len(a)):
        for y in range(x, len(a)):
            current = a[x]
            next = a[y]
            if next < current:
                numSwaps += 1
                a[x] = next
                a[y] = current
    print('Array is sorted in %s swaps.' %(numSwaps))
    print('First Element: %s' %(a[0]))
    print('Last Element: %s' %(a[len(a)-1]))

arr = [3,1,2,9, 5, 7, 6]



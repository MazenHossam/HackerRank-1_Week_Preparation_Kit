import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    LD=0
    RD=0
    for i in range(len(arr)):
        LD+=arr[i][i]
        RD+=arr[len(arr)-1-i][i]
    return abs(LD-RD)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

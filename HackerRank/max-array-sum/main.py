#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.


def maxSubsetSum(arr):
    lst = 1
    di = []
    for x in range(len(arr)):
        print(di)
        if arr[x] > 0:
            if len(di) == 0:
                di.append(arr[x])
            else:
                if x - lst > 1:
                    i1 = di[0]
                    if len(di) == 1:
                        di.append(i1 + arr[x])
                    else:
                        i2 = di[1]
                        if i1 > i2:
                            di.append(i1 + arr[x])
                        else:
                            di.append(i2 + arr[x])
                else:
                    if len(di) > 1:
                        i = di[0]
                        di.append(i + arr[x])
                    else:
                        di.append(arr[x])
            lst = x
            if len(di) > 2:
                di.remove(min(di))

    if len(di) == 0:
        return max(arr)
    return max(di)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

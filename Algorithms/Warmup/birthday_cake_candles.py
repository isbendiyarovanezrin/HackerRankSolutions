# Language: Python 3

import os

def birthdayCakeCandles(candles):
    n = 0
    maxCandle = max(candles)
    for i in range(candles_count):
        if maxCandle == candles[i]:
            n += 1
    return n       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
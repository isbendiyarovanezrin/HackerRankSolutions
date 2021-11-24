# Language: Python 3

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for i in range(n):
        if arr[i] > 0:
            positive += 1
        elif arr[i] == 0:
            zero += 1
        else:
            negative += 1
    
    pn = positive/n  
    nn = negative/n
    zn = zero/n

    print(pn)
    print(nn)
    print(zn)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
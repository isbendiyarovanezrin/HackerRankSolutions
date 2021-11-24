# Language: Python 3

def miniMaxSum(arr):
    miniMaxArr = []
    
    s1 = arr[1] + arr[2] + arr[3] + arr[4]
    s2 = arr[0] + arr[2] + arr[3] + arr[4]
    s3 = arr[0] + arr[1] + arr[3] + arr[4]
    s4 = arr[0] + arr[1] + arr[2] + arr[4]
    s5 = arr[0] + arr[1] + arr[2] + arr[3]
    
    miniMaxArr.append(s1)
    miniMaxArr.append(s2)
    miniMaxArr.append(s3)
    miniMaxArr.append(s4)
    miniMaxArr.append(s5)
    
    minNumber = min(miniMaxArr)
    maxNumber = max(miniMaxArr)
    
    print(minNumber, maxNumber)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

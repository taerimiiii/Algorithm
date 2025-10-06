import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 20000
arr[0] = 1
if n == 1 :
    print(1)
else :
    for i in range(1, 20000) :
        arr[i] = arr[i-1] + i * 6
        if arr[i] >= n :
            print(i+1)
            break

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split(',')))

if k == 0 :
    answer = arr
else :
    for i in range(k) :
        length = len(arr)
        answer = [0] * (length-1)
        for i in range(length-1) :
            answer[i] = arr[i+1] - arr[i]
        arr = answer


l = len(answer)
for i in range(l-1) :
    print(answer[i], end=',')

print(answer[-1])
import sys

def back_tracking(num) :
    if num == n :
        sum_val = 0
        for i in range(n - 1) :
            sum_val += abs(arr[index[i]] - arr[index[i + 1]])
        answer.append(sum_val)
        return

    for i in range(n) :
        if i not in index :
            index.append(i)
            back_tracking(num + 1)
            index.pop()

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = []
index = []

back_tracking(0)

print(max(answer))

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
length = len(arr)
idx_arr = [[i, arr[i], 0] for i in range(length)]

idx_arr.sort(key=lambda x: x[1])

rank = 0
curr = idx_arr[0][1]
idx_arr[0][2] = 0
for i in range(1, length) :
    if curr != idx_arr[i][1] :
        rank += 1
        curr = idx_arr[i][1]
    idx_arr[i][2] = rank

idx_arr.sort(key=lambda x: x[0])

for i in range(length) :
    print(idx_arr[i][2], end=' ')
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]
max_idx_list = [0]

for i in range(1, n) :
    if arr[i] > max_val :
        max_val = arr[i]
        max_idx_list = [i]
    elif arr[i] == max_val :
        max_idx_list.append(i)

length = len(max_idx_list)
mid = n / 2 - 0.5
far = (mid - max_idx_list[0]) + (mid - max_idx_list[length-1])
if far < 0 :
    print('B')
elif far == 0 :
    print('X')
else :
    print('R')

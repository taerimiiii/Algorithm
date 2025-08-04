import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

print(round(sum(arr)/n))
print(arr[n//2])

cnt = dict()
for i in arr:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

mx = max(cnt.values())
mx_lst = []

for i in cnt:
    if cnt[i] == mx:
        mx_lst.append(i)

print(mx_lst[0]) if len(mx_lst) == 1 else print(mx_lst[1])

print(arr[-1] - arr[0])
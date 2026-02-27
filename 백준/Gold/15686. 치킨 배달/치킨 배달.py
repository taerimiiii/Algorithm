import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())

houses = []
chickens = []
for i in range(n) :
    arr = list(map(int, input().split()))
    for j in range(n) :
        if arr[j] == 1 :
            houses.append([i, j])
        elif arr[j] == 2 :
            chickens.append([i, j])


combi = combinations(chickens, m)
answer = sys.maxsize
for chicken in combi :
    sum_val = 0
    for house in houses :
        min_val = sys.maxsize
        for i in range(m) :
            min_val = min(abs(chicken[i][0] - house[0]) + abs(chicken[i][1] - house[1]), min_val)
        sum_val += min_val
    answer = min(sum_val, answer)

print(answer)
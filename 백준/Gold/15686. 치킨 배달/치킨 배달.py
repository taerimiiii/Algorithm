import sys
input = sys.stdin.readline

def dfs(depth, idx) :
    global answer

    if depth == m :
        sum_val = 0
        for house in houses :
            min_val = sys.maxsize
            for select_chicken in select_chickens :
                min_val = min(abs(select_chicken[0] - house[0]) + abs(select_chicken[1] - house[1]), min_val)
            sum_val += min_val
        answer = min(sum_val, answer)
        return

    for i in range(idx, len(chickens)) :
        select_chickens.append(chickens[i])
        dfs(depth + 1, i + 1)
        select_chickens.pop()


n, m = map(int, input().split())

houses = []
chickens = []
for i in range(n) :
    arr = list(map(int, input().split()))
    for j in range(n) :
        if arr[j] == 1 :
            houses.append((i, j))
        elif arr[j] == 2 :
            chickens.append((i, j))

select_chickens = []
answer = sys.maxsize
dfs(0, 0)
print(answer)
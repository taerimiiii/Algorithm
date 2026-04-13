import sys
input=sys.stdin.readline
from math import ceil, log2


def init(ar, tree, node, start, end) :
    if not start - end :
        tree[node] = ar[start]
        
    else:
        init(ar, tree, node + node, start, (start + end) >> 1)
        init(ar, tree, node -~node, -~((start + end) >> 1), end)
        tree[node] = mi(tree[node+node], tree[node-~node])


def mi(a:list, b:list) -> list :
    if a[0] > b[0] :
        return b
    return a


def update(arr, tree, node, start, end, idx, va):
    if idx < start or idx > end :
        return
    
    if not start - end :
        arr[idx] = [va, idx + 1]
        tree[node] = [va, idx + 1]
        return
    
    update(arr, tree, node + node, start, (start + end) >> 1, idx, va)
    update(arr, tree, node -~node, -~((start + end) >> 1), end, idx, va)

    tree[node] = mi(tree[node + node], tree[node -~node])


def query(tree, node, start, end, left, right) :
    if left > end or right < start :
        return [float('inf'), float('inf')]
    
    if left <= start and end <= right :
        return tree[node]
    
    lm = query(tree, node + node, start, (start + end) >> 1, left, right)
    rm = query(tree, node -~node, -~((start + end) >> 1), end, left, right)

    return mi(lm, rm)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

for i in range(n) :
    arr[i] = [arr[i], -~i]

hi = ceil(log2(n))
tree = [0] * (2 << hi)

init(arr, tree, 1, 0, ~-n)

for i in range(m) :
    que, *r = map(int, input().split())

    if not ~-que :
        i, v = r
        update(arr, tree, 1, 0, ~-n, ~-i, v)

    else :
        i, j = r
        print(query(tree, 1, 0, ~-n, ~-i, ~-j)[1])






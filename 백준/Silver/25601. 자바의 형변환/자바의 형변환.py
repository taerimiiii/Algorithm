import sys
input = sys.stdin.readline

def possible(tree, x, y):
    parent = x
    while parent in tree:
        parent = tree[parent]
        if parent == y:
            return 1
    return 0

n = int(input().strip())
tree = dict()

for i in range(n-1):
    a, b = input().split()
    tree[a] = b

x, y = input().split()

print(possible(tree, x, y) or possible(tree, y, x))
import sys
input = sys.stdin.readline

n = int(input())
write = input()
arr = [ ['#'] * (2*n+1) for _ in range(2*n+1) ]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
direct = 1
x, y = n, n
arr[x][y] = '.'

for i in range(n) :
    w = write[i]
    if w == 'R' :
        direct = (direct + 1) % 4
    elif w == 'L' :
        direct = (direct + 3) % 4
    else :
        x, y = x + dxs[direct], y + dys[direct]
        arr[x][y] = '.'

top, bottom, right, left = 2*n, 0, 0, 2*n
for i in range(2*n+1) :
    for j in range(2*n+1) :
        if arr[i][j] == '.' :
            if i < top :
                top = i
            if i > bottom :
                bottom = i
            if j > right :
                right = j
            if j < left :
                left = j

for i in range(top, bottom + 1) :
    for j in range(left, right + 1) :
        print(arr[i][j], end='')
    print()
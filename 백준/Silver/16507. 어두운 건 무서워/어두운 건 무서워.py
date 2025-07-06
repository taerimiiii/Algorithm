from sys import stdin
input = stdin.readline

r, c, q = map(int, input().split())

picture_sum = [ [0] * (c+1) for _ in range(r+1) ]
for i in range(1, r+1) :
    picture = [0] + list(map(int, input().split()))
    for j in range(1, c+1) :
        picture_sum[i][j] = picture_sum[i-1][j] + picture_sum[i][j-1] - picture_sum[i-1][j-1] + picture[j]

for _ in range(q) :
    x1, y1, x2, y2 = map(int, input().split())
    sum_val = picture_sum[x2][y2] - picture_sum[x2][y1-1] - picture_sum[x1-1][y2] + picture_sum[x1-1][y1-1]
    cnt = (x2-x1+1) * (y2-y1+1)
    mean = sum_val // cnt
    print(mean)
from sys import stdin
input = stdin.readline


n, k = map(int, input().split())

arr = [ [1] * n for _ in range(n) ]

for i in range(2, n) :
    for j in range(1, i) :
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

print(arr[n - 1][k - 1])
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
arr_2d = [ [int(c) for c in string] for string in arr]

lenth = 1
max_length = lenth

for lenth in range(1, n + 1):
    for i in range(n - lenth + 1) :
        for j in range(m - lenth + 1) :
            if arr_2d[i][j] == arr_2d[i + lenth - 1][j] and arr_2d[i][j] == arr_2d[i][j + lenth - 1] and arr_2d[i + lenth - 1][j + lenth - 1] == arr_2d[i][j] :
                max_length = lenth
                break

print(max_length ** 2)

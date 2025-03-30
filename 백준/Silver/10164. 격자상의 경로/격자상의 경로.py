def change_2dindex(k) :
    global m
    row = 0
    while k > m :
        k -= m
        row += 1
    col = k - 1
    return row, col

n, m, k = map(int, input().split())

if k == 0 :
    arr = [ [1] * m for _ in range(n) ]
    for i in range(1, n) :
        for j in range(1, m) :
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j]
    print(arr[n - 1][m - 1])
else :
    row, col = change_2dindex(k)
    arr1 = [ [1] * (col + 1) for _ in range(row + 1) ]
    for i in range(1, row + 1) :
        for j in range(1, col + 1) :
            arr1[i][j] = arr1[i][j - 1] + arr1[i - 1][j]
    arr2 = [ [1] * (m - col) for _ in range(n - row) ]
    for i in range(1, n - row) :
        for j in range(1, m - col) :
            arr2[i][j] = arr2[i][j - 1] + arr2[i - 1][j]
    #print(arr1)
    #print(arr2)
    #print(row, col)
    print(arr1[row][col] * arr2[n - row - 1][m - col - 1])

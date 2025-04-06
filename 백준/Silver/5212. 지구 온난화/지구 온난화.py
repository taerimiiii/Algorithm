# 땅이 바다가 되는지 판단하는 함수
def is_sea(x, y):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    target = 0
    for dx, dy in zip(dxs, dys) :
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny) :
            target += 1
        else :
            if arr[nx][ny] == '.' :
                target += 1
    if target >= 3 :
        return 1
    return 0

def in_range(x, y) :
    global r, c
    if x >= 0 and x < r and y >= 0 and y < c :
        return 1
    return 0

# 출력 범위 구하는 함수
def get_print_range(r, c) :
    min_row, min_col, max_row, max_col = r, c, 0, 0
    for i in range(r) :
        for j in range(c) :
            if arr[i][j] == 'O' :
                arr[i][j] = '.'
            elif arr[i][j] == 'X' :
                min_row = min(i, min_row)
                min_col = min(j, min_col)
                max_row = max(i, max_row)
                max_col = max(j, max_col)
    return min_row, min_col, max_row, max_col

# 입력 처리
r, c = map(int, input().split())
arr = [[''] * c for _ in range(r)]
for i in range(r) :
    string = input()
    for j in range(c) :
        arr[i][j] = string[j]

# 50년 후
for i in range(r) :
    for j in range(c) :
        if arr[i][j] == 'X' :
            if is_sea(i, j) :
                arr[i][j] = 'O'

# 출력 범위
min_row, min_col, max_row, max_col = get_print_range(r, c)

# 출력
for i in range(min_row, max_row + 1) :
    for j in range(min_col, max_col + 1) :
        print(arr[i][j], end = '')
    print()

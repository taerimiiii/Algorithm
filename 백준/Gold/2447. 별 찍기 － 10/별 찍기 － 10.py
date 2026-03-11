import sys
input = sys.stdin.readline

# 재귀 호출
# 좌표 값을 함께 넘겨야 함
# 그렇다면 좌표를 찍을 크기는 어떻게 구하는가? A. 재귀호출에 넘기는 n 값으로 한다.

def back_tracking(n, x, y, is_star) :
    if n < 3 :
        if is_star :
            arr[x][y] = "*"
        else :
            arr[x][y] = " "
        return
    
    count = 0
    for i in range(x, x+n, n//3) :
        for j in range(y, y+n, n//3) :
            count += 1
            if count == 5 :
                back_tracking(n//3, i, j, False)
            else :
                back_tracking(n//3, i, j, is_star)


n = int(input())
arr = [["0"] * n for _ in range(n)]
back_tracking(n, 0, 0, True)

for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end='')
    print()
import sys
input = sys.stdin.readline

def cut(y, x, curr_n): 
    color = arr[y][x]
    for i in range(y, y + curr_n) :
        for j in range(x, x + curr_n) :
            if color != arr[i][j] :
                next_n = curr_n//2
                cut(y, x, next_n)
                cut(y, x + next_n, next_n)
                cut(y + next_n, x, next_n)
                cut(y + next_n, x + next_n, next_n) 
                return
    if color == 0:
        answers[0] += 1
    else :
        answers[1] += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answers = [0,0]
cut(0,0,n)

print(answers[0])
print(answers[1])

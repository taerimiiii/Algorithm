from collections import deque

def bfs(j,i) :

    global flag
    q = deque([(j, i)])

    directY = [-1, 1, 0, 0]
    directX = [0, 0, -1, 1]

    while q :
        y, x = q.popleft()

        for k in range(4) :
            dy = directY[k] + y
            dx = directX[k] + x

            if dy < 0 or dy >= N or dx < 0 or dx >= M :
                continue
            if arr[dy][dx] == 0 and (dy == N-1) :
                flag = "YES"
                arr[dy][dx] = 1
                q.append([dy,dx])
            elif arr[dy][dx] == 0 :
                arr[dy][dx] = 1
                q.append([dy,dx])
                
N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

flag = "NO"

for i in range(M) :
    if arr[0][i] == 0 :
        arr[0][i] = 1
        bfs(0, i)

print(f"{flag}")
# 벨트 회전 함수
def container_move(n) :
    # 벨트 회전
    temp = arr[2 * n - 1]
    for i in range(2 * n - 1, 0, -1) :
        arr[i] = arr[i - 1]
    arr[0] = temp
    
    # 벨트 회전과 함께 로봇도 이동
    for i in range(n - 1, 0, -1) :
        robot_arr[i] = robot_arr[i - 1]
    robot_arr[0] = 0

# 로봇 이동 함수
def robot_move(n) :
    robot_arr[n - 1] = 0
    for i in range(n - 2, -1, -1) :
        if robot_arr[i] == 1 and robot_arr[i + 1] == 0 and arr[i + 1] != 0:
            robot_arr[i + 1] = 1
            robot_arr[i] = 0
            arr[i + 1] -= 1

# 로봇 올리는 함수
def robot_up() :
    if robot_arr[0] == 0 and arr[0] != 0 :
        robot_arr[0] = 1
        arr[0] -= 1

# 종료 판단 함수
def is_break(k) :
    cnt = 0
    for elem in arr :
        if elem == 0 :
            cnt += 1
    if cnt >= k :
        return 1
    return 0

n, k = map(int, input().split())
arr = list(map(int, input().split()))

robot_arr = [0] * n
ans = 0

while not is_break(k) :
    ans += 1
    container_move(n)
    robot_move(n)
    robot_up()

print(ans)

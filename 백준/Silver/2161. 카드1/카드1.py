import sys
input = sys.stdin.readline
from collections import deque

# 입력 처리
n = int(input())

# range를 이용하여 1부터 n까지 큐 선언
queue = deque(range(1, n+1))

# 동작을 판별할 변수 선언
# 홀수이면 제일 위에 있는 카드를 바닥에 버리는 동작,
# 짝수이면 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기는 동작.
cnt = 0

# 카드 옮기기
while queue :

    cnt += 1

    if cnt % 2 :                        # 홀수번째 동작이라면,
        print(queue.popleft(), end=' ') # 제일 위에 있는 카드를 바닥에 버리기.
    else :                              # 짝수번째 동작이라면,
        temp = queue.popleft()          # 제일 위에 있는 카드를
        queue.append(temp)              # 제일 아래에 있는 카드 밑으로 옮기


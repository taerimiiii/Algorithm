import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))  # 건물의 높이들

stack = [[0, 1000000]] # 건물높이, 건물번호
cnt = [0] * n       # i번째 건물에서 볼 수 있는 건물의 개수
result = [0] * n    # i번째 건물에서 볼 수 있는 건물 중 거리가 가장 가까운 건물의 번호 중 작은 번호
# 위에서 i번째는 인덱스+1 임. 주의.

# 정방향으로 돌면서 본인 기준 왼쪽에서 볼 수 있는 건물 구하기.
for i in range(n) :
    # 스택이 비어있지 않고, 건물의 높이가 스택의 맨 마지막 원소의 높이보다 크거나같을 경우
    while stack and arr[i] >= stack[-1][0] :
        stack.pop() # 본인보다 작거나같은 건물은 볼 수 없으므로, 마지막 원소를 삭제
    
    # 스택이 비어있지 않다면
    if stack :  
        result[i] = stack[-1][1]    # i번째 건물에서 볼 수 있는 건물 중 거리가 가장 가까운 건물은 스택의 맨 마지막 원소의 건물번호
        cnt[i] += len(stack)        # i번째 건물에서 볼 수 있는 건물의 개수는 스택의 길이만큼 더해짐.
    
    # 스택의 맨 마지막에 지금 건물높이와 건물번호 추가
    stack.append([arr[i], i+1])


# 스택 초기화
stack = [[0, 1000000]]

# 역방향으로 돌면서 본인 기준 오른쪽에서 볼 수 있는 건물 구하기.
for i in range(n-1, -1, -1) :
    # 스택이 비어있지 않고, 건물의 높이가 스택의 맨 마지막 원소의 높이보다 크거나같을 경우
    while stack and arr[i] >= stack[-1][0] :
        stack.pop() # 본인보다 작거나같은 건물은 볼 수 없으므로, 마지막 원소를 삭제
    
    # 스택이 비어있지 않다면
    if stack :
        # 오른쪽 인덱스는 스택의 마지막 원소의 건물번호 (=오른쪽 건물 번호)
        right_idx = stack[-1][1]
        
        # 정방향 탐색에서 가까운 건물을 찾지 못한 경우
        if result[i] == 0 :
            result[i] = right_idx   # i번째 건물에서 볼 수 있는 건물 중 거리가 가장 가까운 건물은 right_idx(스택의 맨 마지막 원소의 건물번호)
        
        # 정방향 탐색에서 가까운 건물을 찾은 경우
        else :
            # 왼쪽 인덱스는 정방향에서 찾은 가까운 건물번호 (=왼쪽 건물 번호)
            left_idx = result[i]
            
            # 왼쪽 건물이 현재 건물에서 떨어진 거리 구하기
            dist_left = (i + 1) - left_idx
            # 오른쪽 건물이 현재 건물에서 떨어진 거리 구하기
            dist_right = right_idx - (i + 1)
            
            # 만약 역방향 탐색에서 찾은 오른쪽 건물 거리가 왼쪽 건물 거리보다 가까운 경우,
            if dist_right < dist_left :
                result[i] = right_idx   # 오른쪽 건물 번호로 갱신.
            # 왼쪽과 오른쪽 거리가 동일한 경우 작은 번호를 출력하므로, < 연산을 사용해야 함. <= 연산을 사용하면 큰 번호인 오른쪽 번호를 출력하므로 틀림.
                
    # i번째 건물에서 볼 수 있는 건물의 개수 연산
    cnt[i] += len(stack)

    # 스택의 맨 마지막에 지금 건물높이와 건물번호 추가
    stack.append([arr[i], i+1])


# 출력 처리
for i in range(n) :
    # 건물에서 볼 수 있는 건물의 개수가 있다면
    if cnt[i] > 0 :
        print(cnt[i], result[i])    # 볼 수 있는 건물 개수와 가까운 건물 번호 중 작은 번호 출력

    # 건물에서 볼 수 있는 건물의 개수가 없다면
    else :
        print(cnt[i])


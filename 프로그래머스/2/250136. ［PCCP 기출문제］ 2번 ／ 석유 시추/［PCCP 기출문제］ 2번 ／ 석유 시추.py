from collections import deque
from collections import defaultdict

# 구현 문제. 접근은 아래와 같이 했습니다.
# 주어진 격자에는 석유 영역마다 고유 번호를 붙여 정보를 저장하고,
# 키: 석유 영역 번호, 값: 영역 크기 를 가지는 딕셔너리를 생성하여,
# 각 열을 set 처리하여 합을 계산한다.

# 격자 내부 범위인지 판단하는 함수
def in_range(x, y, n, m):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


def solution(land):
    
    n = len(land)       # 격자 세로 길이(row)
    m = len(land[0])    # 격자 가로 길이(col)
    
    visited = [ [False] * m for _ in range(n) ] # 격자 방문 여부 배열
    
    area_num = 2                # 석유 영역의 고유 번호. 격자가 0과 1로 주어지므로 구분을 위해 2부터 시작
    area_size = defaultdict()   # '키: 석유영역고유번호, 값: 영역크기' 를 가지는 딕셔너리
    
    dxs = [1, 0, -1, 0]         # 4방향 탐색
    dys = [0, 1, 0, -1]
    
    # 석유 영역 처리
    for i in range(n):
        for j in range(m):
            # 이번 격자에 석유가 있고, 방문한 적이 없다면, 석유 영역의 크기를 구한다.
            if land[i][j] == 1 and not visited[i][j]:
                # 영역 크기를 구하는데 필요한 변수 선언
                queue = deque()
                size = 1    # 영역 크기
                
                # 초기값 처리
                queue.append((i, j))
                visited[i][j] = True
                land[i][j] = area_num
                
                # 인접한 모든 석유 영역을 탐색
                while queue:
                    x, y = queue.popleft()
                    
                    for direct in range(4):
                        nx, ny = x + dxs[direct], y + dys[direct]
                        
                        # 인접한 격자가 내부에 위치해 있고, 석유가 있으며, 방문한 적이 없는 경우
                        if in_range(nx, ny, n, m) and land[nx][ny] == 1 and not visited[nx][ny]:
                            # 탐색 및 방문 처리
                            queue.append((nx, ny))
                            visited[nx][ny] = True 
                            land[nx][ny] = area_num
                            size += 1
                
                # 석유 영역을 나타내는 딕셔너리 갱신
                area_size[area_num] = size
                
                # 석유 고유 영역 번호 갱신
                area_num += 1

    # (디버깅) 구한 격자 출력문
    # for i in range(n):
    #     for j in range(m):
    #         print(land[i][j], end=' ')
    #     print()
    # print(area_size)
    
    
    total_area_len = len(area_size) # 석유 영역의 개수
    answer = 0                      # 정답 저장
    
    # 각 열에 시추관을 꽂아 뽑을 수 있는 석유 양 구하기 
    for col in range(m):
        visited_area = [False] * (total_area_len + 2)   # 석유영역고유번호가 2부터 시작하므로 +2
        curr_col_count = 0                       # 현재 열에서 뽑을 수 있는 석유 양을 저장할 변수
        
        for row in range(n):
            area_num = land[row][col]

            # 이번 격자에 석유가 있고, 이번 석유 영역을 방문하지 않은 경우
            if area_num != 0 and not visited_area[area_num]:
                # 방문 및 연산 처리
                visited_area[area_num] = True
                curr_col_count += area_size[area_num]
        
        # 정답 최대값으로 갱신
        answer = max(answer, curr_col_count)
                
    return answer

from collections import deque
from collections import defaultdict

def in_range(x, y, n, m):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def solution(land):
    
    n = len(land)
    m = len(land[0])
    
    visited = [ [False] * m for _ in range(n) ]
    
    area_num = 2
    area_size = defaultdict()
    
    # 격자에는 영역 번호를 저장
    # [영역번호] = 석유 크기 를 가지는 리스트 하나 생성
    # 격자 열을 set 하여 합을 계산
    
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                land[i][j] = area_num
                count = 1
                
                while queue:
                    x, y = queue.popleft()
                    
                    for direct in range(4):
                        nx, ny = x + dxs[direct], y + dys[direct]
                        if in_range(nx, ny, n, m) and land[nx][ny] == 1 and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            land[nx][ny] = area_num
                            count += 1
                
                area_size[area_num] = count
                area_num += 1


    # for i in range(n):
    #     for j in range(m):
    #         print(land[i][j], end=' ')
    #     print()
    # print(area_size)
    
    total_area_len = len(area_size)
    answer = 0
    
    for col in range(m):
        visited_area = [False] * (total_area_len+2)
        curr_col_count = 0
        
        for row in range(n):
            area_num = land[row][col]

            if area_num != 0:
                if not visited_area[area_num]:
                    visited_area[area_num] = True
                    curr_col_count += area_size[area_num]
        
        answer = max(answer, curr_col_count)
                
                
                    
    
    return answer

# land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
# print(solution(land))
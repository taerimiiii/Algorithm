from collections import deque

def bfs(start, n, graph, target_wire) :
    # 변수 선언
    queue = deque()
    visited = [False] * (n + 1)
    
    # 초기값 설정
    queue.append(start)
    visited[start] = True
    count = 1
    
    # bfs
    while queue :
        node = queue.popleft()
        for neighbor in graph[node] :
            # 끊어진 전선인 경우는 탐색을 건너뜀
            if (node == target_wire[0] and neighbor == target_wire[1]) or (node == target_wire[1] and neighbor == target_wire[0]) :
                continue
            
            # 방문하지 않은 노드이면, 방문 처리.
            if not visited[neighbor] :
                queue.append(neighbor)
                visited[neighbor] = True
                count += 1
                
    return count

def solution(n, wires) :
    # 입력처리
    graph = {i: [] for i in range(1, n + 1)}
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
        
    # 송전탑 개수의 차이(절대값) 저장 변수
    min_val = float('inf')
    
    # 모든 전선을 하나씩 끊어보며 탐색
    for wire in wires :
        cnt1 = bfs(wire[0], n, graph, wire)
        cnt2 = n - cnt1  # 반대편 전력망의 노드 개수
        
        # 정답 갱신
        min_val = min(min_val, abs(cnt1 - cnt2))
        
    return min_val
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()
    
    i = 0
    for priority in priorities:
        queue.append((priority, i))
        i += 1
    
    while queue:
        # 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼내기
        curr = queue.popleft()
        curr_priority = curr[0]
        curr_index = curr[1]
        
        # 더 높은 우선순위가 있는지 검사
        is_success = False
        for other in queue:
            if other[0] > curr_priority:
                is_success = True
                break  # 하나라도 더 높은 게 있으면 종료!
        
        if is_success:
            # 더 높은 우선순위가 있다면 맨 뒤로 보내기
            queue.append(curr)
        else:
            # 없다면 프로세스를 실행
            answer += 1
            
            # 원래 위치가 찾던 위치와 같다면 정답 반환
            if curr_index == location:
                return answer

    return answer
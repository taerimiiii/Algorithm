def solution(k, dungeons):
    
    def dfs(curr_k, cnt):
        answer = cnt
        
        for i in range(n):
            if not visited[i] and curr_k >= dungeons[i][0]:
                visited[i] = True
                answer = max(answer, dfs(curr_k - dungeons[i][1], cnt + 1))
                visited[i] = False
                
        return answer
    
    
    # 변수 선언
    n = len(dungeons)
    visited = [False] * n
            
    # dfs
    answer = dfs(k, 0)
    
    return answer
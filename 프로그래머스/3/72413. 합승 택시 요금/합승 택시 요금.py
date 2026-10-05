import sys

def solution(n, s, a, b, fares):
    # 아주 큰 값 설정
    INF = sys.maxsize
    
    # 그래프 선언
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
        
    # 그래프 초기값 설정
    for c, d, f in fares:
        graph[c][d] = f     # 양방향 처리
        graph[d][c] = f

    # 본인에게 가는 비용 처리
    for i in range(1, n + 1):
        graph[i][i] = 0     # 본인에게 오는 가장 저렴한 비용 = 0원
        
    # 플로이드 워셜
    for k in range(1, n + 1):           # k=중간지점=거쳐 가는 환승 지점
        for i in range(1, n + 1):       # i=시작지점
            for j in range(1, n + 1):   # j=도착지점
                if graph[i][k] + graph[k][j] < graph[i][j]: # 출발지점(i)->중간지점(k)->도착지점(j)가 현재 저장되어 있는 출발지점(i)->도착지점(j) 보다 작은 경우
                    graph[i][j] = graph[i][k] + graph[k][j] # 최솟값 갱신
                    
    # 최저 요금 구하기
    min_fare = INF
    for k in range(1, n + 1):   # k=중간지점=합승이 끝나는 지점
        # 출발지(s) -> 환승지(i) 비용 + 환승지(i) -> A집(a) 비용 + 환승지(i) -> B집(b) 비용
        curr_fare = graph[s][k] + graph[k][a] + graph[k][b]
        # 최솟값 갱신
        if curr_fare < min_fare:
            min_fare = curr_fare
            
    return min_fare


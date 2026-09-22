def solution(n, s, a, b, fares):
    # 무한대 값 설정 (최대 요금 100,000 * 최대 노드 수 200 보다 큰 값)
    INF = int(1e9)
    
    # 2차원 거리 배열 초기화
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    # 간선 정보(fares)를 바탕으로 초기 요금 설정 (양방향)
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
        
    # 플로이드 워셜 알고리즘 수행
    # k: 거쳐 가는 환승 지점
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # 최저 예상 요금 찾기
    min_fare = INF
    
    # i를 합승이 끝나는 지점(헤어지는 지점)으로 가정
    for i in range(1, n + 1):
        # 출발지(s) -> 환승지(i) 비용 + 환승지(i) -> A집(a) 비용 + 환승지(i) -> B집(b) 비용
        fare = dist[s][i] + dist[i][a] + dist[i][b]
        if fare < min_fare:
            min_fare = fare
            
    return min_fare
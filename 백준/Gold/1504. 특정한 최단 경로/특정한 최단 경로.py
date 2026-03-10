import sys
input = sys.stdin.readline
import heapq

# 1번 -> A -> B -> N번
# 1번 -> B -> A -> N번

# 가중치는 양수이므로 두 정점 간의 최단거리에서 사이클이 생길 수는 없음
# 1번에서 A, B 가는 최단거리 구하는 다익스트라 1번 돌리고,
# A, B 간 최단거리 구하는 다익스트라 1번 돌리고,
# N번에서 A, B 가는 최단거리 구하는 다익스트라 1번 돌린다.
# 양방향이므로 문제 없음.
# 그리고 둘 중 최솟값 구하기

# 시간복잡도 계산
# E * log(V)
# 대충 200,000 * 10
# 한 번에 이백만번 세번 돌면 육백만번 

MAXVAL = sys.maxsize

def dijkstra(start, graph) :
    queue = [(start, 0)]
    distances = [MAXVAL] * (n+1)

    while queue :
        curr_node, curr_distance = heapq.heappop(queue)

        if distances[curr_node] < curr_distance :
            continue

        for neighboor, weight in graph[curr_node] :
            distance = curr_distance + weight
            if distances[neighboor] > distance :
                distances[neighboor] = distance
                heapq.heappush(queue, (neighboor, distance))

    return distances

def is_going(target) :
    if target == MAXVAL :
        return False
    return True

n, e = map(int, input().split())

graph = {i:[] for i in range(1, n+1)}

for i in range(e) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

one_distances = dijkstra(1, graph)
one_to_v1 = one_distances[v1]
one_to_v2 = one_distances[v2]

v1_to_v2 = dijkstra(v1, graph)[v2]

n_distances = dijkstra(n, graph)
n_to_v1 = n_distances[v1]
n_to_v2 = n_distances[v2]

min_val = MAXVAL
if is_going(one_to_v1) and is_going(v1_to_v2) and is_going(n_to_v2) :
    if v1 == 1 and v2 == n :
        min_val = min(min_val, v1_to_v2)
    elif v1 == 1 :
        min_val = min(min_val, v1_to_v2 + n_to_v2)
    elif v2 == n :
        min_val = min(min_val, one_to_v1 + n_to_v2)
    else :
        min_val = min(min_val, one_to_v1 + v1_to_v2 + n_to_v2)
if is_going(one_to_v2) and is_going(v1_to_v2) and is_going(n_to_v1) :
    if v1 == 1 and v2 == n :
        min_val = min(min_val, v1_to_v2)
    elif v1 == 1 :
        min_val = min(min_val, v1_to_v2 + n_to_v1)
    elif v2 == n :
        min_val = min(min_val, one_to_v2 + n_to_v1)
    else :
        min_val = min(min_val, one_to_v2 + v1_to_v2 + n_to_v1)

if min_val == MAXVAL :
    print(-1)
else :
    print(min_val)
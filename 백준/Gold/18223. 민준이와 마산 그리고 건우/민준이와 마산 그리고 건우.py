import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, distance):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

n, m, friend = map(int, input().split())
graph= [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = 1_000_000_000
distance = [INF] * (n+1)
distance_friendship = [INF] * (n+1)

dijkstra(1, distance)
dijkstra(friend, distance_friendship)

least_distance = distance[n]
passpoint_distance = distance_friendship[1] + distance_friendship[n]

if least_distance == passpoint_distance:
    print("SAVE HIM")
else:
    print("GOOD BYE")
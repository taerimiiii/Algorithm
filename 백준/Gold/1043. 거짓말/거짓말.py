import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, graph) :
    queue = deque()
    visited = [False] * (n+1)
    queue.append(start)
    visited[start] = True

    while queue :
        node = queue.popleft()
        for neighboor in graph[node] :
            if not visited[neighboor] :
                queue.append(neighboor)
                visited[neighboor] = True

    return visited


n, m = map(int, input().split())
know = list(map(int, input().split()))
know_num = know[0]

people = {i:[] for i in range(n+1)}
for i in range(1, know_num) :
    people[know[i]].append(know[i+1])
    people[know[i+1]].append(know[i])

parties = [list(map(int, input().split())) for _ in range(m)]
for i in range(m) :
    party = parties[i]
    party_num = party[0]

    for j in range(1, party_num) :
        if party[j+1] not in people[party[j]] :
            people[party[j]].append(party[j+1])
            people[party[j+1]].append(party[j])

#print(people)

if know_num == 0 :
    start_node = 0
else :
    start_node = know[1]

is_normal_talk = bfs(start_node, people)
#print(is_normal_talk)

answer = 0
for i in range(m) :
    party = parties[i]
    party_num = party[0]

    success = True
    for j in range(1, party_num+1) :
        if is_normal_talk[party[j]] :
            success = False
            break
    
    if success :
        answer += 1
        #print("답", i)

print(answer)

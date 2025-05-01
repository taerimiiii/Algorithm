n, m = map(int, input().split())

listen = [input() for _ in range(n)]
see = [input() for _ in range(m)]

answer = list(set(listen) & set(see))
answer.sort()

print(len(answer))
for elem in answer :
    print(elem)
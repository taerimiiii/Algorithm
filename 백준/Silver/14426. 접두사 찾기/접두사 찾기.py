n, m = map(int, input().split())
target = [input() for _ in range(n)]
test = [input() for _ in range(m)]

target.sort()
test.sort()

answer = 0
i, j = 0, 0
while i < n and j < m :
    if target[i][:len(test[j])] == test[j] :
        answer += 1
        j += 1
    elif target[i] > test[j] :
        j += 1
    elif target[i] < test[j] :
        i += 1

print(answer)
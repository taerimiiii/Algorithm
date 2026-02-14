import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    people = [ list(map(int, input().split())) for _ in range(n) ]

    people.sort(key=lambda x: x[0])

    min_val = people[0][1]
    answer = 1
    for i in range(1, n) :
        if people[i][1] < min_val :
            min_val = people[i][1]
            answer += 1
    
    print(answer)
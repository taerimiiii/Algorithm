import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n) :
    ox = input().strip()
    ox_len = len(ox)
    score = 0
    count = 0

    for i in range(ox_len) :
        if ox[i] == "O" :
            count += 1
            score += count
        else :
            count = 0
    
    print(score)
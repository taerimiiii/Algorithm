import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_score = max(arr)

answer = []
for score in arr :
    answer.append(score / max_score * 100)
avg = sum(answer) / n
print(avg)
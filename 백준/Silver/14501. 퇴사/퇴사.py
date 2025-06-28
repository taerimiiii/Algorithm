from sys import stdin
input = stdin.readline

def back_tracking(x) :
    #print(answer)
    if x+arr[x][0] >= n or (possible_day[x+arr[x][0]] == 0 and x+arr[x][0] >= possible_n):
        #print("조건에 걸림", answer)
        sum_val = 0
        for elem in answer :
            sum_val += arr[elem][1]
        temp.append(sum_val)
        return

    for i in range(x+arr[x][0], n) :
        if possible_day[i] and (i not in answer):
            answer.append(i)
            back_tracking(i)
            answer.pop()
        

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
possible_day = [1] * n

# 그만두어 상담을 못하는 경우
for i in range(n) :
    if arr[i][0] + i > n :
        possible_day[i] = 0

possible_n = n
for i in range(n-1, -1, -1) :
    if possible_day[i] :
        possible_n = i + 1
        break

# 1일 일을 하는 경우, 2일 일을 하는 경우, 3일 일을 하는 경우... 마지막 날 까지 반복
max_val = 0
for start in range(possible_n) :
    if possible_day[start] :
        answer = [start]
        temp = []
        back_tracking(start)
        max_val = max(max(temp), max_val)
        #print(start, max_val)

print(max_val)

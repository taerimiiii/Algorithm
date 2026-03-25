import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# i개 말이 참이라고 말하는 수를 저장하는 배열
count_arr = [0] * (n+1)

for i in range(n) :
    # 옳다는 말이 한 말의 개수를 넘으면 무조건 틀림
    if arr[i] > n :
        continue

    count_arr[arr[i]] += 1

success = False
for i in range(n, -1, -1) :
    if i == count_arr[i] :
        success = True
        answer = i
        break

if success :
    print(answer)
else :
    print(-1)
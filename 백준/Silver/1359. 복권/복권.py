import sys
input = sys.stdin.readline
from itertools import combinations as cb

# 입력 처리
n, m, k = map(int, input().split())

# 탐색할 숫자 목록
number_list = list(range(n))

# 조건을 만족하는 당첨 횟수
correct_cb = 0

# 조합 탐색. number_list에서 m개를 뽑는 모든 경우의 수를 확인
for cb_num_list in cb(number_list, m) :

    # 이번 조합에서 맞힌 수의 개수
    cnt = 0

    # 뽑힌 조합 안에 있는 숫자들을 하나씩 꺼내어 확인
    for num in cb_num_list :
        # 그 숫자가 m보다 작다면 카운트를 올린다
        if num < m :
            cnt += 1

    # 맞힌 수가 k개를 넘는다면 당첨 횟수를 올린다
    if cnt >= k :
        correct_cb += 1

# 전체 경우의 수
all_cb = len(list(cb(number_list, m)))

# 출력
print(correct_cb / all_cb)
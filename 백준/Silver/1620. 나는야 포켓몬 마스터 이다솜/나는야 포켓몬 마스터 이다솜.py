import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 번호로 이름을 찾기 위한 리스트 (1번 인덱스부터 사용)
arr = [''] * (n + 1)

# 이름으로 번호를 찾기 위한 딕셔너리
name_to_num = {}

for i in range(1, n + 1) :
    name = input().strip()
    arr[i] = name             # 인덱스(번호)에 이름 저장
    name_to_num[name] = i     # 문자열(이름)을 Key로, 번호를 Value로 저장

# 검사해야 하는 문제들 입력
problems = [ input().strip() for _ in range(m) ]

# 답 구하기
for i in range(m) :
    problem = problems[i]
    
    if '1' <= problem <= '999999' :
        # 입력이 숫자인 경우, 리스트에서 인덱스로 바로 접근
        print(arr[int(problem)])

    else :
        # 입력이 문자인 경우, 딕셔너리에서 Key(이름)로 바로 접근
        print(name_to_num[problem])
import sys
input = sys.stdin.readline

# 음계 8개를 저장할 리스트와 상태를 체크할 변수 선언
# C++의 배열 입력을 시뮬레이션하기 위해 입력을 한 번에 리스트로 받습니다.
arr = list(map(int, input().split()))
asc = 0 # 오름차순 확인용 변수
dsc = 0 # 내림차순 확인용 변수

# 반복문을 통해 8개의 숫자의 순서를 확인한다.
for i in range(8):
    
    # 현재 숫자가 순서대로(1, 2, 3...) 들어있는지 확인
    if arr[i] == i + 1:
        asc += 1
    # 현재 숫자가 역순으로(8, 7, 6...) 들어있는지 확인
    elif arr[i] == 8 - i:
        dsc += 1

# 조건문을 통해 카운트 결과에 따라 결과값을 출력한다.
# 8개 음이 모두 순서대로라면 ascending
if asc == 8:
    print("ascending")
# 8개 음이 모두 역순이라면 descending
elif dsc == 8:
    print("descending")
# 둘 다 아니라면 mixed
else:
    print("mixed")
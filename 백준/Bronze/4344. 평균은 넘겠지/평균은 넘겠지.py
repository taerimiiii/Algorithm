import sys
input = sys.stdin.readline

# C 입력처리
c = int(input())

# 
for _ in range(c) :
    test_case = list(map(int, input().split()))
    student_num = test_case[0]
    scores = test_case[1:]

    average = sum(scores) / student_num

    count = 0
    for i in range(student_num) :
        if scores[i] > average :
            count += 1
    
    rate = count / student_num * 100

    print(f"{round(rate, 3)}%")
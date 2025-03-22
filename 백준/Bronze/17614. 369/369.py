n = int(input())
answer = ['3', '6', '9']

cnt = 0
for string in range(1, n + 1) :
    number = str(string)
    for digit in number :
        if digit in answer :
            cnt += 1
print(cnt)
string = input()
lenth = len(string)

cnt = 0
for elem in string :
    if elem == ' ' :
        cnt += 1

if string[0] == ' ' :
    cnt -= 1
if string[lenth - 1] == ' ' :
    cnt -= 1

print(cnt + 1)
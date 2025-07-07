from sys import stdin
input = stdin.readline

while 1 :
    n = input()
    if n == "0\n" :
        break

    length = len(n) - 1
    success = 1
    for i in range(length // 2) :
        if n[i] != n[length - i - 1] :
            success = 0
            break

    if success :
        print('yes')
    else :
        print('no')
        

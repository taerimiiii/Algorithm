import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    p = input().strip()
    n = int(input())
    arr = list(input().split(','))
    if n == 0 :
        arr = []
    elif n == 1 :
        arr[0] = arr[0][1:-2]
    else :
        arr[0] = arr[0][1::]
        arr[-1] = arr[-1][0:-2]
    #print(arr)

    p_len = len(p)
    direct = 0 # 짝수 앞, 홀수 뒤
    success = True
    for i in range(p_len) :
        if p[i] == 'R' :
            direct += 1
        else :
            if len(arr) == 0 :
                success = False
                break
            if direct % 2 :
                arr.pop()
            else :
                arr.pop(0)
    
    if success :
        arr_len = len(arr)
        if direct % 2 :
            print('[', end='')
            for i in range(arr_len-1, -1, -1) :
                print(arr[i], end='')
                if i != 0 :
                    print(',', end='')
            print(']')
        else :
            print('[', end='')
            for i in range(arr_len) :
                print(arr[i], end='')
                if i != arr_len - 1 :
                    print(',', end='')
            print(']')
    else :
        print("error")
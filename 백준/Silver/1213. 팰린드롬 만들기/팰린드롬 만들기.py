import sys
input = sys.stdin.readline

name = input().strip()
length = len(name)

arr = sorted([name[i] for i in range(length)])
answer = [''] * (length // 2)
success = True

# print(arr.pop(0))

if length % 2 == 0 :
    for i in range(length // 2) :
        if arr[i * 2] != arr[i * 2 + 1] :
            success = False
            break
        answer[i] = arr[i*2]
    if success :
        for i in range(length // 2) :
            print(answer[i], end='')
        for i in range(length // 2 - 1, -1, -1) :
            print(answer[i], end='')
    else :
        print("I\'m Sorry Hansoo")

else :
    idx = 0
    odd_cnt = 0
    for i in range(length//2+1) :
        if len(arr) == 1 or arr[0] != arr[1] :
            if odd_cnt != 0 :
                success = False
                break
            odd_cnt += 1
            odd = arr[0]
            arr.pop(0)

        else :
            answer[idx] = arr[0]
            idx += 1
            arr.pop(0)
            arr.pop(0)
        # else :
        #     if odd_cnt != 0 :
        #         success = False
        #         break
        #     odd_cnt += 1
        #     odd = arr[0]
        #     arr.pop(0)
    if success :
        for i in range(length // 2) :
            print(answer[i], end='')
        print(odd, end='')
        for i in range(length // 2 - 1, -1, -1) :
            print(answer[i], end='')
    else :
        print("I\'m Sorry Hansoo")
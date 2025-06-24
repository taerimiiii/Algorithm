from sys import stdin
input = stdin.readline

def back_tracking(x) :
    if x == 6 :
        for elem in answer :
            print(elem, end = ' ')
        print()
        return

    for j in range(k) :
        if arr[j] not in answer and (len(answer) == 0 or arr[j] > answer[-1]):
            answer.append(arr[j])
            back_tracking(x + 1)
            answer.pop()


arr_2d = []
while 1 :
    temp = list(map(int, input().split()))
    if temp[0] == 0 :
        break
    arr_2d.append(temp)


arr2d_lenth = len(arr_2d)
for i in range(arr2d_lenth) :
    answer = []
    arr = arr_2d[i]
    k = arr.pop(0)
    arr.sort()
    back_tracking(0)
    print()

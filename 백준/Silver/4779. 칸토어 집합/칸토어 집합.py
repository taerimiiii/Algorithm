import sys
input = sys.stdin.readline

def back_tracking(start, end) :
    global arr
    curr_n = (end - start + 1) // 3

    if curr_n == 0 :
        return
    
    mid_start = start + curr_n
    mid_end = mid_start + curr_n

    for i in range(mid_start, mid_end) :
        arr[i] = " "

    back_tracking(start, mid_start - 1)
    back_tracking(mid_end, end)


while True :
    try :
        n = int(input())
    except :
        break
    

    arr = ["-"] * (3 ** n)
    start = 0
    end = 3 ** n - 1
    
    back_tracking(start, end)
    for elem in arr :
        print(elem, end='')
    print()
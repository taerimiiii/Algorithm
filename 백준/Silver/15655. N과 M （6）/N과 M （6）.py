import sys
input = sys.stdin.readline

def back_tracking(x) :
    if len(answer) == m :
        for elem in answer :
            print(elem, end=' ')
        print()
        return

    for i in range(x, n) :
        answer.append(arr[i])
        back_tracking(i+1)
        answer.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

answer = []

back_tracking(0)
import sys
input = sys.stdin.readline

def back_tracking(x) :
    if len(arr) == m :
        for elem in arr :
            print(elem, end=' ')
        print()
        return

    for i in range(1, n+1) :
        if visited[i] :
            continue
        arr.append(i)
        visited[i] = True
        back_tracking(i+1)
        arr.pop()
        visited[i] = False

n, m = map(int, input().split())

arr = []
visited = [False] * (n+1)

back_tracking(1)
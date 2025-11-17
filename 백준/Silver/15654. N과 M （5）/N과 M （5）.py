import sys
input = sys.stdin.readline

def back_track(path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    for i in range(n):
        if arr[i] not in path:
            path.append(arr[i])
            back_track(path)
            path.pop()
            

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

back_track([])
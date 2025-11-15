import sys
input = sys.stdin.readline

def back_track(depth, start):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, n + 1):
        answer.append(i)
        back_track(depth + 1, i)
        answer.pop()

n, m = map(int, input().split())
answer = []

back_track(0, 1)
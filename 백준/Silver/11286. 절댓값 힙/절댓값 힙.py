import sys
input = sys.stdin.readline
import heapq

n = int(input())
arr = []
for _ in range(n) :
    x = int(input())
    if x == 0 :
        if len(arr) == 0 :
            print(0)
        else :
            out = heapq.heappop(arr)
            # print("out", out)
            if out > int(out) :
                print(int(out))
            else :
                print(int(out) * (-1))
    else :
        if x < 0 :
            x = x * (-1) + 0.0
        else :
            x = x + 0.1
        heapq.heappush(arr, x)
        
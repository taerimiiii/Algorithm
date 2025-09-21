import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
baseball = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
num, strike, ball = "", 0, 0

for _ in range(n):
    num, strike, ball = input().split()
    strike, ball = int(strike), int(ball)

    delete = []
    for i in range(len(baseball)):
        s, b = 0, 0
        
        for j in range(3):
            if int(num[j]) in baseball[i]:
                if baseball[i][j] == int(num[j]) :
                    s += 1
                else :
                    b += 1

        if s != strike or b != ball :
            delete.append(baseball[i])

    for elem in delete:
        baseball.remove(elem)

print(len(baseball))
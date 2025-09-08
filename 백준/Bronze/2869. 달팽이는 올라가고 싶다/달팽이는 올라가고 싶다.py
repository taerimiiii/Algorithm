import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

curr_h = 0
height = a - b
last_v = v - a

answer = 0
if last_v % height > 0 :
  answer += 1
answer += last_v // height + 1

print(answer)
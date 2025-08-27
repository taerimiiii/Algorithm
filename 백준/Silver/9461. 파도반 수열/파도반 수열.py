import sys
input = sys.stdin.readline

sequence = [1] * 101
sequence[4] = 2
sequence[5] = 2
for i in range(6, 101) :
  sequence[i] = sequence[i-1] + sequence[i-5]

t = int(input())
for _ in range(t) :
  n = int(input())
  print(sequence[n])
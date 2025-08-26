import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case) :
  n = int(input())
  group = {}
  for _ in range(n) :
    value, key = input().split()
    if key not in group :
      group[key] = []
    group[key].append(value)
  
  cnt = 1
  for key in group :
    cnt *= len(group[key]) + 1
  print(cnt - 1)
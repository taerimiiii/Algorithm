import sys
input = sys.stdin.readline

d, k = map(int, input().split())

success = 0
for a in range(1, k) : # 1, k
  if success :
    break
  for b in range(a, k) : # a, k
    num1, num2 = a, b
    sum_val = 0
    for i in range(d-2) :
      sum_val = num1 + num2
      num1, num2 = num2, sum_val
    if sum_val > k :
      break
    elif sum_val == k :
      print(a)
      print(b)
      success = 1
      break

import sys
input = sys.stdin.readline

while 1 :
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0 :
    break
  else :
    max_len = max(a, b, c)
    if max_len == a :
      if a**2 == b**2 + c**2 :
        print("right")
      else :
        print("wrong")
    elif max_len == b :
      if b**2 == a**2 + c**2 :
        print("right")
      else :
        print("wrong")
    else :
      if c**2 == a**2 + b**2 :
        print("right")
      else :
        print("wrong")
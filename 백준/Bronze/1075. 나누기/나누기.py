n = int(input())
f = int(input())

n = n - (n%100)

while True:
  if n % f == 0:
    break
  else:
    n += 1

print(str(n)[-2:])

N, m, M, T, R = map(int, input().split())

time = 0
now = m
if m + T > M :
  print(-1)
else:
  while True:
    if N == 0:
      break
    if now + T <= M:
      now += T
      N -= 1
    elif now - R < m:
      now = m
    elif now - R >= m:
      now -= R

    time += 1

  print(time)
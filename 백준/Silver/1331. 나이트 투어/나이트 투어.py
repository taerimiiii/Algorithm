import sys
input = sys.stdin.readline

def check_valid(curr, next) :
  if abs(ord(curr[0]) - ord(next[0])) == 2 and abs(int(curr[1]) - int(next[1])) == 1 :
    return 1
  elif abs(ord(curr[0]) - ord(next[0])) == 1 and abs(int(curr[1]) - int(next[1])) == 2 :
    return 1
  else:
    return 0

curr = input().strip()
arr = [curr]
move = [input().strip() for _ in range(35)]

cnt = 1
for i in range(35) :
  next = move[i]
  arr.append(next)

  if check_valid(curr, next) == 1 :
    cnt += 1
    curr = next
  else:
    break

if cnt == 36 and len(set(arr))== 36 and check_valid(arr[0], arr[-1]) :
  print('Valid')
else:
  print('Invalid')
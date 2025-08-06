import sys
input = sys.stdin.readline

def get_num(arr_sorted, x) :
  length = len(arr_sorted)
  left, right = 0, length
  mid = (left + right) // 2
  while mid >= left :
    if arr_sorted[mid][1] == x :
      return arr_sorted[mid][0]
    elif arr_sorted[mid][1] < x :
      left = mid + 1
    else :
      right = mid - 1
    mid = (left + right) // 2
  return 0


n, m = map(int, input().split())
arr = [ [i+1, ''] for i in range(n)]

for i in range(n) :
  arr[i][1] = input().strip()

arr_sorted = sorted(arr, key=lambda x: x[1])

problems = [ input().strip() for _ in range(m)]

for i in range(m) :
  problem = problems[i]
  if '1' <= problem <= '999999' :
    print(arr[int(problem)-1][1])
  else :
    print(get_num(arr_sorted, problem))

import sys
input = sys.stdin.readline

def binary_search(left, right, target) :
  while left <= right : # 왼이 오른 넘어갈 때가 최대
    mid = (left + right) // 2
    cnt = 0
    for elem in arr :
      cnt += elem // mid
    
    if cnt < target : # 길이가 너무 짧으면, 오른+1
      right = mid - 1
    else :            # 길이가 타겟에 적절하거나 긴 경우
      left = mid + 1  # 1. 길이가 타겟에 적절한 경우, 최대값을 구하기 위해 왼+1.
                      #    어느 순간 왼이 오른을 넘어가면, 그때의 오른 값이 최대값. 
                      # 2. 길이가 길면, 왼+1
  return right

k, n = map(int, input().split())
arr = sorted([int(input()) for _ in range(k)])

max_val = max(arr)
print(binary_search(1, max_val, n))
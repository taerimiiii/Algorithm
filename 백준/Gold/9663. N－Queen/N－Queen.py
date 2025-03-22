n = int(input())

arr = [0] * n

def is_possible(curr_row):
    for front_row in range(curr_row):
        if arr[curr_row] == arr[front_row] or abs(curr_row - front_row) == abs(arr[curr_row] - arr[front_row]):
            return False
    return True 

def dfs(row):
    if row == n:
        return 1
    
    ans = 0
    for col in range(n):
        arr[row] = col #[row, col]에 퀸 두기
        if is_possible(row):
            ans += dfs(row + 1)
    return ans

print(dfs(0))
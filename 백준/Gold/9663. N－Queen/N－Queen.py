import sys
input=sys.stdin.readline

def is_success(curr_row) :
    for front_row in range(curr_row) :
        if arr[front_row] == arr[curr_row] or curr_row - front_row == abs(arr[curr_row] - arr[front_row]) :
            return False
    return True

def dfs(row) :
    if row == n :
        return 1
    
    ans = 0
    for col in range(n) :
        arr[row] = col
        if is_success(row) :
            ans += dfs(row+1)

    return ans

n = int(input())

arr = [0] * n

print(dfs(0))
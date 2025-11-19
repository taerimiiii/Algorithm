def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember = nums[i]
            dfs()
            visited[i] = False
            temp.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

dfs()
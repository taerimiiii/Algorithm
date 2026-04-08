n = int(input())
games = []
for _ in range(n):
    game = list(map(int,input().split()))
    games.append(game)

for i in range(n):
    ans = 0
    for j in range(3):
        cur = games[i][j]
        check = 1 
        for k in range(n):
            if k == i:
                continue
                # 중복 체크 
            if games[k][j] == cur:
                check = 0;
                break
        if check == 1 : 
            ans += cur
    print(ans)
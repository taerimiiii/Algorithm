def solution(grid):
    
    def next_xy(x, y, direct) :
        nx = x + dxs[direct]
        ny = y + dys[direct]
        if not in_range(nx, ny) :
            x = nx % row
            y = ny % col
            return x, y
        return nx, ny
    
    def next_direct(x, y, direct):
        if grid[x][y] == 'S':
            direct = direct
        elif grid[x][y] == 'L':
            direct = (direct + 3) % 4
        else:
            direct = (direct + 1) % 4
        return direct
    
    def in_range(x, y):
        if 0 <= x < row and 0 <= y < col:
            return True
        return False

    def len_cycle(x, y, direct):
        cnt = 1
        target_x, target_y, target_direct = x, y, direct
        
        while True:
            x, y = next_xy(x, y, direct)
            direct = next_direct(x, y, direct)
            visited[x][y][direct] = True
            
            if target_x == x and target_y == y and target_direct == direct:
                break
                
            cnt += 1
        
        return cnt
    
    answer = []
    
    row = len(grid)
    col = len(grid[0])
    
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    
    visited = [ [[False] * 4 for _ in range(col)] for _ in range(row) ]
    
    for i in range(row):
        for j in range(col):
            for d in range(4):
                if not visited[i][j][d]:
                    visited[i][j][d] = True
                    answer.append(len_cycle(i, j, d))
    
    answer.sort()
    
    return answer
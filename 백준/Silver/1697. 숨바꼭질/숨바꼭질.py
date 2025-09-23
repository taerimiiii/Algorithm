import sys
input = sys.stdin.readline

n, k = map(int, input().split())

search = [n]
sec = 0
visited = [False] * 100001

# 이동 처리 함수
def move(pos, nxt, locations):
    if 0 <= nxt <= 100000 and not visited[nxt]:
        if nxt == k:
            return True
        visited[nxt] = True
        locations.append(nxt)
    return False

if n == k:
    print(0)
else:
    success = True
    while success:
        locations = []
        sec += 1
        for elem in search:
            # 세 가지 이동을 함수로 처리
            if move(elem, elem + 1, locations): 
                success = False
                break
            if move(elem, elem - 1, locations): 
                success = False
                break
            if move(elem, elem * 2, locations): 
                success = False
                break
        search = locations

    print(sec)
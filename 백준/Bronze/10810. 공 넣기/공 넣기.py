import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 0번부터 N번까지 바구니들
# 실제로 사용하는 건 1번부터 N번까지 바구니
baskets = [0] * (n+1)

for _ in range(m) :
    i, j, k = map(int, input().split())
    for idx in range(i, j+1) :
        baskets[idx] = k

for number in baskets[1:] :
    print(number, end=' ')
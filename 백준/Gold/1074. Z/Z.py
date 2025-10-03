import sys
input = sys.stdin.readline

def z(n, r, c):
    # n: 현재 2^n 크기의 정사각형
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    size = half * half

    # 1사분면 (좌상단)
    if r < half and c < half:
        return z(n - 1, r, c)

    # 2사분면 (우상단)
    elif r < half and c >= half:
        return size + z(n - 1, r, c - half)

    # 3사분면 (좌하단)
    elif r >= half and c < half:
        return 2 * size + z(n - 1, r - half, c)

    # 4사분면 (우하단)
    else:
        return 3 * size + z(n - 1, r - half, c - half)

n, r, c = map(int, input().split())
print(z(n, r, c))

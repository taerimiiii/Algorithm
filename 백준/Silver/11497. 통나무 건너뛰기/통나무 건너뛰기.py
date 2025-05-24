for _ in range(int(input())):

    n = int(input())
    array = sorted(list(map(int, input().split())))
    height = 0

    for i in range(2, n):
        height = max(height, abs(array[i] - array[i - 2]))

    print(height)
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
m = int(input())

not_sort_num = 0
s_sort = [True] * n
for i in range(n) :
    if s[i] != i :
        not_sort_num += 1
        s_sort[i] = False

for _ in range(m) :
    x, y = map(int, input().split())

    if x != y :
        if s[x] == x :
            prev_x = True
        else :
            prev_x = False

        if s[y] == y :
            prev_y = True
        else :
            prev_y = False

        s[x], s[y] = s[y], s[x]

        if s[x] == x :
            curr_x = True
        else :
            curr_x = False

        if s[y] == y :
            curr_y = True
        else :
            curr_y = False
            
        if prev_x and not curr_x :
            not_sort_num += 1
        elif not prev_x and curr_x :
            not_sort_num -= 1

        if prev_y and not curr_y :
            not_sort_num += 1
        elif not prev_y and curr_y :
            not_sort_num -= 1

    if not_sort_num == 0 :
        print(0, end=' ')
    elif n == 2 :
        print(1, end=' ')
    else :
        print(-1, end=' ')

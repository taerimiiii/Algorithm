from sys import stdin
input = stdin.readline


string = input()

ans = 0
for i in range(65, 91) :
    for j in range(i+1, 91) :
        x = chr(i)
        y = chr(j)

        cnt_x, cnt_y = 0, 0
        for k in range(52) :
            if string[k] == x and cnt_x == 1:
                x2 = k
                cnt_x = 2
            elif string[k] == y and cnt_y == 1 :
                y2 = k
                cnt_y = 2
            elif string[k] == x :
                x1 = k
                cnt_x = 1
            elif string[k] == y :
                y1 = k
                cnt_y = 1
            elif cnt_x == 2 and cnt_y == 2:
                break

        if (y1 < x2 < y2 and x1 < y1) or (x1 < y2 < x2 and y1 < x1) :
            #print(x1, x2, y1, y2)
            ans += 1

print(ans)
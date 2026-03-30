import sys
input = sys.stdin.readline

string1 = input().strip()
string2 = input().strip()
len_string1 = len(string1)
len_string2 = len(string2)

# dp 만들기
dp = [ [0] * (len_string2 + 1) for _ in range(len_string1 + 1) ]
for i in range(1, len_string1 + 1) :
    for j in range(1, len_string2 + 1) :
        if string1[i-1] == string2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


if max(dp[-1]) != 0 :

    point1 = len_string1
    point2 = len_string2

    answer = ""

    while True :
        if dp[point1][point2] == 0 :
            break

        if dp[point1][point2] == dp[point1-1][point2] :
            point1 -= 1

        elif dp[point1][point2] == dp[point1][point2-1] :
            point2 -= 1

        elif ((dp[point1][point2]-1) == dp[point1-1][point2-1]) :
            point1 -= 1
            point2 -= 1
            answer += string2[point2]

    print(len(answer))
    print(answer[::-1])

else :
    print(0)
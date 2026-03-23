import sys
input = sys.stdin.readline

string1 = input().strip()
string2 = input().strip()
string1_len = len(string1)
string2_len = len(string2)

# dp 만들기
dp = [ [0] * (string2_len + 1) for _ in range(string1_len + 1) ]
for i in range(1, string1_len + 1) :
    for j in range(1, string2_len+1) :
        if string1[i-1] == string2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


if max(dp[-1]) != 0 :

    start1 = string1_len
    start2 = string2_len

    answer = ""

    while True :
        if dp[start1][start2] == 0 :
            break

        if dp[start1][start2] == dp[start1-1][start2] :
            start1 -= 1

        elif dp[start1][start2] == dp[start1][start2-1] :
            start2 -= 1

        elif ((dp[start1][start2]-1) == dp[start1-1][start2-1]) :
            start1-=1
            start2-=1
            answer += string2[start2]

    print(len(answer))

else :
    print(max(dp[-1]))

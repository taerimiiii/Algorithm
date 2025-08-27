import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = int(input())

max_val = 23*3600 + 59*60 + 60
to_sec = a*3600 + b*60 + c
ans_to_sec = (to_sec + d) % max_val

ans_a = ans_to_sec // 3600
ans_b = (ans_to_sec % 3600) // 60
ans_c = ans_to_sec % 3600 % 60

print(ans_a, ans_b, ans_c)
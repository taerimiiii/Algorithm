import sys
input=sys.stdin.readline

n = input().strip()

num_list = [0] * 10

for num in n :
    num_list[int(num)] += 1

num_list[6] = num_list[9] = (num_list[6] + num_list[9] + 1) // 2

print(max(num_list))
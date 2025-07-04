arr = list(map(int, input().split()))
sum_val = 0
for elem in arr :
	sum_val += elem * elem
print(sum_val % 10)
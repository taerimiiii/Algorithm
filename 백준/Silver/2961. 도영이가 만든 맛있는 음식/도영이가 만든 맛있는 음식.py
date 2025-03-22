from itertools import combinations

n = int(input())
input_arr=[list(map(int,input().split())) for _ in range(n)]

result = 1000000000

for cmbs in [combinations(input_arr, i) for i in range(1, n + 1)]:
    for c in cmbs:
        s_val, b_val = 1, 0
        for s, b in c:
            s_val *= s
            b_val += b
        result = min(result, abs(s_val - b_val))
        
print(result)
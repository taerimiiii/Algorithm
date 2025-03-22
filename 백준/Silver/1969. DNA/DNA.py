def get_max() :
    max_index = 0
    max_val = DNA_count[0]
    for i in range(4) :
        if DNA_count[i] > max_val :
            max_index = i
            max_val = DNA_count[i]
    return max_index, max_val

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
DNA = ['A', 'C', 'G', 'T']

answer_str = ""
answer_cnt = 0
for digit in range(m) :
    DNA_count = [0] * 4
    for i in range(n) :
        for cnt_idx in range(4) :
            if arr[i][digit] == DNA[cnt_idx] :
                DNA_count[cnt_idx] += 1
    max_index, max_val = get_max()
    answer_str = answer_str + DNA[max_index]
    answer_cnt = answer_cnt + (n - max_val)

print(answer_str)
print(answer_cnt)
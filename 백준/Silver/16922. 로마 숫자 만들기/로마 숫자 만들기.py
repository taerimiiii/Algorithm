def choose(curr_n, start, total):
    if curr_n == 0:
        num_sum_set.add(total)
        return
    for i in range(start, 4):
        choose(curr_n - 1, i, total + number_list[i])

n = int(input())
number_list = [1, 5, 10, 50]
num_sum_set = set()

choose(n, 0, 0)

print(len(num_sum_set))
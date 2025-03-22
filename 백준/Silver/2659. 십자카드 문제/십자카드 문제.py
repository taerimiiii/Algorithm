def change_clock_number(n1, n2, n3, n4) :
    clock_num1 = n1 * 1000 + n2 * 100 + n3 * 10 + n4
    clock_num2 = n2 * 1000 + n3 * 100 + n4 * 10 + n1
    clock_num3 = n3 * 1000 + n4 * 100 + n1 * 10 + n2
    clock_num4 = n4 * 1000 + n1 * 100 + n2 * 10 + n3
    clock_nums = [clock_num1, clock_num2, clock_num3, clock_num4]
    return min(clock_nums)

i1, i2, i3, i4 = map(int, input().split())
input_clock = change_clock_number(i1, i2, i3, i4)

is_clock_num = set()
for num1 in range(1, 10) :
    for num2 in range(1, 10) :
        for num3 in range(1, 10) :
            for num4 in range(1, 10) :
                clock_number = change_clock_number(num1, num2, num3, num4)
                is_clock_num.add(clock_number)

sort_clock_num = sorted(is_clock_num)
print(sort_clock_num.index(input_clock) + 1)
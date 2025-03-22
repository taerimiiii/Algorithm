def get_digit(number) :
    if number < 10 :
        digit_list.append(number)
        return
    digit_list.append(number % 10)
    number = number // 10
    get_digit(number)


n = int(input())

cnt = 0
for number in range(1, n + 1) :
    digit_list = []
    get_digit(number)
    for i in range(len(digit_list)) :
        if digit_list[i] == 3 or digit_list[i] == 6 or digit_list[i] == 9:
            cnt += 1

print(cnt)
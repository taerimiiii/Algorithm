import sys
input = sys.stdin.readline

bin = input().strip()

length = len(bin)

zero = length % 3
bin = '0' * (3 - zero) + bin
length = len(bin)

for i in range(0, length, 3) :
    string = bin[i:i+3]
    if string == '000' :
        if i == 0 :
            continue
        else :
            print(0, end='')
    elif string == '001' :
        print(1, end='')
    elif string == '010' :
        print(2, end='')
    elif string == '011' :
        print(3, end='')
    elif string == '100' :
        print(4, end='')
    elif string == '101' :
        print(5, end='')
    elif string == '110' :
        print(6, end='')
    else :
        print(7, end='')
arr = [int(input()) for _ in range(9)]

def get_no_people() :
    for i in range(8) :
        for j in range(i + 1, 9) :
            target = 0
            for k in range(9) :
                if i == k or j == k :
                    continue
                target += arr[k]
            if target == 100 :
                return i, j

a, b = get_no_people()
for i in range(9) :
    if i == a or i == b :
        continue
    print(arr[i])
def get_a_and_c(m, seed, x1, x2) :
    for a in range(m) :
        for c in range(m) :
            if x1 == (a * seed + c) % m :
                if x2 == (a * x1 + c) % m:
                    return a, c

m, seed, x1, x2 = map(int, input().split())

a, c = get_a_and_c(m, seed, x1, x2)
print(a, c)
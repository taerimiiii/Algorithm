n = int(input())
people = [input() for _ in range(n)]
fin_people = [input() for _ in range(n - 1)]

target = dict()
for person in people :
    if person not in target.keys() :
        target[person] = 1
    else :
        target[person] += 1

for person in fin_people :
    if person in target.keys() :
        target[person] += 1

for key, val in target.items() :
    if val % 2 == 1:
        print(key)
        break
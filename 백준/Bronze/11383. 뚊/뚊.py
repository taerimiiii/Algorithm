n, m = map(int, input().split())
original = []
two_m = []

for i in range(1, (n*2)+1) :
    if i <= n :
        original.append(input())
    else:
        two_m.append(input())
  
for j in range(n) :
    new = ''
    for s in original[j] :
        new += s*2
    original[j] = new


if original == two_m :
    print('Eyfa')
else:
    print('Not Eyfa')
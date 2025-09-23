import sys
input = sys.stdin.readline

def back_tracking(arr, target, sec, is_in) :
    locations = []
    sec += 1
    for elem in arr :
        a, b, c = elem + 1, elem - 1, elem * 2
        if a == target or b == target or c == target:
            return sec
        if not is_in[a] :
            locations.append(a)
        if not is_in[b] :
            locations.append(b)
        
        locations.append(c)
    print(locations, sec)

    back_tracking(locations, target, sec)

n, k = map(int, input().split())

search = [n]
sec = 0
is_in = [False] * 100001

success = True

if n == k :
    success = False

while success :
    locations = []
    sec += 1
    for elem in search :
        if 0 <= elem + 1 <= 100000 :
            x = elem + 1
            if x == k :
                success = False
                break
            if not is_in[x] :
                locations.append(x)
                is_in[x] = True

        if 0 <= elem - 1 <= 100000 :
            x = elem - 1
            if x == k :
                success = False
                break
            if not is_in[x] :
                locations.append(x)
                is_in[x] = True

        if 0 <= elem * 2 <= 100000 :
            x = elem * 2
            if x == k :
                success = False
                break
            if not is_in[x] :
                locations.append(x)
                is_in[x] = True
    search = locations

print(sec)
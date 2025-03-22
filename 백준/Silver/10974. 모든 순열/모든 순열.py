def printing() :
    for elem in answer :
        print(elem, end = ' ')
    print()

def choose(curr_n) :
    if curr_n == 0 :
        printing()
        return
    
    for k in range(1, n + 1) :
        if k not in answer :
            answer.append(k)
            choose(curr_n - 1)
            answer.pop()
    return

n = int(input())

answer = []
choose(n)
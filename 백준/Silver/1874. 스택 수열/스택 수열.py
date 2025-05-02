def isEmpty(top) :
    if top == -1 :
        return True
    return False

n = int(input())
target = [int(input()) for _ in range(n)]

ta_idx = 0
success = 1

answer = [''] * (2 * n)
ans_idx = 0

num = 1
top = -1
stack = [] #[0] * (n + 1)

while ta_idx < n :
    if isEmpty(top) :
        top += 1
        stack.append(num)
        num += 1
        
        answer[ans_idx] = '+'
        ans_idx += 1

    else :
        if stack[top] == target[ta_idx] :
            stack.pop()
            top -= 1
            ta_idx += 1
            
            answer[ans_idx] = '-'
            ans_idx += 1

        elif stack[top] > target[ta_idx] :
            success = 0
            break

        else :
            top += 1
            stack.append(num)
            num += 1
            
            answer[ans_idx] = '+'
            ans_idx += 1

if success :
    for elem in answer :
        print(elem)
else :
    print("NO")

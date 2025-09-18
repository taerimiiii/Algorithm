import sys
input = sys.stdin.readline
from collections import deque

priority_queue = deque()
weight_queue = deque()

n, m = map(int, input().split())
for _ in range(n) :
    p, w = map(int, input().split())
    priority_queue.append(p)
    weight_queue.append(w)

container_stack = deque()
temp_stack = deque()
answer = 0

for prio in range(m, 0, -1) :
    prio_num = 0
    while prio in priority_queue :
        curr_qrio = priority_queue.popleft()
        curr_wei = weight_queue.popleft()
        if curr_qrio != prio :
            priority_queue.append(curr_qrio)
            weight_queue.append(curr_wei)
            answer += curr_wei
        else :
            while prio_num != 0 and container_stack[-1] < curr_wei :
                # print(prio_num, container_stack, temp_stack)
                prio_num -= 1
                temp_wei = container_stack.pop()
                temp_stack.append(temp_wei)
                answer += temp_wei
            prio_num += 1
            container_stack.append(curr_wei)
            answer += curr_wei
            while temp_stack :
                prio_num += 1
                temp_wei = temp_stack.pop()
                container_stack.append(temp_wei)
                answer += temp_wei
print(answer)
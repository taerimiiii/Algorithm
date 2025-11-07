import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    min_heap = []
    max_heap = []
    nums = {}

    k = int(input())
    for _ in range(k) :
        char, n = input().split()
        n = int(n)

        if char == 'I' :
            if n in nums :
                nums[n] += 1
            else :
                nums[n] = 1
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)

    # print(nums)
    # print(min_heap, max_heap)
        else :
            if n == 1 and max_heap :
                length = len(max_heap)
                success = False
                for _ in range(length) :
                    max_val = -heapq.heappop(max_heap)
                    if max_val in nums :
                        success = True
                        break
    
                if success :
                    nums[max_val] -= 1
                    if nums[max_val] == 0 :
                        del nums[max_val]

            elif n == -1 and min_heap :
                length = len(min_heap)
                success = False
                for _ in range(length) :
                    min_val = heapq.heappop(min_heap)
                    if min_val in nums :
                        success = True
                        break

                if success :
                    nums[min_val] -= 1
                    if nums[min_val] == 0 :
                        del nums[min_val]

    if nums :
        while min_heap :
            min_val = heapq.heappop(min_heap)
            if min_val in nums :
                break
        while max_heap :
            max_val = -heapq.heappop(max_heap)
            if max_val in nums :
                break
        print(max_val, min_val)
    else :
        print("EMPTY")

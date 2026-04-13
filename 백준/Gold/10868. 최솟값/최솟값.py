import sys
input = sys.stdin.readline

# 세그먼트 트리
class minsegment :
    def __init__(self, arr) :
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (self.n * 4)

    def build(self, left, right, i = 1) :
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]

        mid = (left + right) // 2
        self.tree[i] = min(self.build(left, mid, i * 2), self.build(mid+1, right, i * 2 +1))
        return self.tree[i]

    def search(self, start, end, left, right, i = 1) :
        if right < start or end < left :
            return float('inf')

        if left <= start and end <= right :
            return self.tree[i]

        mid = (start + end) // 2
        return min(self.search(start, mid, left, right, i * 2), self.search(mid+1, end, left, right, i * 2 +1))

# 입력
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = minsegment(arr)
tree.build(0, n-1)

targets = []
for i in range(m) :
    inputs = tuple(map(int, input().split()))
    targets.append(inputs)

# 트리
for target in targets :
    if len(target) == 1:
        start = target
        end = target
    else:
        start = target[0] - 1
        end = target[1] - 1

    print(tree.search(0, n-1, start, end))
import sys
input = sys.stdin.readline

x = int(input())
targets = [64]

while sum(targets) > x :
  targets[-1] //= 2
  if sum(targets) < x :
    targets.append(targets[-1])

print(len(targets))
import sys
input = sys.stdin.readline

string = input().strip()
length = len(string)
target = [string[i] for i in range(length)]
answers = []

for i in range(1, length-1) :
  for j in range(i+1, length) :
    first = target[:i]
    second = target[i:j]
    third = target[j:]

    first.reverse()
    second.reverse()
    third.reverse()

    answers.append("".join(first + second + third))

print(min(answers))
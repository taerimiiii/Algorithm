import sys
input = sys.stdin.readline

s1, s2 = map(int, input().split())

is_sample = True
for _ in range(s1) :
    sample, answer = map(int, input().split())
    if sample != answer :
        is_sample = False

is_system = True
for _ in range(s2) :
    system, answer = map(int, input().split())
    if system != answer :
        is_system = False

if not is_sample :
    print("Wrong Answer")
elif is_system :
    print("Accepted")
else :
    print("Why Wrong!!!")
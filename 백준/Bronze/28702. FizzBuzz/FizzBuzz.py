import sys
input = sys.stdin.readline

for i in range(3, 0, -1) :
    x = input().strip()
    if x != "Fizz" and x != "Buzz" and x != "FizzBuzz" :
        n = int(x) + i

if not n % 3 and not n % 5:
    print("FizzBuzz")
elif not n % 3 and n % 5:
    print("Fizz")
elif n % 3 and not n % 5:
    print("Buzz")
else:
    print(n)
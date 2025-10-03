import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0
n = 2 ** n

while n > 1 :
	n //= 2

	if r < n and c < n :
		cnt += 0

	elif r < n and c >= n : 
		cnt += n * n * 1
		c -= n
        
	elif r >= n and c < n : 
		cnt += n * n * 2
		r -= n
        
	else:
		cnt += n * n * 3
		r, c = r - n, c - n
    
print(cnt)
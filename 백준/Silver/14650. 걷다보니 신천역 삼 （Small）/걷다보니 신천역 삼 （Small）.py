import sys
input=sys.stdin.readline
n=int(input())
se=[0,1,2]
s=[]
t=[]

def Bfs(arr):
    if len(arr)==n:
        k=0

        for i in range(n):

            k+=arr[i]*(10**(n-i-1))

        t.append(k)
    
        return

    for i in se:    

        arr.append(i)

        Bfs(arr)

        arr.pop()


Bfs(s)

sum1=0
for k in t:
    
    if k%3==0 and len(str(k))==n:
        if k!=0:
            
            sum1+=1
print(sum1)
n=int(input())
a=[]
b=[1 for i in range (n)]
for i in range(n):
    a[i]=int(input())
for i in range(n):
    for j in range(n):
        if(j!=i):
            b[i]*=a[j]
for i in range(n):
    print(b[i],end=" ")
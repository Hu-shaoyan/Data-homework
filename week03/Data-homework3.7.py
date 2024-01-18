def min(m,n):
    if m <= n:
        return m
    else:
        return n

m = int(input())
n = int(input())
t=min(m,n)
while t>=2:
    if m%t==0 and n%t==0:
        print("最大公约数为 %d" %t)
        break
    t-=1

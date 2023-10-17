#第一种：用蒙特卡洛法模拟
import random
count=0
for i in range(100000):
    x=random.random()
    y=random.random()
    if (x*x+y*y)<1:
        count+=1
result=float(count/100000*4)
print("pi=%.10f"%result)

#第二种：梅钦级数法
n=10
t=20
b=10**t
x1=b*4//5
x2=b//-239
s=x1+x2
n*=2
for i in range(3,n,2):
    x1//=-25
    x2//=-57121
    x=(x1+x2)//i
    s+=x
result=s*4
result//=10**10
pi=float(result/10**10)
print("pi=%.10f"%pi)

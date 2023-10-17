import random
c=int(input())
g=c/random.randint(1,100)
while (abs(g*g-c)>0.0001):
    g=(g+c/g)/2
print(g)
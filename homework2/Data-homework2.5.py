c=int(input())
g=c/2
while (abs(g*g-c)>0.0001):
    g=(g+c/g)/2
print(g)
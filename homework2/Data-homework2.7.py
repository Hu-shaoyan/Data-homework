c=10
g=c/2
while abs(g**3-c)>0.00001:
    g=2*g/3+c/3*g*g
print(g)
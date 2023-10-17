import random
g=0
for i in range(0,3):
    if(i*i>2 and g==0):
        g=i-1
while (abs(g*g-2)>0.0001):
    g+=0.00001
print(g)
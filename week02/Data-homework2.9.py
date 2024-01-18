import random
import math
count=0
for i in range(1000):
    x=random.uniform(2,3)
    y=random.uniform(0,30)
    if y<(x*x+4*x*math.sin(x)):
        count+=1
print(count/1000*30)
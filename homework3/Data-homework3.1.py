import math
number=float(input())
result=0
for i in range(7):
    result+=math.floor(number*2)/(10**(i+1))
    if number*2==1:
        break
    else:
        number=number*2-math.floor(number*2)
print(result)
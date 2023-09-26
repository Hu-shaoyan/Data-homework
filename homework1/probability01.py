# 频率
import random
i = 1
result = 0
time = 0
while i <= 1000000:
      x = random.uniform(0,1)
      y = random.uniform(0,1)
      z = x+y
      if z < 1.4:
         result += 1
      time += 1
      i += 1
print(result/time)

# 几何
probability=(1-0.6*0.6*0.5)/1
print(probability)
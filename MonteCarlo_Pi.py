import numpy as np
t_size = 1000000
sum = 0
x, y = np.random.random(t_size), np.random.random(t_size)
for i in range(t_size):
    if x[i]**2 + y[i]**2 < 1.0:
        sum += 1
res = sum/float(t_size)*4
print("Pi is approximately: " + str(res))


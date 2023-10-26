import numpy as np
a = np.array([2, 3, 4])
print(a)
a = np.arange(1, 12, 2)
print(a)
a = np.linspace(1, 12, 6)
print(a)
print(a.reshape(3, 2))
print(a)
a = a.reshape(3, 2)
print(a.size)
print(a.shape)
print(a.dtype)
print(a.itemsize)
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
b = np.array((1, 2, 3))
print(b)
b = np.array([5, 3, 4], float)
print(b)
try:
    b = np.array(1, 2, 3)
except Exception as e:
    print(repr(e))
b = np.array([1, 2, 3, 4], dtype=complex)
print(b)
print(a < 4)
print(a)
a *= 3
print(a)
a = np.zeros((3, 4))
print(a)
a = np.random.random((2, 3))
print(a)
a = np.random.randint(0, 4, 5)
print(a)
a=np.arange(10)
print(a)
np.random.shuffle(a)
print(a)
print(np.random.randn(10))
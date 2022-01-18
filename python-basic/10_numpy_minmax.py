import numpy as np

arr = []

n, m = map(int, input().split(' '))

for i in range(n):
    a = list(map(int, input().split(' ')))
    arr.append(a)

arr = np.array(arr)
m = np.min(arr, axis=1)
M = np.max(m)

print(M)

import numpy as np

arr = []

n, m = map(int, input().split(' '))

for i in range(n):
    a = list(map(int, input().split(' ')))
    arr.append(a)

arr = np.array(arr)
m = np.mean(arr, axis=1)
v = np.var(arr, axis=0)
s = np.std(arr)

print(m)
print(v)
print(round(s, 11))

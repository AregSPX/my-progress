import numpy as np

arr1 = np.random.randint(1, 6, size=(4,))
print(arr1)
arr2 = np.random.randint(1, 4, size=(4,))
print(arr2)

print((arr1 - arr2)**2)

arr1[arr1 % 2 == 1] += 1
print(arr1)

Array = np.vstack([arr1, arr2])

print(Array)

Threshold = 3

Array[Array > Threshold] = Threshold

print(Array)
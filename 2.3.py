import numpy as np

arr = ([15, 12, 25, 65, 5, 6, 14])
print("original array = ", arr)
maxValue = np.amax(arr)
minValue = np.amin(arr)
print("max = ", maxValue)
print("min = ", minValue)

arr = ([[15, 25, 65], [85, 74, 2], [65, 78, 3]])
print("Original array:", arr)
print('\nmedian of arr :', np.median(arr))
print("\nmedian of arr, axis = 0", np.median(arr, axis=0))
print("\nmedian of arr, axis = 1", np.median(arr, axis=1))

arr1 = np.arange(5,9).reshape(4)
arr2 = np.arange(2,10).reshape(2,4)
new_arr = np.broadcast(arr1,arr2)

res = arr2 * arr1
print("\nresult=",res)

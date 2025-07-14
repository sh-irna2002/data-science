import numpy as np
array1=np.array([1,2,3,4,5])
array2=np.array([1,6,3,8,9])
print(array1)
print(array2)
if np.array_equal(array1, array2):
	print("array are eqyal")
else:
	print("array are not equal") 

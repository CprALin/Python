import numpy as np

print("First array")
a = np.array([1,2,3])
print(a)

print()

print("Second array")
b = np.array([[0,3,2,4,5],[4,5,6,7,8]])
print(b)

print()
print('Get Dimension')
print('a :',a.ndim ,'|', 'b :',b.ndim)

print()
print('Shape')
print('a :', a.shape,'|', 'b :', b.shape)

print()
print('Get a specific element from array a or b')
print('Last number from a:',a[-1],'|','Position third , first list: ', b[0,2])

print()
print('Get a specific row')
print(b[0,:])

print()
print('Get a specific column')
print(b[:,2])

print()

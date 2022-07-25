import numpy as np
arr=np.array([[5,9,8],[9,8,7],[9,8.5,7],[5,8,9]])
print(arr)

a=arr.shape
print(a)
aa=arr.reshape(2,3,2)
print(aa)
print(arr.ndim)
print(arr.size)




a_1d = np.arange(3)
print(a_1d)
# [0 1 2]

a_2d = np.arange(12).reshape((3, 4))
print(a_2d)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

a_3d = np.arange(24).reshape((2, 3, 4))
print(a_3d)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
#
#
a=np.array([[12 ,13 ,14, 15],
  [16 ,17 ,18, 19],
   [20, 21 ,22 ,23]])
print(a.ndim)
print(a_1d.ndim)
# 1

print(type(a_1d.ndim))
# <class 'int'>

print(a_2d.ndim)
# 2

print(a_3d.ndim)
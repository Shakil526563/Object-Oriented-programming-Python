from array import *
try:
 array_num = array('i', [1,3,5,7,9])
 for i in array_num:
     print(i)
 print("Access first three items individually")
 print(array_num[0])
 print(array_num[1])
 print(array_num[8])

except:
 print("not")
import numpy as np
try:
 array_num = np.array([5,8,9,8,7])
 for i in array_num:
     print(i)
 print("Access first three items individually")
 print(array_num[0])
 print(array_num[1])
 print(array_num[8])

except:
 print("not")
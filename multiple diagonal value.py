import numpy as np
from numpy import diagonal

def aaa(a,b):
  h=a.reshape(3,3)
  j=b.reshape(3,3)
  c=np.diagonal(h)
  d=np.diagonal(j)
  pr=c*d
  p=np.array(pr)
  print(p)

a=16
b=16
f=np.array([5,6,5,8,7,9,7,8,5])
d=np.array([5,8,7,9,5,4,6,7,5])
print(aaa(f,d))



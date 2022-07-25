import numpy as np
n=np.array([[2,4],[3,5],[9,8]])
print(n)
print(type(n))
n=[2,5,6]
e=list(filter(lambda s:s%2==0,n))
v=np.array(e)
print(v)
print(e)
import numpy as np
output = np.array([[x for x in range(2,21,2)],[x for x in range(1,22,2)]])
print(output)
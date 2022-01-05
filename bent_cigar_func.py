#!/usr/bin/env python
# coding: utf-8

# In[2]:


# bent_cigar_function

import numpy as np

def bent_cigar_func(x_local):
    D=x_local.size     # size of Numpy vector x_local
    bent_cigar = pow(x_local[0],2)
    for i in range(1,D):
        x_i=x_local[i]
        bent_cigar +=pow(10,6)*pow(x_local[i],2)
    return bent_cigar


x_local=np.array([2,3,4,5])
b=bent_cigar_func(x_local)
print (b)


# In[ ]:





# In[ ]:





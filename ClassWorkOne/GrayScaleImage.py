#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from scipy import misc
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


pic=plt.imread("./source/picture1.jpg")


# In[ ]:





# In[6]:


plt.imshow(pic)


# In[9]:


#YUV亮度灰度化
weight=np.array([0.3,0.59,0.11])
pic1=np.dot(pic,weight)


# In[14]:


pic1


# In[13]:


plt.imshow(pic1,cmap='gray')


# In[21]:


pic1.max()


# In[22]:


pic1.min()


# In[37]:


#128灰度级
#pic2t=np.zeros(shape=(pic1.shape[0],pic1.shape[1]))
for i in range(0,pic1.shape[0]):
    for j in range(0,pic1.shape[1]):
        pic1[i,j]=(128*pic1[i,j])//(pic1.max()-pic1.min())


# In[40]:



plt.imshow(pic1,cmap='gray')


# In[41]:


print(pic1.max(),pic1.min())


# In[43]:


#64灰度级
#pic2t=np.zeros(shape=(pic1.shape[0],pic1.shape[1]))
for i in range(0,pic1.shape[0]):
    for j in range(0,pic1.shape[1]):
        pic1[i,j]=(64*pic1[i,j])//(pic1.max()-pic1.min())
plt.imshow(pic1,cmap='gray')


# In[ ]:


#32灰度级
#pic2t=np.zeros(shape=(pic1.shape[0],pic1.shape[1]))
for i in range(0,pic1.shape[0]):
    for j in range(0,pic1.shape[1]):
        pic1[i,j]=(32*pic1[i,j])//(pic1.max()-pic1.min())
plt.imshow(pic1,cmap='gray')


# In[45]:


#16灰度级
#pic2t=np.zeros(shape=(pic1.shape[0],pic1.shape[1]))
for i in range(0,pic1.shape[0]):
    for j in range(0,pic1.shape[1]):
        pic1[i,j]=(16*pic1[i,j])//(pic1.max()-pic1.min())
plt.imshow(pic1,cmap='gray')


# In[ ]:


#8灰度级
#pic2t=np.zeros(shape=(pic1.shape[0],pic1.shape[1]))
for i in range(0,pic1.shape[0]):
    for j in range(0,pic1.shape[1]):
        pic1[i,j]=(8*pic1[i,j])//(pic1.max()-pic1.min())
plt.imshow(pic1,cmap='gray')


# In[ ]:





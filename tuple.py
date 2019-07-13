#!/usr/bin/env python
# coding: utf-8

# In[1]:


roles = ("Admin", "Operator", "User")
#or following line will create the same Tuple
# roles = "Admin", "Operator", "User"

print(roles[0])


# In[3]:


roles = ("Admin", "Operator", "User")
roles[2] = "Customer"


# In[4]:


roles = ()


# In[5]:


permission = ( ("Admin", "Operator", "User"), ("Developer", "Tester"),[1, 2, 3], {"Stage" : "Development"})
print(permission[3]["Stage"])


# In[6]:


numbers = (1, 2, 3)
a,b,c = numbers
print(a)
print(b)
print(c)


# In[7]:


a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


# In[ ]:





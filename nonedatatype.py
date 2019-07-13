#!/usr/bin/env python
# coding: utf-8

# In[1]:


type(None)


# In[3]:


None == False


# In[6]:


None == ""


# In[7]:


None == []


# In[8]:


None == 0


# In[9]:


None == None


# In[16]:


a = None 
a == None


# In[17]:


print(a)


# In[18]:


def my_func():
    print("Printing Hello");
what_i_got = my_func()
print(what_i_got)
    


# In[24]:


def my_func(x = None):
    if x:
        return x * x
    else:
        return 0
    
print(my_func())
print(my_func(5))
    


# In[ ]:





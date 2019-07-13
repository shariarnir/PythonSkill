#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [2, 4, 6, 7]
my_list[3] = [8]
print(my_list)


# In[2]:


my_nums = { 1 : 1, 2 : 4, 3 : 9, 4 : "What?"}
my_nums[4] = 16
print(my_nums)


# In[3]:


my_list = [2, 4, 6, 8]
my_list[4] = 10


# In[4]:


my_nums = { 1 : 1, 2 : 4, 3 : 9, 4 : 16 }
my_nums[5] = 25 
print(my_nums)


# In[5]:


nums = { 1 : "one", 2 : "two", 3 : "three",}
print(1 in nums)
print("three" in nums)
print(4 not in nums)


# In[6]:


my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums[5])


# In[7]:


my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums.get(5))


# In[10]:


my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums.get(5,"5 not in my numbers!"))


# In[11]:


my_nums = {1 : 1, 2 : 4, 3 : 9, 4 : 16}
print(my_nums.get(4,"5 not in my numbers!"))


# In[ ]:





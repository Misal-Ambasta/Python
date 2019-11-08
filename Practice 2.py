
# coding: utf-8

# ## Task 1:
# ### 1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[17]:


def myreduce(func, seq):
    first= seq[0]
    for i in seq[1:]:
       first = func(first, i)
    return first


# In[20]:


myreduce(lambda a,b:a+b, [1,1,1,1,4] )


# ### 1.2 Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[68]:


def myfilter(func, seq):
    for i in seq[0:]:
        func(i)
        if func(i)== True:
            print(i)
    


# In[65]:


def is_even(x):
    if x % 2 == 0:
        return True
     


# In[71]:


myfilter(is_even, [1, 3, 10, 45, 6, 50,2])


# In[73]:


list(myfilter(is_even, [1, 3, 10, 45, 6, 50]))


# ### Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# 

# In[83]:


my_list = [i for i in 'ACADGILD']
print(my_list)


# ### ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

# In[114]:


s =[]
a = 'xyz'
for i in 'xyz':
     print(i,i+i,i+i+i,i+i+i+i)
    



# coding: utf-8

# ## Task 1
# 
# ### 1. Write a program which will find all such numbers which are divisible by 7 but are not a multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[72]:


b=[]
for x in range(2000,3201):
    if (x%7==0) and (x%5!=0):
        b.append(str(x))

print (','.join(b))

#print(b)

len(b)


# ### 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[223]:


n = input("Whats ur name :: ")
m= input("Enter last name :: ")

print("Reverser order ::" + m+" "+ n)
    


# In[99]:


n = input("Whats ur name :: ")

for x in range(len(n)-1,-1,-1):
    print(n[x])


# ### 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
# ##### Formula: V=4/3 * π * r 3

# In[146]:


r = 6

v = (4/3)*3.14*r*r*r

v


# ## Task 2
# 
# ### 1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.
# 

# In[151]:


n=int(input("Enter number of elements you want to input :: "))

m=[]

for x in range(0, n):
    e = int(input())
    m.append(e)
print(m)


# ### 2. Create the below pattern using nested for loop in Python.
# 

# In[187]:


n=5
for x in range(0,5):
    for j in range(0, x+1):
        print('* ', end="")
    print()
for y in range(0,4):
    for i in range(4,y,-1):
        print('* ', end="")
    print()


# ### 3. Write a Python program to reverse a word after accepting the input from the user.

# In[189]:


m = input("Whats ur name :: ")
n=[]
for x in range(len(m)-1,-1,-1):
    n.append(str(m[x]))

print (''.join(n))
    


# ### 4. Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# In[219]:


string = "WE, THE PEOPLE OF INDIA,\n      having solemnly resolved to constitute India into a SOVEREIGN,!\n             SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n              and to secure to all its citizens"

print(string)


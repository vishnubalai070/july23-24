#!/usr/bin/env python
# coding: utf-8

# In[21]:


"logical operators"

n=25
print(n<20 or n<30)


# In[20]:


n=24
print(n>23 and n>30)


# In[29]:


a=input("enter a number")
print(a, not 30)


# In[30]:


a=10
b=20
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)


# In[31]:


"input function"
a=("vishnu")
b=10
c=3.4
d=[3,4,5]
print(type(a))
print(type(b))
print(type(c))
print(type(d)) 


# In[1]:


"convertion int float str "
a=str(input('enter a number'))
print(a)
print(type(a))


# In[2]:


"convertion int float str "
a=float(input('enter a number'))
print(a)
print(type(a))
      


# In[18]:


"sep and end arugument"
str1="code"
str2="io"
print(str1,'_', sep='', end='')
print(str2)


# In[23]:


a=10
b=30
c=(a+b)
d=(a*b)
e=(a/b)
f=(a-b)
print(c)
print(d)
print(e)
print(f)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))


# In[36]:


r=10
x=r**5
r%=x
print(r)
z=r*5*5
print(z)
r%=x
print(x)


# In[ ]:





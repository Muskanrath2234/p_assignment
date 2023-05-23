#!/usr/bin/env python
# coding: utf-8

# # Q.1 Create one variable containing following type of data:
# 

# ### String 

# In[14]:


p = 'python'
p


# ### list 

# my_list = [7,17,2.5,'ms', True]
# my_list

# ### float 

# In[11]:


F_value = 9.6
F_value


# ### tuple

# In[17]:


Tuple  =  (2,5,7.7)
Tuple


# # Q.2 Given are some following variables containing data :
# 

# ### var1=' '

# it is a string-type variable(str). we have used double or single quotes to represent string .

# ###  var2='[DS,ML,Python]'

# it is a string-type variable. 

# ### var3 =['DS','ML','Python']

# it is a list type varible 

# ### var4= 1.

# it is a int type variblale.

# ### Q.4 Create a list of length 10 of  your choice cointaing multiple types of data. using for loop print the element and its data type.

# In[38]:


a= [45,5.6,'jay',True,False,9,9.6,'sita','ram',2]
for i in a:
    print(i)
    print(type(i))


# ## Q.3 Expain following operator 

# In[30]:


#1. Division(/)
d= 4/2
d


# #2.  modulus (%) it give remainder value
# m =5%2
# m

# In[33]:


#3. flor division (//)
f = 7//2
f


# In[35]:


#4. ** used for power calculation
p = 9**3
p


# ## Q.5 using a while loop. Verify if the number A is purely divisible by number B and if so then how many times it can be divisible.

# In[57]:


A= 64
B=2
i =0
while A%B ==0:
    A=A/B
    i=i+1
if A==1:
    print("A  is purely divisible", i, "times")
else:
    print("not divisible")


#  ## Q.6 Create a list containing 25 int type data  item. using for loop and if condition print if the element is divisible by 3 or not 
# 

# In[63]:


N = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in N:
    if i%3 ==0:
        print(i, "is divisible by 3 ")
    else:
        print(i, "not divisible by 3",)


# ## Q.7 What do you understand about mutable and immutable data types? Give examples for both this property.

# ### Mutable :- mutable object can be changed after it is created  without changing its identity .
# ###    Examples: list ,set
#             

# ### Immutable :- immutable datatypes are objects that cannot be modified after they have been created.
# ###  Examples:- int, string , complex 

# In[72]:


my_list = [2, 5,'apple']
my_list[1]=8
my_list 


# In[75]:


s = 'nootbook'
s[3]


# In[76]:


s[3]= i


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # TO PRINT ALL THE PRIME NUMBERS BETWEEN 1 TO 200 USINF FOR LOOP

# In[1]:


minimum=1


# In[2]:


maximum=200


# In[5]:


print("Prime numbers between", minimum , "and", maximum , "are:")


for num in range(1,200+1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
       


# # END

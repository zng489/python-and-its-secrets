#!/usr/bin/env python
# coding: utf-8

# In[6]:


dog = 'smart'
horse = 'dumb'
dog = 'small'
horse = 'big'

if dog == 'smart':
    print('you`re right')
elif dog == 'small':
    print('right')


# In[4]:


if dog == 'smart':
    print('you`re right')
elif dog == 'small':
    print('right')


# In[10]:


eat = 'eggplant'

if eat == 'pizza':
    print('delicious')
elif eat == 'pasta':
    print('okay, i may eat')
else:
    print('no, i dont like it')


# In[12]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[22]:


mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number:{num}')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tests = int(input())

for i in range(tests):
    n, k = map(int, input().split())
    if (k + (n % 2)) % 4 <= 1:
        print('YES')
    else:
        print('NO')
        
        
        
    


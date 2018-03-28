
# coding: utf-8

# In[1]:


#0326/main.py
from source import calculator
a = int(input('insert num1:'))
b = int(input('insert num2:'))
c = input('輸入+-*/:')
if c == '+':
    print(calculator.addnum(a,b))
elif c == '-':
    print(calculator.minusnum(a,b))
elif c =='*':
    print(calculator.multiplynum(a,b))
else:
    print(calculator.divide(a,b))



# coding: utf-8

# In[6]:

#floating lookback option

import numpy as np
print('floating lookback')

s0=100
sigma=0.5
K=110
T=1
Step=10000
N=12
C=0
P=0
r=0.05

for i in range(Step):
    S_list=[]
    S=s0
    for j in range(N):
        WT=np.random.randn()*np.sqrt(T/N)
        S=S*np.exp((r-0.5*sigma**2)*(T/N)+sigma*WT)
        S_list.append(S)
    
    C+=max(0,max(S_list)-S)
    P+= max(0, S-min(S_list))
    
call_price=(C/Step)*np.exp(-r*T)
put_price=(P/Step)*np.exp(-r*T)
print('Call Price:',call_price)
print('Put Price', put_price)


# In[7]:

#lookback option

import numpy as np
print('lookback')

s0=100
sigma=0.5
K=110
T=1
Step=10000
N=12
C=0
P=0
r=0.05

for i in range(Step):
    min_price=2000
    S=s0
    for j in range(N):
        WT=np.random.randn()*np.sqrt(T/N)
        S=S*np.exp((r-0.5*sigma**2)*(T/N)+sigma*WT)
        if s0<min_price:
            min_price=s0
    
    C+=max(0,max(S_list)-S)
    P+= max(0, S-min(S_list))
    
call_price=(C/Step)*np.exp(-r*T)
put_price=(P/Step)*np.exp(-r*T)
print('Call Price:',call_price)
print('Put Price', put_price)


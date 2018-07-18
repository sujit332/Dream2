
# coding: utf-8

# In[2]:


def calc_factorial(n):
    if n==0:
        return 1
    else:
        return n*calc_factorial(n-1)
    


# In[4]:


calc_factorial(5)


# In[5]:


calc_factorial(4)


# In[ ]:


n=int(input("Enter a number"))

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
            print(i)
        else:
            continue
    if count > 2:
        return " N is not a prime number"
    else:
        return "N is a prime number"
is_prime(n)


# In[ ]:


n=int(input("Enter a number"))

def is_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
            print(i)
        else:
            continue
    if count > 2:
        return " N is not a prime number"
    else:
        return "N is a prime number"
is_prime(n)


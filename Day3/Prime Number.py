
# coding: utf-8

# In[3]:


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


# In[4]:


list1=input("Enter Strings").split(',')
print(list1)


# In[5]:


list1=input("Enter Strings").split(',')
def str_count(l):
    return len(l)
str_count(list1)


# In[8]:


def str_delim_count(lst,delim=' '):
    list1=lst.split(delim)
    return len(list1)
inp_list=input("Enter Strings")
str_delim_count(inp_list)
str_delim_count(inp_list,'|')


# In[15]:


def str_word_length(str1,delim=' '):
    lst=str1.split(delim)
    cnt_lst=[len(lst[i]) for i in range(len(lst))]
    return cnt_lst

str_word_length('This is a test string','t')


# In[20]:


n=int(input("Enter a number"))

def print_primes(n):
      pri_list=[i  for i in range(1,n+1) if n%i==0]
      return pri_list
print_primes(n)


# In[28]:


lst= input("Enter list of numbers:").split(',')
d=int(input("Enter a divisor"))

def multiple_yesno(lst,d):
      pri_list=['Yes' if int(n)%d==0 else 'No' for n in lst ]
      return pri_list
multiple_yesno(lst,d)


# In[32]:


lst= input("Enter list of Strings:").split(',')
d=input("Enter the ending char:")

def endsWith_Str(lst,d):
      out_list=[n for n in lst if n.endswith(d)==True]
      return out_list
endsWith_Str(lst,d)


# In[46]:


lst= input("Enter list of Strings:").split(',')
d=input("Enter the ending char:")

def substr_idx(lst,d):
      out_list=[i for i in range(len(lst)) if lst[i].find(d)!=-1]
      return out_list
substr_idx(lst,d)


# In[59]:


inp_sal=input("Enter Salaray for Tax calculation:")
tuple1=[(50000, 0.08), (100000, 0.10), (150000, 0.15)]
def cal_tax(inp_sal):
    tax=0
    for x,y in tuple1:
        
        if x>=inp_sal:
            tax= tax+(x*y)
            print(x,y)
            print(tax)
            print(x-inp_sal)
            return tax+cal_tax(inp_sal-x)
        else:
            print(x)
            continue
        
cal_tax(70000)           
            
        
            
    
    
    


# In[48]:





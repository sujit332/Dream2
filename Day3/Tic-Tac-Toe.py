
# coding: utf-8

# In[24]:


l1=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]

p1= input("Enter player1 choice:")
p2= input("Enter player1 choice:")
type(l1)
        
def print_board():
    for i in range(0,9,3):
        print(l1[i],l1[i+1],l1[i+2])

def update_board(inp_pat,l1,player):
    for i in range(len(l1)):
        if l1[i]==inp_pat and player=1:
            l1[i]='X'
        elif l1[i]==inp_pat and player=2:
            l1[i]='O'
            
            
            


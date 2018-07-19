
# coding: utf-8

# In[6]:


class Dog:
    def __init__(self,name):
        self.name=name
    def bark_name(self):
        print("Bark Name is {}".format(self.name))
        
D1=Dog("Puppy")
D2=Dog("Pluto")

D1.bark_name()
    


# In[24]:


class Animal:
    def __init__(self,name,category,age=10,eat_meat='Y'):
        print("Creating an instance of Animal")
        #print("Category can be **fly,swim or walk**")
        self.name = name
        self.age = age
        self.category = category
        self.eat_meat = eat_meat
        
    def identify_category(self):
        if self.category == 'swim':
            print("This is swimming {}".format(self.name))
        elif self.category == 'fly':
            print("This is flying {}".format(self.name))
        else:
            print("These is Walking {}".format(self.name))
            
    def eat_meat1(self):
        if self.eat_meat == 'Y':
            print("Non Vegetarian {}".format(self.name))
        else:
            print("Vegetarian {}".format(self.name))

A1=Animal('Dog','walk',15)
A2=Animal('Fish','swim')
A3=Animal('Dove','fly',5,'N')
A4=Animal('Frog','swim',5,'Y')
        
A1.identify_category()
A1.eat_meat1()
A2.identify_category()
A2.eat_meat1()
A3.identify_category()
A3.eat_meat1()
A4.identify_category()
A4.eat_meat1()


# In[33]:


import random
print(random.randint(0, 5))


# In[95]:


import random

dlist=[4,6,6,8,8,8,8,10,10,12,20,20,20]

print(dlist)
    
    
def select_dices_to_remove(dlist,n):
    list3=[]
    for i in range(0,n):
        random_index = random.randint(0,len(dlist))
        list3.append(dlist[random_index])
    return list3
        
    
removed_list=select_dices_to_remove(dlist,3)
print(removed_list)

remaining_list=dlist
for i in range(0,3):
    if removed_list[i] in dlist:
        remaining_list.remove(removed_list[i])

print(remaining_list)

die1= remaining_list.pop()
die2= remaining_list.pop()
print(die1,die2)
rand1=random.randint(1,die1)
rand2=random.randint(1,die2)
    
print(rand1,rand2,rand1+rand2)


# In[172]:


# Nouns: bag, dice, game
# Verbs: roll, draw, sum
import random
class Die:    
    def __init__(self, num_sides):        
        if num_sides > 20:            
            raise ValueError("You can't have more than a 20 sided die!") 
        if num_sides % 2 != 0:
            raise ValueError("You can't have an odd-sided die")
        self._num_sides = num_sides    
    def roll(self):        
        return random.randint(1, self._num_sides)
class Bag:
    
    def __init__(self, dice_dict):        
        self.dice_dict=dict(dice_dict)
        if  len(dict(self.dice_dict)) ==0:
            raise ValueError("Bag is empty.You can't draw any die!") 
        print(self.dice_dict)
        
    def draw(self,num_things=2):
        draw_list=[]
        draw_list=[i for i in self.dice_dict.keys()]
        Dies=[]
        for i in range(num_things):
            Dies.append(Die(draw_list[i]))
            #dict(self.dice_dict)[draw_list[i]].value-=1
        return Dies
    def show(self):
        print(self.dice_dict)
      
if __name__ == '__main__':
    b = Bag({4:1, 6:2, 8:4, 12:1, 20:3})
    set_aside = b.draw(num_things=3)
    print("set_aside",set_aside)
    drawn = b.draw(num_things=2)
    s = sum([die.roll() for die in drawn])
    print(s)


# In[179]:


'''
Area of a Circle
'''
import math
class Circle:
    def __init__(self,radius=2):
        self.radius= radius
    def compute_area(self,inp_radius=2):
        return(math.pi*(inp_radius**2))
if __name__=='__main__':
    c1=Circle()
    print(c1.compute_area(6))


# In[184]:


'''
Area of a Rectangle
'''
import math
class Rectangle:
    def __init__(self,length=2,width=3):
        self.length= length
        self.width= width
        
    def compute_area(self,length=2,width=3):
        return(length*width)
if __name__=='__main__':
    r1=Rectangle()
    print(r1.compute_area(6))
    print(r1.compute_area(6,4))
    print(r1.compute_area())


# In[204]:


class Person:
    def __init__(self,name):
        self.name=name
    def legally_change_name(self,new_name):
         self.name=new_name        
    def introduce_myself(self):
        print("Hello I am {} ".format(self.name))
        
if __name__=='__main__':
    p1=Person('Sujatha')
    p1.introduce_myself()
    p1.legally_change_name('Sam')
    p1.introduce_myself()
    p1.legally_change_name('Tin')
    p1.introduce_myself()
    
    
    

    


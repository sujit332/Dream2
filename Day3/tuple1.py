input1=input("Enter numbers seperated by commas")

list1 = input1.split(',')
l1=[]

for i in range(0,len(list1)-1,2):
    l1.append((list1[i],list1[i+1]))
print(l1)

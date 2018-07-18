x= input("Enter a String")
l1 = list(x)
l2=['a','e','i','0','u']
l3=[]
for i in range(len(l1)):
    if l1[i] in l2:
           continue
    else:
        l3.append(l1[i])
print(l3)



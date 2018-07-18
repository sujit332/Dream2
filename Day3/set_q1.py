input1=input("Please enter a list1")
input2=input("Please enter a list2")

l1=input1.split(',')
l2=input2.split(',')

set1=set(l1)
set2=set(l2)

print(sorted("".join(set1.intersection(set2))))


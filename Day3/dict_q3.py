input1=input("Please enter a coordinate-word pair in the format (x, y, word)")

l1=input1.split(',')


dict1={}

dict1={(l1[i],l1[i+1]):l1[i+2]  for i in range(0,len(l1)-1,3)}
print(dict1)

input2=input("Enter x and y")

for i in dict1:
    print(i)


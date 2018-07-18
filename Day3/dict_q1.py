input1=input("Enter numbers seperated by dash")

list1 = input1.split('-')

dict1={int(i):int(i)*int(i) for i in list1}

print(dict1)

x=input("Enter the input String")
c=input("Enter the starting character")

count =0
for i in x:
    if i.upper() == c.upper():
        count += 1
print("Number of occurances",count)

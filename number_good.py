x= int(input("Enter a  number"))

if x < 10 and x>0:
    print("This is a good number")
elif x>=10 and x<=99:
    if x%2 !=0:
        print("This is a better number")
    else:
        print("This the best number")
else:
    print("Horrible number")

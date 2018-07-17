x=int(input("Enter a number"))

if x%2 == 0:
    if x%3 == 0:
        print("even divisible by 3")
    else:
        print("even")
else:
    if x%3 == 0:
        print("odd divisible by 3")
    else:
        print("odd")

    

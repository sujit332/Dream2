input1 = 'a'
set1=set()
while input1 !='q':
    input1=input("Please enter a list of words")
    if input1=='v':
        print(set1)
        break
    
    set1.add(input1)

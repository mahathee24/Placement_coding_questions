# create a  traingle  with guve number of rows    
a=int(input("Enter the number of rows: "))
for i in range(a):
    for i in range(a-i): #i+1 for straight right angle  triangle 
        print("*",end=" ")
    print()
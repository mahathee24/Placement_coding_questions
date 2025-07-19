a=[]
a=int(input("Enter the number "))
for i in range(10,100):
    if i%3==0 and i%4==0 and i%5==0 and i%7==0:
        if i%a==0:
            a.append(i)
        print(i)
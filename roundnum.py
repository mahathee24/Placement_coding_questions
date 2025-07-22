n=int(input("enter the number"))
l=[]
while( n not in l):
    l.append(n)
    n=sum(int(d)**2 for d in str(n))
print("the square number is ",n)



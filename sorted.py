#given the number  in even and odd , names imn the list sort it in ascending order
a=[10,11,"zakir","bala",123,44,53,"anuj",20,46,7,"jack"]
a1=[]
a2=[]
a3=[]
for i in a:
    if(type(i)==str):
        a3.append(i)
    elif (i%2==0):
        a1.append(i)
    else:
        a2.append(i)
        a1.sort()
        a2.sort()
        a3.sort()
        a=a1+a2+a3
print(a) # Convert all elements to string for sorting


#enter no of blocks :3
#enter no of lines :4
#enter no of stars :5
#-------------BLOCK1-------------
#* * * * *
#* * * * *
#* * * * *
#* * * * *

a=int(input("Enter no of blocks"))
b=int(input("Enter no of lines"))
c=int(input("Enter no stars"))
for i in range(a):
    print("----------BLOCK",i+1,"--------------")
    line=b-i
    if line<=0:
        continue
    for i in range(line):
        for j in range(c):
            print("*",end=" ")

        print()

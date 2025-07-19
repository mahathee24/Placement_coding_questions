#2D and 4D dimension matrix 
a=[[[11,22,33],
    [44,55,66],
    [77,12,32]],

   [[41,42,43],
    [52,54,56],
    [98,97,95]]]
#here we have make 11,44,77 to be printid separatley 
for i in range(2):#iterates through the blocks 
    for j in range(3): #iterates through the rows
        for k in range(3): #iterates through the columns
            print(a[i][j][k], end=" ")
        print()
    print("------") #this is to separate the 3d matrix
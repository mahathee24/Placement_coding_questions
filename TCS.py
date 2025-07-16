#print a triangle shaped pattern of numbers  
#1
#3 * 2
#4 5 6
#10 9 8  7
#11 12 13 14 15
#21 20 19 18 17 16
a = int(input("Enter the number of rows: "))
num = 1

for i in range(1, a + 1):
    row = []
    for j in range(i):
        row.append(num)
        num += 1
    
    if i % 2 == 0:
        row.reverse()
    
    print(" * ".join(map(str, row)))



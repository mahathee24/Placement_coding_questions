#you are given with total number of heads and legs of a group if hens and cows and each hen has one head and two legs and each cow has one head and four legs. 
# write  a program to determine the number of hens and cows in the group
a=int(input("Enter the number of heads: "))
b=int(input("Enter the number of legs: "))
if b % 2 != 0 or a == 0 or b == 0 or b < 2 * a or b > 4 * a:
    print("Invalid input")
else:
    hens = (4 * a - b) // 2
    cows = a - hens
    print("No of hens:", hens)
    print("No of cows:", cows)
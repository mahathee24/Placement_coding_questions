#find the missing number without sorting in a list 
a=[1,3,6,7,2,4,5,9]
n=len(a)
missing_number = sum(range(1, n + 2)) - sum(a)
print("The missing number is:", missing_number)
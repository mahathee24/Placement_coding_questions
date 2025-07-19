names=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
memo=[0,1,1,1,2,2,1,2,1,2]
salary=[1000,2000,3000,4500,2000,5000,1500,2300,1300,1100]
#zip (names, memo amd salary) together
zipped_list = list(zip(names, memo, salary))

#remove if sal<4000
filtered_list = [item for item in zipped_list if item[2] >= 4000]
#extract the remaming employee in any list 
remaining_employees=[item[0]  < 4000 for item in filtered_list]
print("Remaining employees after removal:", remaining_employees)
sorted_employees = sorted(remaining_employees)
print("Sorted remaining employees:", sorted_employees)
#memo>=2 if so append in another list 
memo_list = [item[0] for item in filtered_list if item[1] >= 2]
print("Employees with memo >= 2:", memo_list)
#combine remaining_employees and memo_list
combined_list=list(set(remaining_employees) | set(memo_list))
print("Combined list of remaining and memo employees:", combined_list)

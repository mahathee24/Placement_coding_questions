#Anagram problem we have to remove the white space , reverse them and check if they are equal
str1=input("Enter the first string1: ")
str2=input("Enter the second string2: ")
str1=str1.replace(" ", "")
str2=str2.replace(" ", "")

str1 = ''.join(sorted(str1)) 
str2=''.join(sorted(str2))
 # Sort characters of the first string
if str1== str2:
    print("anagram")
else:
    print("not anagram")
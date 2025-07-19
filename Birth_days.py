from datetime import datetime
a=input("Enter your birth date (dd/mm/yyyy): ")
b=input ("enter the birth date(yyyy-mm-dd):")
d1=datetime.strptime(a,"%y-%m-%d")
d2=datetime.strptime(b,"%d/%m/%Y")
diff=d1-d2
print("your age is :" ,abs(diff.months),"days")

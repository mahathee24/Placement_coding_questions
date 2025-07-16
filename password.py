#enter the password which has to decide rhe special char, digits, operators,uppercase,lowercase
s = input("enter the password:")
sp = 0
dg = 0
uc = 0
lw = 0
if len(s) < 7:
    for i in s:
        if i.isdigit():
            dg += 1
        elif i.islower():
            lw += 1
        elif i.isupper():
            uc += 1
        else:
            sp+=1
    print("bad password")
else:
    print("good password")

            
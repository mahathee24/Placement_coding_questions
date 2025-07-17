#so we have to enter the boy name and girl name and if the letters are same then replace it with 2 number 

boy = input("Enter the boy's name: ").lower().replace(" ", "")
girl = input("Enter the girl's name: ").lower().replace(" ", "")

a1 = list(boy)
a2 = list(girl)

for ch in a1[:]:  # iterate over a copy to avoid issues when removing
    if ch in a2:
        a1.remove(ch)
        a2.remove(ch)


# Total unmatched letters
total_unmatched = len(a1) + len(a2)
print("Remaining letters:", a1 + a2)
print("Total unmatched letters:", total_unmatched)

ans=['F','L','A','M','E','s']
index=0
while(len(ans)!=1):
    index=(index+(total_unmatched-1))%len(ans)
    ans.pop(index)
print("the relation is ",ans[0])
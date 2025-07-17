import random
name1=input("Enter player1")
name2=input("Enter playEr2")
print("Comp has fixed 5nums in range of 1 to 10")
print("you guys have to guess it.. Ready??")

nums=[]
while len(nums)!=5:
    d=random.randint(1,10)
    if d not in nums:
        nums.append(d)
print("---------------")

s1=0
s2=0
player1=[]
player2=[] 

for i in range(3):
    print("------ROYUND{}-------".format(i+1))
    print("Dear {} guess ur choice".format(name1))
    ch=int(input())
    while ch in player1 or ch in player2:
        print("You have already guessed this number, try again")
        ch=int(input())
    player1.append(ch)
    if ch in nums:
        print("---------correct--------")
        s1=s1+1
    else:
        print("--------WRONG--------")
    
    print("Dear {} guess ur choice ".format(i+1))
    ch=int(input())
    player2.append(ch)
    if ch in nums:
        print("---------correct--------")
        s2=s2+1
    else:
        print("--------WRONG--------")
print("---------------")
print("Player1 {} has scored {}".format(name1,s1))
print("Player2 {} has scored {}".format(name2,s2))
if s1>s2:
    print("player1 {} has won the game". format(name1))
elif s2>s1:
    print("player2 {} has won the game". format(name2))
else:
    
    print("Its a tie")





#shortlisted students should not be notorious and have more than 5 grdes 
notorious=["anuj","darshan","rohith"]
names=["anu","darshan","rohith","jack","priya","bala","rai","ram","raj","ben"]
score=[2,5,6,8,3,5,6,9,8,2]

for i in range(len(names)):
    if score [i]>5:
        if names[i] not in notorious:
            print(names[i])
            

